import os
from datetime import datetime, timezone


class ManagerBackups:

    def __init__(self):
        self.path_dir = '/home/bolivar/backup_switches/'

    def __delete_old(self, path_dir) -> dict:
        cont = 0
        all_ordened_files = sorted(os.listdir(path_dir))
        all_ordened_files.reverse()
        if len(all_ordened_files) > 30:
            for file in all_ordened_files:
                cont += 1
                if cont > 30:
                    # deleta os arquivos (mantem os últimos 30 de cada diretório)
                    command = f"rm {path_dir}/{file}"
                    print(command)
                    os.system(command)

    def __get_all_dirs(self) -> dict:
        all_dirs: list = []
        for dir in os.listdir(self.path_dir):
            if 'st-' in dir or 'stpoe-' in dir:
                path = self.path_dir + dir
                all_dirs.append(path)
        return all_dirs

    def manager_bkp(self):
        all_dirs = self.__get_all_dirs()
        for path_dir in all_dirs:
            self.__delete_old(path_dir)


if __name__ == '__main__':
    mb = ManagerBackups()
    dates = mb.manager_bkp()
