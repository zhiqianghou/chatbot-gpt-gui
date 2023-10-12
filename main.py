from PyQt6.QtWidgets import QApplication, QTextEdit, QLineEdit, QPushButton, QMainWindow
import sys


class ChatbotWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setMinimumSize(700,500)

		# Add chat area widget
		self.chat_area = QTextEdit(self)
		self.chat_area.setGeometry(10,10,500,300)
		self.chat_area.setReadOnly(True)

		# Add e input field widget
		self.input_field = QLineEdit(self)
		self.input_field.setGeometry(10, 320, 500,30 )

		# Add the button widget
		self.button = QPushButton("Send", self)
		self.button.setGeometry(515, 320, 100, 30)
		self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
