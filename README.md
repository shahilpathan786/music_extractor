# 🎵 YouTube Audio Downloader

A simple and elegant web application to download audio from YouTube videos and convert them to WAV format.

## Features

✨ **Easy to Use**
- Simple, intuitive web interface
- Paste YouTube URL and download with one click

🎵 **Audio Conversion**
- Automatically extracts audio from YouTube videos
- Converts to WAV format (192 kbps quality)
- Downloads the best available audio quality

🎨 **Modern UI**
- Dark theme interface
- Responsive design
- Real-time download status updates

## Prerequisites

Before running this application, make sure you have:

- **Python 3.8+** installed on your system
- **FFmpeg** installed and configured (required for audio processing)
  - Download: https://ffmpeg.org/download.html
  - For Windows: Extract FFmpeg and ensure the `bin` folder is in your PATH or configured in the app

## Installation

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/yourusername/Music_Extractor.git
   cd Music_Extractor
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r Requirements.txt
   ```

## Configuration

### FFmpeg Setup

The application requires FFmpeg to be installed:

1. **Windows**
   - Download from https://ffmpeg.org/download.html
   - Extract the files
   - Update the `FFMPEG_PATH` in `app.py` to point to your FFmpeg bin folder:
     ```python
     FFMPEG_PATH = r"C:\path\to\ffmpeg\bin"
     ```

2. **macOS**
   ```bash
   brew install ffmpeg
   ```

3. **Linux**
   ```bash
   sudo apt-get install ffmpeg  # Debian/Ubuntu
   # or
   sudo yum install ffmpeg       # RedHat/CentOS
   ```

## Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - Or navigate there manually

3. **Download audio**
   - Paste a YouTube URL in the input field
   - Click "Download Audio"
   - Wait for the audio to be extracted and converted
   - Click the "⬇ Download WAV File" button to save

## Dependencies

- **streamlit** - Web framework for the UI
- **yt-dlp** - YouTube downloader and extractor
- **pydub** - Audio processing library

See `Requirements.txt` for the complete list.

## Troubleshooting

### "FFmpeg not found"
- Make sure FFmpeg is installed and the path in `app.py` is correct
- On Windows, you may need to restart after adding FFmpeg to PATH

### "Download failed"
- Check your internet connection
- Ensure the YouTube URL is valid and public
- Some videos may have restrictions on downloading

### Permission errors
- On macOS/Linux, you may need to use `sudo` or adjust file permissions

## Limitations

- Downloads may fail for age-restricted or geographically restricted videos
- Large videos may take longer to process
- Some videos may not have available audio streams

## License

This project is open source and available for personal use.

## Contributing

Feel free to fork this repository and submit pull requests for improvements!

## Disclaimer

This tool is for educational purposes. Users are responsible for ensuring their use complies with YouTube's Terms of Service and local copyright laws.

---

**Questions or Issues?** Feel free to open an issue or contact the repository owner.
