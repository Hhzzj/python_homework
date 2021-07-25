from PySide2.QtWidgets import QApplication
from ui.gui import GuiJosephusCircle

if __name__ == '__main__':
    app = QApplication([])  # QApplication 提供了整个图形界面程序的底层管理功能
    josephus_circle = GuiJosephusCircle()
    josephus_circle.window.show()  # 使得放在主窗口的控件，要能全部显示在界面
    app.exec_()  # 进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理
