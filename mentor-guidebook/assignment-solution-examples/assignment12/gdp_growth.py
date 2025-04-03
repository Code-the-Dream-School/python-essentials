from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder(return_type='pandas')

# Initialize Dash app
app = Dash(__name__)

countries = df['country'].drop_duplicates()
# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    country_df = df[df['country']==country]
    fig = px.line(country_df, x="year", y="gdpPercap", title=f"{country} Per Capita GDP")
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)