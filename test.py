


import plotly.graph_objects as go



LATS = [39.6094856, 39.6094856, 39.6086845, 39.6077614, 39.608017, 39.608757]
LONS = [-3.430547, -3.430547, -3.43145895, -3.4323709, -3.43223, -3.43099689]
ALTS = [697.200012, 697.200012, 790.400024, 852.599976, 835.299988, 725.299988]


fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon = LONS,
    lat = LATS,
    line = {'width': 2, "color": "#AAAAAA"},
    marker = {'size': 10, "color": ["#ff0000"]*6}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': (max(LONS) + min(LONS))/2.0, 'lat': (max(LATS) + min(LATS))/2.0},
        'style': "open-street-map",
        'zoom': 15})

fig.show()

