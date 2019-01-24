from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

appl = QApplication([])

make_window = QWidget()
l = QVBoxLayout()

l.addWidget(QPushButton('Button 1'))
l.addWidget(QPushButton('Button 2'))

make_window.setLayout(l)
make_window.show()

appl.exec_()
