"""PYUPPAAL
"""
from .verifyta import Verifyta


def set_verifyta_path(verifyta_path: str):
    """Set verifyta path, and you will get tips if `verifyta_path` is invalid.
    This function will check whether `verifyta_path` is valid by following steps:
    1. run '{verifyta_path} -h' with cmd
    2. check whether '-h [ --help ]' is in the result

    Args:
        verifyta_path (str): absolute path to `verifyta`
    """
    Verifyta().set_verifyta_path(verifyta_path)


class DeveloperTools:
    """
    给开发者用的开发工具, 用于内部测试, 可以在多平台进行测试。 普通用户无法使用。
    """
    @staticmethod
    def get_verifyta_path_dev(uppaal_version: int = 4):
        import os

        curr_dir = os.path.dirname(os.path.abspath(__file__))

        uppaal_dir = "/home/runner/work/PyUPPAAL-Automation/PyUPPAAL-Automation/.github/workflows/uppaal64-4.1.24/"

        path_dir = {
            'Windows': os.path.join(uppaal_dir, 'bin-Windows/verifyta.exe'),
            'Linux': os.path.join(uppaal_dir, 'bin-Linux/verifyta'),
            'Darwin': os.path.join(uppaal_dir, 'bin-Darwin/verifyta')
        }
        return path_dir[Verifyta.get_env()]

    @staticmethod
    def set_verifyta_path_dev(uppaal_version: int = 4):
        """给开发者测试用的，用户别用这个

        Returns:
            None
        """
        path = DeveloperTools.get_verifyta_path_dev(uppaal_version)
        set_verifyta_path(path)
