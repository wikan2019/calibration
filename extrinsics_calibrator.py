import os


class extrinsics_calibrator(object):
    def __init__(self):
        pass

    @classmethod
    def calibrater_extrinsics(cls, extrinsics_configs_path: str):
        calibrator_exe_path = "~/Projects/SaicCalibration/laptop/calibration_test"
        cmd = calibrator_exe_path + " " + extrinsics_configs_path
        os.system(cmd)

    @classmethod
    def fuse_extrinsics(cls, extrinsics_configs_path: str):
        calibrator_exe_path = "~/Projects/SaicCalibration/laptop/fusion_jsons"
        cmd = calibrator_exe_path + " " + extrinsics_configs_path
        os.system(cmd)
