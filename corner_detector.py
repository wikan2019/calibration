import os
from json_interf import JsonInterf
import numpy as np
from path_operator import PathOperator
import shutil


class CornerDetector(object):
    def __init__(self):
        pass

    @classmethod
    def test(cls):
        cmd = "cd ~/Shell &&"
        cmd += " vim "
        os.system(cmd)

    @classmethod
    def corner_detect(cls, image_path: str):
        exe_path = "/home/huikang/saic_calibration/CORNER_DETECT/build "
        cmd = "cd " + exe_path
        cmd += "&& ./corner_detect "
        cmd += image_path
        print(cmd)
        os.system(cmd)

    @classmethod
    def prepare_dir(cls, extrinsics_image: str):
        pixel_pair_dir = os.path.join(extrinsics_image, "2d-3d")
        front_3d_txt = os.path.join(pixel_pair_dir, "front_3d.txt")
        rear_3d_txt = os.path.join(pixel_pair_dir, "rear_3d.txt")
        PathOperator.create_file(front_3d_txt)
        PathOperator.create_file(rear_3d_txt)

    @classmethod
    def prepare_file(cls, extrinsics_image: str):
        image_dir = os.path.join(extrinsics_image, "image")
        PathOperator.mkdir(image_dir)
        name_list = ['front', 'right', "rear", "left"]
        for i in range(0, 4):
            source_image = os.path.join(extrinsics_image, "sop_cali_img",
                                        name_list[i] + "_raw.jpg")
            target_image = os.path.join(extrinsics_image, "image",
                                        name_list[i] + ".jpg")
            shutil.copyfile(source_image, target_image)

    @classmethod
    def front_2d_3d_merge(cls, extrinsics_image_dir: str):
        exe_path = "/home/huikang/saic_calibration/CORNER_DETECT/build"
        two_d_path = os.path.join(exe_path, "deug.txt")
        two_d_pixel = JsonInterf.read(two_d_path)

        three_d_coords = np.loadtxt(
            os.path.join(extrinsics_image_dir, "2d-3d", "front_3d.txt"))
        two_d_three_d_array = []
        for i in range(0, three_d_coords.shape[0]):
            pixel = np.array(two_d_pixel[str(int(three_d_coords[i][0]))])
            three_d = three_d_coords[i][1:]
            two_d_three_d_array.append(np.hstack([pixel, three_d]))
        two_d_three_d_array = np.vstack(two_d_three_d_array)
        np.savetxt(os.path.join(extrinsics_image_dir, "2d-3d", "front.txt"),
                   two_d_three_d_array, fmt='%0.6f')

    @classmethod
    def rear_2d_3d_merge(cls, extrinsics_image_dir: str):
        exe_path = "/home/huikang/saic_calibration/CORNER_DETECT/build"
        two_d_path = os.path.join(exe_path, "deug.txt")
        two_d_pixel = JsonInterf.read(two_d_path)
        three_d_coords = np.loadtxt(
            os.path.join(extrinsics_image_dir, "2d-3d", "rear_3d.txt"))
        two_d_three_d_array = []
        for i in range(0, three_d_coords.shape[0]):
            pixel = np.array(two_d_pixel[str(int(three_d_coords[i][0]))])
            three_d = three_d_coords[i][1:]
            two_d_three_d_array.append(np.hstack([pixel, three_d]))
        two_d_three_d_array = np.vstack(two_d_three_d_array)
        np.savetxt(os.path.join(extrinsics_image_dir, "2d-3d", "rear.txt"),
                   two_d_three_d_array, fmt='%0.6f')
