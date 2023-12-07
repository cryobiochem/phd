import streamlit as st  # 🎈 data web app development
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import numpy as np  # generate numbers for functions
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
st.markdown("##### A data science project by Bruno M. Guerreiro © 2024")
st.write('---')

tab1, tab2, tab3, tab4, database = st.tabs(["Who am I",
                                        "CryoPol-DB",
                                        "Database Generation",
                                        "Digital Appendix",
                                        "Database"])
with tab1:
    st.empty()
    #
with tab2:
    st.empty()
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
    with st.expander('Energetics of Ice Nucleation'):
        st.write('The nucleation activation energy barrier $\Delta G_n$ is an energetic balance between opposing contributions. When a cluster of a new phase forms, the system decreases its free energy. This is the :blue[driving force] for nucleation and is directly proportional to the volume of the cluster, or $n$:')
        st.latex(r'-\frac{4}{3} \pi r ^ 3 \Delta G_v')

        st.write('In contrast, forming an interface between the parent phase and the new cluster has an :red[energetic cost], proportional to the surface area of the cluster, or $n^{2/3}$:')
        st.latex(r'4\pi r^2 \gamma_{\text{SL}}')

        st.write('The system will follow the :green[energy barrier landscape], which can be expressed by a combination of gain and cost functions:')
        st.latex(r'\Delta G_n = -\frac{4}{3} \pi r^3 \Delta G_v + 4\pi r^2 \gamma_{SL}')

        st.subheader('Critical and equilibrium radii, $r^*$ and $r_{eq}$')
        st.markdown('- At $r < r^*$, clusters will grow and decay continuously, due to thermal fluctuations.')
        st.markdown('- When $r = r^*$, a cluster that gains a single atom will overcome the energy barrier to transition to a stable nuclei than can grow. The radius $r^*$ is the minimum size a nuclei can possess in the system.')
        st.markdown('- At $r > r^*$, we have still in non-spontaneous $\Delta G > 0$ territory. Here, the stable nuclei will grow up to a max radius of $r_{eq}$, which is when $\Delta G_n = \Delta G = 0$. $r_{eq}$ is called the equilibrium radius when it occurs when the system reaches thermodynamic equilibrium, but it is not the center point in a Boltzmann distribution of nuclei sizes. When the negative free energy landscape begins, crystallization is finally spontaneous and can proceed to bigger sizes.')
        st.write('---')


        def calculate_curves(delta_G_v, gamma_SL, r):
            InterfacialEnergy = 4 * np.pi * r ** 2 * gamma_SL
            VolumeFreeEnergy = -4 / 3 * np.pi * r ** 3 * delta_G_v
            NucleationEnergyBarrier = -4 / 3 * np.pi * r ** 3 * delta_G_v + 4 * np.pi * r ** 2 * gamma_SL
            return InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier
        def find_equilibrium_radius(r, NucleationEnergyBarrier):
            zero_crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier)))[0]
            valid_zero_crossings = zero_crossings[NucleationEnergyBarrier[zero_crossings] != 0]
            if len(valid_zero_crossings) > 0:
                r_equilibrium = r[valid_zero_crossings[0]]
                return r_equilibrium
            else:
                return None
        def find_critical_radius(r, NucleationEnergyBarrier):
            peak_index = np.argmax(NucleationEnergyBarrier)
            r_critical = r[peak_index]
            return r_critical


        col1, col2 = st.columns(2)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("$\gamma$", min_value=0.00, max_value=1.00, value=0.90,
                                 step=0.01, key='nucleation1')

        with col2:
            delta_G_v = st.slider("$\Delta G_v$", min_value=0.000, max_value=0.400,
                                  value=0.270, step=0.001, key='nucleation2')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier = calculate_curves(delta_G_v, gamma_SL, r)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Interfacial energy": InterfacialEnergy, "Volumetric free energy": VolumeFreeEnergy,
                "Nucleation barrier": NucleationEnergyBarrier}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Interfacial energy", "Volumetric free energy", "Nucleation barrier"],
                      color_discrete_map={"Interfacial energy": "red", "Volumetric free energy": "blue",
                                          "Nucleation barrier": "green"})
        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="&#8710;G",
                          # https://www.toptal.com/designers/htmlarrows/math/
                          yaxis_range=[-200, 200], xaxis_range=[0, 12])

        # Plot equilibrium radius
        r_equilibrium = find_equilibrium_radius(r, NucleationEnergyBarrier)
        if r_equilibrium is not None:
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius'))
            fig.add_annotation(x=r_equilibrium, y=0, text='Equilibrium Radius', showarrow=True, arrowhead=1, ax=0,
                               ay=-10)

        # Plot critical radius
        r_critical = find_critical_radius(r, NucleationEnergyBarrier)
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]], mode='markers',
                       marker=dict(color='green', size=8),
                       name='Critical Radius'))
        fig.add_annotation(x=r_critical, y=NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)],
                           text='Critical Radius', showarrow=True,
                           arrowhead=1, ax=-0, ay=-10)

        # Add a static curve based on Curve 3 with constant values
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Pure water'))

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("But nucleation is Heterogenous"):
        st.latex(r'\Delta G_n^{het} = \Bigg[-\frac{4}{3}\pi r^3 \Delta G_v + 4\pi r^2 \gamma_{SL}\Bigg] \Bigg[\frac{2- 3\cos(\theta) + \cos^{3}(\theta)}{4}\Bigg]')

        def calculate_curves(delta_G_v, gamma_SL, r, theta):
            InterfacialEnergy = 4 * np.pi * r ** 2 * gamma_SL
            VolumeFreeEnergy = -4 / 3 * np.pi * (r ** 3) * delta_G_v
            NucleationEnergyBarrier = -4 / 3 * np.pi * r ** 3 * delta_G_v + 4 * np.pi * r ** 2 * gamma_SL
            Heterogenous = NucleationEnergyBarrier * (2 - 3 * np.cos(np.radians(theta)) + np.cos(np.radians(theta)) ** 3) / 4
            return InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier, Heterogenous


        def calculate_critical_equilibrium_radius(r, curve):
            # Calculate the critical radius
            peak_index = np.argmax(curve)
            r_critical = r[peak_index]

            # Calculate the equilibrium radius
            zero_crossings = np.where(np.diff(np.sign(curve)))[0]
            valid_zero_crossings = zero_crossings[curve[zero_crossings] != 0]
            if len(valid_zero_crossings) > 0:
                r_equilibrium = r[valid_zero_crossings[0]]
            else:
                r_equilibrium = None

            return r_critical, r_equilibrium


        col1, col2, col3 = st.columns(3)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("$\gamma$", min_value=0.00, max_value=1.00, value=0.90,
                                 step=0.01, key='nucleation_eq_1_2')

        with col2:
            delta_G_v = st.slider("$\Delta G_v$", min_value=0.000, max_value=0.400,
                                  value=0.270, step=0.001, key='nucleation_eq_2_2')

        with col3:
            theta = st.slider("$\Theta$", min_value=0.0, max_value=90.0, value=90.0, step=1.0, key='nucleation_eq_3_1')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier, Heterogenous = calculate_curves(delta_G_v, gamma_SL, r, theta)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Homogeneous": NucleationEnergyBarrier, "Heterogeneous": Heterogenous}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Homogeneous", "Heterogeneous"],
                      color_discrete_map={"Homogeneous": "green", "Heterogeneous": "purple"})
        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="ΔG",
                          yaxis_range=[-200, 200], xaxis_range=[0, 12])

        ### Calculate equilibrium radius and critical radius for Homogeneous curve
        r_critical, r_equilibrium = calculate_critical_equilibrium_radius(r, NucleationEnergyBarrier)

        ### Calculate equilibrium radius and critical radius for Heterogeneous curve
        r_critical_het, r_equilibrium_het = calculate_critical_equilibrium_radius(r, Heterogenous)

        # Add light green markers for the equilibrium radius in Curve 3
        if r_equilibrium:
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius (Homogeneous)'))

        # Add light purple markers for the equilibrium radius in Heterogeneous curve
        if r_equilibrium_het:
            fig.add_trace(
                go.Scatter(x=[r_equilibrium_het], y=[0], mode='markers', marker=dict(color='pink', size=8),
                           name='Equilibrium Radius (Heterogeneous)'))

        # Add green marker for the critical radius in Curve 3
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]], mode='markers',
                       marker=dict(color='green', size=8),
                       name='Critical Radius (Homogeneous)'))

        # Add purple marker for the critical radius in Heterogeneous curve
        fig.add_trace(
            go.Scatter(x=[r_critical_het], y=[Heterogenous[np.argmax(Heterogenous)]], mode='markers',
                       marker=dict(color='purple', size=8),
                       name='Critical Radius (Heterogeneous)'))

        # Add the Heterogeneous curve based on the equation
        fig.add_trace(go.Scatter(x=r, y=Heterogenous, mode='lines', line=dict(color='purple'), name='Heterogeneous'))

        # Add a static curve based on Curve 3 with constant values
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Reference'))
        fig.update_layout(showlegend=True)

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)


    with st.expander("Zeldovich factor $Z$"):

        st.write(
            'The size interval $\Delta r$ characterizes the energy profile around the critical size $r^*$. Two pieces of evidence and one inference point to a necessary reduction in $\Delta r$:')
        st.markdown('- POM experiments showed crystal sizes 10x smaller.')
        st.markdown('- Isochoric experiments showed a narrowing of $\Delta T_n$.')
        st.markdown(
            '- Inferences from rheology data and gel-induced selective polymorphism point to a reduction in crystal size distribution.')
        st.write('')
        st.write(
            'Therefore, the $\Delta r$ component appears highly connected to $\Delta T_n$, and should equally decrease to 1/3.')


        def calculate_curves(delta_G_v, gamma_SL, r):
            InterfacialEnergy = 4 * np.pi * r ** 2 * gamma_SL
            VolumeFreeEnergy = -4 / 3 * np.pi * r ** 3 * delta_G_v
            NucleationEnergyBarrier = -4 / 3 * np.pi * r ** 3 * delta_G_v + 4 * np.pi * r ** 2 * gamma_SL
            return InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier


        def find_equilibrium_radius(r, NucleationEnergyBarrier):
            zero_crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier)))[0]
            valid_zero_crossings = zero_crossings[NucleationEnergyBarrier[zero_crossings] != 0]
            if len(valid_zero_crossings) > 0:
                r_equilibrium = r[valid_zero_crossings[0]]
                return r_equilibrium
            else:
                return None


        def find_critical_radius(r, NucleationEnergyBarrier):
            peak_index = np.argmax(NucleationEnergyBarrier)
            r_critical = r[peak_index]
            return r_critical, peak_index


        def calculate_delta_r(NucleationEnergyBarrier, k, T, kT_correction_factor):
            NucleationEnergyBarrier_y = NucleationEnergyBarrier.copy()
            y_value = NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)] - k * T * kT_correction_factor
            crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier - y_value)))[0]
            deltaR_min = {"y value": y_value, "x1 value": r[crossings[0]]}
            deltaR_max = {"y value": y_value, "x2 value": r[crossings[1]]}
            deltaR = deltaR_max["x2 value"] - deltaR_min["x1 value"]
            return deltaR, deltaR_min, deltaR_max


        def calculate_kT_percentage(NucleationEnergyBarrier, k, T, kT_correction_factor):
            kT_value = k * T * kT_correction_factor
            max_energy_barrier = NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]
            kT_percentage = (kT_value / max_energy_barrier) * 100
            return kT_percentage


        def calculate_Zeldovich(deltaR):
            Zeldovich = 2 / (np.pi ** (1 / 2) * deltaR)
            return Zeldovich


        k = 1.380649e-23  # Boltzmann constant
        T = 373.15  # Temperature in Kelvin
        kT_correction_factor = 1e21  # 1e21 is a temporary factor to relatively describe the graph

        col1, col2 = st.columns(2)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("$\gamma$", min_value=0.00, max_value=1.00, value=0.90,
                                 step=0.01, key='deltaR_1')

        with col2:
            delta_G_v = st.slider("$\Delta G_v$", min_value=0.000, max_value=0.400,
                                  value=0.270, step=0.001, key='deltaR_2')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier = calculate_curves(delta_G_v, gamma_SL, r)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Interfacial energy": InterfacialEnergy, "Volumetric free energy": VolumeFreeEnergy,
                "Nucleation barrier": NucleationEnergyBarrier}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Interfacial energy", "Volumetric free energy", "Nucleation barrier"],
                      color_discrete_map={"Interfacial energy": "red", "Volumetric free energy": "blue",
                                          "Nucleation barrier": "green"})

        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="&#8710;G",
                          yaxis_range=[-200, 200], xaxis_range=[0, 12])

        # Plot equilibrium radius
        r_equilibrium = find_equilibrium_radius(r, NucleationEnergyBarrier)
        if r_equilibrium is not None:
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius'))
            fig.add_annotation(x=r_equilibrium, y=0, text='Equilibrium Radius', showarrow=True, arrowhead=1, ax=0,
                               ay=-10)

        # Find the critical radius and its index
        r_critical, peak_index = find_critical_radius(r, NucleationEnergyBarrier)
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]], mode='markers',
                       marker=dict(color='green', size=8),
                       name='Critical Radius'))
        fig.add_annotation(x=r_critical, y=NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)],
                           text='Critical Radius', showarrow=True,
                           arrowhead=1, ax=-0, ay=-10)

        # Calculate deltaR
        deltaR, deltaR_min, deltaR_max = calculate_delta_r(NucleationEnergyBarrier, k, T, kT_correction_factor)

        # Plot deltaR_min and deltaR_max as orange markers and a horizontal orange line
        fig.add_trace(go.Scatter(x=[deltaR_min["x1 value"], deltaR_max["x2 value"]],
                                 y=[deltaR_min["y value"], deltaR_max["y value"]],
                                 mode='markers', marker=dict(color='orange', size=8),
                                 name='Delta R'))
        fig.add_shape(type="line",
                      x0=deltaR_min["x1 value"], y0=deltaR_min["y value"],
                      x1=deltaR_max["x2 value"], y1=deltaR_max["y value"],
                      line=dict(color='orange', width=2))

        # Static curve: Homogeneous Nucleation of pure water as reference
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Pure water'))

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

        # Calculate percentage described by kT
        kT_percentage = calculate_kT_percentage(NucleationEnergyBarrier, k, T, kT_correction_factor)

        # Calculate Zeldovich factor
        Zeldovich = calculate_Zeldovich(deltaR)

        stat1, stat2, stat3 = st.columns(3)
        with stat1: st.metric("**Thermal fluctuations (%)**", round(kT_percentage, 2))
        with stat2: st.metric("$\Delta r$", round(deltaR, 3))
        with stat3: st.metric("$Z$", round(Zeldovich, 2))

        st.write('In another perspective, the Zeldovich factor $Z$ controls the flatness of the energy profile. For two systems having the same free energy barriers, the system with the flatter free energy landscape near the barrier has **more diffusive nucleation dynamics** and a lower nucleation rate.')



    with st.expander("Effect of volumetric confinement: partition of $n$"):
        st.write(
            'The previous energy profiles have a relationship to the total number of atoms $n$ available in the system to migrate to the cluster.')
        st.markdown('- The volumetric free energy is proportional to $-n$.')
        st.markdown('- The interfacial energy is proportional to $n^{2/3}$.')

        import streamlit as st
        import numpy as np
        import pandas as pd
        import plotly.express as px
        import plotly.graph_objects as go


        def calculate_curves(delta_G_v, gamma_SL, r, n):
            InterfacialEnergy = 4 * np.pi * r ** 2 * gamma_SL * (n ** (2 / 3))
            VolumeFreeEnergy = -4 / 3 * np.pi * r ** 3 * delta_G_v * n
            NucleationEnergyBarrier = -4 / 3 * np.pi * r ** 3 * delta_G_v * n + 4 * np.pi * r ** 2 * gamma_SL * (
                        n ** (2 / 3))
            return InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier


        def find_equilibrium_radius(r, NucleationEnergyBarrier):
            zero_crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier)))[0]
            valid_zero_crossings = zero_crossings[NucleationEnergyBarrier[zero_crossings] != 0]
            if len(valid_zero_crossings) > 0:
                r_equilibrium = r[valid_zero_crossings[0]]
                return r_equilibrium
            else:
                return None


        def find_critical_radius(r, NucleationEnergyBarrier):
            peak_index = np.argmax(NucleationEnergyBarrier)
            r_critical = r[peak_index]
            return r_critical, peak_index


        def calculate_delta_r(NucleationEnergyBarrier, k, T, kT_correction_factor):
            NucleationEnergyBarrier_y = NucleationEnergyBarrier.copy()
            y_value = NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)] - k * T * kT_correction_factor
            crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier - y_value)))[0]
            deltaR_min = {"y value": y_value, "x1 value": r[crossings[0]]}
            deltaR_max = {"y value": y_value, "x2 value": r[crossings[1]]}
            deltaR = deltaR_max["x2 value"] - deltaR_min["x1 value"]
            return deltaR, deltaR_min, deltaR_max


        def calculate_kT_percentage(NucleationEnergyBarrier, k, T, kT_correction_factor):
            kT_value = k * T * kT_correction_factor
            max_energy_barrier = NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]
            kT_percentage = (kT_value / max_energy_barrier) * 100
            return kT_percentage


        def calculate_Zeldovich(deltaR):
            Zeldovich = 2 / (np.pi ** (1 / 2) * deltaR)
            return Zeldovich


        k = 1.380649e-23  # Boltzmann constant
        T = 373.15  # Temperature in Kelvin
        kT_correction_factor = 1e21  # 1e21 is a temporary factor to relatively describe the graph

        col1, col2, col3 = st.columns(3)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("$\gamma$", min_value=0.00, max_value=1.00, value=0.90, step=0.01, key='meeting1')

        with col2:
            delta_G_v = st.slider("$\Delta G_v$", min_value=0.01, max_value=1.00, value=0.30, step=0.01,
                                  key='meeting2')

        with col3:
            # Create slider for the variable n
            n = st.slider("n", min_value=0.01, max_value=2.00, value=1.00, step=0.01, key='meeting3')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier = calculate_curves(delta_G_v, gamma_SL, r, n)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Interfacial energy": InterfacialEnergy, "Volumetric free energy": VolumeFreeEnergy,
                "Nucleation barrier": NucleationEnergyBarrier}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Interfacial energy", "Volumetric free energy", "Nucleation barrier"],
                      color_discrete_map={"Interfacial energy": "red", "Volumetric free energy": "blue",
                                          "Nucleation barrier": "green"})

        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="∆G", yaxis_range=[-200, 200], xaxis_range=[0, 12])

        # Plot equilibrium radius
        r_equilibrium = find_equilibrium_radius(r, NucleationEnergyBarrier)
        if r_equilibrium is not None:
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius'))
            fig.add_annotation(x=r_equilibrium, y=0, text='Equilibrium Radius', showarrow=True, arrowhead=1, ax=0,
                               ay=-10)

        # Find the critical radius and its index
        r_critical, peak_index = find_critical_radius(r, NucleationEnergyBarrier)
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]], mode='markers',
                       marker=dict(color='green', size=8), name='Critical Radius'))
        fig.add_annotation(x=r_critical, y=NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)],
                           text='Critical Radius', showarrow=True, arrowhead=1, ax=-0, ay=-10)

        # Calculate deltaR
        deltaR, deltaR_min, deltaR_max = calculate_delta_r(NucleationEnergyBarrier, k, T, kT_correction_factor)

        # Plot deltaR_min and deltaR_max as orange markers and a horizontal orange line
        fig.add_trace(go.Scatter(x=[deltaR_min["x1 value"], deltaR_max["x2 value"]],
                                 y=[deltaR_min["y value"], deltaR_max["y value"]], mode='markers',
                                 marker=dict(color='orange', size=8), name='Delta R'))
        fig.add_shape(type="line", x0=deltaR_min["x1 value"], y0=deltaR_min["y value"], x1=deltaR_max["x2 value"],
                      y1=deltaR_max["y value"], line=dict(color='orange', width=2))

        # Static curve: Homogeneous Nucleation of pure water as reference
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Pure water'))

        # Calculate Zeldovich factor from deltaR
        Z = calculate_Zeldovich(deltaR)

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

        # Calculate percentage described by kT
        kT_percentage = calculate_kT_percentage(NucleationEnergyBarrier, k, T, kT_correction_factor)

        # Display metrics
        stat1, stat2, stat3 = st.columns(3)
        with stat1:
            st.metric("**Thermal fluctuations (%)**", round(kT_percentage, 2))
        with stat2:
            st.metric("∆r", round(deltaR, 3))
        with stat3:
            st.metric("Z", round(Z, 2))

    st.write('---')

    st.header('Kinetic Rationale')
    with st.expander("Zeldovich factor"):


        st.subheader('Zeldovich factor')



    with st.expander("Effect of viscosity $\eta$"):
        st.empty()

    st.write('---')

