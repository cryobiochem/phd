import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime
import plotly.graph_objects as go

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

# Nucleation
st.header ('1. Nucleation & Growth of ice')
st.write('During solidification, the atomic arrangement changes from a random or short-range order to a long range order or crystal structure. Nucleation occurs when a small nucleus begins to form in the liquid, the nuclei then grows as atoms from the liquid are attached to it. The crucial point is to understand it as a balance between the free energy available from the driving force, and the energy consumed in forming new interface. Once the rate of change of free energy becomes negative, then an embryo can grow.')

st.subheader("Critical radius $r^*$")
st.write('The critical radius $r^*$ is the checkpoint at which an embryo undergoing growth-decay fluctuations is finally stable enough to survive and grow further. Whenever $r \geq r^*$, nucleation begins.')
st.write('The critical radius $r^*$ is the checkpoint at which an embryo undergoing growth-decay fluctuations is finally stable enough to survive and grow further. Whenever $r \geq r^*$, nucleation begins. The critical radius can be determined as follows: ')

st.latex(r'r*= \frac{2\gamma_SL}{∆G_v}')


# Define the function to calculate r* based on the equation
def calculate_r_star(delta_G_v, gamma_SL):
    return 2 * gamma_SL / delta_G_v

# Set up the Streamlit app
st.title("Visualization of r* Equation")

# Create sliders for the variables
delta_G_v = st.slider("Change in Gibbs free energy per unit volume", min_value=1.0, max_value=50.0, value=5.0)
gamma_SL = st.slider("Surface tension of the liquid-gas interface", min_value=0.1, max_value=1.0, value=0.5)

# Generate random x values
x = np.linspace(0, 10, 100)

# Calculate corresponding r* values based on the equation
y = calculate_r_star(delta_G_v, gamma_SL) * np.sin(x)

# Create the plotly figure
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

# Update layout, axis labels, and axes ranges
fig.update_layout(
    title="r* = 2 * gamma_SL / delta_G_v * sin(x)",
    xaxis_title="x",
    yaxis_title="r*",
    xaxis_range=[0, 5],
    yaxis_range=[-2, 2]
)

# Display the plot with real-time updates
st.plotly_chart(fig, use_container_width=True)


st.write('---')
















# Create interaction plot with sliders
st.write('The following graph expresses this equation:')


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