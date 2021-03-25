import sys
import glob
from inspect import getsourcefile
from os.path import abspath
import os
import find_file

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QMessageBox

import listUI
import mainUI
import settingsUI2
import addUI
import sort_listUI


# вывод таблицы с файлами (удаление файлов - сделать)
class Show_List(QMainWindow, listUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.open_file)
        self.pushButton.clicked.connect(self.delete_file)
        self.pushButton_2.clicked.connect(self.sort_table)
        self.show_table()

    def show_table(self):  # (готово)
        row = 0
        self.files = []
        if sort_params == []:
            self.files = music + videos + books
        elif sort_params != []:
            if 'music' in sort_params:
                self.files += music
            if 'video' in sort_params:
                self.files += videos
            if 'book' in sort_params:
                self.files += books
        self.tableWidget.setRowCount(len(self.files) - 1)
        for i in self.files:
            column = 0
            for j in i.split('::')[0:2:]:
                self.tableWidget.setItem(row, column, QTableWidgetItem(j))
                column += 1
            row += 1
        self.modified = {}

    def open_file(self):  # (готово)
        rows = [i.row() for i in self.tableWidget.selectedItems()]
        try:
            os.startfile(self.files[rows[0]].split('::')[2])
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setText('Не удалось открыть файл')
            msg.exec_()

    def delete_file(self):  # надо посмотреть через работу с файлами и работа с таблицами Qt
        pass

    def sort_table(self):
        global table_self
        table_self = self
        self.sort_list = Sort_Table()
        self.sort_list.show()

# настройки (готово)
class Settings(QWidget, settingsUI2.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.checkBox.stateChanged.connect(self.wav)
        self.checkBox_2.stateChanged.connect(self.txt)
        self.checkBox_3.stateChanged.connect(self.ogg)
        self.checkBox_4.stateChanged.connect(self.flac)
        self.checkBox_5.stateChanged.connect(self.aac)

    def run(self):
        r = open('settings.txt', 'w')
        r.close

    def wav(self):
        r = open('settings.txt', 'a')
        r.write('.wav')
        r.close()

    def aac(self):
        r = open('settings.txt', 'a')
        r.write('.aac')
        r.close()

    def flac(self):
        r = open('settings.txt', 'a')
        r.write('.flac')
        r.close()

    def ogg(self):
        r = open('settings.txt', 'a')
        r.write('.ogg')
        r.close()

    def txt(self):
        r = open('settings.txt', 'a')
        r.write('.txt')
        r.close()


# сортировка (готово)
class Sort_Table(QWidget, sort_listUI.Ui_Form):
    def __init__(self):
        global sort_params
        sort_params = []
        super().__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.book)
        self.checkBox_2.stateChanged.connect(self.video)
        self.checkBox_3.stateChanged.connect(self.music)
        self.pushButton.clicked.connect(self.reset)
        self.pushButton_2.clicked.connect(self.done)

    def music(self, state):
        global sort_params
        if state == Qt.Checked:
            sort_params.append('music')
        else:
            sort_params.remove('music')

    def video(self, state):
        global sort_params
        if state == Qt.Checked:
            sort_params.append('video')
        else:
            sort_params.remove('video')

    def book(self, state):
        global sort_params
        if state == Qt.Checked:
            sort_params.append('book')
        else:
            sort_params.remove('book')

    def reset(self):
        global sort_params
        sort_params = []

    def done(self):
        try:
            Show_List.show_table(table_self)
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setText('Не удалось отсортировать')
            msg.exec_()


# основное меню (готово)
class Main(QMainWindow, mainUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.liststart)
        self.pushButton_3.clicked.connect(self.settingsstart)

    def settingsstart(self):
        self.settings_start = Settings()
        self.settings_start.show()

    def liststart(self):
        self.list_start = Show_List()
        self.list_start.show()


# поиск и добавление файлов в список
find_file
f = open('list_of_books.txt', mode='r+')
sort_params = f.read().split('\n')
f.close()
books, videos, music = [], [], []
for i in sort_params:
    if 'book' in i:
        books.append(i)
    elif 'video' in i:
        videos.append(i)
    elif 'music' in i:
        music.append(i)
# список с сортировками
sort_params = []
# self для таблицы, чтобы обновлять
table_self = ''
# запуск приложения
app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())