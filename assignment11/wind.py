# Task 3

import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type ='pandas')

print(df.head(10))
print(df.tail(10))


df['strength'] = df['strength'].str.replace((r'-.*|\+'), '', regex=True).astype(float)

fig = px.scatter(df, x='frequency', y='strength', color='direction',  hover_data=['direction', 'frequency'], title='Strength vs Frequency') 
fig.write_html('wind.html', auto_open = True, include_plotlyjs = 'cdn')