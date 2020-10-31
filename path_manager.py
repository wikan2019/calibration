import os
from path_manager_options import PathManagerOptions
from path_operator import PathOperator


class PathManager(PathOperator):
    def __init__(self):
        super().__init__()
        self._data_car_sequence = ""

    def set_path_manager_options(self,
                                 path_manager_options: PathManagerOptions) -> 'PathManager':
        self._data_car_sequence = path_manager_options.data_car_sequence
        return self

    def intrinsic_image_dir(self) -> str:
        return os.path.join(self.home_dir(), "intrinsics",
                            self._data_car_sequence, "intrinsics")

    def extrinsics_image_dir(self) -> str:
        return os.path.join(self.home_dir(), 'extrinsics',
                            self._data_car_sequence)

    def template_camera_configs_dir(self) -> str:
        return os.path.join(self.home_dir(), "extrinsics", "template_configs")

    def front_template_camera_configs_path(self) -> str:
        return os.path.join(self.template_camera_configs_dir(), "0.json")

    def right_template_camera_configs_path(self) -> str:
        return os.path.join(self.template_camera_configs_dir(), "1.json")

    def rear_template_camera_configs_path(self) -> str:
        return os.path.join(self.template_camera_configs_dir(), "2.json")

    def left_template_camera_configs_path(self) -> str:
        return os.path.join(self.template_camera_configs_dir(), "3.json")

    def front_image_path(self) -> str:
        return os.path.join(self.extrinsics_image_dir(), "image", "front.jpg")

    def rear_image_path(self) -> str:
        return os.path.join(self.extrinsics_image_dir(), "image", "rear.jpg")

    def extrinsics_configs_path(self) -> str:
        return os.path.join(self.extrinsics_image_dir(), "configs.json")
