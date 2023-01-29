from dash import Dash,dcc,html
app=Dash(__name__)
app.layout= html.Div([
    html.H1("Hello Dash!!!"),
    html.Div("Dash is working fine."),

   dcc.Graph(
        id='Simple graph',
        figure={
            'data' : [
                {
                    'x':[4,5,6],
                    'y':[12,13,14],
                    'type':'bar',
                    'name':'First chart'
                },
                {

                    'x':[1,2,3,4],
                    'y':[23,34,54,66],
                    'type':'bar',
                    'name':'Second Chart'
                }
            ],
            'layout':{
                'title': 'Simple Bar Chart'
            }
        }
    )
])

if __name__ == '__main__' :
    app.run_server(port=4050,debug=True)