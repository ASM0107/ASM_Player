DARK_THEME = """
QMainWindow {
    background-color: #1e1e1e;
    color: #ffffff;
}

QWidget {
    background-color: #1e1e1e;
    color: #ffffff;
    font-family: 'Segoe UI', Arial, sans-serif;
}

QPushButton {
    background-color: #333333;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 6px 12px;
    color: #ffffff;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #444444;
    border: 1px solid #777777;
}

QPushButton:pressed {
    background-color: #222222;
}

QSlider::groove:horizontal {
    border: 1px solid #333333;
    height: 6px;
    background: #444444;
    margin: 2px 0;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #ff8c00;
    border: 1px solid #ff8c00;
    width: 14px;
    margin: -4px 0;
    border-radius: 7px;
}

QSlider::sub-page:horizontal {
    background: #ff8c00;
    border: 1px solid #333333;
    height: 6px;
    border-radius: 3px;
}

QMenuBar {
    background-color: #2d2d2d;
    color: white;
}

QMenuBar::item {
    background-color: transparent;
    padding: 4px 10px;
}

QMenuBar::item:selected {
    background-color: #444444;
}

QMenu {
    background-color: #2d2d2d;
    color: white;
    border: 1px solid #444444;
}

QMenu::item:selected {
    background-color: #ff8c00;
    color: white;
}

QLabel {
    color: #cccccc;
}
"""
