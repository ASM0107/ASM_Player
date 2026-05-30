DARK_THEME = """
QMainWindow {
    background-color: #121212;
    color: #e0e0e0;
}

QWidget {
    background-color: #121212;
    color: #e0e0e0;
    font-family: 'Segoe UI', Inter, Arial, sans-serif;
}

QPushButton {
    background-color: #2a2a2a;
    border: 1px solid #3a3a3a;
    border-radius: 6px;
    padding: 6px 14px;
    color: #ffffff;
    font-weight: 600;
}

QPushButton:hover {
    background-color: #3a3a3a;
    border: 1px solid #5a5a5a;
}

QPushButton:pressed {
    background-color: #1a1a1a;
}

QPushButton:checked {
    background-color: #0078D7;
    color: #ffffff;
}

QComboBox {
    background-color: #2a2a2a;
    border: 1px solid #3a3a3a;
    border-radius: 6px;
    padding: 4px 10px;
    color: #ffffff;
}

QComboBox:hover {
    border: 1px solid #5a5a5a;
}

QComboBox::drop-down {
    border-left: 1px solid #3a3a3a;
    width: 20px;
}

QSlider::groove:horizontal {
    border: 1px solid #2a2a2a;
    height: 6px;
    background: #333333;
    margin: 2px 0;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #0078D7;
    border: 2px solid #121212;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QSlider::handle:horizontal:hover {
    background: #3399FF;
}

QSlider::sub-page:horizontal {
    background: #0078D7;
    border: 1px solid #2a2a2a;
    height: 6px;
    border-radius: 3px;
}

QMenuBar {
    background-color: #1a1a1a;
    color: #e0e0e0;
}

QMenuBar::item {
    background-color: transparent;
    padding: 6px 12px;
}

QMenuBar::item:selected {
    background-color: #333333;
}

QMenu {
    background-color: #1a1a1a;
    color: #e0e0e0;
    border: 1px solid #333333;
}

QMenu::item {
    padding: 6px 24px 6px 24px;
}

QMenu::item:selected {
    background-color: #0078D7;
    color: #ffffff;
}

QLabel {
    color: #b0b0b0;
    font-size: 13px;
}
"""
