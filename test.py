import plotly.graph_objects as go
import numpy as np

# LATS = [39.6094856, 39.6094856, 39.6086845, 39.6077614, 39.608017, 39.608757]
# LONS = [-3.430547, -3.430547, -3.43145895, -3.4323709, -3.43223, -3.43099689]
# ALTS = [697.200012, 697.200012, 790.400024, 852.599976, 835.299988, 725.299988]

LATS = [40.405124333, 40.405124333, 40.405124333, 40.4051245, 40.4051245, 40.4051245, 40.4051245, 40.405124333, 40.405124333, 40.4051245, 40.4051245, 40.405124333, 40.405124333, 40.405124333, 40.405124333, 40.405124333, 40.405124333, 40.405124333, 40.405124333, 40.405124333, 40.405124167, 40.405124167, 40.405124167, 40.405124167, 40.405124167, 40.405124, 40.405123833, 40.405123833, 40.405125667, 40.405127333, 40.4051275, 40.405127667, 40.4051275, 40.405126833, 40.405126167, 40.405126167, 40.405126333, 40.405129333, 40.405132833, 40.405132833, 40.4051325, 40.405133333, 40.405134167, 40.405136167, 40.405135333, 40.405134833, 40.405134667, 40.4051355, 40.4051335, 40.405132667, 40.405131833, 40.405132, 40.4051295, 40.405128333, 40.405123833, 40.405123167]
LONS = [-3.7002555, -3.7002555, -3.7002555, -3.7002555, -3.7002555, -3.7002555, -3.700255667, -3.700255833, -3.700255667, -3.700255833, -3.700256, -3.700256167, -3.700256333, -3.700256667, -3.700256833, -3.700257, -3.700257167, -3.700257333, -3.700257667, -3.700257833, -3.700258, -3.700258167, -3.700258333, -3.7002585, -3.700258667, -3.700258833, -3.700259167, -3.700259333, -3.700259333, -3.700259833, -3.700259333, -3.7002595, -3.700259667, -3.700259667, -3.700260167, -3.7002605, -3.700260167, -3.700258667, -3.700256167, -3.700257333, -3.700257833, -3.7002565, -3.700256167, -3.700253667, -3.700254667, -3.700252, -3.700249833, -3.7002505, -3.7002495, -3.700250167, -3.700246833, -3.700246333, -3.700246333, -3.700244333, -3.700244333, -3.700245]
ALTS = [650]*len(LATS)


LATS = [ (i - 40.405124333)*100 for i in LATS]
LONS = [ (i + 3.7002555)*100 for i in LONS]


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
# fig.show()

a = fig.to_html()
open("index2.html", "wb").write(bytes(a, "utf-8"))
