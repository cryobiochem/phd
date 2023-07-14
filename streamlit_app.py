import streamlit as st  # 🎈 data web app development
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import numpy as np  # generate numbers for functions
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import plotly.graph_objects as go
import altair as alt
from datetime import time, datetime # to simulate a real time data, time loop

# https://blog.streamlit.io/how-to-build-a-real-time-live-dashboard-with-streamlit/
# https://30days.streamlit.app/?challenge=Day9

st.set_page_config(
    page_title="Cryobiophysics by B. M. Guerreiro",
    page_icon="🧊",
    #layout="wide",
)

st.title("🧊 Cryobiophysics")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Who am I",
                                        "CryoPol-DB",
                                        "Database Generation",
                                        "Digital Appendix",
                                        "beta-test"])
with tab1:
    st.empty()
    #
with tab2:
    db = pd.read_csv("./data/db-streamlit-test.csv", skiprows=1)

    # Customize Ag-Grid options here: https://archive.is/20230531152052/https://towardsdatascience.com/7-reasons-why-you-should-use-the-streamlit-aggrid-component-2d9a2b6e32f0
    gb = GridOptionsBuilder.from_dataframe(db)
    # 1. Add pagination
    gb.configure_pagination()
    # 2. Columns can be pinned, grouped and aggregated
    gb.configure_side_bar()
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
    # 3. Allow the Ag-Grid to interact with other Streamlit objects
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    from st_aggrid.shared import GridUpdateMode

    # Construct the db
    gridOptions = gb.build()
    data = AgGrid(db,
                  gridOptions=gridOptions,
                  enable_enterprise_modules=True,
                  allow_unsafe_jscode=True,
                  update_mode=GridUpdateMode.SELECTION_CHANGED
                  )
with tab3:
    st.subheader('Motivation')
    st.write(
        '*Small-molecule cryoprotectants like glycerol, DMSO and trehalose have been extensively studied mechanistically regarding their antifreeze effect. Larger molecules such as PEG and some polyampholytes have also shown potential towards ice growth inhibition. However, cryopreservation research using carbohydrate polymers – particularly bio-based polysaccharides – has been lacking. Despite their inherent biocompatibility that tackles one of the main issues of cryoprotectant exposure, cytotoxicity, most literature focuses purely on post hoc biological viability rather than mechanistic clarifications towards their function, with regards to ice binding, modulation or inhibition. Polysaccharides produced by psychrophiles (cold-adapted microorganisms) that ensure survival in extreme sub-zero habitats are a prime comparative model towards understanding this structure-function interplay. In this review, we summarize the current literature on polysaccharides used in cryopreservation applications and attempt to discern the structural features that contribute to antifreeze performance, from the point of view of polysaccharide-ice interactions.*')

    st.subheader('CryoPol-DB')
    st.write(
        'A database containing 145 extremophilic exopolysaccharides (EPS) characterized by 128 organic and 16 mathematically calculated parameters was compiled. The database was split into categories, with 12 variables characterizing microorganism identity, 22 variables for microorganism growth/EPS production conditions, 33 for polysaccharide composition, 12 for polysaccharide structure, 10 for EPS macromolecular fractions, 33 for polysaccharide characteristics (15 for physicochemical properties + 18 for biological functions) and 14 for cryoprotection (7 for biological evidence + 7 for explanatory mechanisms of action). Publishing metadata such as year published, journal and impact factor were discarded for this study. The full database can be found [here](https://cryobiophysics.streamlit.app/#implications-of-a-polysaccharide-gel-undercooler-in-classical-nucleation-theory).')

    option = st.selectbox('Select a category...',
                          ('Home',
                           '*Ab initio* considerations',
                           'Host growth & habitat',
                           'EDA: Composition',
                           'EDA: Structure',
                           'EDA: Properties',
                           'EDA: Function',
                           'MLAP Calculations'))

    if option == 'Home':
        st.write('')

    if option == '*Ab initio* considerations':
        st.write('under maintenance')

    if option == 'Host growth & habitat':
        st.subheader('Select extremophile category')
        extremeType = st.select_slider(
            'Select a type of extremophile:',
            options=['Psychrophile', 'Thermophile', 'Halophile', 'Mesophile', 'Alkaliphile', 'Halothermophile',
                     'Haloalkaliphile'])
        st.write('You have visualizing data on:', extremeType)

    if option == 'EDA: Composition':

        # Slider
        st.subheader('Monomer composition')

        fucose = st.slider('Fucose content (wt.%)', 0, 100, 10)
        st.write("Visualizing all polysaccharides with at least", fucose, '% fucose content.')

        # Example 2
        st.subheader('Compositional range')

        fuc_range = st.slider(
            'Select an interval:',
            0.0, 100.0, (5.0, 25.0))
        st.write("Visualizing all polysaccharides with a fucose content between", fuc_range, '%.')

    else:
        st.write('')
