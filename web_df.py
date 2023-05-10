# Import packages
from dash import Dash, html, dash_table
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = ""
path = ""

service = Service(executable_path=path)
driver = webdriver.Chrome(service=Service)
driver.get(website)


# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
