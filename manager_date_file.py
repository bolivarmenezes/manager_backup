import os
from datetime import datetime, timezone
import glob


class ManagerBackups:

    def __init__(self):
        self.path_dir = '/home/bolivar/backup_switches/'
        print(f"diretório: {self.path_dir}")

    def get_last_date(self):
        file_and_date: dict = {}
        all_paths = self.__get_path_dir()
        # para cada diretório, varre os arquivos e ordena (decrescente) por data
        for path in all_paths:
            files = glob.glob(path + '/*')
            for file in files:
                print(file)

    def __get_path_dir(self):
        dir = glob.glob(self.path_dir + '/*')
        path_dir = []
        for path in dir:
            # print(path)
            path_dir.append(path)
        return path_dir

    def manager_bkp(self):
        print(f'função do manager_bkp')
        file_and_date = self.__get_all_files_and_date()
        for path in file_and_date.keys():
            date = file_and_date[path]
            dir = path.split('/st')[0] + '/'
            name_dir = path.split('/')[-1].split('_')[0].split('.')[0]
            print(f'diretorio name_dir: {name_dir}')
            year = str(date.today().year)
            if year not in path:
                print(f'tem ano: {year}')
                new_name = str(date) + '__' + path.split('/')[-1]
                print(f'Nome: {new_name}')
                # new_name = path.split('.cfg')[0] + '_' + str(date) + '.cfg'
            else:
                new_name = path
                print(f'new_name: {new_name}')

            # cria o diretório
            self.__create_dir_if_no_exist(name_dir)

            # renomeia o arquivo, para adicionar a data, se ainda não foi renomeado
            if year not in path:
                command = f'mv {path} {dir}{new_name}'
                os.system(command)
                print(new_name)
                print('renomeia o arquivo, para adicionar a data, se ainda não foi renomeado')
                print(command)

            # mudar de dono
            command = f"chown debian:debian -R {dir}{new_name}"
            print(command)
            os.system(command)

            # move o arquivo pro diretório
            command = f'mv {dir}{new_name} {dir}{name_dir}/'
            print(f"move o arquivo para o diretório: {command}")
            os.system(command)


if __name__ == '__main__':
    mb = ManagerBackups()
    dates = mb.get_last_date()
