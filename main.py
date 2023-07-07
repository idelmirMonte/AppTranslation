import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit
from translate import Translator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-Time Translation App")
        self.setGeometry(100, 100, 400, 300)

        self.input_label = QLabel("Input Text:", self)
        self.input_label.move(20, 20)

        self.input_text = QLineEdit(self)
        self.input_text.setGeometry(20, 50, 360, 30)

        self.translate_button = QPushButton("Translate", self)
        self.translate_button.setGeometry(150, 100, 100, 30)
        self.translate_button.clicked.connect(self.translate_text)

        self.output_label = QLabel("Translated Text:", self)
        self.output_label.move(20, 150)

        self.output_text = QTextEdit(self)
        self.output_text.setGeometry(20, 180, 360, 90)

    def translate_text(self):
        text = self.input_text.text().strip()
        dest = "es"  # Idioma de destino (por ejemplo, inglés)
        translation = translate_text(text, dest)
        self.output_text.setText(translation)


def translate_text(text, dest):
    translator = Translator(to_lang=dest)
    translation = translator.translate(text)
    return translation


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


