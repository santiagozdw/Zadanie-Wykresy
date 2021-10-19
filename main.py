import plotly.graph_objects as go

height = [1000, 1500, 2700, 5000,]
bars = ('Greg', 'Daniel', 'John', 'Mark')

data = go.Bar(x=bars, y=height)
layout = {
	'title': 'Salaries with plotly'
}
fig = go.Figure(data, layout)
fig.show()