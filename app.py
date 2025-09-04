import streamlit as st
import streamlit.components.v1 as components
import os

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
