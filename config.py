from PySide6.QtCore import QSize, QPoint
from third_party import IntFormatting, FloatFormatting, StrFormatting

MAIN_WINDOW_TITLE = "Avellon tech"
MAIN_WINDOW_ICON_PATH = ""
MAIN_WINDOW_MINIMUM_SIZE = QSize(800, 450)
ICON_WINDOW_PATH = "resource/img/favicon.ico"
MAIN_MENU_LOGO_PATH = "resource/img/logo.png"

DEFAULT_BUTTON_SIZE = QSize(200, 50)
SEQUENCE_NUMBER_SHORTCUT_MODE = "SEQNUM"
NO_SHORTCUT_MODE = "NO"

DEFAULT_PROJECT_NAME = "Avellon_Project_"

BOREHOLE_INFO_SAVE_FILENAME = "info.txt"
DEFAULT_PROJECT_FOLDER = 'projects'

DEFAULT_BOREHOLE_NAME_FONT_SIZE = 40

DEFAULT_X_AXES_MODE = "DEFAULT_X_AXES_MODE"
F4T44_X_AXES_MODE = "F4T44_X_AXES_MODE"
DEFAULT_SENSOR_AMOUNT = 4
DEFAULT_MEASUREMENT_NUMBER = 21


ALLOWED_FILE_LOAD_FORMATS = ['csv']

FILE_DIALOG_FOLDER_FILTER = "FOLDER_FILTER"
FILE_DIALOG_CSV_FILTER = "CSV files (*.csv)"
FILE_DIALOG_SAVE_FILTERS = ["JPG files (*.jpg; *.jpeg)", "PNG files (*.png)",
                            "JPG files (*.jpg; *.jpeg);; PNG files (*.png)"]
DEFAULT_FOLDER_NAME_FOR_SELECT = "data"
DEFAULT_FOLDER_NAME_TO_SAVE = "save_data"
TYPES_OF_SAVING_FILE = ['png', 'jpg', 'jpeg']
DEFAULT_FORMAT_OF_FILENAME = "%Y_%m_%d_%H_%M_%S"
TMP_FOR_WORK_FILENAME = "WORK_VERSION.csv"


PIPE_SECTION_SIZE = QSize(600, 150)
SOLID_PIPE_SIZE = QSize(500, 100)
DEFAULT_PIPE_LENGTH_IN_METERS = 1
DASH_PIPE_SIZE = QSize(SOLID_PIPE_SIZE.width(), int(SOLID_PIPE_SIZE.height() / 2))
RELATIVE_DASH_PIPE_POSITION = QPoint(0, int(SOLID_PIPE_SIZE.height() / 4))
SOLID_PIPE_LINE_WIDTH = 3
DASH_PIPE_LINE_WIDTH = 1
CRACK_LINE_FOR_PIPE_WIDTH = 2
CRACK_PIPE_FONT_SIZE = 16
SENSOR_PIPE_FONT_SIZE = 24

UPPER_SIDE = 'upper'
BOTTOM_SIDE = 'bottom'

LEFT_RIGHT_DIRECTION = '->'
RIGHT_LEFT_DIRECTION = '<-'

MAX_CRACK_AMOUNT = 10

PIPE_CRACK_DEPTH_UNIT = "мм"
PIPE_CRACK_POSITION_UNIT = "м"

CSV_FILE_HEADER_SIZE = 6
CSV_FILE_HEADER_CONTENT = {
    "Time Base": IntFormatting('μs'),
    "Sampling Rate": FloatFormatting('MSa/s'),
    "Amplitude":  FloatFormatting('V'),
    "Amplitude resolution": FloatFormatting('mV'),
    "Data Uint": StrFormatting(''),
    "Data points": IntFormatting(''),
}

COLOR_NAMES = ['red', 'blue', 'green', 'orange', 'burlywood',
               'darkcyan', 'darkgoldenrod', 'pink',
               'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
               'darksalmon', 'darkseagreen', 'darkslateblue', 'darkturquoise', 'darkviolet',
               'deeppink', 'deepskyblue', 'dodgerblue', 'firebrick', 'forestgreen', 'fuchsia',
               'gold', 'honeydew', 'indianred', 'lavender', 'lavenderblush', 'pink',
               'lawngreen', 'lemonchiffon', 'lightgoldenrodyellow', 'lightgreen',
               'lightsteelblue', 'lime', 'limegreen', 'magenta', 'maroon', 'mediumvioletred',
               'midnightblue', 'olive', 'orchid', 'palegoldenrod', 'plum',
               'purple', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen',
               'skyblue', 'slateblue', 'springgreen', 'steelblue', 'thistle', 'violet', 'black']


# WARNING TITLES
FILE_NOT_EXIST_WARNING_TITLE = "File not exist"
WRONG_TYPE_WARNING_TITLE = "Wrong type"
WRONG_FILENAME_WARNING_TITLE = "Wrong filename"
INCORRECT_FILE_CONTENT_WARNING_TITLE = "Incorrect file content"
NOT_EMPTY_FOLDER_WARNING_TITLE = "Not empty folder"
UNKNOWN_WARNING_TITLE = "Unknown warning"


# WARNING MESSAGE
UNKNOWN_WARNING_MESSAGE = "Неизвестная ошибка при чтении файла."

