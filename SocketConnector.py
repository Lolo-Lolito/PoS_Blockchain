

class SocketConnector():

    def __init__(self, ip , port):
        self.ip = ip
        self.port = port

    def equals(self, connector):
        if self.ip == connector.ip and self.port == connector.port:
            return True
        else : 
            return False