__author__ = 'HayatoKimura'
"""
checkconfig(
  check_index, #�����R���t�B�O
  configls     #read_all()�Ŏ擾�����R���t�B�O���X�g
)
�߂�l �����R���t�B�O���R���t�B�O���X�g�ɑ��݂���Ƃ���True��Ԃ��܂�
"""
def checkconfig(check_index,configls):
    checkflg = False
    for i in range(0,len(configls)):
        TrueIsexist = check_index in configls[i]
        if TrueIsexist==True:
            checkflg=True
            return checkflg

    return checkflg

