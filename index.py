python
import pandas as pd
import plotly.express as px
from flask import Flask, render_template

app = Flask(__name__)

# Load dataset
def load_data():
    gender_data = pd.read_excel('Distribution_of_Pensioners_per_Gender.xlsx')
    total_data = pd.read_excel('Distribution_of_Pensioners.xlsx')
    return gender_data, total_data

# Prepare data for visualization
def prepare_visualizations(gender_data, total_data):
    # Example Visualization 1: Gender Distribution per Quarter
    gender_fig = px.bar(
        gender_data,
        x='Quarter',
        y='Count',
        color='Gender',
        title='Gender Distribution of Pensioners per Quarter'
    )

    # Example Visualization 2: Total Pensioners Per Quarter
    total_fig = px.line(
        total_data,
        x='Quarter',
        y='Total',
        title='Total Pensioners Per Quarter'
    )

    return gender_fig, total_fig

@app.route('/')
def index():
    gender_data, total_data = load_data()
    gender_fig, total_fig = prepare_visualizations(gender_data, total_data)

    gender_plot = gender_fig.to_html(full_html=False)
    total_plot = total_fig.to_html(full_html=False)

    return render_template('dashboard.html', gender_plot=gender_plot, total_plot=total_plot)

if __name__ == '__main__':
    app.run(debug=True)
