import os
import re
from datetime import datetime, timezone


class RenameBackups:

    def __init__(self):
        self.path_dir = '/home/bolivar/backup_switches/'

    def __get_all_files_and_date(self) -> list:
        files_path: list = []
        for file in os.listdir(self.path_dir):
            try:
                if 'cfg' not in file:
                    path_dir_st = self.path_dir + file
                    for file in os.listdir(path_dir_st):
                        path_file = path_dir_st + '/' + file
                        files_path.append(path_file)
            except IndexError:
                pass
        return files_path

    def manager(self):
        files = self.__get_all_files_and_date()
        for path in files:
            old_name = path.split('/')[-1]
            path_dir = path.split(old_name)[0]
            year = str(datetime.today().year)
            # testa se tem data
            if year in old_name:
                # testa se a data ta no lugar correto
                if '__' in old_name:
                    pass
                    # se entrou aqui, é porque não precisa de mudança
                else:
                    # testa a data
                    try:
                        new_name = str(re.findall(r'^\w{1,5}-\w{1,15}-\d{1,4}(?:[a-zA-Z]{0,})', old_name)[0])
                        date_name = str(re.findall(r'\d{4}-\d{2}-\d{2}', old_name)[0]) + '__'
                    except IndexError:
                        stat_result = os.stat(path_dir + old_name)
                        date_name = str(datetime.fromtimestamp(stat_result.st_mtime, tz=timezone.utc).date()) + '__'

                    # print(f'data: {date_name} name: {new_name}')
                    model_name = str(
                        old_name.replace(new_name, '').replace(date_name.strip('__'), '').replace('.cfg', '')).strip()
                    if model_name == '_':
                        model_name = '_NaN_'
                    # print(model_name)

                    new_path = path_dir + date_name + new_name + model_name
                    if ' ' not in str(new_path.strip().split('_')[-2]):
                        new_path = new_path[:-1]

                    command = 'mv ' + path + ' ' + new_path + '.cfg'
                    print(command)
                    os.system(command)


if __name__ == '__main__':
    mb = RenameBackups()
    dates = mb.manager()
