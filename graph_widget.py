import os
import numpy as np
import pandas as pd
from uuid import uuid4
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QSizePolicy
from pyqtgraph import PlotWidget, mkPen
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from third_party import MyWarning
import config as cf


class AbstractDataFrame:
    def __init__(self, name_: str, parent_: QWidget = None):
        self.name = name_
        self.id = uuid4()
        self.active = True
        self.data = None
        self.header = None
        self.parent = parent_

    def __eq__(self, other_) -> bool:
        return self.id == other_

    def is_correct_read(self) -> bool:
        return self.data is not None

    def clear(self):
        self.active = False
        self.data = self.header = None

    def data_init(self): ...


class XYDataFrame(AbstractDataFrame):
    def __init__(self, filename_: str, parent_: QWidget = None):
        super().__init__(os.path.basename(filename_), parent_)
        self.filename = filename_
        self.data = None
        self.max_y = None
        is_exception = False

        if not os.path.exists(self.filename) or not os.path.isfile(self.filename):
            QMessageBox.warning(self.parent, cf.FILE_NOT_EXIST_WARNING_TITLE,
                                f"{self.filename} - не существует или не является файлом!", QMessageBox.Ok)

        else:
            self.data = pd.read_csv(self.filename, header=None)

        try:
            self.header = self.header_init()
        except MyWarning as mw:
            QMessageBox.warning(self.parent, mw.exception_title, mw.message, QMessageBox.Ok)
            is_exception = True
        except:
            QMessageBox.warning(self.parent, cf.UNKNOWN_WARNING_TITLE, cf.UNKNOWN_WARNING_MESSAGE, QMessageBox.Ok)
            is_exception = True

        if is_exception:
            self.clear()
        self.data_init()

    def clear(self):
        self.active = False
        self.data = self.header = self.max_y = None

    def is_correct_read(self) -> bool:
        return self.data is not None and self.header is not None

    def header_init(self) -> dict:
        res = dict()
        for i in range(cf.CSV_FILE_HEADER_SIZE):
            dot_index = self.data.iloc[i][0].find(':')
            if dot_index == -1 or \
                    self.data.iloc[i][0][:dot_index] not in cf.CSV_FILE_HEADER_CONTENT:
                raise MyWarning(cf.INCORRECT_FILE_CONTENT_WARNING_TITLE,
                                f"Выбранный файл: - {self.filename} - имеет неправильное наполнение в хедере!")
            header_name = self.data.iloc[i][0][:dot_index]
            res[header_name] = cf.CSV_FILE_HEADER_CONTENT[header_name] \
                .get(self.data.iloc[i][0][dot_index + 1:])
        return res

    def data_init(self) -> None:
        if not self.is_correct_read():
            return
        self.data = self.data.drop(index=[0, 1, 2, 3, 4, 5])
        self.data = {'y': self.data[0].astype(float).values.tolist()}
        self.max_y = max(self.data['y'])

    @staticmethod
    def get_data_x(data_points_: int, time_base_: int) -> dict:
        x_data = {'x': []}
        step = time_base_ * 16 / data_points_ * 0.001
        for i in range(data_points_):
            x_data['x'].append((i - 1) * step)
        return x_data


class MaxesDataFrame(AbstractDataFrame):
    def __init__(self, name_: str, maxes_: list, parent_: QWidget = None, max_value_: float = None):
        super().__init__(name_, parent_)
        self.data = {'y': maxes_, 'ry': []}
        self.max_value = None

        self.data_init(max_value_)
        # print(self.data)

        self.tmp_value = None

    def max(self, max_value_: float = None) -> float:
        if max_value_ is not None:
            self.max_value = max_value_
        if self.max_value is None and len(self.data['y']):
            self.max_value = max(self.data['y'])
        return self.max_value

    def data_init(self, max_value_: float = None) -> None:
        self.compute_relative_data(max_value_)

    def compute_relative_data(self, max_value_: float = None) -> None:
        max_of_maxes = max_value_
        if max_of_maxes is None:
            max_of_maxes = self.max()
        for max_ in self.data['y']:
            self.data['ry'].append(max_ / max_of_maxes)

    @staticmethod
    def get_data_x(data_points_: int, start_point_: int = 0, step_: int = 1) -> dict:
        x_dataframe = {'x': []}
        for i in range(start_point_, start_point_ + data_points_ * step_, step_):
            x_dataframe['x'].append(i)
        return x_dataframe


class AbstractQtGraphWidget(PlotWidget):
    def __init__(self, data_frames_, parent_: QWidget = None):
        super().__init__(parent_)
        self.id = uuid4()
        self.data_frames = data_frames_
        self.dict_data_x = dict()
        self.base_init()
        self.lines = []
        self.legend = self.addLegend()

    def base_init(self):
        self.setBackground('w')
        self.showGrid(x=True, y=True)

    def graph_init(self) -> None: ...

    def data_x_init(self) -> None: ...

    def recreate(self, data_frames_) -> None:
        for line in self.lines:
            line.clear()
        self.data_frames = data_frames_
        self.data_x_init()
        self.base_init()
        self.graph_init()


