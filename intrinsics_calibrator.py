
import os

class intrinsics_calibrator(object):
    def __init__(self):
        pass

    @classmethod
    def calibrate_intrinsics(cls,image_dir: str):
        for i in range(0, 4):
            cmd = "matlab -nodesktop -batch \""
            save_intrinsics_path = image_dir + "/cam" + str(i) + ".txt"
            raw_image_dir = image_dir + "/cam" + str(i)
            cmd += "addpath(\'/home/huikang/Projects/Intrinsics_calibration/matlab\');"
            cmd += "image_dir=\'" + raw_image_dir + "\';"
            cmd += "save_path=\'" + save_intrinsics_path + "\';"
            cmd += "intrinsics_calibration(image_dir,save_path);"
            cmd += "exit"
            cmd += "\""
            print(cmd)
            os.system(cmd)
