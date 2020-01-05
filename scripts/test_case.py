
from until import GetExcel,GetRequest
import xlrd
from conf.setting import EXCEL_PATH
from conf.log import logger


import pytest

class TestCase():
    try:
        @pytest.mark.parametrize('d',GetExcel.GetExcelData(EXCEL_PATH).get_data())
        def test_case(self,d):
            logger('{}'.format(__file__)).info('start projectʼ')
            response = GetRequest.RequestHandler(d).get_response()
            logger('{}'.format(__file__)).info(response)
            print(response)
            assert response[0] == response[1]
    except:
        print('2222')
