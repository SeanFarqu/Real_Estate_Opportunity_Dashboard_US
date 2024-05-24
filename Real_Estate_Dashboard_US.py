import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.express as px
import geopandas as gpd

# Load the dataset
df = pd.read_csv('State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')

# Optional dataset preview in sidebar
if st.sidebar.checkbox('Show Dataset Preview'):
    st.sidebar.write("Dataset preview:")
    st.sidebar.write(df.head())

# Reshape the data from wide to long format
df_long = df.melt(id_vars=["RegionID", "SizeRank", "RegionName", "RegionType", "StateName"], 
                  var_name="Date", value_name="Zhvi")
df_long['Date'] = pd.to_datetime(df_long['Date'], format='%Y-%m-%d')

# Function to predict future home prices using Prophet
def predict_future_prices(df, years_ahead=5):
    future_months = years_ahead * 12
    model = Prophet()
    df_prophet = df.rename(columns={'Date': 'ds', 'Zhvi': 'y'})
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=future_months, freq='M')
    forecast = model.predict(future)
    future_price = forecast.iloc[-1]['yhat']
    return future_price

# Calculate the latest home prices and future prices
latest_data = df_long[df_long['Date'] == df_long['Date'].max()]
average_prices = latest_data.groupby('RegionName')['Zhvi'].mean().reset_index()
average_prices['FuturePrice'] = average_prices['RegionName'].apply(lambda state: predict_future_prices(df_long[df_long['RegionName'] == state]))

# Determine best investment opportunities
average_prices['PriceIncrease'] = average_prices['FuturePrice'] - average_prices['Zhvi']
average_prices['Opportunity'] = average_prices['PriceIncrease'].rank(ascending=False)

# Load US states shapefile from local directory
us_states = gpd.read_file("/Users/seanfarquharson/Documents/ne_110m_admin_1_states_provinces/ne_110m_admin_1_states_provinces.shp")

us_states = us_states.merge(average_prices, how='left', left_on='name', right_on='RegionName')

# Create the map
fig = px.choropleth(us_states,
                    geojson=us_states.geometry,
                    locations=us_states.index,
                    color='PriceIncrease',
                    hover_name='RegionName',
                    hover_data=['Zhvi', 'FuturePrice', 'PriceIncrease'],
                    title='US Housing Market: Best Buyer Opportunities',
                    color_continuous_scale='Viridis')

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})

# Streamlit App
st.title('Real Estate Opportunity Dashboard')
st.write("""
This dashboard provides insights into the US housing market, highlighting the best buyer opportunities for long-term investment based on forecasted home price increases.
""")

st.plotly_chart(fig)

# Allow user to explore specific states
st.header('Explore Specific States')
state = st.selectbox('Select a state to explore', sorted(df_long['RegionName'].unique()))
state_data = df_long[df_long['RegionName'] == state]

fig2 = px.line(state_data, x='Date', y='Zhvi', title=f'Historical Home Values in {state}')
st.plotly_chart(fig2)

