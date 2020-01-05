import zipfile
import os
# BASE_STATIC_CASE_RESULT:我Django static下面的某个路径
BASE_STATIC_CASE_RESULT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_STATIC_CASE_RESULT)
base_dir = os.path.join(BASE_STATIC_CASE_RESULT, 'report')  # 要压缩文件夹的根路径
zip_file_name = 'report.zip'
f = zipfile.ZipFile(os.path.join(BASE_STATIC_CASE_RESULT, zip_file_name), 'w', zipfile.ZIP_DEFLATED)
for dir_path, dir_name, file_names in os.walk(base_dir):
    # 要是不replace，就从根目录开始复制
    file_path = dir_path.replace(base_dir, '')
    # 实现当前文件夹以及包含的所有文件
    file_path = file_path and file_path + os.sep or ''
    for file_name in file_names:
        f.write(os.path.join(dir_path, file_name), file_path + file_name)
f.close()