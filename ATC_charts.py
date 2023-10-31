import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv("netflix_titles.csv")

#print(df.head())

# Pie
## Group and count
group_netflix=df.type.value_counts()

## Set coulors
colors = ['gold', 'mediumturquoise']

def pie_chart(df):

    fig = trace = go.Pie(labels=group_netflix.index,values=group_netflix.values,pull=[0.05]) # Actual Data
    layout = go.Layout(title="TV Shows VS Movies", height=400, legend=dict(x=1.1, y=1.3)) # layout for data
    fig = go.Figure(data=[trace],layout=layout)
    fig.update_traces(hoverinfo='label+percent',
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.update_layout(height=500,width=700)

    return fig



# Hist

def hist_chart(df):
    fig2 = px.histogram(df,x="release_year", title="Number of movies/shows released over the years", color="release_year")
    ## Update the layout
    fig2.update_layout(bargap=0.2)
    ## add borders around bars
    fig2.update_traces(marker_line_width=1, marker_line_color="black", showlegend=False)
    ## Add lines on x and y axes
    fig2.update_layout(xaxis=dict(showline=True, linewidth=2, linecolor='black'),
                   yaxis=dict(showline=True, linewidth=2, linecolor='black'))
    ## Remove the gray background (setting it to white)
    fig2.update_layout(plot_bgcolor='white')

    return fig2

# line chart
grouped2 = df.groupby(['release_year', 'type']).size().reset_index(name='count')
#print(grouped2)

def line_chart(grouped2):

    fig4 = px.line(grouped2,x="release_year", y="count", title="Number of movies/shows released over the years",
               color='type')
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

