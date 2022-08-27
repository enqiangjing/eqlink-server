from eqlink.components.load_conf import LoadConf, get_run_params
import sys


class AppConf(LoadConf):
    def __init__(self, path):
        """
        配置文件读取
        :param path: 配置文件路径
        """
        super().__init__(path, get_run_params(sys.argv[1:]))

    def read_server(self):
        return {
            'HOST': self.node_read('link_server.host'),
            'PORT': self.node_read('link_server.port'),
            'BUF_SIZE': self.node_read('link_server.buf_size'),
            'BACKLOG': self.node_read('link_server.backlog')
        }
