import os
from typing import List
import json
import numpy as np
from json_interf import JsonInterf


class ConfigsWriter(object):
    def __init__(self):
        self.intrinsics_dir = None  # type: str

        self.extrinsics_dir = None  # type: str

    @classmethod
    def write_total_configs(cls, extrinsics_dir: str):
        configs = {}
        configs["vis"] = True
        configs["save_cali_img"] = True
        configs["save_cali_img_path"] = os.path.join(extrinsics_dir,
                                                     "cali_image")
        configs["mode_bak"] = "image"
        configs["camera_num"] = 4
        configs["mode"] = ["file", "image", "file", "image"]
        json_path_list = []
        for i in range(0, 4):
            json_path_list.append(
                os.path.join(extrinsics_dir, "configs_per_camera",
                             str(i) + ".json"))
        configs["cali_params_json_paths"] = json_path_list
        configs["res_json_file_num"] = 4

        res_file_paths = []
        res_index = ["front", "right", "rear", "left"]
        for i in range(0, 4):
            res_file_paths.append(os.path.join(extrinsics_dir, "res_per_camera",
                                               res_index[i] + ".json"))
        configs["res_json_file_paths"] = res_file_paths
        configs["fusion_res_json_file_path"] = os.path.join(extrinsics_dir,
                                                            "res.json")
        configs["fusion_res_bin_file_path"] = os.path.join(extrinsics_dir,
                                                           "res_camera_calib.bin")
        JsonInterf.save(configs, os.path.join(extrinsics_dir, "configs.json"))

    @classmethod
    def write_front_configs(cls, intrisics_dir: str, extrinsics_dir: str,
                            template_configs_path: str):
        configs = JsonInterf.read(template_configs_path)
        configs["video_path"] = os.path.join(extrinsics_dir, "2d-3d",
                                             "front.txt")
        path=cls.get_existed_dir(extrinsics_dir,"res_per_camera")
        configs["calibration_result_path"] = os.path.join(extrinsics_dir,
                                                          "res_per_camera",
                                                          "front.json")
        intrinsisc = np.loadtxt(os.path.join(intrisics_dir, "cam0.txt"))
        configs["intrinsics"] = intrinsisc.tolist()
        path=cls.get_existed_dir(extrinsics_dir,"configs_per_camera")
        JsonInterf.save(configs,
                        os.path.join(extrinsics_dir, "configs_per_camera",
                                     "0.json"))

    @classmethod
    def write_right_configs(cls, intrisics_dir: str, extrinsics_dir: str,
                            template_configs_path: str):
        configs = JsonInterf.read(template_configs_path)
        configs["video_path"] = os.path.join(extrinsics_dir, "image",
                                             "right.jpg")
        configs["calibration_result_path"] = os.path.join(extrinsics_dir,
                                                          "res_per_camera",
                                                          "right.json")
        intrinsisc = np.loadtxt(os.path.join(intrisics_dir, "cam1.txt"))
        configs["intrinsics"] = intrinsisc.tolist()
        JsonInterf.save(configs,
                        os.path.join(extrinsics_dir, "configs_per_camera",
                                     "1.json"))

    @classmethod
    def write_left_configs(cls, intrisics_dir: str, extrinsics_dir: str,
                           template_configs_path: str):
        configs = JsonInterf.read(template_configs_path)
        configs["video_path"] = os.path.join(extrinsics_dir, "image",
                                             "left.jpg")
        configs["calibration_result_path"] = os.path.join(extrinsics_dir,
                                                          "res_per_camera",
                                                          "left.json")
        intrinsisc = np.loadtxt(os.path.join(intrisics_dir, "cam3.txt"))
        configs["intrinsics"] = intrinsisc.tolist()
        JsonInterf.save(configs,
                        os.path.join(extrinsics_dir, "configs_per_camera",
                                     "3.json"))

    @classmethod
    def write_rear_configs(cls, intrisics_dir: str, extrinsics_dir: str,
                           template_configs_path: str):
        configs = JsonInterf.read(template_configs_path)
        configs["video_path"] = os.path.join(extrinsics_dir, "2d-3d",
                                             "rear.txt")
        configs["calibration_result_path"] = os.path.join(extrinsics_dir,
                                                          "res_per_camera",
                                                          "rear.json")
        intrinsisc = np.loadtxt(os.path.join(intrisics_dir, "cam2.txt"))
        configs["intrinsics"] = intrinsisc.tolist()
        JsonInterf.save(configs,
                        os.path.join(extrinsics_dir, "configs_per_camera",
                                     "2.json"))

    @classmethod
    def get_existed_dir(cls,dir:str,sub_dir:str)->str:
        tmp_dir=os.path.join(dir,sub_dir)
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)
        return tmp_dir