with database:
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # Load Data
    db = pd.read_csv("./data/db-streamlit-test.csv", skiprows=1)
    db.fillna('[Unknown]', inplace=True)

    # Sidebar Filters
    st.sidebar.header("Database Navigation")

    # Toggle button for README visibility
    show_readme = st.sidebar.button("Toggle README")

    # Selectbox for choosing the parameter with a default text
    selected_parameter = st.sidebar.selectbox("Distributions by parameter",
                                              ["Select type of distribution here...", "Extremophile Type", "Kingdom",
                                               "Phylum", "Respiration"])

    # Visualization based on selection
    if show_readme:
        st.subheader("About the database")
        st.write(
            'A database containing 145 extremophilic exopolysaccharides (EPS) characterized by 128 organic and 16 mathematically calculated parameters was compiled. The database was split into categories, with 12 variables characterizing microorganism identity, 22 variables for microorganism growth/EPS production conditions, 33 for polysaccharide composition, 12 for polysaccharide structure, 10 for EPS macromolecular fractions, 33 for polysaccharide characteristics (15 for physicochemical properties + 18 for biological functions) and 14 for cryoprotection (7 for biological evidence + 7 for explanatory mechanisms of action).')

    elif selected_parameter == "Extremophile Type":
        st.header('Distribution of polysaccharide dataset by:')
        extremetype_pie = px.pie(db, names='ExtremeType', title='Extremophile Type')
        st.plotly_chart(extremetype_pie)

    elif selected_parameter == "Kingdom":
        kingdom_pie = px.pie(db, names='Kingdom', title='Kingdom')
        st.plotly_chart(kingdom_pie)

    elif selected_parameter == "Phylum":
        phylum_pie = px.pie(db, names='Phylum', title='Phylum')
        st.plotly_chart(phylum_pie)

    elif selected_parameter == "Respiration":
        st.header('Type of respiratory metabolism')

        # Create a 3x3 panel for pie charts using make_subplots
        row_count = 3
        col_count = 3
        fig = make_subplots(rows=row_count, cols=col_count, subplot_titles=db['ExtremeType'].unique(),
                            specs=[[{'type': 'pie'}] * col_count] * row_count)

        # Iterate over each unique ExtremeType and create a pie chart
        for i, extreme_type in enumerate(db['ExtremeType'].unique()):
            row_num = (i // col_count) + 1
            col_num = (i % col_count) + 1

            filtered_data = db[db['ExtremeType'] == extreme_type]
            pie_chart = go.Figure(
                go.Pie(labels=filtered_data['Respiration'].unique(), values=filtered_data['Respiration'].value_counts()))
            fig.add_trace(pie_chart['data'][0], row=row_num, col=col_num)

        # Update layout and show the plot
        fig.update_layout(height=600, width=800)
        st.plotly_chart(fig)

st.write('---')
st.markdown('<div style="text-align: right;"><sub>Bruno M. Guerreiro © 2024</sub></div>', unsafe_allow_html=True)