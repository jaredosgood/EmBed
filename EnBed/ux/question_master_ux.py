import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout

class TextGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Input GUI")

        # Widgets
        self.input_area = QTextEdit()
        self.display_area = QTextEdit()
        self.display_area.setReadOnly(True)  # Make the display area read-only
        self.submit_button = QPushButton("Submit Text")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_area)
        layout.addWidget(self.display_area)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        # Signal connection
        self.submit_button.clicked.connect(self.process_user_question)

    def process_user_question(self):
        input_text = self.input_area.toPlainText()

        # Backend Processing Placeholder (Your logic goes here)
        # Example: Print the text and display it
        print("Submitted text:", input_text)
        self.display_area.setText(input_text)
        # return the 'input_text' to the backend processing function
        return input_text

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = TextGUI()
#     gui.show()
#     sys.exit(app.exec_())
