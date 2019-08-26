import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from data import *

# The end for data cleaning

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H4("ACT Student Score", style={"color": "Black", "textAlign": 'center'}),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='student',
                options=[{'label': i, 'value': i} for i in names],
                value=f'{names[0]}'
            )
        ],
            style={'width': '45%', 'display': 'inline-block'}
        ),
    ]),

    dcc.Graph(id='sd_grade'),

    html.Hr(),

    html.H4("ACT Subject Score", style={"color": "Black", "textAlign": 'center'}),

    html.Div([
        html.Div([
            dcc.RadioItems(
                id='subject',
                options=[{'label': i, 'value': i} for i in columns],
                value='Math',
                labelStyle={'display': 'inline-block'}
            )
        ],
            style={'width': '60%', 'display': 'inline-block'}
        )
    ]),

    dcc.Graph(id="subject_grade"),

    html.Hr(),

    html.H6("Enter Diagnostic Test Result", style={"coler": "Black", "textAlign": "center"}),

    html.Table([
        html.Tr([
            html.Td(['Enter English below']),
            html.Td(["Enter Math below"]),
            html.Td(['Enter reading below'])
        ])
    ]),


    html.Div([
        dcc.Input(id='eng-in', value='32', type='text'),
        dcc.Input(id='math-in', value='33', type='text'),
        dcc.Input(id='reading-in', value='34', type='text')

    ]),

    html.Div(html.Div(id='out'))



])

# style={'columnCount': 2})


@app.callback(
    Output('sd_grade', 'figure'),
    [Input('student', 'value')]
            )
def update_graph(student_name):

    return {
        'data': [
            go.Bar(
                x=df.index,
                y=df[f"{student_name}"]
            )

        ]
    }


@app.callback(
     Output('subject_grade', 'figure'),
    [Input("subject", "value")]
            )
def update_graph2(subject_name):

    return{
        'data': [
            go.Line(
                y=df_sd[f"{subject_name}"],
                x=df_sd["Name"]
            )
        ]
    }


@app.callback(
    Output(component_id='out', component_property='children'),
    [Input('eng-in','value'), Input('math-in', 'value'),
     Input('reading-in','value')]
)
def update_output_div(eng, math, reading):
    test_score = [[eng, math, reading]]
    pred_science = rfModel.predict(test_score)

    return 'Future Science Score :  "{0}" '.format(pred_science.round(0))


if __name__ == '__main__':
    app.run_server(debug=True)

