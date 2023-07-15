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
    with st.expander("Classical Nucleation Theory"):
        #st.markdown('#### Implications of a polysaccharide gel undercooler in Classical Nucleation Theory')

        # Authors & Affiliations
        #st.markdown('B. M. Guerreiro¹²*, M.M. Dionísio³, J.C. Lima³, J.C. Silva⁴, F. Freitas¹²*')
        #st.markdown('¹UCIBIO – Applied Molecular Biosciences Unit, Department of Chemistry, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
        #st.markdown('²Associate Laboratory i4HB - Institute for Health and Bioeconomy, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
        #st.markdown('³LAQV-REQUIMTE, Department of Chemistry, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
        #st.markdown('⁴CENIMAT/I3N, Department of Physics, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
        #st.write('*Corresponding authors.')


        # Nucleation
        st.header('1. Nucleation & Growth of ice')
        st.write('During solidification, the atomic arrangement changes from a random or short-range order to a long range order or crystal structure. Nucleation occurs when a small nucleus begins to form in the liquid, the nuclei then grows as atoms from the liquid are attached to it. The crucial point is to understand it as a balance between the free energy available from the driving force, and the energy consumed in forming new interface. Once the rate of change of free energy becomes negative, then an embryo can grow.')

        st.subheader("Critical radius $r^*$")
        st.write('The critical radius $r^*$ is the checkpoint at which an embryo undergoing growth-decay fluctuations is finally stable enough to survive and grow further. Whenever $r \geq r^*$, nucleation begins. The critical radius can be determined as follows: ')

        st.latex(r'r*= \frac{2\gamma_SL}{∆G_v}')


        st.subheader('Heterogenous Ice Nucleation')
        st.write('The nucleation activation energy barrier $\Delta G_n$ is an energetic balance between opposing contributions. When a cluster of a new phase forms, the system decreases its free energy. This is the :blue[driving force] for nucleation and is directly proportional to the volume of the cluster, or $n$:')
        st.latex(r'-\frac{4}{3} \pi r ^ 3 \Delta G_v')
        st.write('A two-phase system implies the creation of an interface between the parent phase and the new cluster. This has an energetic cost, proportional to the surface area of the cluster, or $n^{2/3}$:')
        st.latex(r'4\pi r^2 \gamma_{\text{SL}}')

        st.write('The energy barrier a system must overcome to nucleate is then expressed by a combination of gain and cost functions:')
        st.latex(r'\Delta G_n = -\frac{4}{3} \pi r^3 \Delta G_v + 4\pi r^2 \gamma_{SL}')

        st.write('Past the critical radius $r^*$, the system will enter equilibrium when $\Delta G_n = \Delta G$, which corresponds to when $\Delta G_n = 0$. Here, we can define the equilibrium radius $r_{eq}$, which expresses the average size that most ice nuclei will achieve, by a Boltzmann distribution.')


        def calculate_curves(delta_G_v, gamma_SL, r):
            curve1 = 4 * np.pi * r ** 2 * gamma_SL
            curve2 = -4 / 3 * np.pi * r ** 3 * delta_G_v
            curve3 = -4 / 3 * np.pi * r ** 3 * delta_G_v + 4 * np.pi * r ** 2 * gamma_SL
            return curve1, curve2, curve3


        col1, col2 = st.columns(2)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("Surface tension of the solid-liquid interface", min_value=0.00, max_value=1.00, value=0.35,
                                 step=0.01, key='nucleation_eq_1')

        with col2:
            delta_G_v = st.slider("Change in Gibbs free energy per unit volume", min_value=0.000, max_value=0.500,
                                  value=0.110, key='nucleation_eq_2')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        curve1, curve2, curve3 = calculate_curves(delta_G_v, gamma_SL, r)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Interfacial energy": curve1, "Volumetric free energy": curve2, "Nucleation barrier": curve3}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Interfacial energy", "Volumetric free energy", "Nucleation barrier"],
                      color_discrete_map={"Interfacial energy": "red", "Volumetric free energy": "blue", "Nucleation barrier": "green"})
        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="&#8710;G", #https://www.toptal.com/designers/htmlarrows/math/
                          yaxis_range=[-200,200], xaxis_range=[0,12])

        ### Calculate equilibrium radius
        # Identify the indices where curve3 crosses zero (excluding the origin)
        zero_crossings = np.where(np.diff(np.sign(curve3)))[0]
        valid_zero_crossings = zero_crossings[curve3[zero_crossings] != 0]
        # Add light green markers for zero crossings in Curve 3
        if len(zero_crossings) > 0:
            r_equilibrium = r[valid_zero_crossings[0]]
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius'))
            fig.add_annotation(x=r_equilibrium, y=0, text='Equilibrium Radius', showarrow=True, arrowhead=1, ax=0,
                               ay=-10)

        ### Calculate critical radius
        peak_index = np.argmax(curve3)
        r_critical = r[peak_index]
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[curve3[peak_index]], mode='markers', marker=dict(color='green', size=8),
                       name='Critical Radius'))
        fig.add_annotation(x=r_critical, y=curve3[peak_index], text='Critical Radius', showarrow=True, arrowhead=1,
                           ax=-0, ay=-10)

        # Add a static curve based on Curve 3 with constant values
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Pure water'))


        # Display the plot
        st.plotly_chart(fig, use_container_width=True)
        st.write('---')



    st.subheader("2023")
    for i in range(1, 5):
        with st.expander(f"Expander {i}"):
            st.empty()
with tab5:
    st.empty()