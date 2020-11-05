import os
from typing import List


class PathOperator(object):
    def __init__(self):
        pass

    @classmethod
    def create_file(cls, filename: str):
        path = filename[0:filename.rfind("/")]
        if not os.path.isdir(path):  # 无文件夹时创建
            os.makedirs(path)
        if not os.path.isfile(filename):  # 无文件时创建
            fd = open(filename, mode="w", encoding="utf-8")
            fd.close()
        else:
            pass

    @classmethod
    def mkdir(cls,path:str):
        if not os.path.isdir(path):  # 无文件夹时创建
            os.makedirs(path)

    @classmethod
    def home_dir(cls)->str:
        return os.path.expanduser("~")
    
    @classmethod
    def file_abs_path_in(cls,dir:str)->List[str]:
        paths=[]
        for filename in os.listdir(dir):
            paths.append(os.path.join(dir,filename))
        return paths

    @classmethod
    def remove_file(cls,file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)




