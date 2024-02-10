import configparser

config = configparser.RawConfigParser()
config.read("C:\\credence automation by tushar sir\\nocommon 5\\utilities\\readconfigfile.py")

#config.read("..\\Configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getEmail():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password

