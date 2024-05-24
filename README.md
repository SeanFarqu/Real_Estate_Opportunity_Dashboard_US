# Real Estate Consulting Dashboard

## Overview

This Real Estate Consulting Dashboard provides insights into the US housing market. It highlights the best buyer opportunities for long-term investment based on forecasted home price increases. The dashboard uses historical housing price data and the Prophet model for time series forecasting to predict future prices.

## Features

- **US Housing Market Map**: A choropleth map that visualizes the best investment opportunities based on forecasted price increases.
- **State-Specific Analysis**: Allows users to explore historical home values for specific states.
- **Interactive Data Preview**: Option to view a preview of the dataset in the sidebar.

## Setup

### Prerequisites

Ensure you have the following installed:
- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:
git clone https://github.com/SeanFarqu/real-estate-dashboard.git
cd real-estate-dashboard

2. **Install the required packages**:
pip install streamlit pandas plotly geopandas prophet fiona

3. **Download the Natural Earth shapefile**:
- If you haven't done so already, download the "Admin 1 - States, Provinces" shapefile from [Natural Earth](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).
- Extract the contents to a directory, e.g., `ne_110m_admin_1_states_provinces`.

4. **Ensure the shapefile is in the correct directory**:
- Place the extracted shapefile in the repository directory or update the path in the script if necessary.

## Usage

1. **Run the Streamlit app**:
streamlit run Real_Estate_Dashboard.py

2. **Explore the Dashboard**:
- The main page displays a map of the US with color-coded regions representing the best investment opportunities based on forecasted price increases.
- Use the sidebar to optionally view a preview of the dataset.
- Use the dropdown menu to select a state and explore its historical home values.

## Files in the Repository

- `Real_Estate_Dashboard.py`: The main Python script for running the Streamlit dashboard.
- `State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv`: The dataset containing historical home prices.
- `ne_110m_admin_1_states_provinces.*`: The shapefiles for US states from Natural Earth.

## Acknowledgements

- Data source: [Zillow](https://www.zillow.com/research/data/)
- Shapefile: [Natural Earth](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/)
- Forecasting model: [Prophet](https://facebook.github.io/prophet/)
