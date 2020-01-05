
import xlrd
from conf.setting import EXCEL_PATH
from conf.log import logger

class GetExcelData():
    def __init__(self,file_name):
        self.file_name = file_name

    def get_data(self):
        l=[]
        book = xlrd.open_workbook(self.file_name)
        logger('file:{},class:{}'.format(__file__,self.__class__)).info(self.file_name)
        sheet = book.sheet_by_index(0)
        logger('file:{},class:{}'.format(__file__, self.__class__)).info(sheet.name)
        title = sheet.row_values(0)
        for row in range(1,sheet.nrows):
            l.append(dict(zip(title,sheet.row_values(row))))
        print(l)
        return l


if __name__ == '__main__':
    g = GetExcelData(EXCEL_PATH)
    print(EXCEL_PATH)
    g.get_data()