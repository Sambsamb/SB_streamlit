# Based on https://docs.streamlit.io/library/get-started/create-an-app
# Github URL https://github.com/Sambsamb/SB_streamlit/blob/master/uberpickupexample.py
# Streamlit URL https://sambsamb-sb-streamlit-uberpickupexample-9w4ie0.streamlitapp.com/
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
'Sam Boutros'
st.text('FHSU - Fall 2022 - INF601 Advanced Python')
st.write('Prof. Jason Zeller')
st.text('Week 6 - Streamlit practice')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache  # Effortless caching
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the website user know the data is loading.
data_load_state = st.text('Loading data...')
data = load_data(10000)  # Load 10,000 rows of data into the dataframe.
data_load_state.text("Done! (using st.cache)")  # Notify the user that the data was successfully loaded.

# Inspect the raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Draw a histogram
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# Plot data on a map
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)



