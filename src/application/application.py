"""
注册中心启动
"""
from eqlink.main.server import LinkServer
from eqlink.components.read_module import ReadModule
from threading import Thread

''' 子模块加载器 '''
read_module = ReadModule('configuration')


class Application:
    def __init__(self, path, store_path):
        """
        初始化
        :param path: 配置文件路径
        """
        self.server_conf = read_module.read('read_conf').AppConf(path).read_server()
        self.store_path = store_path

    def __link_server__(self):
        """
        注册中心服务初始化
        """
        LinkServer(self.server_conf, self.store_path).server_init()


def main():
    """
    启动注册中心
    """
    Thread(target=Application('configuration/profiles/app.yaml', '../storage/server_list').__link_server__).start()


if __name__ == '__main__':
    main()
