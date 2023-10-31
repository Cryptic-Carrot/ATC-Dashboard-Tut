import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from ATC_charts import df, pie_chart, hist_chart, grouped2, line_chart
from ATC_navbar import navbar

app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])

app.layout = dbc.Container([
    html.Div(id="parent", children=[navbar]),
    dbc.Row(
        [dbc.Col(
            [html.H1(id="H1", children="ATC Club Netflix Dashboard")],
            xl=12, lg=12, md=12, sm=12, xs=12)], style={"textAlign": "center", "marginTop": 30, "marginBottom": 30}),
    html.Br(), #adding break
    html.Br(), #adding break
    dbc.Row([
        dbc.Col([dcc.Graph(id="", figure=pie_chart(df))]),
        dbc.Col([dcc.Graph(id="", figure=hist_chart(df))])
        ]),
    html.Br(), #adding break
    html.Br(), #adding break
    dbc.Row([
        dbc.Col([dcc.Graph(id="", figure=line_chart(grouped2))]),
    ]),
    ], fluid=True)  # fills up empty space with the graphs

if __name__ == "__main__":
    app.run_server()

