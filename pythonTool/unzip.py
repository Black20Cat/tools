# 批量解压并添加文件后缀

import zipfile
import os
import time
import traceback
import pyzipper


# 找目录下的指定类型文件
def get_files_by_extension(directory, extension):
    file_list = []
    # print(list(os.walk(directory)))
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list


def unzip_and_rename(zip_file, password, destination_folder, new_name, flag=0):
    # 打开压缩文件 zipfile有些压缩方法不支持
    # with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_ref:
        # 设置密码
        zip_ref.setpassword(password.encode())
        # 解压文件
        zip_ref.extractall(destination_folder)

        if flag == 1:
            # 假设只有一个文件被解压，重命名它
            # 如果有多个文件，请根据需要修改此部分代码
            extracted_files = zip_ref.namelist()
            if len(extracted_files) == 1:
                original_file_path = os.path.join(destination_folder, extracted_files[0])
                new_file_path = os.path.join(destination_folder, new_name)
                os.rename(original_file_path, new_file_path)
                print(f"重命名成功: {extracted_files[0]} -> {new_name}")
            else:
                print("解压后的文件数量不为1，无法进行重命名")

        # infolist() 里面的compress_type表示压缩方法
        # first_file_info = zip_ref.infolist()[0]
        # print(first_file_info)
        # compression_method = first_file_info.compress_type

        # 返回压缩方法的名称,不是加密算法，是压缩方法
        # if compression_method == zipfile.ZIP_STORED:
        #     return "Stored (no compression)"
        # elif compression_method == zipfile.ZIP_DEFLATED:
        #     return "Deflated (standard)"
        # elif compression_method == zipfile.ZIP_BZIP2:
        #     return "BZIP2"
        # elif compression_method == zipfile.ZIP_LZMA:
        #     return "LZMA"
        # elif compression_method == zipfile.ZIP_XZ:
        #     return "XZ"
        # elif compression_method == zipfile.ZIP_AES:
        #     return "AES encrypted"
        # else:
        #     return "Unknown compression method"


file_directory = r'D:\pycharm\daima\zip'  # 替换为您的目录路径
extension = '.zip'  # 指定文件类型，例如 '.txt', '.pdf' 等

file_list = get_files_by_extension(file_directory, extension)
print(file_list)

password = 'threatbook'
# password = 'infected'
for zip_file in file_list:
    try:
        destination_folder = file_directory
        new_name = zip_file.split('\\')[-1].replace('.zip', '.lnk')
        unzip_and_rename(zip_file, password, destination_folder, new_name)  # 加参数flag来判断是否需要重命名
    except:
        print(traceback.format_exc())
        time.sleep(3)

os.system('pause')
