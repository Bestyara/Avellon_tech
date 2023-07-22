from PySide6.QtCore import QSize
from third_party import IntFormatting, FloatFormatting, StrFormatting

MAIN_WINDOW_TITLE = "Avellon tech"
MAIN_WINDOW_ICON_PATH = ""
MAIN_WINDOW_MINIMUM_SIZE = QSize(800, 450)
ICON_WINDOW_PATH = "resource/img/favicon.ico"
MAIN_MENU_LOGO_PATH = "resource/img/logo.png"

DEFAULT_BUTTON_SIZE = QSize(200, 50)

SENSOR_AMOUNT = 4

ALLOWED_FILE_LOAD_FORMATS = ['csv']

FILE_DIALOG_CSV_FILTER = "CSV files (*.csv)"
FILE_DIALOG_SAVE_FILTERS = ["JPG files (*.jpg; *.jpeg)", "PNG files (*.png)",
                            "JPG files (*.jpg; *.jpeg)| PNG files (*.png)"]
DEFAULT_FOLDER_NAME_FOR_SELECT = "data"
DEFAULT_FOLDER_NAME_TO_SAVE = "save_data"
TYPES_OF_SAVING_FILE = ['png', 'jpg', 'jpeg']
DEFAULT_FORMAT_OF_FILENAME = "%Y_%m_%d_%H_%M_%S"
TMP_FOR_WORK_FILENAME = "WORK_VERSION.csv"


CSV_FILE_HEADER_SIZE = 6
CSV_FILE_HEADER_CONTENT = {
    "Time Base": IntFormatting('μs'),
    "Sampling Rate": FloatFormatting('MSa/s'),
    "Amplitude":  FloatFormatting('V'),
    "Amplitude resolution": FloatFormatting('mV'),
    "Data Uint": StrFormatting(''),
    "Data points": IntFormatting(''),
}

COLOR_NAMES = ['red', 'blue', 'green', 'orange', 'pink', 'burlywood',
               'chartreuse', 'crimson', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgreen',
               'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
               'darksalmon', 'darkseagreen', 'darkslateblue', 'darkturquoise', 'darkviolet',
               'deeppink', 'deepskyblue', 'dodgerblue', 'firebrick', 'forestgreen', 'fuchsia',
               'gold', 'honeydew', 'indianred', 'lavender', 'lavenderblush', 'pink',
               'lawngreen', 'lemonchiffon', 'lightgoldenrodyellow', 'lightgreen',
               'lightsteelblue', 'lime', 'limegreen', 'magenta', 'maroon', 'mediumvioletred',
               'midnightblue', 'olive', 'orchid', 'palegoldenrod', 'plum',
               'purple', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen',
               'skyblue', 'slateblue', 'springgreen', 'steelblue', 'thistle', 'violet']


# WARNING TITLES
FILE_NOT_EXIST_WARNING_TITLE = "File not exist"
WRONG_FILENAME_WARNING_TITLE = "Wrong filename"
INCORRECT_FILE_CONTENT_WARNING_TITLE = "Incorrect file content"
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