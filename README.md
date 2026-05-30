# ASM Media Player

ASM Media Player is a modern, cross-platform media player built using Python and PyQt6. It aims to provide a robust, VLC-like experience with a sleek dark theme and seamless media playback capabilities.

## Features

- **Media Playback**: Supports a variety of video and audio formats (MP4, MKV, AVI, WMV, MP3, WAV, etc.) using `PyQt6.QtMultimedia`.
- **Modern UI**: A clean, custom dark theme providing an industry-grade look and feel.
- **Controls**: Play/Pause, Stop, Progress slider with time display, and Volume control.
- **Cross-Platform**: Runs on Windows, macOS, and Linux seamlessly.

## Prerequisites

- **Python 3.8+**
- (Optional but recommended) A virtual environment

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/asm-player.git
   cd asm-player
   ```

2. **Create a virtual environment (Optional):**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script to launch the application:
```bash
python main.py
```

Use `File -> Open File...` (or `Ctrl+O`) to load your media and enjoy.

## Architecture

- `main.py`: Entry point of the application, initializing the global styling and the main Qt loop.
- `src/main_window.py`: Core logic for the media player, utilizing `QMediaPlayer` and `QVideoWidget`.
- `src/styles.py`: Contains the stylesheet (QSS) defining the dark aesthetics.
- `requirements.txt`: Project dependencies for easy setup.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
