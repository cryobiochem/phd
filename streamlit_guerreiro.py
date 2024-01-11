import streamlit as st  # 🎈 data web app development
from streamlit_timeline import timeline
import numpy as np
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import base64
from plotly.subplots import make_subplots
import plotly.graph_objects as go

### METADATA
st.set_page_config(
    page_title="Bruno M. Guerreiro | Portfolio",
    page_icon="🇵🇹",
    layout="wide",
)

### SIDEBAR
st.sidebar.markdown('<div style="text-align: left; margin-bottom: 12px"><a href="https://guerreiro.streamlit.app/">''<img src="https://i.imgur.com/t3cH48K.png" alt="Bruno M. Guerreiro" width="250">'
    '</a></div>', unsafe_allow_html=True)
st.sidebar.markdown("##### A personal portfolio project © 2024.")
st.sidebar.caption('Bruno M. Guerreiro is a Biochemistry Ph.D. with 7 years of experience in cryopreservation research. '
           'Bruno is an internationally renowned scientist, with **9** scientific publications, **10** conference participations, **7** awards and **3** fellowships. '
           'With a life sciences background, Bruno is also a self-growth enthusiast, having accumulated a total of **23 online certifications** in Data Science, Deep Learning, TensorFlow and complementary fields.')

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

# Resume/CV download button
st.sidebar.markdown(f'<a href="https://1drv.ms/b/s!At7e_tE6ZFn0hJoSI8rhGrTpzQKJ3Q?e=kcVa7A" download="Resume_CV.pdf"><button style="cursor: pointer; padding: 10px; border: none; border-radius: 5px;">Download Resume/CV</button></a>', unsafe_allow_html=True)
st.sidebar.caption("📌 Based in Setúbal/Lisbon")
st.sidebar.info("⚠️ For optimal website experience, use light theme & wide mode.")

### CONTENT
aboutme, certs, phd, ds, gd, tw, proj, media = st.tabs(["About me",
                                                         "Certifications",
                                                         "Ph.D.",
                                                         "Data Science",
                                                         "Graphic Design",
                                                         "Technical Writing",
                                                         "Projects",
                                                         "Media"])


with aboutme:
    ### TIMELINE
    with open('timeline.json', "r") as f:
        data = f.read()
    timeline(data, height=600)