'''
"All Files (*.*)|*.*" +
        "|All Pictures (*.emf;*.wmf;*.jpg;*.jpeg;*.jfif;*.jpe;*.png;*.bmp;*.dib;*.rle;*.gif;*.emz;*.wmz;*.tif;*.tiff;*.svg;*.ico)" +
            "|*.emf;*.wmf;*.jpg;*.jpeg;*.jfif;*.jpe;*.png;*.bmp;*.dib;*.rle;*.gif;*.emz;*.wmz;*.tif;*.tiff;*.svg;*.ico" +
        "|Windows Enhanced Metafile (*.emf)|*.emf" +
        "|Windows Metafile (*.wmf)|*.wmf" +
        "|JPEG File Interchange Format (*.jpg;*.jpeg;*.jfif;*.jpe)|*.jpg;*.jpeg;*.jfif;*.jpe" +
        "|Portable Network Graphics (*.png)|*.png" +
        "|Bitmap Image File (*.bmp;*.dib;*.rle)|*.bmp;*.dib;*.rle" +
        "|Compressed Windows Enhanced Metafile (*.emz)|*.emz" +
        "|Compressed Windows MetaFile (*.wmz)|*.wmz" +
        "|Tag Image File Format (*.tif;*.tiff)|*.tif;*.tiff" +
        "|Scalable Vector Graphics (*.svg)|*.svg" +
        "|Icon (*.ico)|*.ico";
'''


HELP_INFO = '''## Функционал

Чтобы построить любой график необходимо загруить файлы и в окне желаемого графика нажать `▷ Построить`. 

Каждый построенный график можно сохранить. Быстро с помощью пункта `Сохранить` в панеле сверху или сочетания клавиш `Ctrl+S`. 
Тогда файл автоматически сохраниться в папку `save_data` в дириктории проекта проекте.
Более детальное сохранение доступно при нажатии `Сохранить как` - `Ctrl+Shift+S`, тогда откроется диалоговое окно 
и появиться возможность выбрать место и имя сохраняемого файла.
В окне любого графика можно поднастроить скважину для всего проекта. Это делается через верхнюю панель `Скважина->Настроить скважину`.
Для получения справочной информации необходимо нажать на `Справка` на верхней панеле.
При нажатии кнопки `Назад` на верхней панеле пользователь вернется в главное меню.
У каждого графика можно убирать отдельные лини с помощью списка галочек.

### Настройка скважины
Настройка скважины есть единое окружение для постройки любого графика.
Для постройки некоторых из них необходимо определенное количество исходных файлов с данными.

При открытии экрана настройки скважины изначально будут доступны 3 кнопки:
* `+ Добавить секцию` - при нажатии которой в списке появляется секция с возможностью ее дальнейшего редактирования.
* `Принять` - все внесенные изменения в настройку секции вступят в силу
* `Отмена` -  все внесенные изменения в настройку секции отменяться, скважина вернется в настройку до открытия окна настройки скважины

В соответсутвующий полях секции можно настроить `Имя` секции, `Глубину` ее месторасположения, `Длину`.
С помощью кнопок `+`, `▽`, `Х` можно добавить новый шаг в секцию,
открыть/закрыть список уже существующих шагов, полностью удалить секцию соответсвенно. У каждой секции должно быть свое уникальное имя 
(Написать два одинаковых программа ва не позволит)
Аналогично у шага можно редактировать его номер, добавлять файлы с данными, открывать/закрывать список добавленных файлов,
удалять шаг. Номер уникален для каждого шага. Добавленные файлы должны иметь разное базвое название по формату `DEFAULT_A_0mm_0.csv`,
В противном случае в проекте останется только последний добавленный файл с повторяющимся именем.
Файлы также можно удалять с помощь кнопки `Х`. 
Пока что изменение имени или номера шага соответсвенно для Секции или Шага сотрет все что есть внутри них.
Галочки у каждого раздела означает, необходимо ли учитывать файл в построении осциллограммы.

### Осциллограмма
Если в скважину добавлены файлы, то с помощью кнопки в верхней панеле
можно построить осциллограмму выбранных файлов (поставлена голчка напротив).
Также строиться Таблица максимумов.

### Частотная характеристика
Для построения частотной характеристики для одного датчика необходим 21 файл с данными в одном шаге.
Также в окне доступна возможность настройки визуализации участка скважины с трещинами.
Настройка производиться в окне называемом кнопкой `Задать параметры трубы`. 
В данном окне есть возможность настроить в соответствующих полях `Длину`, `Диаметр внутренности`, `Толщину стенок`,
`Направление прозвучки`, `Имена датчиков`. А также добавить трещены - `+ Добавить`. `Принять` - все внесенные изменения в настройку секции вступят в силу.
`Отмена` -  все внесенные изменения в настройку секция отменяться, все вернется в настройку до открытия окна.
У каждой трещины можно настроить `Cторону` ее расположения - Верхняя/Нижняя, `Глубину` трещены, `Позицию` на трубе.
 
### График зависимости амплитуды во времени
График можно построить для каждого датчика секции по отдельности, он строиться по имеющимся шагам.
То есть для построения необходимо иметь минимум два шага для датчика, заполненные файлами. 

### Роза ветров
Роза ветров строиться по датчикам секции по номерам измерений для абсолютных значений или для относительных.
Чтобы выбрать способ отображение есть галочка `Абсолютное значение`.
С помощью слайдера можно выбирать номер измерения для отображения соответствующей розы.

'''