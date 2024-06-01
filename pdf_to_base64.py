import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import base64

class PDFToBase64Converter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PDF to Base64 Converter")

        # Create layout
        layout = QtWidgets.QVBoxLayout()

        # Create file selection area
        file_selection_layout = QtWidgets.QHBoxLayout()
        self.file_path_label = QtWidgets.QPlainTextEdit()
        self.file_path_label.setReadOnly(True)
        self.browse_button = QtWidgets.QPushButton("Selecionar PDF")
        self.browse_button.clicked.connect(self.select_file)
        file_selection_layout.addWidget(self.file_path_label)
        file_selection_layout.addWidget(self.browse_button)
        layout.addLayout(file_selection_layout)

        # Create conversion button
        self.convert_button = QtWidgets.QPushButton("Converter para Base64")
        self.convert_button.clicked.connect(self.convert_to_base64)
        layout.addWidget(self.convert_button)

        # Create base64 display area
        self.base64_text = QtWidgets.QPlainTextEdit()
        self.base64_text.setReadOnly(True)
        layout.addWidget(self.base64_text)

        # Set layout
        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Selecionar PDF", "", "PDF Files (*.pdf)")
        if file_path:
            self.file_path_label.setPlainText(file_path)

    def convert_to_base64(self):
        file_path = self.file_path_label.toPlainText()
        if not file_path:
            return

        try:
            with open(file_path, "rb") as pdf_file:
            
                pdf_data = pdf_file.read()
                base64_encoded_data = base64.b64encode(pdf_data).decode('utf-8')
                self.base64_text.setPlainText(base64_encoded_data)
                
        except Exception as e:
            print(f"Error converting PDF: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = PDFToBase64Converter()
    window.show()
    sys.exit(app.exec_())
