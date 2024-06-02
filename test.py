import plotly.graph_objects as go
import numpy as np

LATS = [39.6094856, 39.6094856, 39.6086845, 39.6077614, 39.608017, 39.608757]
LONS = [-3.430547, -3.430547, -3.43145895, -3.4323709, -3.43223, -3.43099689]
ALTS = [697.200012, 697.200012, 790.400024, 852.599976, 835.299988, 725.299988]

# Define colors for each segment
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']

# Generate a list of indices for coloring segments
color_indices = []
for i in range(len(LATS) - 1):
    color_indices.extend([i, i])
color_indices.append(len(LATS) - 2)  # Ensure the last point gets a color

# Create a custom color scale based on the provided colors
custom_colorscale = []
for i, color in enumerate(colors):
    custom_colorscale.append([i / (len(colors) - 1), color])
    custom_colorscale.append([(i + 1) / (len(colors) - 1), color])

# Create the figure with one trace
fig = go.Figure(go.Scattermapbox(
    mode="lines+markers",
    lon=LONS,
    lat=LATS,
    marker=dict(size=10, color="#AAAAAA"),
    line=dict(width=2),  # Transparent line color initially
    customdata=color_indices,  # Use customdata for color indexing
    hoverinfo='none'
))

# Add a colorbar and custom color scale to simulate segment coloring
# fig.update_traces(line=dict(color='customdata'))

# Update the layout
fig.update_layout(
    margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
    mapbox={
        'center': {'lon': (max(LONS) + min(LONS)) / 2.0, 'lat': (max(LATS) + min(LATS)) / 2.0},
        'style': "open-street-map",
        'zoom': 15
    },
    coloraxis_colorbar=dict(
        title="Segments",
        tickvals=list(range(len(colors))),
        ticktext=['Segment {}'.format(i + 1) for i in range(len(colors))],
    )
)

# Show the figure
fig.show()
