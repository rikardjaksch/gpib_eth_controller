import socket


class GpibEthernet(object):
    def __init__(self):
        self.host = ''
        self.port = 0
        self.socket = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

    def connect(self, host, port):
        """
        Connect the internal socket to the destination host and port.
        :param host: String specifying the url/host for the connection.
        :param port: Integer specifying the port for the connection.
        :rtype: False if the connection failed, True otherwise.
        """
        self.host = host
        self.port = port
        try:
            self.socket.connect((self.host, self.port))
            return True
        except socket.error:
            return False

    def disconnect(self):
        """
        Disconnect the internal socket connection.
        """
        self.socket.close()

    def configure(self, data):
        """
        Configure the device that we are connected to using a dictionary
        of key-value pairs.
        :param data: Dictionary containing configuration data.
        """
        # List containing all configuration keys that we support
        valid_config_keys = ['mode', 'auto', 'addr']
        for k in data:
            if k in valid_config_keys:
                self.__send('++{} {}'.format(k, data[k]))

    def query_instrument(self, cmd):
        self.__send(cmd)
        return self.__receive()

    def write_instrument(self, cmd):
        self.__send(cmd)

    def __send(self, cmd):
        cmd += '\n'
        self.socket.send(cmd.encode('ascii'))

    def __receive(self, buffer_size=1024):
        data = self.socket.recv(buffer_size)
        return data
