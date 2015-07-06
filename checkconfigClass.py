__author__ = 'HayatoKimura'
from time import sleep
import telnetlib

class Conf:
    conf_list=""
    def __init__(self,user_name="",hostname="",password="",rawdata=None):
        """

        :param user_name:���[�U�[��
        :param hostname:�z�X�g��
        :param password:�p�X���[�h
        :param rawdata:�����ɃR���t�B�O���X�g���w�肵���ꍇ�����p���܂�
        """
        if rawdata==None:
            HOST = hostname     # your server
            user = user_name    # your username
            password = "*****" # your password
            tn = telnetlib.Telnet(HOST)
            tn.read_until("Password:")
            tn.write( "\n")
            tn.read_until("> ")
            tn.write("show config \n ")
            sleep(1)
            tn.write(" ")
            sleep(1)
            tn.write("exit \n")
            self.conf_list = tn.read_all()
        else:
            self.conf_list=rawdata

    def checkconfig(self,check_index):
        """

        :param check_index:�����R���t�B�O
        :return:�����R���t�B�O�����݂���Ƃ�True��Ԃ��܂�
        """
        confarray=self.conf_list.split("\r\n")
        checkflg = False
        for i in range(0,len(confarray)):
            TrueIsexist = check_index in confarray[i]
            if TrueIsexist==True:
                checkflg=True
                return checkflg

        return checkflg