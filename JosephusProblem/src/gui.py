from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from use_case.read_3_types_files import ZipReader
from use_case.read_3_types_files import CsvReader
from use_case.read_3_types_files import ExcelReader
from use_case.get_people_list import get_people_list
from use_case.entity.josephus_circle import JosephusCircle
from use_case.entity.person import Person


class GuiJosephusCircle:
    def __init__(self):
        # 从文件中加载UI定义
        qfile_josephus_circle = QFile("src/ui/gui_josephus_circle.ui")
        qfile_josephus_circle.open(QFile.ReadOnly)
        qfile_josephus_circle.close()
        # 从 UI 定义中动态创建一个相应的窗口对象ui,控件对象成为窗口对象window的属性
        self.window = QUiLoader().load(qfile_josephus_circle)
        self.window.button_input_by_filepath.clicked.connect(
            self.get_people_list_by_filepath)
        self.window.button_input_by_hand.clicked.connect(
            self.get_people_list_by_hand)
        self.window.button_show_josephus_circle.clicked.connect(
            self.show_josephus_circle)

    def get_people_list_by_filepath(self):
        filepath = self.window.filepath.currentText()
        if filepath.endswith('.xls'):
            reader = ExcelReader(filepath)
        elif filepath.endswith('.csv'):
            reader = CsvReader(filepath)
        elif filepath.endswith('.zip'):
            reader = ZipReader(filepath, "lastname&firstname&id.csv")
        read_list = reader.read()
        self.people_list = get_people_list(read_list)
        QMessageBox.about(self.window, '录入结果', '人员信息录入成功')
        return self.people_list

    def get_people_list_by_hand(self):
        self.people_list = []
        people_data = self.window.people_data_eidt.toPlainText()
        for line in people_data.splitlines():
            if not line.strip():  # 跳过空行
                continue
            line_data = line.split(' ')
            line_data = [
                person_data for person_data in line_data if person_data]
            last_name, first_name, id = line_data
            self.people_list.append(Person(last_name, first_name, id))
        QMessageBox.about(self.window, '录入结果', '人员信息录入成功')
        return self.people_list

    def show_josephus_circle(self):
        interval = int(self.window.interval_eidt.text())
        start = int(self.window.start_eidt.text())
        self.josephus_circle = JosephusCircle(
            self.people_list, interval, start)
        for person in self.josephus_circle:
            QMessageBox.about(self.window, '约瑟夫环输出结果', person.__str__())
        return self.josephus_circle


if __name__ == '__main__':
    app = QApplication([])  # QApplication 提供了整个图形界面程序的底层管理功能
    josephus_circle = GuiJosephusCircle()
    josephus_circle.window.show()  # 使得放在主窗口的控件，要能全部显示在界面
    app.exec_()  # 进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理
