import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QScrollArea

class ScrollableTextWidgets(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建一个滚动区域
        scroll_area = QScrollArea()

        # 创建一个主窗口，包含多个文本框
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        for i in range(5):
            text_edit = QTextEdit()
            layout.addWidget(text_edit)

        # 设置主窗口为滚动区域的小部件
        scroll_area.setWidget(main_widget)
        scroll_area.setWidgetResizable(True)

        # 创建垂直布局
        main_layout = QVBoxLayout()

        # 将滚动区域添加到垂直布局
        main_layout.addWidget(scroll_area)

        # 将布局设置为主窗口的布局
        self.setLayout(main_layout)

        self.setWindowTitle('Scrollable Text Widgets')
        self.setGeometry(100, 100, 400, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScrollableTextWidgets()
    sys.exit(app.exec_())
