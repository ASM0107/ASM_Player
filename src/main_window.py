import os
import sys
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QSlider, QLabel, QFileDialog, QStyle, QMessageBox, QComboBox
)
from PySide6.QtCore import Qt, QUrl, QEvent, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QAction, QIcon, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ASM Media Player")
        self.resize(1024, 576)
        
        # Core Player Initialization
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)
        
        # State variables
        self.is_muted = False
        self.last_volume = 100
        self.is_fullscreen = False
        
        # Setup UI
        self.setup_ui()
        self.setup_menu()
        self.setup_shortcuts()
        
        # Event Filters
        self.video_widget.installEventFilter(self)
        
        # Connect signals
        self.media_player.playbackStateChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.errorChanged.connect(self.handle_error)

    def setup_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # Video area
        self.video_widget.setStyleSheet("background-color: black;")
        self.main_layout.addWidget(self.video_widget, stretch=1)
        
        # Controls area
        self.controls_widget = QWidget()
        controls_layout = QVBoxLayout(self.controls_widget)
        controls_layout.setContentsMargins(15, 10, 15, 15)
        
        # Progress slider
        self.position_slider = QSlider(Qt.Orientation.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)
        controls_layout.addWidget(self.position_slider)
        
        # Buttons and time labels
        buttons_layout = QHBoxLayout()
        
        # Play/Pause
        self.play_button = QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.play_button.setToolTip("Play/Pause (Space)")
        self.play_button.clicked.connect(self.toggle_playback)
        buttons_layout.addWidget(self.play_button)
        
        # Stop
        self.stop_button = QPushButton()
        self.stop_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop))
        self.stop_button.setToolTip("Stop")
        self.stop_button.clicked.connect(self.stop_playback)
        buttons_layout.addWidget(self.stop_button)
        
        # Skip Backwards
        self.skip_back_btn = QPushButton()
        self.skip_back_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaSkipBackward))
        self.skip_back_btn.setToolTip("Skip Back 10s (Left Arrow)")
        self.skip_back_btn.clicked.connect(lambda: self.skip(-10000))
        buttons_layout.addWidget(self.skip_back_btn)
        
        # Skip Forwards
        self.skip_fwd_btn = QPushButton()
        self.skip_fwd_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaSkipForward))
        self.skip_fwd_btn.setToolTip("Skip Forward 10s (Right Arrow)")
        self.skip_fwd_btn.clicked.connect(lambda: self.skip(10000))
        buttons_layout.addWidget(self.skip_fwd_btn)
        
        # Time Label
        self.time_label = QLabel("00:00 / 00:00")
        buttons_layout.addWidget(self.time_label)
        
        buttons_layout.addStretch()
        
        # Playback Speed
        self.speed_combo = QComboBox()
        self.speed_combo.addItems(["0.5x", "1.0x", "1.25x", "1.5x", "2.0x"])
        self.speed_combo.setCurrentIndex(1)
        self.speed_combo.currentTextChanged.connect(self.change_speed)
        self.speed_combo.setToolTip("Playback Speed")
        buttons_layout.addWidget(self.speed_combo)
        
        # Mute/Volume
        self.mute_button = QPushButton()
        self.mute_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolume))
        self.mute_button.setToolTip("Mute/Unmute (M)")
        self.mute_button.setCheckable(True)
        self.mute_button.clicked.connect(self.toggle_mute)
        buttons_layout.addWidget(self.mute_button)
        
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(100)
        self.volume_slider.setFixedWidth(120)
        self.volume_slider.setToolTip("Volume (Up/Down Arrows)")
        self.volume_slider.valueChanged.connect(self.set_volume)
        buttons_layout.addWidget(self.volume_slider)
        
        # Fullscreen Toggle
        self.fullscreen_button = QPushButton("⛶")
        self.fullscreen_button.setToolTip("Toggle Fullscreen (F or Double Click)")
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)
        buttons_layout.addWidget(self.fullscreen_button)
        
        controls_layout.addLayout(buttons_layout)
        self.main_layout.addWidget(self.controls_widget)
        self.central_widget.setLayout(self.main_layout)

    def setup_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        
        open_action = QAction("&Open File...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def setup_shortcuts(self):
        # Space to toggle playback handled in keyPressEvent directly for reliability
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.toggle_playback()
        elif event.key() == Qt.Key.Key_Right:
            self.skip(10000)
        elif event.key() == Qt.Key.Key_Left:
            self.skip(-10000)
        elif event.key() == Qt.Key.Key_Up:
            self.volume_slider.setValue(min(100, self.volume_slider.value() + 5))
        elif event.key() == Qt.Key.Key_Down:
            self.volume_slider.setValue(max(0, self.volume_slider.value() - 5))
        elif event.key() == Qt.Key.Key_F:
            self.toggle_fullscreen()
        elif event.key() == Qt.Key.Key_M:
            self.toggle_mute()
        elif event.key() == Qt.Key.Key_Escape and self.is_fullscreen:
            self.toggle_fullscreen()
        else:
            super().keyPressEvent(event)

    def eventFilter(self, obj, event):
        if obj == self.video_widget:
            if event.type() == QEvent.Type.MouseButtonDblClick:
                self.toggle_fullscreen()
                return True
        return super().eventFilter(obj, event)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Media", "", 
            "Media Files (*.mp4 *.mkv *.avi *.wmv *.mov *.mp3 *.wav *.flac);;All Files (*)"
        )
        if file_name:
            self.media_player.setSource(QUrl.fromLocalFile(file_name))
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
            self.media_player.play()

    def toggle_playback(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def stop_playback(self):
        self.media_player.stop()

    def skip(self, ms):
        new_pos = max(0, min(self.media_player.duration(), self.media_player.position() + ms))
        self.media_player.setPosition(new_pos)

    def change_speed(self, text):
        speed = float(text.replace('x', ''))
        self.media_player.setPlaybackRate(speed)

    def toggle_mute(self):
        self.is_muted = not self.is_muted
        self.mute_button.setChecked(self.is_muted)
        
        if self.is_muted:
            self.last_volume = self.volume_slider.value()
            self.audio_output.setVolume(0)
            self.mute_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolumeMuted))
        else:
            self.audio_output.setVolume(self.last_volume / 100.0)
            self.mute_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolume))
            self.volume_slider.setValue(self.last_volume)

    def set_volume(self, volume):
        if not self.is_muted:
            self.audio_output.setVolume(volume / 100.0)
            self.last_volume = volume

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            self.controls_widget.hide()
            self.menuBar().hide()
            self.showFullScreen()
        else:
            self.controls_widget.show()
            self.menuBar().show()
            self.showNormal()

    def media_state_changed(self, state):
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))

    def position_changed(self, position):
        if not self.position_slider.isSliderDown():
            self.position_slider.setValue(position)
        self.update_time_label(position, self.media_player.duration())

    def duration_changed(self, duration):
        self.position_slider.setRange(0, duration)
        self.update_time_label(self.media_player.position(), duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_time_label(self, position, duration):
        pos = position // 1000
        dur = duration // 1000
        
        pos_str = f"{pos // 60:02d}:{pos % 60:02d}"
        dur_str = f"{dur // 60:02d}:{dur % 60:02d}"
        
        if dur >= 3600:
            pos_str = f"{pos // 3600:02d}:{pos_str}"
            dur_str = f"{dur // 3600:02d}:{dur_str}"
            
        self.time_label.setText(f"{pos_str} / {dur_str}")

    def handle_error(self):
        error_msg = self.media_player.errorString()
        if error_msg:
            QMessageBox.critical(self, "Error", f"Media Player Error: {error_msg}")
