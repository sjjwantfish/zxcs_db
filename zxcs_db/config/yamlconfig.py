import os
import shutil
from collections import UserDict

import yaml

from zxcs_db.config.options import ServerModeEnum


class YamlConfig(UserDict):
    def __init__(self, config_file=None, **kwargs):
        super(YamlConfig, self).__init__(**kwargs)
        if not config_file:
            return
        with open(config_file, encoding="utf-8") as f:
            c = yaml.full_load(f)
            self.update(c)

    @staticmethod
    def _create_config_from_template(config_file):
        if not os.path.exists(config_file):
            name, ext = os.path.splitext(config_file)
            temp_file = "%s.template%s" % (name, ext)
            if os.path.exists(temp_file):
                shutil.copyfile(temp_file, config_file)
            else:
                raise RuntimeError("no config.yaml or config.template.yaml!")

    @staticmethod
    def _create_config_by_server_mode(server_mode: ServerModeEnum) -> str:
        dir_path = os.getcwd()
        # 读取 config.yaml
        env_config_file = os.path.join(dir_path, "config.yaml")
        if not os.path.exists(env_config_file):
            YamlConfig._create_config_from_template(env_config_file)
        # if server_mode in [ServerModeEnum.local, ServerModeEnum.dev]:
        #     env_config_file = os.path.join(dir_path, "config.yaml")
        #     YamlConfig._create_config_from_template(env_config_file)
        # elif server_mode == ServerModeEnum.test:
        #     env_config_file = os.path.join(dir_path, "config.test.yaml")
        # elif server_mode == ServerModeEnum.prod:
        #     env_config_file = os.path.join(dir_path, "config.prod.yaml")
        # else:
        #     raise Exception("Unknown Server Mode")
        # if not os.path.exists(env_config_file):
        #     raise Exception(f"config file {env_config_file} not exists!")
        return env_config_file


def get_config(file_path=None):
    """读取并返回配置字典"""

    if file_path is None:
        server_mode = os.getenv("SERVER_MODE")
        file_path = YamlConfig._create_config_by_server_mode(server_mode)

    config = YamlConfig(file_path)
    return config
