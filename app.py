import streamlit as st
import yt_dlp
import os
import tempfile

# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="YouTube Audio Downloader",
    page_icon="",
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

st.title(" YouTube Audio Downloader")

youtube_url = st.text_input(
    "Paste YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

def download_audio(url):
    temp_dir = tempfile.mkdtemp()
    output_template = os.path.join(temp_dir, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        },
        "socket_timeout": 30,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": False,
        "no_warnings": False,
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
                    label=" Download WAV File",
                    data=audio_file,
                    file_name=f"{title}.wav",
                    mime="audio/wav"
                )

        except Exception as e:
            error_msg = str(e)
            if "403" in error_msg or "Forbidden" in error_msg:
                st.error("❌ YouTube blocked the request. This can happen due to:\n- Geographic restrictions\n- Account age/restrictions\n- Rate limiting\n\nTry again in a few minutes or use a different video.")
            elif "Video unavailable" in error_msg or "private" in error_msg.lower():
                st.error("❌ This video is unavailable (private, deleted, or restricted).")
            elif "HTTP Error" in error_msg:
                st.error(f"❌ Network error: {error_msg}")
            else:
                st.error(f"❌ Error: {error_msg}")
