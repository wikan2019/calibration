import argparse
from path_manager_options import PathManagerOptions


class ArgumentParser(object):
    _argument = None # type: argparse.ArgumentParser

    def __init__(self):
        pass

    @classmethod
    def args_parser(cls):
        parser = argparse.ArgumentParser(description="CameraCalibration")
        parser.add_argument("--data_car_sequence", default='')
        return parser

    @classmethod
    def get_path_manager_options(cls)-> PathManagerOptions:
        path_manager_options = PathManagerOptions()
        path_manager_options.data_car_sequence = cls._argument.data_car_sequence
        return path_manager_options
