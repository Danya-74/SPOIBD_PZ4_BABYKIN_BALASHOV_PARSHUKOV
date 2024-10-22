import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QTextEdit, QTabWidget, QLabel, QLineEdit, QFormLayout, QMessageBox
)


class TabApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Приложение")
        self.setGeometry(300, 100, 800, 600)

        # Центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Вкладки
        self.tabs = QTabWidget()

        # Добавляем вкладки
        self.tabs.addTab(self.scan_folder_tab(), "Сканировать папку")
        self.tabs.addTab(self.edit_file_tab(), "Редактировать файл")
        self.tabs.addTab(self.save_text_tab(), "Сохранить текст")
        self.tabs.addTab(self.form_tab(), "Сохранить данные с формы")
        self.tabs.addTab(self.read_list_tab(), "Читать лист")

        # Расположение
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.central_widget.setLayout(layout)

    def scan_folder_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.folder_label = QLabel("Выберите папку:")
        self.folder_button = QPushButton("Сканировать папку")
        self.file_list = QTextEdit()

        self.folder_button.clicked.connect(self.scan_folder)

        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_button)
        layout.addWidget(self.file_list)
        tab.setLayout(layout)

        return tab

    def scan_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder:
            self.file_list.clear()
            for root, dirs, files in os.walk(folder):
                for file in files:
                    self.file_list.append(os.path.join(root, file))

    def edit_file_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.file_content = QTextEdit()
        self.open_button = QPushButton("Открыть файл")
        self.save_button = QPushButton("Сохранить изменения")

        self.open_button.clicked.connect(self.open_file)
        self.save_button.clicked.connect(self.save_file)

        layout.addWidget(self.file_content)
        layout.addWidget(self.open_button)
        layout.addWidget(self.save_button)
        tab.setLayout(layout)

        return tab

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as f:
                self.file_content.setText(f.read())

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(self.file_content.toPlainText())

    def save_text_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.text_to_save = QTextEdit()
        self.save_text_button = QPushButton("Сохранить текст в файл")

        self.save_text_button.clicked.connect(self.save_text)

        layout.addWidget(self.text_to_save)
        layout.addWidget(self.save_text_button)
        tab.setLayout(layout)

        return tab

    def save_text(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
        if folder:
            file_name = os.path.join(folder, "output.txt")
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(self.text_to_save.toPlainText())
            QMessageBox.information(self, "Успех", "Текст успешно сохранён!")

    def form_tab(self):
        tab = QWidget()
        layout = QFormLayout()

        self.field1 = QLineEdit()
        self.field2 = QLineEdit()
        self.field3 = QLineEdit()
        self.field4 = QLineEdit()
        self.field5 = QLineEdit()

        self.save_form_button = QPushButton("Сохранить данные")
        self.save_form_button.clicked.connect(self.save_form_data)

        layout.addRow("Поле 1:", self.field1)
        layout.addRow("Поле 2:", self.field2)
        layout.addRow("Поле 3:", self.field3)
        layout.addRow("Поле 4:", self.field4)
        layout.addRow("Поле 5:", self.field5)
        layout.addWidget(self.save_form_button)
        tab.setLayout(layout)

        return tab

    def save_form_data(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить данные формы", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'a', encoding='utf-8') as f:
                f.write(f"Поле 1: {self.field1.text()}\n")
                f.write(f"Поле 2: {self.field2.text()}\n")
                f.write(f"Поле 3: {self.field3.text()}\n")
                f.write(f"Поле 4: {self.field4.text()}\n")
                f.write(f"Поле 5: {self.field5.text()}\n")
            QMessageBox.information(self, "Успех", "Данные формы успешно сохранены!")

    def read_list_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.list_content = QTextEdit()
        self.load_list_button = QPushButton("Загрузить лист")

        self.load_list_button.clicked.connect(self.load_list)

        layout.addWidget(self.list_content)
        layout.addWidget(self.load_list_button)
        tab.setLayout(layout)

        return tab

    def load_list(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                self.list_content.setText("".join(lines))

app = QApplication(sys.argv)
window = TabApp()
window.show()
sys.exit(app.exec_())