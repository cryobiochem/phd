import streamlit as st  # 🎈 data web app development
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import numpy as np  # generate numbers for functions
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt
from datetime import time, datetime # to simulate a real time data, time loop

### METADATA
st.set_page_config(
    page_title="Bruno M. Guerreiro | Portfolio",
    page_icon="🇵🇹",
    #layout="wide",
)

### MAIN TITLE
st.title("🇵🇹 Bruno M. Guerreiro")
st.markdown("##### A personal portfolio project © 2024.")
st.caption('Bruno M. Guerreiro is a Biochemistry Ph.D. with 7 years of experience in cryopreservation research. '
           'Bruno is an internationally renowned scientist, with **9** scientific publications, **10** conference participations, **7** awards and **3** fellowships. '
           'With a life sciences background, Bruno is also a self-taught enthusiast, having accumulated a total of **23 online certifications** in Data Science, Deep Learning, TensorFlow and complementary fields.')

### SIDEBAR
st.sidebar.title("🇵🇹 Bruno M. Guerreiro")
st.sidebar.markdown("##### A personal portfolio project © 2024.")
st.sidebar.caption('Bruno M. Guerreiro is a Biochemistry Ph.D. with 7 years of experience in cryopreservation research. '
           'Bruno is an internationally renowned scientist, with **9** scientific publications, **10** conference participations, **7** awards and **3** fellowships. '
           'With a life sciences background, Bruno is also a self-taught enthusiast, having accumulated a total of **23 online certifications** in Data Science, Deep Learning, TensorFlow and complementary fields.')

# Create 4 columns for the logos with reduced spacing
gmail, scholar, github, linkedin, c5, c6, c7, c8 = st.sidebar.columns(8)

# Add clickable logos side by side for Gmail, Google Scholar, Github, and Linkedin with reduced spacing
gmail.markdown('<div style="text-align: left"><a href="https://mail.google.com/mail/u/0/?view=cm&fs=1&to=guerreiro.bms@gmail.com&su=New%20job%20opportunity%20for%20Bruno%20M.%20Guerreiro" target="_blank">'
    '<img src="https://lh3.googleusercontent.com/0rpHlrX8IG77awQMuUZpQ0zGWT7HRYtpncsuRnFo6V3c8Lh2hPjXnEuhDDd-OsLz1vua4ld2rlUYFAaBYk-rZCODmi2eJlwUEVsZgg" alt="Gmail" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)

scholar.markdown('<div style="text-align: left"><a href="https://scholar.google.com/citations?user=nbyAZasAAAAJ&hl=en" target="_blank">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Google_Scholar_logo.svg/2048px-Google_Scholar_logo.svg.png" alt="Google Scholar" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)

github.markdown('<div style="text-align: left"><a href="https://github.com/cryobiochem" target="_blank">'
    '<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="Github" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)

linkedin.markdown('<div style="text-align: left"><a href="https://www.linkedin.com/in/bmguerreiro/" target="_blank">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png" alt="LinkedIn" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)

st.sidebar.write('')

if st.sidebar.button("Resume/CV"):
    # Add the download link for Resume
    st.sidebar.markdown('<div style="text-align: left">[Download Resume/CV here](link_to_resume)</div>')


### CONTENT
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["About me",
                                                         "PhD",
                                                         "Data Science",
                                                          "Graphic Design",
                                                          "Technical Writing",
                                                          "Projects",
                                                          "Media",
                                                          "Blog"])

st.write('---')
st.markdown('<div style="text-align: right;"><sub>Bruno M. Guerreiro © 2024</sub></div>', unsafe_allow_html=True)