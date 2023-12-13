import streamlit as st  # 🎈 data web app development
from streamlit_timeline import timeline
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import base64

### METADATA
st.set_page_config(
    page_title="Bruno M. Guerreiro | Portfolio",
    page_icon="🇵🇹",
    layout="wide",
)

### SIDEBAR

# Custom JavaScript code to open the sidebar by default
#st.sidebar.title("🇵🇹 Bruno M. Guerreiro")
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

st.write('---')
st.markdown('<div style="text-align: right;"><sub>Bruno M. Guerreiro © 2024</sub></div>', unsafe_allow_html=True)


with aboutme:
    ### TIMELINE
    with open('timeline.json', "r") as f:
        data = f.read()
    timeline(data, height=600)

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
        with col1: st.info("EDA")
        with col2: st.info("Feature Engineering")
        with col3: st.info("Data Visualization")
        with col4: st.info("Critical Thinking")
        with col5: st.info("Problem Solving")
        with col6: st.info("Storytelling")

    st.markdown("")

    phd_colormap = {'Thermophile': 'indianred', 'Halothermophile': 'sandybrown',
                    'Psychrophile': 'deepskyblue', 'Halophile': 'mediumseagreen',
                    'Mesophile': 'black', 'Haloalkaliphile': 'lightpink', 'Alkaliphile': 'darkorchid'}

    col1, col2 = st.columns(2)

    with col1:
        st.empty()

    with col2:
        year_df = pd.read_excel("data/year.xlsx")

        fig = px.violin(data_frame=year_df, x='Year', y='ExtremeType', orientation='h', color='ExtremeType',
                        color_discrete_map=phd_colormap
                        ).update_traces(orientation='h', side='positive', width=1, points='all', pointpos=0, jitter=0.35,
                        marker_size=8
                        ).update_yaxes(categoryorder="min descending", title_text=""
                                       ).update_xaxes(dtick=10)

        fig.update_xaxes(title_text="<b>Year of publication</b>")  # Set x-axis title

        fig.update_layout(
            width=500,  # Set the width of the chart
            height=400,  # Set the height of the chart
            showlegend=False,
            title_text="<b>What has been the research focus over the years?</b>",
        )

        # Display the plot using Streamlit
        st.plotly_chart(fig, use_container_width=True, theme=None)

    # Multiselect for selecting chapters
    st.subheader("Choose a database")
    selected_database = st.selectbox("", ["Visualize a database here...",
                                          "CryoPolDB",
                                          "Complementary monomer database"])

    if "Visualize a database here..." in selected_database:
        st.write("")
    if "CryoPolDB" in selected_database:
        data = pd.read_csv("./data/streamlit-poldb.csv")
    if "Complementary monomer database" in selected_database:
        monomers = pd.read_csv("./data/streamlit-mondb.csv")

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

with media:
    st.header("Media")
    st.caption("During my career, I have participated in several outreach activities, out of excitement to communicate and teach what I'm passionate for. This involved volunteer lectures,"
               "ambassadorial participations, being interviewed for national newspapers and participating in podcasts. Find here the relevant media outreach where I was privileged to share my contributions so far.")

    st.expander("'Organs with longer shelf-life', in print, Expresso journal")