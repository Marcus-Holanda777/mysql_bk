import os
from subprocess import Popen
from datetime import datetime
import zipfile
import shutil


class Mysqlbk:
    def __init__(self, periodo: datetime, raiz: str, host: str,
                 db: str, usa: str, pw: str = '') -> None:
        self.periodo = periodo.strftime('%Y%m%d_%Hh%Mm%Ss')
        self.raiz = raiz
        self.host = host
        self.db = db
        self.usa = usa
        self.pw = pw

    def compactarBk(self, saida):
        try:
            with zipfile.ZipFile(saida[:-3] + 'zip', 'w') as zipar:
                zipar.write(saida, saida.split('\\')[-1], compress_type=zipfile.ZIP_DEFLATED)
        except Exception as e:
            print(e)
        else:
            os.unlink(saida)
    
    def copiarBk(self, origem: str) -> None:
        destino = '\\\\pmenos\\setores\\ProjetodePrevencaodePerdas\\09. Provisório\Marcus\\bk_mysql'
        arq = origem.split('\\')[-1][:-3] + '.zip'

        shutil.copy(origem[:-3] + 'zip', os.path.join(destino, arq))


    def fazerBackup(self, pastasaida: str) -> None:
        if not os.path.isdir(pastasaida):
            os.mkdir(pastasaida)
        saida = os.path.join(pastasaida, '%s%s.sql' % (self.db, self.periodo))
        comando = f'mysqldump -h {self.host} -u{self.usa} -p{self.pw} --column-statistics=0 {self.db} > {saida}'

        Popen(comando, cwd=self.raiz, shell=True).wait()

        self.compactarBk(saida)
        self.copiarBk(saida)


my = Mysqlbk(datetime.now(),
             'C:\Program Files\MySQL\MySQL Workbench 8.0',
             '127.0.0.1', 'lojas', 'marcus', 'abcd.1234')

saida = r'c:\bk_mysql'
my.fazerBackup(saida)
