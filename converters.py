import os

ping = os.system('ping 15.55.5.56')
if ping == 0:
    print('Taken')
else:
    print('Available')