class OscilloscopeGraphWidget(AbstractQtGraphWidget):
    def __init__(self, data_frames_: dict, parent_: QWidget = None):
        super().__init__(data_frames_, parent_)
        self.graph_init()
        self.setTitle("Данные осциллографа")
        self.setLabel('left', 'Напряжение (мВ)')
        self.setLabel('bottom', 'Время (с)')

    def data_x_init(self) -> None:
        self.dict_data_x = dict()
        for key in self.data_frames.keys():
            for dataframe in self.data_frames[key]:
                if dataframe.header['Data points'] not in self.dict_data_x:
                    self.dict_data_x[dataframe.header['Data points']] = dict()
                if dataframe.header['Time Base'] not in self.dict_data_x[dataframe.header['Data points']]:
                    self.dict_data_x[dataframe.header['Data points']][dataframe.header['Time Base']] \
                        = XYDataFrame.get_data_x(dataframe.header['Data points'], dataframe.header['Time Base'])

    def graph_init(self) -> None:
        self.legend.clear()
        if len(self.data_frames.keys()) < 1:
            return
        color_i, c = 0, 0
        for key in self.data_frames.keys():
            for i in range(len(self.data_frames[key])):
                if color_i >= len(cf.COLOR_NAMES):
                    color_i = 0
                if c >= len(self.lines):
                    self.lines.append(self.plot(self.dict_data_x[self.data_frames[key][i].header['Data points']]
                                                [self.data_frames[key][i].header['Time Base']]['x'],
                                                self.data_frames[key][i].data["y"], pen=mkPen(cf.COLOR_NAMES[color_i])))
                elif self.data_frames[key][i].active:
                    self.lines[c].setData(self.dict_data_x[self.data_frames[key][i].header['Data points']]
                                          [self.data_frames[key][i].header['Time Base']]['x'],
                                          self.data_frames[key][i].data["y"])
                self.legend.addItem(self.lines[c], self.data_frames[key][i].name)
                c += 1
                color_i += 1


class FrequencyResponseGraphWidget(AbstractQtGraphWidget):
    def __init__(self, data_frames_: dict, parent_: QWidget = None):
        super().__init__(data_frames_, parent_)
        self.graph_init()
        self.setTitle("Частотная характеристика")
        self.setLabel('left', 'U, В')
        self.setLabel('bottom', 'f, кГц')

    def data_x_init(self) -> None:
        self.dict_data_x = {'0': MaxesDataFrame.get_data_x(21, 4, 2)}

    def graph_init(self) -> None:
        self.legend.clear()
        if len(self.data_frames.keys()) < 1:
            return
        color_i, c = 0, 0
        for key in self.data_frames.keys():
            for i in range(len(self.data_frames[key])):
                if color_i >= len(cf.COLOR_NAMES):
                    color_i = 0
                if c >= len(self.lines):
                    self.lines.append(self.plot(self.dict_data_x['0']['x'],
                                                self.data_frames[key][i].data["y"],
                                                pen=mkPen(cf.COLOR_NAMES[color_i])))
                elif self.data_frames[key][i].active:
                    self.lines[c].setData(self.dict_data_x['0']['x'],
                                          self.data_frames[key][i].data["y"])
                self.legend.addItem(self.lines[c], self.data_frames[key][i].name)
                c += 1
                color_i += 1
            # break


class AmplitudeTimeGraphWidget(AbstractQtGraphWidget):
    def __init__(self, data_frames_: dict, parent_: QWidget = None):
        super().__init__(data_frames_, parent_)
        self.graph_init()
        self.setTitle("Зависимость амплитуды во времени")
        self.setLabel('left', 'Значение')
        self.setLabel('bottom', 'Шаг')

    def data_x_init(self) -> None:
        # self.dict_data_x = {'0': MaxesDataFrame.get_data_x(21)}
        pass

    def graph_init(self) -> None:
        self.legend.clear()
        if len(self.data_frames.keys()) < 1:
            return
        color_i, c = 0, 0
        for key in self.data_frames.keys():
            for i in range(len(self.data_frames[key])):
                if color_i >= len(cf.COLOR_NAMES):
                    color_i = 0
                if c >= len(self.lines):
                    self.lines.append(self.plot(self.dict_data_x[key]['x'],
                                                self.data_frames[key][i].data["y"],
                                                pen=mkPen(cf.COLOR_NAMES[color_i])))
                elif self.data_frames[key][i].active:
                    self.lines[c].setData(self.dict_data_x[key]['x'],
                                          self.data_frames[key][i].data["y"])
                self.legend.addItem(self.lines[c], self.data_frames[key][i].name)
                c += 1
                color_i += 1


# MATPLOTLIB GRAPH
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111, projection='polar')
        self.sensor_name_list = ['A', '', 'B', '', 'C', '', 'D', '']
        self.axes_init()
        FigureCanvasQTAgg.__init__(self, self.fig)
        FigureCanvasQTAgg.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)

    def axes_init(self) -> None:
        self.ax.set_title("Label", va='bottom')
        angle_and_name_list = self.sensor_name_list.copy()
        for i in range(len(angle_and_name_list)):
            angle_and_name_list[i] = str(45 * i) + '° ' + angle_and_name_list[i]
        self.ax.set_xticklabels(angle_and_name_list)


class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

        self.theta = np.array([0, 90, 180, 270, 360]) / 180 * np.pi

    def set_data(self, data_frame_dict_: dict, index_: int = 0, is_relative_: bool = False):
        for section_name in data_frame_dict_.keys():
            is_active = True
            data_list = [0] * (cf.DEFAULT_SENSOR_AMOUNT + 1)
            for dataframe in data_frame_dict_[section_name]:
                if not dataframe.is_correct_read() or not dataframe.active or \
                        len(dataframe.data['ry' if is_relative_ else 'y']) <= index_ and \
                        int(dataframe.name) < cf.DEFAULT_SENSOR_AMOUNT + 1:
                    is_active = False
                    continue
                data_list[int(dataframe.name)] = dataframe.data['ry' if is_relative_ else 'y'][index_]
            data_list[-1] = data_list[0]
            if is_active:
                self.canvas.ax.plot(self.theta, data_list, label=section_name)
        self.canvas.ax.legend()
        self.canvas.draw()

    def clear(self):
        self.canvas.ax.clear()
        self.canvas.axes_init()
