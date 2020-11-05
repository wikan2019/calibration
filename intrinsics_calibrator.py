import os
from path_operator import PathOperator
from typing import List
import xml.etree.ElementTree as ET
from json_interf import JsonInterf
import numpy as np


class intrinsics_calibrator(object):
    def __init__(self):
        pass

    @classmethod
    def calibrate_intrinsics(cls, image_dir: str):
        for i in range(0, 4):
            cmd = "matlab -nodesktop -batch \""
            save_intrinsics_path = image_dir + "/cam" + str(i) + ".txt"
            save_error_path=image_dir+ "/cam"+str(i)+"_error.txt"
            raw_image_dir = image_dir + "/cam" + str(i)
            cmd += "addpath(\'~/Projects/Intrinsics_calibration/matlab\');"
            cmd += "image_dir=\'" + raw_image_dir + "\';"
            cmd += "save_path=\'" + save_intrinsics_path + "\';"
            cmd+="error_path=\'" +save_error_path + "\';"
            cmd += "intrinsics_calibration(image_dir,save_path,error_path);"
            cmd += "exit"
            cmd += "\""
            print(cmd)
            os.system(cmd)

    @classmethod
    def sort_out_result(cls,image_dir:str):
        result_content={}
        for i in range(0,4):
            id="cam"+str(i)
            result_content[id]=cls.calibrate_result(i,image_dir)
        JsonInterf.save(result_content,os.path.join(image_dir,"res_total.json"))

    @classmethod
    def calibrate_result(cls,camera_idx:int,image_dir:str)->dict:
        camera_result={}
        intrinsics=np.loadtxt(os.path.join(image_dir,"cam"+str(camera_idx)+".txt"))
        camera_result["intrinsics"]=intrinsics.tolist()
        intrinsics_error=np.loadtxt(os.path.join(image_dir,"cam"+str(camera_idx)+"_error.txt"))
        camera_result["intrinsics_error"]=intrinsics_error.tolist()
        return camera_result

    @classmethod
    def remove_non_chess_images(cls, intrinsics_img_dir: str,
                                remove_non_chess_img_pro_dir: str):
        for i in range(0, 4):
            cam_dir = os.path.join(intrinsics_img_dir, "cam" + str(i))
            image_files = PathOperator.file_abs_path_in(cam_dir)
            cls.save_vidmxl(image_files, remove_non_chess_img_pro_dir)
            cls.run_remove_non_chess_img_exe(remove_non_chess_img_pro_dir)
            cls.remove_image_excluve_in(intrinsics_img_dir, i)

    @classmethod
    def save_vidmxl(cls, image_files: List[str],
                    remove_non_chess_img_pro_dir: str):
        print(image_files)
        text = cls.file_path_list_to_string(image_files)
        xml_path = os.path.join(remove_non_chess_img_pro_dir, "VID5.xml")
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for elem in root.iter('images'):
            elem.text = text
        tree.write(xml_path)
        with open(xml_path, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('<?xml version="1.0"?>\n' + content)

    @classmethod
    def file_path_list_to_string(cls,image_files:List[str])->str:
        image_string='\n'
        for image_path in image_files:
            image_string+=image_path+"\n"
        return image_string

    @classmethod
    def run_remove_non_chess_img_exe(cls, remove_non_chess_img_pro_dir: str):
        exe_path = os.path.join(remove_non_chess_img_pro_dir, "build",
                                "SelectFullCornerImage")

        parameter_path = os.path.join(remove_non_chess_img_pro_dir, "in_VID5.xml")
        cmd = exe_path + " " + parameter_path
        print(cmd)
        os.system(cmd)

    @classmethod
    def remove_image_excluve_in(cls, intrinsics_img_dir: str, idx: int):
        idx_list = [0, 1, 2, 3]
        idx_list.remove(idx)
        excluve_camera_image_dir = os.path.join(intrinsics_img_dir,
                                                "cam" + str(idx))
        for filename in os.listdir(excluve_camera_image_dir):
            for camera_idx in idx_list:
                duplicate_image_path = os.path.join(intrinsics_img_dir,
                                                    "cam" + str(camera_idx),
                                                    filename)
                PathOperator.remove_file(duplicate_image_path)

