# -1
利用pytest框架实现读取excel到比对请求结构，输入报告并右键发送
目录结构
:\py_tests\ # 我的是D盘的 py_tests 目录，所有操作都在 py_tests 目录内完成
    |_conf 配置文件
    ├─scripts     #编写测试用例的文件夹
    │  ├─test_case.py   # 用例脚本文件 
    │  └─__init__.py
    ├─report    --报告生成的文件夹
    │  ├─report.html   # pytest-html生成的用例报告
    │  ├─assets  # pytest-html的依赖目录
    ├─until 数据处理
    ├─logs   # 保存log文件
    ├─data   # 测试用例
    ├─pytest.ini  # 配置文件
    └─run主运行文件
