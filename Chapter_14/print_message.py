import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

class simple_app(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Main app window'
		self.left = 20
		self.top = 20
		self.height = 300
		self.width = 400
		self.app_initialize()
		

	def app_initialize(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.height, self.width)
		b = QPushButton('Click', self)
		b.setToolTip('Click on the button !!')
		b.move(100,70)
		self.l = QLabel(self)
		self.l.resize(100,50)
		self.l.move(100,200)
		b.clicked.connect(self.on_click)
		self.show()

	@pyqtSlot()
	def on_click(self):		
		self.l.setText("Hello World")

if __name__ == '__main__':
	appl = QApplication(sys.argv)
	ex = simple_app()
	sys.exit(appl.exec_())


