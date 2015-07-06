__author__ = 'HayatoKimura'
"""
checkconfig(
  check_index, #検索コンフィグ
  configls     #read_all()で取得したコンフィグリスト
)
戻り値 検索コンフィグがコンフィグリストに存在するときにTrueを返します
"""
def checkconfig(check_index,configls):
    checkflg = False
    for i in range(0,len(configls)):
        TrueIsexist = check_index in configls[i]
        if TrueIsexist==True:
            checkflg=True
            return checkflg

    return checkflg