with tab4:
    st.subheader("2020")
    with st.expander("Implications of a polysaccharide gel undercooler in Classical Nucleation Theory, *Carb Pol*, **2023**"):
        st.markdown('#### Implications of a polysaccharide gel undercooler in Classical Nucleation Theory')

        # Authors
        st.markdown('B. M. Guerreiro¹²*, M.M. Dionísio³, J.C. Lima³, J.C. Silva⁴, F. Freitas¹²*')
        # Affiliations
        st.markdown(
            '¹UCIBIO – Applied Molecular Biosciences Unit, Department of Chemistry, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
        st.markdown(
            '²Associate Laboratory i4HB - Institute for Health and Bioeconomy, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
        st.markdown(
            '³LAQV-REQUIMTE, Department of Chemistry, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
        st.markdown(
            '⁴CENIMAT/I3N, Department of Physics, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
        st.write('*Corresponding authors.')

        st.write('---')

        # Nucleation
        st.header('1. Nucleation & Growth of ice')
        st.write(
            'During solidification, the atomic arrangement changes from a random or short-range order to a long range order or crystal structure. Nucleation occurs when a small nucleus begins to form in the liquid, the nuclei then grows as atoms from the liquid are attached to it. The crucial point is to understand it as a balance between the free energy available from the driving force, and the energy consumed in forming new interface. Once the rate of change of free energy becomes negative, then an embryo can grow.')

        st.subheader("Critical radius $r^*$")
        st.write(
            'The critical radius $r^*$ is the checkpoint at which an embryo undergoing growth-decay fluctuations is finally stable enough to survive and grow further. Whenever $r \geq r^*$, nucleation begins.')
        st.write(
            'The critical radius $r^*$ is the checkpoint at which an embryo undergoing growth-decay fluctuations is finally stable enough to survive and grow further. Whenever $r \geq r^*$, nucleation begins. The critical radius can be determined as follows: ')

        st.latex(r'r*= \frac{2\gamma_SL}{∆G_v}')

        # Create interaction plot with sliders
        st.write('The following graph expresses this equation:')


        # Define the function to calculate r* based on the equation
        def calculate_r_star(delta_G_v, gamma_SL):
            return 2 * gamma_SL / delta_G_v


        # Set up the Streamlit app
        st.title("Visualization of r* Equation")

        # Create sliders for the variables
        delta_G_v = st.slider("Change in Gibbs free energy per unit volume", min_value=1.0, max_value=10.0, value=5.0,
                              step=0.01)
        gamma_SL = st.slider("Surface tension of the liquid-gas interface", min_value=0.1, max_value=1.0, value=0.5,
                             step=0.01)

        # Generate random x values
        x = np.linspace(0, 10, 100)

        # Calculate corresponding r* values based on the equation
        y = calculate_r_star(delta_G_v, gamma_SL) * np.sin(x)

        # Create a pandas DataFrame with x and y values
        data = {"x": x, "r*": y}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="x", y="r*", title="")

        # Update layout and axes ranges
        fig.update_layout(
            xaxis_range=[0, 5],
            yaxis_range=[-2, 2]
        )

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

        st.write('---')

        st.subheader('Heterogenous Ice Nucleation')

    st.subheader("2023")
    for i in range(1, 5):
        with st.expander(f"Expander {i}"):
            st.empty()
with tab5:
    st.empty()
    #https://github.com/Kanaries/pygwalker