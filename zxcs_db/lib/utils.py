import base64
import codecs
import hashlib
import re
import socket
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Union

import chardet
import xmltodict
from loguru import logger


def camel_case(string: str) -> str:
    """
    将 a_bc_de 转换为 aBcDe
    """
    string = re.sub(r"(_|-)+", " ", string).title().replace(" ", "")
    return string[0].lower() + string[1:]


def req_json(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res.status_code != 200:
            logger.error(f"{func.__name__} fail: {res.content}")
            return {}
        return res.json()

    return wrapper


class Common:
    @staticmethod
    def get_host_ip() -> str:
        """
        查询本机ip地址

        Returns:
            本机IP
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    @staticmethod
    def base64(s: str) -> str:
        return base64.b64encode(s.encode("utf-8")).decode()

    @staticmethod
    def is_contain_chinese(s: str):
        for c in s:
            if "\u4e00" <= c <= "\u9fff":
                return True
        return False

    @staticmethod
    def timing_val(func):
        def wrapper(*arg, **kw):
            t1 = time.time()
            res = func(*arg, **kw)
            t2 = time.time()
            logger.debug(f"【TIME】{func.__name__} 运行了 {(t2 -t1)}")
            return res

        return wrapper

    @staticmethod
    def get_file_encoding(file: Path) -> str:
        content = codecs.open(file, "rb").read(1024)
        return chardet.detect(content)["encoding"]

    @staticmethod
    def check_xml_format(file: Path) -> bool:
        """
        检查 xml 文件格式

        params:
            file: xml 文件

        return:
            bool True - 文件格式正确； False - 文件格式不正确
        """
        xmllint_cmd = "xmllint --format --noout {}"
        code = subprocess.call(xmllint_cmd.format(file.absolute()), shell=True)
        if code == 0:
            return True
        org_enc = Common.get_file_encoding(file)
        content = codecs.open(file, "r", encoding=org_enc, errors="ignore").read()
        tmp_file = NamedTemporaryFile()
        codecs.open(tmp_file.name, "w", encoding="utf-8").write(content)
        code = subprocess.call(xmllint_cmd.format(tmp_file.name), shell=True)
        if code == 0:
            return True
        try:
            xmltodict.parse(content)
            return True
        except Exception:
            pass
        try:
            ET.fromstring(content)
            return True
        except Exception:
            pass
        return False

    @staticmethod
    def convert_file_encoding(source: Path, target: Path = None, out_enc="utf-8"):
        if not source.is_file():
            raise Exception(f"{source} is not a file")
        source_encoding = Common.get_file_encoding(source)
        if not source_encoding:
            raise Exception(f"unknow encoding: {source}")
        if source_encoding == out_enc:
            return
        content = codecs.open(source, "rb").read()
        if not target:
            target = source
        codecs.open(target, "wb").write(
            # content.decode(source_encoding, errors="ignore").encode(out_enc)
            content.decode("ascii", errors="ignore").encode(out_enc)
        )
        return Path(target)

    @staticmethod
    def compute_md5(file: Union[str, Path]) -> str:
        """
        计算文件的md5

        Args:
            file: 文件路径

        Returns:
            md5值，字符串
        """
        m = hashlib.md5()
        if isinstance(file, str):
            file = Path(file)

        if not file.exists():
            raise Exception("{} doesn't exist".format(file))

        with file.open("rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                m.update(data)
        return m.hexdigest()
