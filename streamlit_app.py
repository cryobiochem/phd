import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime

st.header('Digital Appendix')
st.markdown('#### Implications of a polysaccharide gel undercooler in Classical Nucleation Theory')

# Authors
st.markdown('B. M. Guerreiro¹²*, M.M. Dionísio³, J.C. Lima³, J.C. Silva⁴, F. Freitas¹²*')
# Affiliations
st.markdown('¹UCIBIO – Applied Molecular Biosciences Unit, Department of Chemistry, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
st.markdown('²Associate Laboratory i4HB - Institute for Health and Bioeconomy, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
st.markdown('³LAQV-REQUIMTE, Department of Chemistry, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
st.markdown('⁴CENIMAT/I3N, Department of Physics, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
st.write('*Corresponding authors.')

st.write('---')

# Example 2

st.header ('1. Nucleation & Growth of ice')
st.write('During solidification, the atomic arrangement changes from a random or short-range order to a long range order or crystal structure. Nucleation occurs when a small nucleus begins to form in the liquid, the nuclei then grows as atoms from the liquid are attached to it. The crucial point is to understand it as a balance between the free energy available from the driving force, and the energy consumed in forming new interface. Once the rate of change of free energy becomes negative, then an embryo can grow.')

st.subheader("Critical radius $r^*$")
st.write('The critical radius $r^*$ is the checkpoint at which an embryo undergoing growth-decay fluctuations is finally stable enough to survive and grow further. Whenever $r \geq r^*$, nucleation begins.')
st.write('The critical radius $r^*$ is the checkpoint at which an embryo undergoing growth-decay fluctuations is finally stable enough to survive and grow further. Whenever $r \geq r^*$, nucleation begins. The critical radius can be determined as follows: ')

st.latex(r'r*= \frac{2\gamma_SL}{∆G_v}')

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

st.subheader('Select extremophile category')
extremeType = st.select_slider(
    'Select a type of extremophile:',
    options=['Psychrophile', 'Thermophile', 'Halophile', 'Mesophile', 'Alkaliphile', 'Halothermophile', 'Haloalkaliphile'])
st.write('You have visualizing data on:', extremeType)