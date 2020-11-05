import os

from argument_parser import ArgumentParser
from configs_writer import ConfigsWriter
from corner_detector import CornerDetector
from extrinsics_calibrator import extrinsics_calibrator
from intrinsics_calibrator import intrinsics_calibrator
from path_manager import PathManager

if __name__ == '__main__':
    ArgumentParser._argument = ArgumentParser.args_parser().parse_args()
    path_manager = PathManager().set_path_manager_options(
        ArgumentParser.get_path_manager_options())

    intrinsics_calibrator.remove_non_chess_images(
        path_manager.intrinsic_image_dir(),
        path_manager.remove_non_chess_image_pro_dir())
    
    intrinsics_calibrator.calibrate_intrinsics(
        path_manager.intrinsic_image_dir())

    intrinsics_calibrator.sort_out_result(path_manager.intrinsic_image_dir())

    ConfigsWriter.write_total_configs(path_manager.extrinsics_image_dir())
    ConfigsWriter.write_front_configs(path_manager.intrinsic_image_dir(),
                                      path_manager.extrinsics_image_dir(),
                                      path_manager.front_template_camera_configs_path())

    ConfigsWriter.write_right_configs(path_manager.intrinsic_image_dir(),
                                      path_manager.extrinsics_image_dir(),
                                      path_manager.right_template_camera_configs_path())

    ConfigsWriter.write_rear_configs(path_manager.intrinsic_image_dir(),
                                     path_manager.extrinsics_image_dir(),
                                     path_manager.rear_template_camera_configs_path())

    ConfigsWriter.write_left_configs(path_manager.intrinsic_image_dir(),
                                     path_manager.extrinsics_image_dir(),
                                     path_manager.left_template_camera_configs_path())

    CornerDetector.prepare_dir(path_manager.extrinsics_image_dir())
    CornerDetector.prepare_file(path_manager.extrinsics_image_dir())
    CornerDetector.corner_detect(path_manager.front_image_path())
    CornerDetector.front_2d_3d_merge(path_manager.extrinsics_image_dir())

    CornerDetector.corner_detect(path_manager.rear_image_path())
    CornerDetector.rear_2d_3d_merge(path_manager.extrinsics_image_dir())

    extrinsics_calibrator.calibrater_extrinsics(
        path_manager.extrinsics_configs_path())
    extrinsics_calibrator.fuse_extrinsics(
        path_manager.extrinsics_configs_path())
