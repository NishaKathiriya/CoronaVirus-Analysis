import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import plotly.express as px
import mysql.connector
import os
# MySQL database connection function
def get_data_from_mysql(query):
    # Retrieve secrets from Streamlit
    db_user = st.secrets["mysql"]["DB_USER"]
    db_password = st.secrets["mysql"]["DB_PASSWORD"]
    db_host = st.secrets["mysql"]["DB_HOST"]
    db_port = st.secrets["mysql"]["DB_PORT"]
    db_name = st.secrets["mysql"]["DB_NAME"]

    # Create the database connection string
    connection_string = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)
    
    # Connect and fetch data
    with engine.connect() as connection:
        data = pd.read_sql(query, connection)
    
    return data

# Fetch data from MySQL
query = "SELECT * FROM corona_data"
df = get_data_from_mysql(query)

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Ensure relevant columns are numeric
df['Confirmed'] = pd.to_numeric(df['Confirmed'], errors='coerce')
df['Deaths'] = pd.to_numeric(df['Deaths'], errors='coerce')
df['Recovered'] = pd.to_numeric(df['Recovered'], errors='coerce')

# Set up Streamlit layout and title
st.title("COVID-19 Analytics Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
country_filter = st.sidebar.multiselect(
    "Select Country/Region:", 
    options=df["Country/Region"].unique(), 
    default=[]
)

# Date range input
date_filter = st.sidebar.date_input(
    "Select Date Range", 
    [df["Date"].min().date(), df["Date"].max().date()]  # Use .date() to convert to native date
)

# Apply filters to the data
filtered_df = df[(df["Country/Region"].isin(country_filter)) &
                (df["Date"].between(pd.to_datetime(date_filter[0]), pd.to_datetime(date_filter[1])))]

# Display filtered data
st.write("Filtered Data", filtered_df)

# Streamlit Metrics
st.subheader("Key Metrics")
total_confirmed = filtered_df["Confirmed"].sum()
total_deaths = filtered_df["Deaths"].sum()
total_recovered = filtered_df["Recovered"].sum()

st.metric("Total Confirmed Cases", f"{total_confirmed:,}")
st.metric("Total Deaths", f"{total_deaths:,}")
st.metric("Total Recovered", f"{total_recovered:,}")

# Monthly average calculations
if not filtered_df.empty:
    monthly_avg = filtered_df.resample('M', on='Date').mean(numeric_only=True)[["Confirmed", "Deaths", "Recovered"]]

    # Line chart for monthly averages
    st.subheader("Monthly Averages")
    st.line_chart(monthly_avg)

    # Most frequent values per month
    most_frequent = filtered_df.groupby(pd.Grouper(key='Date', freq='M')).agg(lambda x: x.mode()[0])
    st.subheader("Most Frequent Values per Month")
    st.write(most_frequent[["Confirmed", "Deaths", "Recovered"]])

    # Minimum values per year
    min_values = filtered_df.resample('Y', on='Date').min(numeric_only=True)[["Confirmed", "Deaths", "Recovered"]]
    st.subheader("Minimum Values per Year")
    st.write(min_values)

    # Maximum values per year
    max_values = filtered_df.resample('Y', on='Date').max(numeric_only=True)[["Confirmed", "Deaths", "Recovered"]]
    st.subheader("Maximum Values per Year")
    st.write(max_values)

    # Total cases by month
    total_cases_by_month = filtered_df.groupby(pd.Grouper(key='Date', freq='M')).sum(numeric_only=True)[["Confirmed", "Deaths", "Recovered"]]
    st.subheader("Total Cases per Month")
    st.bar_chart(total_cases_by_month)

    # Analysis of spread with respect to confirmed cases
    st.subheader("Analysis of Confirmed Cases")
    st.write("Total Confirmed:", total_confirmed)
    st.write("Average Confirmed:", filtered_df["Confirmed"].mean())
    st.write("Variance of Confirmed:", filtered_df["Confirmed"].var())
    st.write("Standard Deviation of Confirmed:", filtered_df["Confirmed"].std())

    # Analysis of spread with respect to death cases
    st.subheader("Analysis of Death Cases")
    st.write("Total Deaths:", total_deaths)
    st.write("Average Deaths:", filtered_df["Deaths"].mean())
    st.write("Variance of Deaths:", filtered_df["Deaths"].var())
    st.write("Standard Deviation of Deaths:", filtered_df["Deaths"].std())

    # Analysis of spread with respect to recovered cases
    st.subheader("Analysis of Recovered Cases")
    st.write("Total Recovered:", total_recovered)
    st.write("Average Recovered:", filtered_df["Recovered"].mean())
    st.write("Variance of Recovered:", filtered_df["Recovered"].var())
    st.write("Standard Deviation of Recovered:", filtered_df["Recovered"].std())

    # Find Country with highest number of Confirmed cases
    highest_confirmed_country = filtered_df.groupby("Country/Region")["Confirmed"].sum().idxmax()
    st.write("Country with Highest Confirmed Cases:", highest_confirmed_country)

    # Find Country with lowest number of Death cases
    lowest_death_country = filtered_df.groupby("Country/Region")["Deaths"].sum().idxmin()
    st.write("Country with Lowest Death Cases:", lowest_death_country)

    # Find top 5 countries with highest recovered cases
    top_recovered_countries = filtered_df.groupby("Country/Region")["Recovered"].sum().nlargest(5)
    st.subheader("Top 5 Countries with Highest Recovered Cases")
    st.write(top_recovered_countries)


# Horizontal Bar Chart using Plotly
st.subheader("Deaths by Country (Bar Chart)")
deaths_by_country = filtered_df.groupby("Country/Region")["Deaths"].sum()
bar_chart = px.bar(
    deaths_by_country.reset_index(),
    x="Deaths",
    y="Country/Region",
    orientation='h',
    title="Deaths by Country",
    labels={"Deaths": "Total Deaths", "Country/Region": "Country"}
)

st.plotly_chart(bar_chart)


# Bar graph using Plotly
st.subheader("Confirmed Cases by Province")
bar_chart = px.bar(
    filtered_df,
    x="Province",
    y="Confirmed",
    color="Country/Region",
    title="Confirmed Cases by Province"
)
st.plotly_chart(bar_chart)

# Data Table Expander
with st.expander("Show Data Table"):
    st.write(filtered_df)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background-color: #d3d3d3;
    }
    </style>
    """,
    unsafe_allow_html=True
)
