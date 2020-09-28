"""Steps
1. Rename into specific way ( Factory_year_№_contract№ )
2. Have default directory
    2.1 Put file in this directory
3. Get list of files in directory
    - print(list)
4. Choose file to work with(default_index=0)
    - would be define automatically:
        +destination
        +new_name
        +info
5. Default things to do:
    - Move(destination) -> Ask "Move it here? print(destination) FIXME
    - Rename() -> apply new_name
    - create info.txt
    - create .DWG file with template(шаблон)
    - Open directory
"""
import os
import pylightxl
import shutil

from pathlib import Path


PATH_TO_FILES = Path.home() / 'Desktop/poop'
DESTINATION_ROOT = Path.home() / 'Desktop/poop goes hear'

# for testing
TEMP_EXEL = '23.xlsx'
TEMP_EXEL_PATH = Path.home() / 'Desktop/poop'


def make_dict_from_2columns_in_exel(path: str, name: str, which_list=1, column1=1, column2=2):
    """Takes:
    path to file,
    name of the file with extension,
    which list = number of list (!NOT a NAME of the list!)
    first column,
    second column.

    :return dict
    """
    data1 = pylightxl.pylightxl.readxl(str(path) + '/' + str(name))  # database with all sheets from file
    name_of_list = data1.ws_names[which_list - 1]
    sheet = data1.ws(str(name_of_list))

    col1_list = sheet.col(column1)
    col2_list = sheet.col(column2)
    how_to_name_dict = dict(zip(col1_list, col2_list))
    return how_to_name_dict


def make_list_of_info(path: str, name: str, which_list=1):
    data1 = pylightxl.pylightxl.readxl(str(path) + '/' + str(name))  # database with all sheets from file
    name_of_list = data1.ws_names[which_list - 1]
    sheet = data1.ws(str(name_of_list))
    return sheet


class WorkDocFileRenamer:
    """Only works if file named in proper way"""
    def __init__(self, name: str, path=(Path.home() / 'Desktop/poop')):
        self.name = name
        self.extension = '.' + str(name.split('.')[-1])
        self.path = path
        self.full_path = str(self.path) + '/' + name

        self.factory = self.name.split('.')[0].split()[0]
        self.year = self.name.split('.')[0].split()[1]
        self.number = self.name.split('.')[0].split()[2]

    def show(self):
        return self.name

    def should_it_be_rename(self):  # FIXME probably should rethink the concept of this function
        """:returns True or False"""
        need_length = (3, 4)
        need_extension = ['.doc', '.docx']
        length = len(self.name.split('.')[0].split())

        if self.extension in need_extension and length in need_length:
            return True
        else:
            return False

    def rename_docx(self):
        """Looking for doc file with specific name and renaming it.
        Examples:
            Factory_Year_№
            Factory_Year_№_№contract
        """
        if WorkDocFileRenamer.should_it_be_rename(self):
            name_split = self.name.split('.')[0].split()
            factory = name_split[0]
            # year = name_split[1] # for version2
            the_number = name_split[2]

            # if len(name_split) == 4:
            #     contract_number = self.name.split('.')[0].split()[3] # for version2
            # version2 new_name = contract_number + '/' + year + '-ЭПБ-20-' + the_number
            temp = make_dict_from_2columns_in_exel(str(Path.home() / 'Desktop/poop'), '23.xlsx', 3, 1, 5)  # FIXME Hardcode
            list_for_rename = dict(ННК=temp)
            new_name = (str(the_number)
                        + '.'
                        + str(list_for_rename[factory][int(the_number)]
                              + str(self.extension))
                        )

            # RENAMING
            shutil.move(self.full_path, str(self.path) + '/' + new_name)

            # updating class variables
            self.name = new_name
            self.full_path = str(self.path) + '/' + new_name

    def move(self, destination):
        full_path = self.full_path
        Path(destination).mkdir(parents=True, exist_ok=True)
        shutil.move(str(full_path), str(destination))

        # updating class variables
        self.path = destination
        self.full_path = str(self.path) + '/' + self.name

    def destination_for_docx(self):
        """:returns path for file"""
        destination = str(DESTINATION_ROOT / self.factory / 'Материалы' / self.number)
        return destination

    def create_dir_next_to_file(self, name_of_dir: str):
        Path(self.path / name_of_dir).mkdir(parents=True, exist_ok=True)

    def create_default_dirs_next_to_file(self):
        default_list = ['Фото', 'Паспорт', 'Прошлое ЭПБ', 'Проект', 'Полевые']
        for i, j in zip(default_list, range(0, len(default_list))):
            Path(self.path / default_list[j]).mkdir(parents=True, exist_ok=True)

    def remove_dir_next_to_file(self, name_of_dir: str):
        try:
            os.rmdir(self.path / name_of_dir)
        except OSError:
            print("directory must be empty")

    def remove_default_dirs_next_to_file(self):
        default_list = ['Фото', 'Паспорт', 'Прошлое ЭПБ', 'Проект', 'Полевые']
        for i, j in zip(default_list, range(0, len(default_list))):
            try:
                os.rmdir(self.path / default_list[j])
            except OSError:
                print("directory must be empty")

    def create_txt_with_info(self, path_to_exel: str, name_of_exel: str, which_list=1):
        """It's supposed to take info from exel table and make txt file with it"""
        if WorkDocFileRenamer.should_it_be_rename(self):
            the_number = self.name.split('.')[0].split()[2]
        else:
            the_number = self.name.split('.')[0]

        sheet_for_info = make_list_of_info(path_to_exel, name_of_exel, which_list)
        the_number = int(the_number) + 3  # FIXME HARDCODE (make it so it's find row by it self(list->find->get index)

        list_for_info = sheet_for_info.row(the_number)
        default_list = ['Цех:', '\nИнв.№:', '\nОбъем:']
        default_list_values = [list_for_info[2], list_for_info[3], list_for_info[5]]

        txt = open(str(self.path) + "/info.txt", "w+")
        for i, j in zip(default_list, default_list_values):
            txt.write('{} {}'.format(i, j))
        txt.close()

    def open_in_explorer(self):
        os.startfile(self.path)

    def create_dwg_template(self, place_from):  # FIXME template kinda hardcoded, isn't it?
        shutil.copy(str(place_from) + '/template.dwg', str(self.path) + '/template.dwg')


def main_function(path_to_files=Path.home() / 'Desktop/poop'):
    """
    """
    list_of_files = os.listdir(path_to_files)
    print(list_of_files)

    while True:
        try:
            chosen_file = int(input('put index of file(from 0-999):'))
            break
        except:
            print("It's should be a number")

    chosen_file = WorkDocFileRenamer(list_of_files[chosen_file], path_to_files)
    for_move_funct = chosen_file.destination_for_docx()
    chosen_file.move(for_move_funct)
    chosen_file.rename_docx()
    chosen_file.create_txt_with_info(TEMP_EXEL_PATH, TEMP_EXEL, 3)
    chosen_file.create_dwg_template(PATH_TO_FILES)
    chosen_file.open_in_explorer()



if __name__ == '__main__':
    # testing
    main_function()

    """work_list = make_dict_from_2columns_in_exel(Path.home() / 'Desktop/poop', '23.xlsx', 3, 1, 5)
    list_for_rename = dict(ННК=work_list)
    main_function()

    a = WorkDocFileRenamer('ННК 20 30.doc')
    a.destination_for_docx()"""
