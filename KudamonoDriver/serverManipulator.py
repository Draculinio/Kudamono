import subprocess

class ServerManipulator:

    def __init__(self):
        self.process=""

    def open_server(self, server,port=9000):
        """
        Opens the server in a subroprcess. Which server will open depends on the browser you want to use.
        :rtype: subprocess
        :param server: What kind of webdriver will be opened.
        :return: the process.
        :author: Pablo Soifer
        """
        if str.upper(server) == "CHROME":
            self.process = subprocess.Popen("chromedriver.exe --port=" + port)

    def close_server(self):
        """
        Ends the server
        :param self:
        :return:
        """
        print("Finishing webdriver server...")
        self.process.terminate()