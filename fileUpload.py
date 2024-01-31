import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PySide6.QtGui import QPixmap, QImageReader, Qt


class ImageLoaderApp(QMainWindow):
    def __init__(self):
        super(ImageLoaderApp, self).__init__()

        self.setWindowTitle("Image Loader")
        self.setGeometry(100, 100, 600, 400)

        # Create widgets
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.load_button = QPushButton("Load Image", self)
        self.load_button.clicked.connect(self.show_file_dialog)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.load_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setOptions(options)

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.load_and_display_image(file_path)

    def load_and_display_image(self, file_path):
        # Check if the selected file is an image
        image_reader = QImageReader(file_path)
        if image_reader.format().toLower() not in ["png", "jpg", "jpeg", "bmp", "gif"]:
            print("Selected file is not a valid image.")
            return

        # Load the image
        pixmap = QPixmap(file_path)

        # Resize the image (you can adjust the size as needed)
        resized_pixmap = pixmap.scaled(200, 300, Qt.IgnoreAspectRatio)

        # Display the resized image
        self.label.setPixmap(resized_pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageLoaderApp()
    window.show()
    sys.exit(app.exec())
