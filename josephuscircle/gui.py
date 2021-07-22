from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from .josephus import Person
from josephus import JosephusCircle
from josephus import ExcelReader
from josephus import CsvReader
from josephus import ZipReader
from josephus import get_people_list

class GuiJosephusCircle:
    def __init__(self):
        # 从文件中加载UI定义
        qfile_josephus_circle = QFile("ui/qt_josephus_circle.ui")
        qfile_josephus_circle.open(QFile.ReadOnly)
        qfile_josephus_circle.close()
        # 从 UI 定义中动态创建一个相应的窗口对象ui,控件对象成为窗口对象ui的属性
        self.ui = QUiLoader().load(qfile_josephus_circle)
        self.ui.button_input_by_filepath.clicked.connect(self.get_people_list_by_filepath)
        self.ui.button_input_by_hand.clicked.connect(self.get_people_list_by_hand)
        self.ui.button_show_josephus_circle.clicked.connect(self.show_josephus_circle)

    def get_people_list_by_filepath(self):
        filepath = self.ui.filepath.currentText()
        if filepath.endswith('.xls') :
            reader = ExcelReader(filepath)
        elif filepath.endswith('.csv') :
            reader = CsvReader(filepath)
        elif filepath.endswith('.zip') :
            reader = ZipReader(filepath,"lastname&firstname&id.csv")
        read_list = reader.read()
        self.people_list = get_people_list(read_list)
        QMessageBox.about(self.ui,'录入结果','人员信息录入成功')
        return self.people_list

    def get_people_list_by_hand(self):
        self.people_list = []
        people_data = self.ui.people_data_eidt.toPlainText()
        for line in people_data.splitlines():
            if not line.strip():  # 跳过空行
                continue
            line_data = line.split(' ')
            line_data = [person_data for person_data in line_data if person_data]
            last_name,first_name,id = line_data
            self.people_list.append(Person(last_name,first_name,id))
        QMessageBox.about(self.ui,'录入结果','人员信息录入成功')
        return self.people_list

    def show_josephus_circle(self):
        interval = int(self.ui.interval_eidt.text())
        start = int(self.ui.start_eidt.text())
        self.josephus_circle = JosephusCircle(self.people_list,interval,start)
        for person in self.josephus_circle:   
            QMessageBox.about(self.ui,'约瑟夫环输出结果',person.__str__())
        return self.josephus_circle

if __name__ == '__main__':
    app = QApplication([]) #QApplication 提供了整个图形界面程序的底层管理功能
    josephus_circle = GuiJosephusCircle()
    josephus_circle.ui.show()  #使得放在主窗口的控件，要能全部显示在界面
    app.exec_()  #进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理