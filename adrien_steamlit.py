import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

# Page title and sidebar
st.title("Adrien Treuille: The LLM Genius Predicts the Future")
st.sidebar.header("Adjust the Genius Predictions")

# Numerical input sliders for years
years_into_future_bar = st.sidebar.slider("Years Into Future (Bar Chart)", min_value=1, max_value=5, value=3)
years_into_future_line = st.sidebar.slider("Years Into Future (Line Chart)", min_value=1, max_value=5, value=3)

# Create Altair bar chart
def create_bar_chart(years, data):
    chart = alt.Chart(pd.DataFrame({'Years Into Future': years, 'Probability': data})).mark_bar().encode(
        x='Years Into Future:O',
        y='Probability:Q'
    ).properties(
        width=600,
        height=400
    ).configure_title(
        fontSize=16
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    )
    return chart

# Create Altair line chart
def create_line_chart(years, data):
    chart = alt.Chart(pd.DataFrame({'Years Into Future': years, 'Probability': data})).mark_line().encode(
        x='Years Into Future:O',
        y='Probability:Q'
    ).properties(
        width=600,
        height=400
    ).configure_title(
        fontSize=16
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    )
    return chart

# Display Adrien's predictions
st.write("Adrien Treuille's Predictions:")
bar_chart_years = np.arange(0, years_into_future_bar + 1)
bar_chart_data = np.random.uniform(0, 1, len(bar_chart_years))
bar_chart = create_bar_chart(bar_chart_years, bar_chart_data)
st.altair_chart(bar_chart, use_container_width=True)

line_chart_years = np.arange(0, years_into_future_line + 1)
line_chart_data = np.cumsum(np.random.uniform(0, 1, len(line_chart_years)))
line_chart = create_line_chart(line_chart_years, line_chart_data)
st.write("Adrien's thoughts on reaching singularity:")
st.altair_chart(line_chart, use_container_width=True)

# Humorous predictions
st.write("Adrien's Predictions:")
if np.max(bar_chart_data) > 0.5:
    st.write(f"The probability of Generative AI taking over in {years_into_future_bar} years is {np.max(bar_chart_data):.2f}")
else:
    st.write("Don't worry, generative AI won't take over too soon.")

if np.max(line_chart_data) > 0.5:
    st.write(f"The probability of reaching singularity in {years_into_future_line} years is {np.max(line_chart_data):.2f}")
else:
    st.write("The singularity can wait a bit longer. We have time for more coding!")

# Disclaimer
st.write("*Disclaimer: This app is for entertainment purposes only. Adrien Treuille is not actually predicting the future.")
