import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px

# Read data from the xlsx file
df = pd.read_excel('tripadvisor_data.xlsx')
df['min_price'] = df['min_price'].astype(float).fillna(df['min_price'].mean())
df['max_price'] = df['max_price'].astype(float).fillna(df['max_price'].mean())

# Create a folium map centered on the mean latitude and longitude
map_center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=12)

# Add markers for each place
for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        tooltip=f"<b>{row['name']}</b><br><img src='{row['image']}' width='150px'>",
    ).add_to(m)

st.header('The 100 Hotels In Baku')

# Create sidebar filters
classes = sorted(df['class'].unique())
selected_class = st.sidebar.selectbox('Select class', ['', *classes])
min_price = st.sidebar.slider('Minimum price', min_value=float(df['min_price'].min()), max_value=float(df['min_price'].max()), value=float(df['min_price'].min()))
max_price = st.sidebar.slider('Maximum price', min_value=float(df['max_price'].min()), max_value=float(df['max_price'].max()), value=float(df['max_price'].max()))

# Filter data based on sidebar inputs
if selected_class == '':
    filtered_df = df[(df['min_price'] >= min_price) &
                     (df['max_price'] <= max_price)]
else:
    filtered_df = df[(df['class'] == selected_class) & (df['min_price'] >= min_price) & (df['max_price'] <= max_price)]

# Add filtered markers to the map
for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        tooltip=f"<b>{row['name']}</b><br><img src='{row['image']}' width='150px'>",
        icon=folium.Icon(color='green', icon='info-sign'),
    ).add_to(m)

# Display the map
folium_static(m)

# Add charts
st.subheader('Hotel Prices')
fig = px.histogram(filtered_df, x='min_price', nbins=20)
st.plotly_chart(fig)

st.subheader('Hotel Ratings')
fig = px.box(filtered_df, x='class', y='rating')
st.plotly_chart(fig)