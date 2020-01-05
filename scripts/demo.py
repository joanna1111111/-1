import pytest

def setup_function():
    print("方法开始")

def teardown_function():
    print("方法结束")

def setup_module():
    print("模块开始")

def teardown_module():
    print("模块结束")

def test_01():
    print("用例1")
    assert 1
mobile_phone=[10010,10089]
code_list=[19123,310832]
@pytest.mark.parametrize('mobile,code',zip(mobile_phone,code_list))
def test_02(mobile,code):
    print("电话号码是{},验证码是{}".format(mobile,code))

def test_03():
    print("用例3")
    assert 1
def test_04():
    print("用例4")
    assert 1
def test_05():
    print("用例5")
    assert 1
def test_06():
    print("用例6")
    assert 1
def test_07():
    print("用例7")
    assert 1
def test_08():
    print("用例8")
    assert 1






if __name__ == '__main__':
    pytest.main("-s demo1.py")