import streamlit as st
import streamlit.components.v1 as components

# Configure the Streamlit page to accommodate the custom UI
st.set_page_config(
    page_title="SMV Tracker Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit's default header, footer, and menu to make it look like a standalone web app
# Enforcing a light background to seamlessly blend with the dashboard's light theme
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .stApp {
                background-color: #0D1117; 
            }
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def load_local_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Load the HTML file
html_content = load_local_html('dashboard.html')

# Render the HTML using Streamlit Components
# Height is set to a large value, and scrolling is enabled to handle the internal overflow
components.html(
    html_content,
    height=1000, 
    scrolling=True
)