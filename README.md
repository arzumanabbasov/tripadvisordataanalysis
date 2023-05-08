# Baku Hotels Map

This is a web application that displays a map of 100 hotels in Baku, the capital city of Azerbaijan. The application allows users to filter hotels based on their class (1 to 5 stars) and price range, and also provides charts of hotel prices and ratings. 

## Prerequisites

To run this application, you need to have the following software installed on your system:

- Python 3.x
- Streamlit
- Pandas
- Folium
- Streamlit Folium
- Plotly Express

## Installation

1. Clone or download the repository to your local machine.
2. Open a terminal window and navigate to the project directory.
3. Install the required packages by running the following command: `pip install -r requirements.txt`
4. Run the application with the following command: `streamlit run app.py`
5. The application should open in your default web browser.

## Usage

Once the application is running, you can use the sidebar filters to select hotels based on their class and price range. The filtered hotels will be displayed on the map with green markers, while the unfiltered hotels will be displayed with red markers. Hovering over a marker will display the hotel name and image in a tooltip.

You can also view charts of hotel prices and ratings by scrolling down the page. The charts will update dynamically based on the current filter settings.

## Acknowledgements

The data for this application was obtained from TripAdvisor and is for demonstration purposes only. The application was created by Arzuman Abbasov using Python, Streamlit, Pandas, Folium, Streamlit Folium, and Plotly Express.
