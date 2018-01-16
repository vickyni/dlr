HOSTNAME = '9.112.57.52'
PORT = 4444
PARMFILE_NAME = 'dlr.xlsx'
DEF_SHEET_NAME = 'request'
WAITSEC = 30
IS_REMOTE = True
USERNAME = ''
PASSWORD = ''
IS_USER_NEEDED = True

INVALID_VALUES = ['n/a','none,','na', '']

BASE_URL = 'https://w3-03.ibm.com/transform/bacc/cognos/bi01n/ServletGateway/servlet/\
Gateway?b_action=cognosViewer&ui.action=run&ui.object=%2fcontent%2ffolder%5b\
%40name%3d%27IMG%27%5d%2ffolder%5b%40name%3d%27IMG%20NETEZZA%27%5d%2fpackage%\
5b%40name%3d%27IMG%20All%20Labor%20Package%27%5d%2freport%5b%40name%3d%27GDDM%\
20Various%20Labor%20Reports%27%5d&ui.name=GDDM%20Various%20Labor%20Reports&\
run.outputFormat=&run.prompt=true'