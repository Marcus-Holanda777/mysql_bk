import os
from subprocess import Popen
from datetime import datetime


class Mysqlbk:
    def __init__(self, periodo: datetime, raiz: str, host: str,
                 db: str, usa: str, pw: str = '') -> None:
        self.periodo = periodo.strftime('%Y%m%d_%Hh%Mm%Ss')
        self.raiz = raiz
        self.host = host
        self.db = db
        self.usa = usa
        self.pw = pw

    def fazerBackup(self, pastasaida: str) -> None:
        if not os.path.isdir(pastasaida):
            os.mkdir(pastasaida)
        saida = os.path.join(pastasaida, '%s%s.sql' % (self.db, self.periodo))
        comando = f'mysqldump -h {self.host} -u{self.usa} -p{self.pw} --column-statistics=0 {self.db} > {saida}'

        Popen(comando, cwd=self.raiz, shell=True).wait()


my = Mysqlbk(datetime.now(),
             'C:\Program Files\MySQL\MySQL Workbench 8.0 CE',
             'DESKTOP-GUPDSBD', 'perdaconhecida', 'marcus', 'abcd.1234')
my.fazerBackup(r'c:\bbk')
