import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from ATC_navbar import navbar
from ATC_charts import df, pie_chart, hist_chart, grouped2, line_chart

df = pd.read_csv("netflix_titles.csv")
grouped2 = df.groupby(['release_year', 'type']).size().reset_index(name='count')

app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL]) #dbc allows you to customise style

dropdown = dcc.Dropdown(
           id="my_dropdown",
           options=[
               {'label': "Movies", "value": "Movie"},
               {'label': "TV Shows", "value": "TV Show"},
                    ],
           value= "Movies",
           multi=False,
           style={"width": "50%"}
         )

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
    html.Div([
    html.Div([
        html.Label(["Netflix Movies and Shows"]),
        dropdown
    ]),

    html.Div([
        dcc.Graph(id="the_graph")
    ]),
    ])
], fluid=True)

@app.callback(
    Output("the_graph", "figure"),
    [Input("my_dropdown", "value")]
)


def line_chart(my_dropdown):

    dff = grouped2[(grouped2["type"] == my_dropdown)]

    fig4 = px.line(dff, x="release_year", y="count", title="Number of movies/shows released over the years",color='type' )
    ## Update the layout
    fig4.update_layout(bargap=0.2)
    ## add borders around bars
    fig4.update_traces(marker_line_width=1, marker_line_color="black", showlegend=False)
    ## Add lines on x and y axes
    fig4.update_layout(xaxis=dict(showline=True, linewidth=2, linecolor='black'),
                   yaxis=dict(showline=True, linewidth=2, linecolor='black'))
    ## Remove the gray background (setting it to white)
    fig4.update_layout(plot_bgcolor='white')
    return fig4

if __name__ == "__main__":
    app.run_server()