with certs:
    c1_img, c1_text = st.columns([2,5])
    with c1_img:
        st.image("https://udemy-certificate.s3.amazonaws.com/image/UC-ZZHX1T1F.jpg?v=1544266446000", use_column_width="auto")

    with c1_text:
        st.markdown("### Data Science A-Z™: Hands-On Exercises | :blue[*SuperDataScience.com* (2018)]")
        st.markdown("The full walkthrough of how to be a data scientist. This course taught me how to clean and prepare data for analysis, perform basic data visualisations, model and curve-fit data & present findings to stakeholders. The **first capstone project** involved advanced data visualization in Tableau to derive insights from Credit Score and Tenure relationships, while performing churn modelling and Chi-Squared testing. The **second capstone project** involved advanced data mining in Microsoft Visual Studio (SSIS/SQL) to deal with ETL Error Handling on a Vehicle Service database containing more than 1 million entries.")

        st.caption("Skills obtained with this certification: [(See certificate here)](https://ude.my/UC-ZZHX1T1F)")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1: st.info("Data Mining")
        with col2: st.info("Data Visualization")
        with col3: st.info("Tableau")
        with col4: st.info("Gretl")
        with col5: st.info("SSIS")
        with col6: st.info("SQL")

    st.divider()

    c2_img, c2_text = st.columns([2, 5])

    with c2_img:
        st.image("https://i.imgur.com/wUPtNuw.png", use_column_width="auto")

    with c2_text:
        st.markdown("### Data Science Specialization | :blue[*John Hopkins University* (2020)]")
        st.markdown(
            "Covered the concepts and tools for an entire data science pipeline in R programming. Successful participants learn how to use the tools of the trade, think analytically about complex problems, manage large data sets, deploy statistical principles, create visualizations, build and evaluate machine learning algorithms, publish reproducible analyses, and develop data products. The **capstone projects** involved the measuring of atmospheric pollution for assessing societal health problems, and analysis of Fitbit movement activity monitoring to derive activity levels and patterns.")

        st.caption("Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/3543a8a5fd1219abc4e65ffa3856c3a2)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("R programming")
        with col2: st.info("Regression Analysis")
        with col3: st.info("Machine Learning")
        with col4: st.info("Github")

    st.divider()

    c3_img, c3_text = st.columns([2, 5])

    with c3_img:
        st.image("https://i.imgur.com/SNs3nPL.png", use_column_width="auto")
    with c3_text:
        st.markdown("### Deep Learning Specialization | :blue[*deeplearning.ai* (2020)]")
        st.markdown("In this Specialization, I've built neural network architectures such as Convolutional Neural Networks, Recurrent Neural Networks, LSTMs, Transformers, and learned how to make them better with strategies such as Dropout, BatchNorm, and Xavier/He initialization. You mastered these theoretical concepts, learned their industry applications using Python and TensorFlow. As **capstone project**, I tackled real-world cases such as speech recognition, music synthesis, chatbots, machine translation, natural language processing, and more.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/347c89a8fab8b4ddeb55f29674c00d83)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Python")
        with col2: st.info("Deep Learning")
        with col3: st.info("CNNs")
        with col4: st.info("Computer Vision")
        with col5: st.info("NLP")

    st.divider()

    c4_img, c4_text = st.columns([2, 5])
    with c4_img:
        st.image("https://i.imgur.com/XKb0yGo.png", use_column_width="auto")
    with c4_text:
        st.markdown("### TensorFlow Developer | :blue[*deeplearning.ai* (2020)]")
        st.markdown("Following the Deep Learning specialization, I enrolled in a Professional Certificate program to learn how to build and train neural networks using TensorFlow, how to improve network performance using convolutions when trained to identify real-world images, correcting for overfitting using augmentation and dropout, how to teach machines to understand, analyze, and respond to human speech with natural language processing systems. The **capstone projects** involved Customer Sentiment analysis using NLP, and prediction analysis in time-series.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/3e4c0da4f54954f5cca49e43f5433e49)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Python")
        with col2: st.info("Deep Learning")
        with col3: st.info("RNNs")
        with col4: st.info("GRUs")
        with col5: st.info("LSTMs")

    st.divider()

    c5_img, c5_text = st.columns([2, 5])
    with c5_img:
        st.image("https://i.imgur.com/qpbfMVJ.png", use_column_width="auto")
    with c5_text:
        st.markdown("### Responsive Web Design | :blue[*freeCodeCamp* (2020)]")
        st.markdown("As a 300 hour investment lecture, I learned the fundamentals of building websites that work seamlessly across various devices. Several projects were created to show expertise over HTML and CSS programming languages, applied visual design, applied accessibility, web design presentation principles and the creative ways CSS (flexboxes, grids) can be used to enhance user experience.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://www.freecodecamp.org/certification/brunoguerreiro/responsive-web-design)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Web design")
        with col2: st.info("HTML")
        with col3: st.info("CSS")
        with col4: st.info("Front-end")

    st.divider()

    c6_img, c6_text = st.columns([2, 5])
    with c6_img:
        st.image("https://i.imgur.com/MIu8dX4.png", use_column_width="auto")
    with c6_text:
        st.markdown("### Fundamentals of Digital Marketing | :blue[*Google* (2020)]")
        st.markdown("This Interactive Advertising Bureau-accredited course contained 26 modules created by Google trainers, packed full of practical exercises and real-world examples to help you turn knowledge into action in the field of digital marketing. I learned the concepts of creating an online business, building a strong presence that urges call-to-action, how to optimize search ads, geodemographic personalization of products, connect with customers through various forms of marketing (e-mail, video, paid search, local search), optimize website content and perform decision-making analytics. **This course allowed me to better understand how to present web content online to captivate audiences.**")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://drive.google.com/file/d/1La55rHhtuHFwiEpr3i1o3G1yu9XYgA-I/view?usp=sharing)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Marketing")
        with col2: st.info("Web design")
        with col3: st.info("e-Commerce")
        with col4: st.info("SEO")
        with col5: st.info("ROI")
with phd:
    st.header("My Ph.D. Journey")
    st.caption("I have a strong background in life sciences and scientific research, having accumulated 10 years of constant critical thinking and problem-solving capabilities, and almost 7 years of theoretical and applied research focus."
               " My 4-year Ph.D. journey in particular has equipped me with a core skillset of adaptability, efficiency, productivity and being able to get out of a rut. Producing new knowledge in a scientific field"
               " is often a arduous path and requires patience, determination and ambition. Backing up, defending and presenting our ideas is also a part of the research life, such that I have honed"
               "illustration, data visualization, data analysis and public speaking skills that complement my seek for knowledge with the ability to share that knowledge to various audiences.")

    with st.container(border=True):
        st.markdown("Skills demonstrated in this section:")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Critical Thinking")
        with col2: st.info("Problem Solving")
        with col3: st.info("Public Speaking")
        with col4: st.info("Technical Writing")
        with col5: st.info("Data Presentation")

    st.write("")

    st.image("https://i.imgur.com/H26Nnem.png")

    st.write("")
    st.write("")
    st.subheader("Cryopreservation fundamentals + my approach")
    with st.container(border=True):
        st.image("https://i.imgur.com/fW46l27.png")

    st.write("")
    st.write("")
    st.subheader("The organ transplant crisis")
    with st.container(border=True):
        st.image("https://i.imgur.com/5f6BDf9.png")

    st.write("")
    st.write("")
    st.subheader("Lab work methodology")
    with st.container(border=True):
        st.image("https://i.imgur.com/SNt2e6m.jpg")

    st.write("")
    st.write("")
    st.subheader("Some of my contributions (+ visuals)")
    with st.container(border=True):
        st.image("https://i.imgur.com/N74iMeP.jpg")
with ds:
    data = pd.read_csv("./data/streamlit-poldb.csv")
    monomers = pd.read_csv("./data/streamlit-mondb.csv")
    year_df = pd.read_excel("data/year.xlsx")

    data = data[:].iloc[:, 0:158]
    identity = data.iloc[:, :11]
    biometrics = data.iloc[:, 11:33]
    composition = data.iloc[:, 33:66]
    structure = data.iloc[:, 66:78]
    fractions = data.iloc[:, 78:88]
    properties = data.iloc[:, 88:103]
    function = data.iloc[:, 103:121]
    outcome = data.iloc[:, 121:136]
    calculations = data.iloc[:, 136:]

    phd_colormap = {'Thermophile': 'indianred', 'Halothermophile': 'sandybrown',
                    'Psychrophile': 'deepskyblue', 'Halophile': 'mediumseagreen',
                    'Mesophile': 'black', 'Haloalkaliphile': 'lightpink', 'Alkaliphile': 'darkorchid'}

    st.header("Data Science")
    st.caption("Here you'll find several uses of data science tools in my Ph.D. work in cryopreservation. "
               "Please find below several data visualizations from the multidimensional database that I compiled. Briefly, the ability to predict if a polysaccharide may possess cryoprotective function remains a highly complex and challenging problem. "
             "Based on a thorough literature search, a database of **145 polysaccharides** produced from extremophilic microorganisms was compiled, "
             "in an attempt to discern major differences in molecular composition, conformation and functionality based on the natural adaptation to different habitats. "
             "This database contains 128 organic and 16 mathematically calculated parameters, for a total of **144 parameters (or dimensions)**, and a meta-analysis of its "
             "contents is currently being drafted, pending invitation for a special issue in New Biotechnology. The database was split into categories, with 12 variables "
             "characterizing microorganism identity, 22 variables for microorganism growth/EPS production conditions, 33 for polysaccharide composition, 12 for polysaccharide "
             "structure, 10 for EPS macromolecular fractions, 33 for polysaccharide characteristics (15 for physicochemical properties + 18 for biological functions) and "
             "14 for cryoprotection (7 for biological evidence + 7 for explanatory mechanisms of action) as outcome function. Here, you will find a surface-level overview "
             "of the [**CryoPolDB**](http://localhost:8501/#isochoric-nucleation-detection-using-python-automated-workflows) shown in, with helpful visualizations which "
             "allow to explore deep insights in the data.")

    with st.container(border=True):
        st.markdown("Skills demonstrated in this section:")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1: st.info("Python programming")
        with col2: st.info("Plotly")
        with col3: st.info("EDA")
        with col4: st.info("Dashboarding")

    with st.container(border=True):
        fig = px.violin(data_frame=year_df, x='Year', y='ExtremeType', orientation='h', color='ExtremeType',
                        color_discrete_map=phd_colormap
                        ).update_traces(orientation='h', side='positive', width=1, points='all', pointpos=0, jitter=0.35,
                        marker_size=8
                        ).update_yaxes(categoryorder="min descending", title_text=""
                                       ).update_xaxes(dtick=10)

        fig.update_xaxes(title_text="<b>Year of publication</b>")  # Set x-axis title

        fig.update_layout(
            showlegend=False,
            title_text="<b>What has been the research focus over the years?</b>",
        )
        st.plotly_chart(fig, use_container_width=True, theme=None)

    with st.container(border=True):
        # Filter the number of entries by extremophile type, phylum, and geofeature
        extremeType_count = data['ExtremeType'].value_counts()
        phylum_count = data.groupby('ExtremeType')['Phylum'].value_counts()
        geofeature_count = data.groupby('ExtremeType')['Geofeature'].value_counts()

        # Convert to dataframe type
        extremeType_count = pd.DataFrame(extremeType_count)
        phylum_count = pd.DataFrame(phylum_count)
        geofeature_count = pd.DataFrame(geofeature_count)

        # Reorganize the ExtremeType dataframe
        extremeType_count.reset_index(inplace=True)
        extremeType_count.columns = ['ExtremeType', 'Count']

        # Reorganize the Phylum dataframe
        phylum_count.reset_index(inplace=True)
        phylum_count.columns = ['ExtremeType', 'Phylum', 'Count']

        # Reorganize the Geofeature dataframe
        geofeature_count.reset_index(inplace=True)
        geofeature_count.columns = ['ExtremeType', 'Geofeature', 'Count']

        fig = px.pie(extremeType_count, values='Count', color='ExtremeType',
                     color_discrete_sequence=['deepskyblue', 'mediumseagreen', 'indianred', 'black', 'sandybrown',
                                              'darkorchid', 'lightpink'],
                     names='ExtremeType', title='<b>Database equity distribution between extremophilic type</b>')
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True, theme=None)

    with st.container(border=True):
        phylum_count = data.groupby('ExtremeType')['Phylum'].value_counts()
        phylum_count = pd.DataFrame(phylum_count)
        # Reorganize the Phylum dataframe
        phylum_count.reset_index(inplace=True)
        phylum_count.columns = ['ExtremeType', 'Phylum', 'Count']

        fig = px.pie(phylum_count, values='Count',
                     names='Phylum', color_discrete_sequence=px.colors.sequential.Sunset_r,
                     title='<b>Microorganism predominance, by phylum classification</b>')

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True, theme=None)

    with st.container(border=True):
        phylum_count = data.groupby('ExtremeType')['Phylum'].value_counts()
        phylum_count = pd.DataFrame(phylum_count)
        # Reorganize the Phylum dataframe
        phylum_count.reset_index(inplace=True)
        phylum_count.columns = ['ExtremeType', 'Phylum', 'Count']
        # --------------------------
        # make subplots of each phylum
        # --------------------------
        fig = make_subplots(2, 4, specs=[[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}],
                                         [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]],
                            subplot_titles=['Halophile', 'Psychrophile', 'Thermophile', 'Mesophile',
                                            'Halothermophile', 'Alkaliphile', 'Haloalkaliphile'],
                            horizontal_spacing=0.05, vertical_spacing=0.1)

        # for halophile
        haloLabels = []
        haloCount = []
        for i in phylum_count[phylum_count['ExtremeType'] == 'Halophile']['Phylum']:
            haloLabels.append(i)
        for j in phylum_count[phylum_count['ExtremeType'] == 'Halophile']['Count']:
            haloCount.append(j)

        # for psychrophile
        psychroLabels = []
        psychroCount = []
        for i in phylum_count[phylum_count['ExtremeType'] == 'Psychrophile']['Phylum']:
            psychroLabels.append(i)
        for j in phylum_count[phylum_count['ExtremeType'] == 'Psychrophile']['Count']:
            psychroCount.append(j)

        # for thermophile
        thermoLabels = []
        thermoCount = []
        for i in phylum_count[phylum_count['ExtremeType'] == 'Thermophile']['Phylum']:
            thermoLabels.append(i)
        for j in phylum_count[phylum_count['ExtremeType'] == 'Thermophile']['Count']:
            thermoCount.append(j)

        # for mesophile
        mesoLabels = []
        mesoCount = []
        for i in phylum_count[phylum_count['ExtremeType'] == 'Mesophile']['Phylum']:
            mesoLabels.append(i)
        for j in phylum_count[phylum_count['ExtremeType'] == 'Mesophile']['Count']:
            mesoCount.append(j)

        # for halothermophile
        htLabels = []
        htCount = []
        for i in phylum_count[phylum_count['ExtremeType'] == 'Halothermophile']['Phylum']:
            htLabels.append(i)
        for j in phylum_count[phylum_count['ExtremeType'] == 'Halothermophile']['Count']:
            htCount.append(j)

        # for alkaliphile
        alkaliLabels = []
        alkaliCount = []
        for i in phylum_count[phylum_count['ExtremeType'] == 'Alkaliphile']['Phylum']:
            alkaliLabels.append(i)
        for j in phylum_count[phylum_count['ExtremeType'] == 'Alkaliphile']['Count']:
            alkaliCount.append(j)

        # for haloalkaliphile
        haLabels = []
        haCount = []
        for i in phylum_count[phylum_count['ExtremeType'] == 'Haloalkaliphile']['Phylum']:
            haLabels.append(i)
        for j in phylum_count[phylum_count['ExtremeType'] == 'Haloalkaliphile']['Count']:
            haCount.append(j)

        fig.add_trace(go.Pie(labels=haloLabels, values=haloCount), 1, 1)
        fig.add_trace(go.Pie(labels=psychroLabels, values=psychroCount), 1, 2)
        fig.add_trace(go.Pie(labels=thermoLabels, values=thermoCount), 1, 3)
        fig.add_trace(go.Pie(labels=mesoLabels, values=mesoCount), 1, 4)
        fig.add_trace(go.Pie(labels=htLabels, values=htCount), 2, 1)
        fig.add_trace(go.Pie(labels=alkaliLabels, values=alkaliCount), 2, 2)
        fig.add_trace(go.Pie(labels=haLabels, values=haCount), 2, 3)

        fig.update_layout(title="<b>Phylum distribution by extremophilic type</b>")

        st.plotly_chart(fig, use_container_width=True, theme=None)
    with st.container(border=True):
        resp_count = data.groupby('ExtremeType')['Respiration'].value_counts()
        resp_count = pd.DataFrame(resp_count)
        # Reorganize the Phylum dataframe
        resp_count.reset_index(inplace=True)
        resp_count.columns = ['ExtremeType', 'Respiration', 'Count']
        # --------------------------
        # make subplots of each phylum
        # --------------------------
        fig = make_subplots(2, 4,
                            specs=[[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}],
                                   [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]],
                            subplot_titles=['Halophile', 'Psychrophile', 'Thermophile', 'Mesophile',
                                            'Halothermophile', 'Alkaliphile', 'Haloalkaliphile'],
                            horizontal_spacing=0.05, vertical_spacing=0.1)

        # for halophile
        haloLabelsR = []
        haloCountR = []
        for i in resp_count[resp_count['ExtremeType'] == 'Halophile']['Respiration']:
            haloLabelsR.append(i)
        for j in resp_count[resp_count['ExtremeType'] == 'Halophile']['Count']:
            haloCountR.append(j)

        # for psychrophile
        psychroLabelsR = []
        psychroCountR = []
        for i in resp_count[resp_count['ExtremeType'] == 'Psychrophile']['Respiration']:
            psychroLabelsR.append(i)
        for j in resp_count[resp_count['ExtremeType'] == 'Psychrophile']['Count']:
            psychroCountR.append(j)

        # for thermophile
        thermoLabelsR = []
        thermoCountR = []
        for i in resp_count[resp_count['ExtremeType'] == 'Thermophile']['Respiration']:
            thermoLabelsR.append(i)
        for j in resp_count[resp_count['ExtremeType'] == 'Thermophile']['Count']:
            thermoCountR.append(j)

        # for mesophile
        mesoLabelsR = []
        mesoCountR = []
        for i in resp_count[resp_count['ExtremeType'] == 'Mesophile']['Respiration']:
            mesoLabelsR.append(i)
        for j in resp_count[resp_count['ExtremeType'] == 'Mesophile']['Count']:
            mesoCountR.append(j)

        # for halothermophile
        htLabelsR = []
        htCountR = []
        for i in resp_count[resp_count['ExtremeType'] == 'Halothermophile']['Respiration']:
            htLabelsR.append(i)
        for j in resp_count[resp_count['ExtremeType'] == 'Halothermophile']['Count']:
            htCountR.append(j)

        # for alkaliphile
        alkaliLabelsR = []
        alkaliCountR = []
        for i in resp_count[resp_count['ExtremeType'] == 'Alkaliphile']['Respiration']:
            alkaliLabelsR.append(i)
        for j in resp_count[resp_count['ExtremeType'] == 'Alkaliphile']['Count']:
            alkaliCountR.append(j)

        # for haloalkaliphile
        haLabelsR = []
        haCountR = []
        for i in resp_count[resp_count['ExtremeType'] == 'Haloalkaliphile']['Respiration']:
            haLabelsR.append(i)
        for j in resp_count[resp_count['ExtremeType'] == 'Haloalkaliphile']['Count']:
            haCountR.append(j)

        fig.add_trace(go.Pie(labels=haloLabelsR, values=haloCountR), 1, 1)
        fig.add_trace(go.Pie(labels=psychroLabelsR, values=psychroCountR), 1, 2)
        fig.add_trace(go.Pie(labels=thermoLabelsR, values=thermoCountR), 1, 3)
        fig.add_trace(go.Pie(labels=mesoLabelsR, values=mesoCountR), 1, 4)
        fig.add_trace(go.Pie(labels=htLabelsR, values=htCountR), 2, 1)
        fig.add_trace(go.Pie(labels=alkaliLabelsR, values=alkaliCountR), 2, 2)
        fig.add_trace(go.Pie(labels=haLabelsR, values=haCountR), 2, 3)

        fig.update_layout(title="<b>Phylum distribution by type of respiratory metabolism</b>")

        st.plotly_chart(fig, use_container_width=True, theme=None)
    with st.container(border=True):
        # --------------------------
        # Choropleth data cleaning
        # --------------------------

        # FOR GLOBAL MAP
        # convert list from dictionary, to obtain CountryCounts and CountryNames variables
        def getList(dict):
            return [*dict]


        Countries = data['Country'].value_counts().to_dict()
        CountryCounts = list(Countries.values())
        CountryNames = getList(Countries)

        # FOR SUBMAPS
        # filter data of country counts by extreme type, convert to data frame, reset index
        choropleth = data.groupby('ExtremeType')['Country'].value_counts()
        choropleth = pd.DataFrame(choropleth)
        choropleth.columns = ['Count']
        choropleth = choropleth.reset_index()

        # --------------------------
        # Choropleth data plotting
        # --------------------------
        fig = go.Figure()

        # Global Map (trace 0)
        fig.add_trace(go.Choropleth(
            locations=CountryNames,
            locationmode="country names",
            z=CountryCounts,
            text=CountryNames,
            colorscale=px.colors.sequential.Agsunset_r,
            autocolorscale=False,
            reversescale=False,
            marker_line_color='black',
            marker_line_width=0.5,
            colorbar_title='Count',
            zauto=True
        ))

        # Halophile (trace 1)
        halo = choropleth[choropleth['ExtremeType'] == 'Halophile']

        fig.add_trace(go.Choropleth(
            locations=halo['Country'],
            locationmode="country names",
            z=halo['Count'],
            text=halo['Country'],
            colorscale=px.colors.sequential.YlGn,
            autocolorscale=False,
            reversescale=False,
            marker_line_color='black',
            marker_line_width=0.5,
            colorbar_title='Count',
            zauto=True
        ))

        # Psychrophile (trace 2)
        psychro = choropleth[choropleth['ExtremeType'] == 'Psychrophile']

        fig.add_trace(go.Choropleth(
            locations=psychro['Country'],
            locationmode="country names",
            z=psychro['Count'],
            text=psychro['Country'],
            colorscale=px.colors.sequential.Blues,
            autocolorscale=False,
            reversescale=False,
            marker_line_color='black',
            marker_line_width=0.5,
            colorbar_title='Count',
            zauto=True
        ))

        # Thermophile (trace 3)
        thermo = choropleth[choropleth['ExtremeType'] == 'Thermophile']

        fig.add_trace(go.Choropleth(
            locations=thermo['Country'],
            locationmode="country names",
            z=thermo['Count'],
            text=thermo['Country'],
            colorscale=px.colors.sequential.YlOrRd,
            autocolorscale=False,
            reversescale=False,
            marker_line_color='black',
            marker_line_width=0.5,
            colorbar_title='Count',
            zauto=True
        ))

        # Mesophile (trace 4)
        meso = choropleth[choropleth['ExtremeType'] == 'Mesophile']

        fig.add_trace(go.Choropleth(
            locations=meso['Country'],
            locationmode="country names",
            z=meso['Count'],
            text=meso['Country'],
            colorscale=px.colors.sequential.YlOrRd,
            autocolorscale=False,
            reversescale=False,
            marker_line_color='black',
            marker_line_width=0.5,
            colorbar_title='Count',
            zauto=True
        ))

        # Halothermophile (trace 5)
        ht = choropleth[choropleth['ExtremeType'] == 'Halothermophile']

        fig.add_trace(go.Choropleth(
            locations=ht['Country'],
            locationmode="country names",
            z=ht['Count'],
            text=ht['Country'],
            colorscale=px.colors.sequential.YlOrRd,
            autocolorscale=False,
            reversescale=False,
            marker_line_color='black',
            marker_line_width=0.5,
            colorbar_title='Count',
            zauto=True
        ))

        # Alkaliphile (trace 6)
        alkali = choropleth[choropleth['ExtremeType'] == 'Alkaliphile']

        fig.add_trace(go.Choropleth(
            locations=alkali['Country'],
            locationmode="country names",
            z=alkali['Count'],
            text=alkali['Country'],
            colorscale=px.colors.sequential.YlOrRd,
            autocolorscale=False,
            reversescale=False,
            marker_line_color='black',
            marker_line_width=0.5,
            colorbar_title='Count',
            zauto=True
        ))

        # Haloalkaliphile (trace 7)
        ha = choropleth[choropleth['ExtremeType'] == 'Haloalkaliphile']

        fig.add_trace(go.Choropleth(
            locations=ha['Country'],
            locationmode="country names",
            z=ha['Count'],
            text=ha['Country'],
            colorscale=px.colors.sequential.YlOrRd,
            autocolorscale=False,
            reversescale=False,
            marker_line_color='black',
            marker_line_width=0.5,
            colorbar_title='Count',
            zauto=True
        ))

        # create button that changes the data presented. the index of True aligns with the indices of plot traces
        fig.update_layout(
            updatemenus=[go.layout.Updatemenu(
                active=0,
                buttons=list(
                    [dict(label='<i>Choose here...</i>',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False]},
                                {'title': '<i>Click on the dropdown menu to choose what to visualize...</i>',
                                 'showlegend': True}]),
                     dict(label='ALL',
                          method='update',
                          args=[{'visible': [True, False, False, False, False, False, False, False]},
                                {'title': '<b>Global</b> geodemographic distribution of EPS producers',
                                 'showlegend': True}]),
                     dict(label='Halophile',
                          method='update',
                          args=[{'visible': [False, True, False, False, False, False, False, False]},
                                {'title': '<b>Halophile</b> distribution',
                                 'showlegend': True}]),
                     dict(label='Psychrophile',
                          method='update',
                          args=[{'visible': [False, False, True, False, False, False, False, False]},
                                {'title': '<b>Psychrophile</b> distribution',
                                 'showlegend': True}]),
                     dict(label='Thermophile',
                          method='update',
                          args=[{'visible': [False, False, False, True, False, False, False, False]},
                                {'title': '<b>Thermophile</b> distribution',
                                 'showlegend': True}]),
                     dict(label='Mesophile',
                          method='update',
                          args=[{'visible': [False, False, False, False, True, False, False, False]},
                                {'title': '<b>Mesophile</b> distribution',
                                 'showlegend': True}]),
                     dict(label='Halothermophile',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, True, False, False]},
                                {'title': '<b>Halothermophile</b> distribution',
                                 'showlegend': True}]),
                     dict(label='Alkaliphile',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, True, False]},
                                {'title': '<b>Alkaliphile</b> distribution',
                                 'showlegend': True}]),
                     dict(label='Haloalkaliphile',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, True]},
                                {'title': '<b>Haloalkaliphile</b> distribution',
                                 'showlegend': True}]),
                     ])
            )
            ])

        fig.update_layout(
            title_text='Geodemographic distribution of extremophilic types',
            geo=dict(
                showframe=True,
                showcoastlines=True,
                showland=True,
                showlakes=True,
                showrivers=True,
                framewidth=.1,
                projection_type='natural earth'),
            margin=dict(l=0, r=0, t=50, b=0))

        st.plotly_chart(fig, use_container_width = True, theme = None)
    with st.container(border=True):
        metricsByType = pd.DataFrame(identity['ExtremeType']).join(biometrics)

        ### TEMPERATURE
        # obtain all minimum, optimum and maximum TEMPERATURE points for a type of extremophile
        Thermophile_Temp = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['MinT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['OptT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['MaxT']))
        Halothermophile_Temp = np.array(
            list(metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['MinT']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['OptT']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['MaxT']))
        Psychrophile_Temp = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['MinT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['OptT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['MaxT']))
        Halophile_Temp = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Halophile']['MinT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Halophile']['OptT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Halophile']['MaxT']))
        Mesophile_Temp = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['MinT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['OptT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['MaxT']))
        Haloalkaliphile_Temp = np.array(
            list(metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['MinT']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['OptT']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['MaxT']))
        Alkaliphile_Temp = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['MinT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['OptT']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['MaxT']))

        # --------------------------
        # Plot temperature ranges for each extremophile
        # --------------------------
        fig = go.Figure()
        fig.add_trace(
            go.Box(x=Psychrophile_Temp, name='Psychrophile', marker_color='deepskyblue', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))
        fig.add_trace(
            go.Box(x=Haloalkaliphile_Temp, name='Haloalkaliphile', marker_color='lightpink', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))
        fig.add_trace(go.Box(x=Alkaliphile_Temp, name='Alkaliphile', marker_color='darkorchid', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))
        fig.add_trace(go.Box(x=Halophile_Temp, name='Halophile', marker_color='mediumseagreen', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))
        fig.add_trace(
            go.Box(x=Mesophile_Temp, name='Mesophile', marker_color='dimgray', boxpoints='all', jitter=0.5, marker_size=5,
                   pointpos=0))
        fig.add_trace(
            go.Box(x=Halothermophile_Temp, name='Halothermophile', marker_color='sandybrown', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))
        fig.add_trace(go.Box(x=Thermophile_Temp, name='Thermophile', marker_color='indianred', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))

        fig.update_layout(title_text='<b>Temperature</b> range for every extremophilic type',
                          xaxis_title='Temperature (ºC)')
        st.plotly_chart(fig, use_container_width = True, theme = None)

        # ---

        # obtain all minimum, optimum and maximum pH points for a type of extremophile
        Thermophile_PH = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['MinPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['OptPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['MaxPH']))
        Halothermophile_PH = np.array(
            list(metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['MinPH']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['OptPH']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['MaxPH']))
        Psychrophile_PH = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['MinPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['OptPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['MaxPH']))
        Halophile_PH = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Halophile']['MinPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Halophile']['OptPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Halophile']['MaxPH']))
        Mesophile_PH = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['MinPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['OptPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['MaxPH']))
        Haloalkaliphile_PH = np.array(
            list(metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['MinPH']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['OptPH']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['MaxPH']))
        Alkaliphile_PH = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['MinPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['OptPH']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['MaxPH']))

        # --------------------------
        # Plot pH ranges for each geofeature
        # --------------------------
        fig = go.Figure()
        fig.add_trace(
            go.Box(x=Halothermophile_PH, name='Halothermophile', marker_color='sandybrown', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))
        fig.add_trace(
            go.Box(x=Psychrophile_PH, name='Psychrophile', marker_color='deepskyblue', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))
        fig.add_trace(go.Box(x=Thermophile_PH, name='Thermophile', marker_color='indianred', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))
        fig.add_trace(go.Box(x=Halophile_PH, name='Halophile', marker_color='mediumseagreen', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))
        fig.add_trace(
            go.Box(x=Mesophile_PH, name='Mesophile', marker_color='dimgray', boxpoints='all', jitter=0.5, marker_size=5,
                   pointpos=0))
        fig.add_trace(
            go.Box(x=Haloalkaliphile_PH, name='Haloalkaliphile', marker_color='lightpink', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))
        fig.add_trace(go.Box(x=Alkaliphile_PH, name='Alkaliphile', marker_color='darkorchid', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))

        fig.update_layout(title_text='<b>pH</b> range for every extremophilic type',
                          xaxis_title='pH')
        st.plotly_chart(fig, use_container_width=True, theme=None)

        # ---

        # obtain all minimum, optimum and maximum SALT% points for a type of extremophile
        Thermophile_Salt = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['MinSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['OptSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Thermophile']['MaxSalt']))
        Halothermophile_Salt = np.array(
            list(metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['MinSalt']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['OptSalt']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Halothermophile']['MaxSalt']))
        Psychrophile_Salt = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['MinSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['OptSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Psychrophile']['MaxSalt']))
        Halophile_Salt = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Halophile']['MinSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Halophile']['OptSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Halophile']['MaxSalt']))
        Mesophile_Salt = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['MinSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['OptSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Mesophile']['MaxSalt']))
        Haloalkaliphile_Salt = np.array(
            list(metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['MinSalt']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['OptSalt']) + list(
                metricsByType[metricsByType['ExtremeType'] == 'Haloalkaliphile']['MaxSalt']))
        Alkaliphile_Salt = np.array(list(metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['MinSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['OptSalt']) + list(
            metricsByType[metricsByType['ExtremeType'] == 'Alkaliphile']['MaxSalt']))

        # --------------------------
        # Plot salinity ranges for each extremophile
        # --------------------------
        fig = go.Figure()
        fig.add_trace(go.Box(x=Thermophile_Salt, name='Thermophile', marker_color='indianred', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))
        fig.add_trace(go.Box(x=Alkaliphile_Salt, name='Alkaliphile', marker_color='darkorchid', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))
        fig.add_trace(
            go.Box(x=Psychrophile_Salt, name='Psychrophile', marker_color='deepskyblue', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))
        fig.add_trace(
            go.Box(x=Haloalkaliphile_Salt, name='Haloalkaliphile', marker_color='lightpink', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))
        fig.add_trace(
            go.Box(x=Mesophile_Salt, name='Mesophile', marker_color='dimgray', boxpoints='all', jitter=0.5, marker_size=5,
                   pointpos=0))
        fig.add_trace(go.Box(x=Halophile_Salt, name='Halophile', marker_color='mediumseagreen', boxpoints='all', jitter=0.5,
                             marker_size=5, pointpos=0))
        fig.add_trace(
            go.Box(x=Halothermophile_Salt, name='Halothermophile', marker_color='sandybrown', boxpoints='all', jitter=0.5,
                   marker_size=5, pointpos=0))

        fig.update_layout(title_text='<b>Salinity</b> range for every extremophilic type',
                          xaxis_title='Salinity (%)')
        st.plotly_chart(fig, use_container_width=True, theme = None)
    with st.container(border=True):
        data = pd.read_excel("data/composition_pol.xlsx", sheet_name="dataset", skiprows=1)
        monomers = pd.read_excel("data/composition_mon.xlsx", sheet_name="monomers", skiprows=1)
        monomers = monomers.iloc[:, 2:]

        # Create a list of cationic, anionic, and uncharged monomers for composition radar charts
        cationic = []
        anionic = []
        neutral = []

        for i in monomers.index:
            monomer = monomers['Monomer'][i]
            charge = monomers['Expected Charge'][i]
            if charge == -1:
                anionic.append(monomer)
            elif charge == 1:
                cationic.append(monomer)
            else:
                neutral.append(monomer)

        # Obtain list of columns in molar ratio/weight percentage
        composition = pd.Series(["Glc", "Man", "Gal", "Alt", "GlcN", "ManNAc", "GalNAc", "GulNAc", "GlcN", "ManN", "GalN", "GlcA", "GalA", "Rha", "Fuc", "QuiNAc", "FucNAc", "Ara", "Xyl", "Rib", "LDmanHep", "Kdo", "DDmanHep", "Api", "Fru"])

        # obtain global and specific metrics for MOLAR RATIO
        mean = [0.44, 0.48,0.27,0.01,0.07,0.00,0.05,0.01,0.05,0.00,0.03,0.09,0.15,0.07,0.08,0.05,0.01,0.11,0.08,0.01,0.01,0.02,0.00,0.00,0.03]
        median = [0.34,0.50,0.08,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
        mean_Thermophile = data[composition][data['ExtremeType'] == 'Thermophile'].mean()
        mean_Psychrophile = data[composition][data['ExtremeType'] == 'Psychrophile'].mean()
        mean_Halothermophile = data[composition][data['ExtremeType'] == 'Halothermophile'].mean()
        mean_Halophile = data[composition][data['ExtremeType'] == 'Halophile'].mean()
        mean_Haloalkaliphile = data[composition][data['ExtremeType'] == 'Haloalkaliphile'].mean()
        mean_Mesophile = data[composition][data['ExtremeType'] == 'Mesophile'].mean()
        mean_Alkaliphile = data[composition][data['ExtremeType'] == 'Alkaliphile'].mean()

        # instantiate graph
        fig = go.Figure()

        # create barplot traces for MOLAR RATIO (traces 0-8)
        fig.add_trace(
            go.Bar(x=data[composition].columns, y=mean_Thermophile, name='Thermophile', marker_color='indianred'))
        fig.add_trace(
            go.Bar(x=data[composition].columns, y=mean_Psychrophile, name='Psychrophile', marker_color='deepskyblue'))
        fig.add_trace(go.Bar(x=data[composition].columns, y=mean_Halothermophile, name='Halothermophile',
                             marker_color='sandybrown'))
        fig.add_trace(
            go.Bar(x=data[composition].columns, y=mean_Halophile, name='Halophile', marker_color='mediumseagreen'))
        fig.add_trace(go.Bar(x=data[composition].columns, y=mean_Haloalkaliphile, name='Haloalkaliphile',
                             marker_color='lightpink'))
        fig.add_trace(go.Bar(x=data[composition].columns, y=mean_Mesophile, name='Mesophile', marker_color='dimgray'))
        fig.add_trace(
            go.Bar(x=data[composition].columns, y=mean_Alkaliphile, name='Alkaliphile', marker_color='darkorchid'))
        fig.add_trace(go.Scatter(x=data[composition].columns, y=mean, name='Global average', marker_color='black',
                                 mode='markers'))
        fig.add_trace(go.Scatter(x=data[composition].columns, y=median, name='Global median', marker_color='white',
                                 marker_line_width=1, mode='markers'))

        fig.update_layout(barmode='stack', barnorm='',
                          # xaxis={'categoryorder':'total descending'},  ### BAR ORDERING DOESN'T WORK IN BUTTON MAPPING
                          title_text='Compositional fingerprint of all polysaccharide in the database, releaving extremophilic patterns',
                          yaxis_title="Molar ratio (cumulative)",
                          margin=dict(l=0, r=0, t=50, b=0))
        fig.update_xaxes(tickangle=35)

        st.plotly_chart(fig, use_container_width=True, theme="streamlit")
    with st.container(border=True):
        data = pd.read_excel("data/composition_pol.xlsx", sheet_name="dataset", skiprows=1)
        monomers = pd.read_excel("data/composition_mon.xlsx", sheet_name="monomers", skiprows=1)
        monomers = monomers.iloc[:, 2:]

        # Create a list of cationic, anionic, and uncharged monomers for composition radar charts
        cationic = []
        anionic = []
        neutral = []

        for i in monomers.index:
            monomer = monomers['Monomer'][i]
            charge = monomers['Expected Charge'][i]
            if charge == -1:
                anionic.append(monomer)
            elif charge == 1:
                cationic.append(monomer)
            else:
                neutral.append(monomer)

        # Obtain list of columns in molar ratio/weight percentage
        composition = pd.Series(
            ["Glc", "Man", "Gal", "Alt", "GlcN", "ManNAc", "GalNAc", "GulNAc", "GlcN", "ManN", "GalN", "GlcA", "GalA",
             "Rha", "Fuc", "QuiNAc", "FucNAc", "Ara", "Xyl", "Rib", "LDmanHep", "Kdo", "DDmanHep", "Api", "Fru"])


        ### RADAR CHART OF MONOMER POLARITY IN EXTREMOPHILIC EPS

        def percentage(part, whole):
            # Transform absolute data in axis to % of max
            return 100 * float(part) / float(whole)


        fig = go.Figure()

        # Draw opacity region for cationic monomers
        fig.add_trace(go.Barpolar(
            r=[1, 1],
            theta=cationic,
            width=[1, 0.5],
            offset=[0, 0],
            marker_color='steelblue',
            marker_line_width=0,
            opacity=0.3,
            name='Cationic region'
        ))

        # Draw opacity region for anionic monomers
        fig.add_trace(go.Barpolar(
            r=[1, 1],
            theta=anionic,
            width=[1, 0.5],
            offset=[-0.5, -0.5],
            marker_color=['crimson', 'crimson'],
            marker_line_width=0,
            opacity=0.3,
            name='Anionic region'
        ))

        # Draw opacity region for neutral monomers
        fig.add_trace(go.Barpolar(
            r=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            theta=neutral,
            width=[13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            offset=[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            marker_color=['oldlace', 'oldlace'],
            marker_line_width=0,
            opacity=0.6,
            name='Neutral region'
        ))

        # Setting legend groups
        extremophiles = {
            'Type': ['Thermophile', 'Psychrophile', 'Halothermophile', 'Halophile', 'Haloalkaliphile', 'Mesophile'],
            'Color Key': ['crimson', 'lightseagreen', 'peachpuff', 'darkorange', 'mediumpurple', 'mediumseagreen']}

        extremeColorCode = pd.DataFrame(extremophiles, columns=['Type', 'Color Key'])

        for type in extremeColorCode['Type']:
            fig.add_trace(go.Scatterpolar(
                r=[0],
                theta=['Glc'],
                showlegend=True,
                legendgroup=type,
                name=type,
                marker=dict(color='black')
            ))

        # Plotting data points by extremophile
        # Thermophile
        for n in range(len(data)):
            if data.iloc[n]['ExtremeType'] == 'Thermophile':
                fig.add_trace(go.Scatterpolargl(
                    r=data[composition].iloc[n],
                    theta=composition,
                    mode="markers",
                    name=data['Strain'][n],
                    legendgroup='Thermophile',
                    showlegend=False,
                    marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='crimson')
                ))

        # Psychrophile
        for n in range(len(data)):
            if data.iloc[n]['ExtremeType'] == 'Psychrophile':
                fig.add_trace(go.Scatterpolargl(
                    r=data[composition].iloc[n],
                    theta=composition,
                    mode="markers",
                    name=data['Strain'][n],
                    legendgroup='Psychrophile',
                    showlegend=False,
                    marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='lightseagreen')
                ))

        # Halothermophile
        for n in range(len(data)):
            if data.iloc[n]['ExtremeType'] == 'Halothermophile':
                fig.add_trace(go.Scatterpolargl(
                    r=data[composition].iloc[n],
                    theta=composition,
                    mode="markers",
                    name=data['Strain'][n],
                    legendgroup='Halothermophile',
                    showlegend=False,
                    marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='peachpuff')
                ))

        # Halophile
        for n in range(len(data)):
            if data.iloc[n]['ExtremeType'] == 'Halophile':
                fig.add_trace(go.Scatterpolargl(
                    r=data[composition].iloc[n],
                    theta=composition,
                    mode="markers",
                    name=data['Strain'][n],
                    legendgroup='Halophile',
                    showlegend=False,
                    marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='darkorange')
                ))

        # Haloalkaliphile
        for n in range(len(data)):
            if data.iloc[n]['ExtremeType'] == 'Haloalkaliphile':
                fig.add_trace(go.Scatterpolargl(
                    r=data[composition].iloc[n],
                    theta=composition,
                    mode="markers",
                    name=data['Strain'][n],
                    legendgroup='Haloalkaliphile',
                    showlegend=False,
                    marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='mediumpurple')
                ))

        # Mesophile
        for n in range(len(data)):
            if data.iloc[n]['ExtremeType'] == 'Mesophile':
                fig.add_trace(go.Scatterpolargl(
                    r=data[composition].iloc[n],
                    theta=composition,
                    mode="markers",
                    name=data['Strain'][n],
                    legendgroup='Mesophile',
                    showlegend=False,
                    marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='mediumseagreen')
                ))

        fig.update_traces(marker_line_width=1)
        fig.update_layout(template=None, title='<b>Choose extreme types to visualize and compare their radial prevalence:</b>')

        # Choose default initial visualization
        fig.update_traces(visible="legendonly")  # <----- deselect all lines
        fig.data[0].visible = True  # <------ display cationic region
        fig.data[1].visible = True  # <------ display anionic region
        fig.data[2].visible = True  # <------ display neutral region

        st.plotly_chart(fig, use_container_width=True, theme=None)
with gd:
    st.header("Graphic Design")
    st.caption(
        "Complex, accurate demonstrations are essential to convey messages that extend beyond the dimensions of written text. Scientific research in particular benefits"
        " immensely from reliable data visualization, proper color reporting, appropriate choice of graph types, easily interpretable representations during public speaking, "
        "and illustrating very succintly the core results of research in a graphical abstract which often accompanies the publication of a scientific paper.")

    with st.container(border=True):
        st.markdown("Skills demonstrated in this section:")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Adobe Illustrator")
        with col2: st.info("Photoscape X")
        with col3: st.info("GraphPad Prism")
        with col4: st.info("MS Powerpoint")
        with col5: st.info("Creative Content")

    # Multiselect for selecting chapters
    selected_chapters = st.selectbox("Select content to visualize:",
                                       ["Choose here...",
                                        "Pão Nosso news project",
                                        "MDPI Polymers 2021 Best Cover Paper Award",
                                        "Community Content Creation"])

    # Display the content of selected chapters
    if "Pão Nosso news project" in selected_chapters:
        st.header("Pão Nosso News")
        st.caption("The **Pão Nosso News**, a pun of Portuguese origin alluding to *'our everyday bread (or chunk, of information'*, was a daily and weekly digital newspaper curation project, initially designed to disseminate information to teenagers, in one minute or less. The goal involved producing appealing graphic visualizations of the state of affair in Portugal and the world that teens would find captivating. Social media is populated by viralized content that is filtered by algorithms intended to capture attention. This project aimed to re-populate the Instagram feed of teenagers with meaningful content that could contribute towards a more well-informed, intellectual society of the future.")

        st.subheader("Official logotyping")
        st.image("https://i.imgur.com/uYLJZkh.png", width=500)

        st.divider()
        st.subheader("Highlights artwork")
        st.image("https://i.imgur.com/2wnwYs7.png")
        st.divider()
        st.subheader("Daily panel templating (Instagram 9x16 story format)")
        st.image("https://i.imgur.com/D7gctJb.png")
        st.divider()
        st.subheader("Weekly panel templating (Instagram 1x1 post format)")
        st.image("https://i.imgur.com/ZNZ7GGH.png")
        st.divider()
        st.subheader("Final result")
        st.image("https://i.imgur.com/bC2pDzf.png")

    if "MDPI Polymers 2021 Best Cover Paper Award" in selected_chapters:
        st.image("https://i.imgur.com/JyWJvs0.jpg")
    if "Community Content Creation" in selected_chapters:
        st.image("https://i.postimg.cc/c17KFZ2L/atc1.png")
        st.image("https://i.postimg.cc/VLYJTpPB/atc2.png")
        st.image("https://i.postimg.cc/fThcb8nJ/atc3.png")
        st.image("https://i.postimg.cc/tTx6qxB3/atc4.png")
        st.image("https://i.postimg.cc/SKj8P58t/atc5.png")
        st.image("https://i.postimg.cc/wBb5THgp/atc6.png")
with tw:
    st.header("Technical Writing")
    st.caption("Performing research in life sciences requires precision and thoroughness in experimental etiquette. However, proper documentation of findings and"
               " description of equipment, systems and *modus operandi* is essential. Here you can find some examples of technical writing, which required a thorough description"
               "of hardware building, software writing, and methodologies to guarantee the reproducibility of research findings and insights.")

    with st.container(border=True):
        st.markdown("Skills demonstrated in this section:")
        c1,c2,c3,c4 = st.columns(4)
        c1.info("Technical Knowledge")
        c2.info("Proofreading")
        c3.info("Word / LaTeX")

    # Multiselect for selecting chapters
    selected_chapters = st.multiselect("Select content to visualize:", ["Choose here...",
                                                                        "Isochoric Nucleation Detection: Build, architecture, Python-automated workflows",
                                                                        "Data Science tools applied to Life Sciences"])

    # Display the content of selected chapters
    if "Isochoric Nucleation Detection: Build, architecture, Python-automated workflows" in selected_chapters:
        st.markdown("#### Isochoric Nucleation Detection: Build, architecture, Python-automated workflows")

        with open("./data/inde.pdf", "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="85%" height="800" style="display: block; margin: 0 auto;" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    if "Data Science tools applied to Life Sciences" in selected_chapters:
        st.markdown("#### Data Science tools applied to Life Sciences: scraping, loading, analysis, modelling, visualization")

        with open("./data/datasciencetools.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="85%" height="800" style="display: block; margin: 0 auto;" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
with proj:
    st.header("Projects")
    st.caption("In this section you'll find DIY projects that I've created as a direct application of my skills. Some have been developed for practical purposes, mainly for "
               "my Ph.D. work, others were developed as a proof-of-concept that I could convert the learned knowledge into something practical and useful.")

    # Multiselect for selecting chapters
    selected_chapters = st.selectbox("Select content to visualize:",
                                     ["Choose here...",
                                      "Crystal.AI Computer Vision Algorithm",
                                      "CryoPod",
                                      "Isochoric Nucleation Detection",
                                      "Discord Bots"])
with media:
    st.header("Media")
    st.caption("During my career, I have participated in several outreach activities, out of excitement to communicate and teach what I'm passionate for. This involved volunteer lectures,"
               "ambassadorial participations, being interviewed for national newspapers and participating in podcasts. Find here the relevant media outreach where I was privileged to share my contributions so far.")

    st.write("'Organs with longer shelf-life', in print, Expresso journal")

st.write('---')
st.markdown('<div style="text-align: right;"><sub>Bruno M. Guerreiro © 2024</sub></div>', unsafe_allow_html=True)