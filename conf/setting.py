import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH =os.path.join(BASE_DIR,'data')
EXCEL_PATH = os.path.join(DATA_PATH,'接口测试示例.xlsx')
print(EXCEL_PATH)


