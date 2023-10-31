import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime as dt
from wordcloud import WordCloud
from plotly.subplots import make_subplots


df = pd.read_csv("/Users/buhlentozini/Desktop/ATC_club/Buhle_Nosihle_plotly/netflix_titles.csv")

#df.head()



# Pie
## Group and count
group_netflix=df.type.value_counts()
print(group_netflix)


## Set coulors
colors = ['gold', 'mediumturquoise']

trace=go.Pie(labels=group_netflix.index,values=group_netflix.values,pull=[0.05]) # Actual Data

layout = go.Layout(title="TV Shows VS Movies", height=400, legend=dict(x=1.1, y=1.3)) # layout for data

fig = go.Figure(data=[trace],layout=layout)
fig.update_traces(hoverinfo='label+percent', 
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.update_layout(height=500,width=700)

fig.show()





# Hist
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

fig2.show()



# Heatmap

## Extract the required columns for release dates
df['date_added'] = pd.to_datetime(df['date_added'])

# Filtering out rows with missing or incorrect dates
df = df.dropna(subset=['date_added'])
df_cleaned = df.dropna()

## Extract year and month from the 'date_added' column
df['release_year'] = df['date_added'].dt.year
df['release_month'] = df['date_added'].dt.strftime('%B')

## Group data by year and month to get counts
grouped = df.groupby(['release_year', 'release_month']).size().reset_index(name='count')
print(grouped)

## Order the months by their chronological order
months_order = ['December', 'November', 'October', 'September', 'August', 'July', 'June', 'May', 'April', 'March', 'February', 'January']
grouped['release_month'] = pd.Categorical(grouped['release_month'], categories=months_order, ordered=True)

# Check for missing combinations and fill zero counts for all month and year combinations
all_combinations = pd.MultiIndex.from_product([grouped['release_year'].unique(), months_order], names=['release_year', 'release_month'])
all_data = pd.DataFrame(index=all_combinations).reset_index()
merged = all_data.merge(grouped, on=['release_year', 'release_month'], how='left')
merged['count'].fillna(0, inplace=True)

# Create the heatmap using the merged data
fig3 = px.imshow(merged.pivot(index='release_month', columns='release_year', values='count'),
                x=merged['release_year'].unique(),
                y=months_order,
                labels=dict(x="Release Year", y="Release Month", color="Count of Releases"))

fig3.update_layout(
    title="Netflix Releases by Month and Year",
    plot_bgcolor='white',
    xaxis=dict(showline=True, linewidth=2, linecolor='black'),
    yaxis=dict(showline=True, linewidth=2, linecolor='black')
)

fig3.show()



# line graph
grouped2 = df.groupby(['release_year', 'type']).size().reset_index(name='count')
print(grouped2)

fig4 = px.line(grouped2,x="release_year", y="count", title="Number of movies/shows released over the years", color='type')

## Update the layout 
fig4.update_layout(bargap=0.2)

## add borders around bars
#fig4.update_traces(marker_line_width=1, marker_line_color="black", showlegend=False)

## Add lines on x and y axes
fig4.update_layout(xaxis=dict(showline=True, linewidth=2, linecolor='black'),
                   yaxis=dict(showline=True, linewidth=2, linecolor='black'))

## Remove the gray background (setting it to white)
fig4.update_layout(plot_bgcolor='white')

fig4.show()





