import os

def create_result_dir(dir_name="result"):
    """
    创建结果目录
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
