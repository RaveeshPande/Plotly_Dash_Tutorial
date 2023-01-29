from dash import Dash,html,dcc

app= Dash(__name__)
app.layout=html.Div([
    html.H1("Hello Dash!!!"),
    html.Div("Dash - A product")
])

if __name__ == '__main__' :
    app.run_server(port=4050,debug=True)

# help(html.Div) --can be used to find the components of the page. Can be used in jupyter notebook simimlarly for dcc too.    