import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Set page configuration for a wider, more immersive layout
st.set_page_config(layout="wide", page_title="3D Endless Runner")

# --- HIDE STREAMLIT BRANDING ---
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- PAGE CONTENT ---
st.title("🏃‍♂️ 3D Endless Runner")
st.write("🎮🎮A simple 3D game Made By Vivek B Kumar... 🎮🎮")

# --- Function to get audio file as a base64 string ---
def get_audio_base64(file_path):
    """
    Reads an audio file and returns its base64 encoded string.
    """
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# --- Music Player with Play/Pause Button ---
audio_folder = "assets"
music_file = None
for file in os.listdir(audio_folder):
    if file.endswith(('.mp3', '.wav', '.ogg')):
        music_file = file
        break

if music_file:
    audio_path = os.path.join(audio_folder, music_file)
    try:
        audio_base64 = get_audio_base64(audio_path)
        audio_html = f"""
        <style>
            .music-player-container {{
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 1000;
            }}
            .music-player-button {{
                background-color: rgba(255, 255, 255, 0.7);
                border: 2px solid #1E1E1E;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }}
            .music-player-icon {{
                font-size: 20px;
                color: #1E1E1E;
            }}
        </style>
        <div class="music-player-container">
            <button class="music-player-button" onclick="togglePlayPause()">
                <span id="play-pause-icon" class="music-player-icon">▶️</span>
            </button>
        </div>
        <audio id="background-music" loop>
            <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <script>
            var audio = document.getElementById('background-music');
            var icon = document.getElementById('play-pause-icon');
            var isPlaying = false;

            function togglePlayPause() {{
                if (isPlaying) {{
                    audio.pause();
                    icon.textContent = '▶️';
                }} else {{
                    audio.play();
                    icon.textContent = '⏸️';
                }}
                isPlaying = !isPlaying;
            }}
        </script>
        """
        st.components.v1.html(audio_html, height=100, scrolling=False)
    except FileNotFoundError:
        st.warning("Music file not found in 'assets' folder. Background music will not play.")

# --- EMBED THE GAME ---
# Read the HTML file
try:
    with open('game.html', 'r', encoding='utf-8') as f:
        html_string = f.read()

    # Embed the HTML in the Streamlit app
    # Set a fixed height for better gameplay experience
    components.html(html_string, height=620, scrolling=False)

except FileNotFoundError:
    st.error("The 'game.html' file was not found. Please make sure it is in the same directory as this script.")

st.info("🎮 **How to Play:** Use the **Left and Right Arrow Keys** on your keyboard to switch lanes and dodge the orange blocks!")

st.markdown("---")
st.markdown("Created with ❤️ only using GENAI tools")
