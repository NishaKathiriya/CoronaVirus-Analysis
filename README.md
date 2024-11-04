# Coronavirus Analysis Dashboard

**A data analysis dashboard for visualizing the impact of COVID-19 worldwide using Streamlit and MySQL.** This project presents real-time insights into confirmed cases, deaths, and recoveries, allowing users to filter data by country and date to explore COVID-19 metrics dynamically.


## Project Overview
The **Coronavirus Analysis Dashboard** is a web-based application built using Python, Streamlit, MySQL, and visualization libraries like Matplotlib and Plotly. It fetches COVID-19 data from a MySQL database, allowing users to explore the data interactively through visualizations and filtering options.

This project was developed to enhance analytical skills and create a user-friendly interface for visualizing and understanding pandemic trends over time.

## Features
- **Data Filtering**: Filter COVID-19 data by country/region and date range.
- **Key Metrics Display**: Showcases total confirmed cases, deaths, and recoveries.
- **Visualizations**:
  - **Pie Chart**: Visualizes death distribution across countries.
  - **Bar Graph**: Displays confirmed cases by province.
- **Data Table**: Shows the filtered dataset in a tabular format.
- **Customizable Layout**: Includes custom CSS styling for improved appearance.

## Technologies Used
- **Python**
- **Streamlit**: For building the interactive dashboard.
- **MySQL**: For storing and retrieving COVID-19 data.
- **SQLAlchemy**: For connecting to MySQL through SQL queries.
- **Matplotlib & Plotly**: For data visualization.

## Setup Instructions

### Prerequisites
1. **Python 3.7+**: Make sure Python is installed.
2. **MySQL Database**: Install MySQL and set up a database called `coronavirusanalysis`.

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/NishaKathiriya/coronavirus-analysis
   cd coronavirus-analysis
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows use: myvenv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL Database**:
   - Create a database named `coronavirusanalysis`.
   - Import COVID-19 data into a table named `corona_data` within this database.
   - Make sure MySQL service is running and accessible.

5. **Environment Variables (Optional)**:
   If you prefer, set up a `.env` file to store sensitive MySQL credentials:
   ```plaintext
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=yourpassword
   MYSQL_DB=coronavirusanalysis
   MYSQL_PORT=3306
   ```

### Configuration
In `dashboard.py`, modify the database connection function with your MySQL credentials if not using `.env`:

```python
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="coronavirusanalysis",
    port=3306
)
```

## Usage
1. **Run the application**:
   ```bash
   streamlit run dashboard.py
   ```

### Interacting with the Dashboard
- **Filter Data**: Use the sidebar to filter by `Country/Region` and date range.
- **Metrics and Visualizations**: View dynamic charts and metrics.
- **Data Table**: Expand the "Show Data Table" option to explore the raw data.


![image](https://github.com/user-attachments/assets/902d0ac6-336e-4e4d-a920-96cf7df52fdb)


![image](https://github.com/user-attachments/assets/f3eba256-5d80-4626-a9fb-96a08d5c497f)


![image](https://github.com/user-attachments/assets/a33f9222-51e0-4dc6-9504-76873d13c243)


![image](https://github.com/user-attachments/assets/dae78a83-88bb-4518-8bae-a7d09e51054e)


![image](https://github.com/user-attachments/assets/ec2163c7-2d93-4045-8015-8ea793af9ea6)





