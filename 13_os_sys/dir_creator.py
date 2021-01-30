# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую
# директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти папки.
# Проверьте работу функций в этом же модуле.
import os


def create_dirs():
    for i in range(1, 10):
        current_folder = os.getcwd()
        new_dir = os.path.join(current_folder, "new_folder" + str(i))
        os.mkdir(new_dir)
        print("Directory new_folder" + str(i), "created")


def delete_dirs():
    for i in range(1, 10):
        current_folder = os.getcwd()
        new_dir = os.path.join(current_folder, "new_folder" + str(i))
        os.rmdir(new_dir)
        print("Directory new_folder" + str(i), "deleted")


if __name__ == "__main__":
    create_dirs()
    delete_dirs()
