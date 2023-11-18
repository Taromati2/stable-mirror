import os
import glob
import hashlib
import sys
from PIL import Image

# 创建一个全局字典来存储文件的MD5值和路径
file_dict = {}

def get_md5(file_path):
    with Image.open(file_path) as img:
        md5obj = hashlib.md5()
        md5obj.update(img.tobytes())
        hash = md5obj.hexdigest()
    return hash

def traverse_files(file_path):
    # 计算文件的MD5值
    file_md5 = get_md5(file_path)
    # 检查MD5值是否已经在字典中
    if file_md5 in file_dict:
        # 添加文件路径到列表中
        file_dict[file_md5][0].append(file_path)
        # 比较当前文件和最小文件的大小
        if os.path.getsize(file_path) < os.path.getsize(file_dict[file_md5][1]):
            # 更新最小文件
            file_dict[file_md5][1] = file_path
    else:
        # 将文件的MD5值和路径添加到字典中
        file_dict[file_md5] = [[file_path], file_path]

def process_files():
    # 遍历字典中的每个条目
    for file_md5, (file_list, min_file) in file_dict.items():
        # 删除除最小文件外的所有文件，用最小文件替换它们
        for file_path in file_list:
            if file_path != min_file:
                os.remove(file_path)
                os.link(min_file, file_path)
                print(f"重複ファイルを削除しました: {file_path}")

if __name__ == "__main__":
    #如果有argv
    if len(sys.argv) == 2:
        pattern = sys.argv[1]
        for png_file in glob.glob(pattern):
            traverse_files(png_file)
    else:
        #遍历当前目录下的所有文件夹中的png文件
        for png_file in glob.glob("**/*.png", recursive=True):
            traverse_files(png_file)
    process_files()
