import sys
from PyQt6.QtWidgets import QApplication
from src.main_window import MainWindow
from src.styles import DARK_THEME

def main():
    app = QApplication(sys.argv)
    
    # Apply the dark theme globally
    app.setStyleSheet(DARK_THEME)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
