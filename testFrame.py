from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QLabel, QGridLayout, QMainWindow, \
    QGraphicsDropShadowEffect


class RoundedPixmapLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setPixmap(self, pixmap):
        rounded_pixmap = self.rounded_pixmap(pixmap)
        super().setPixmap(rounded_pixmap)

    def rounded_pixmap(self, pixmap):
        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(rounded.rect(), 10, 10)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)

        return rounded


class BookElement(QFrame):
    def __init__(self, title, image_path, parent=None):
        super().__init__(parent)

        self.title = title  # Сохраняем заголовок

        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(30)
        shadow_effect.setColor(Qt.black)
        shadow_effect.setOffset(4, 4)
        self.setGraphicsEffect(shadow_effect)

        layout = QVBoxLayout(self)

        # Загружаем изображение книги
        original_pixmap = QPixmap(image_path)

        # Изменяем размер изображения с сохранением пропорций
        scaled_pixmap = original_pixmap.scaled(QSize(200, 300), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        # Добавляем изображение книги с закругленными углами
        image_label = RoundedPixmapLabel(self)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        # Добавляем текст
        text_label = QLabel(title, self)
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setMaximumWidth(200)
        text_label.setMaximumHeight(40)
        text_label.setStyleSheet("font: 16pt Comic Sans MS")

        text_per = QLabel()
        text_per.setText("Денис")
        text_per.setStyleSheet("font: 13pt")

        layout.addWidget(image_label, alignment=Qt.AlignCenter)
        layout.addWidget(text_label, alignment=Qt.AlignCenter)
        layout.addWidget(text_per, alignment=Qt.AlignCenter)
        layout.setContentsMargins(10, 10, 10, 10)

        # Добавляем стиль для закругленного контура
        self.setStyleSheet("""
            QFrame {
                border-radius: 10px;
                background: #4285B4;
            }
        """)

    def mousePressEvent(self, event):
        # Показываем информацию при клике на виджет
        print(f"Название книги: {self.title}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Библиотека")
        self.setGeometry(100, 100, 800, 600)  # Increased window size

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        central_layout = QGridLayout(central_widget)

        # Создаем несколько элементов книг
        book_data = [
            {"title": "Магическая битва", "image_path": "book_image.jpg"},
            {"title": "Человек-бензопила", "image_path": "book_image2.jpg"},
            {"title": "Берсерк", "image_path": "book_image3.jpg"},
            {"title": "КРД", "image_path": "book_image4.jpg"},
            {"title": "Тест2", "image_path": "book_image.jpg"},
            {"title": "Тест3", "image_path": "book_image2.jpg"},
            {"title": "Тест4", "image_path": "book_image3.jpg"},
            {"title": "Тест5", "image_path": "book_image4.jpg"},
        ]

        row, col = 0, 0  # Initialize row and column counters

        for book_info in book_data:
            book_element = BookElement(book_info["title"], book_info["image_path"], self)
            central_layout.addWidget(book_element, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1

        central_layout.setSpacing(79)  # Adjust spacing between book elements
        central_layout.setContentsMargins(10, 10, 10, 10)

        self.setStyleSheet("""
            QWidget {
                background: #ABCDEF;
            }
        """)


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
