import streamlit as st
import yt_dlp
import os
import tempfile

# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="YouTube Audio Downloader",
    page_icon="🎵",
    layout="centered"
)

# ------------------------
# DARK THEME CSS
# ------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}

h1 {
    text-align: center;
    color: #00D4FF;
}

.stTextInput input {
    background-color: #262730;
    color: white;
}

.stButton button {
    width: 100%;
    background-color: #00D4FF;
    color: black;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🎵 YouTube Audio Downloader")

youtube_url = st.text_input(
    "Paste YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

FFMPEG_PATH = r"C:\Users\Shahil\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

def download_audio(url):
    temp_dir = tempfile.mkdtemp()

    output_template = os.path.join(temp_dir, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "ffmpeg_location": "ffmpeg",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        title = info["title"]

        wav_file = os.path.join(temp_dir, f"{title}.wav")

        return wav_file, title


if st.button("Download Audio"):
    if not youtube_url:
        st.warning("Please enter a YouTube URL")
    else:
        try:
            with st.spinner("Downloading audio..."):
                file_path, title = download_audio(youtube_url)

            st.success("Audio downloaded successfully!")

            with open(file_path, "rb") as audio_file:
                st.download_button(
                    label="⬇ Download WAV File",
                    data=audio_file,
                    file_name=f"{title}.wav",
                    mime="audio/wav"
                )

        except Exception as e:
            st.error(f"Error: {e}")