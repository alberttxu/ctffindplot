import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .csv import read_csv


def start_dash_app(logfile):

    app = dash.Dash(__name__)
    app.title = "ctffindplot"

    app.layout = html.Div(
        children=[
            html.H1(children="ctffindplot"),
            html.Div(children=logfile),
            dcc.RadioItems(
                id="set-refresh",
                value=10 * 1000,
                options=[
                    {"label": "Auto-refresh every 10 seconds", "value": 10 * 1000},
                    {"label": "Off", "value": 2 ** 30},
                ],
            ),
            html.Div(id="graphs", children=[],),
            dcc.Interval(
                id="interval-component",
                interval=10 * 1000,
                n_intervals=0,  # in milliseconds
            ),
        ]
    )

    @app.callback(
        dash.dependencies.Output("interval-component", "interval"),
        [dash.dependencies.Input("set-refresh", "value")],
    )
    def update_interval(value):
        return value

    @app.callback(
        Output("graphs", "children"), [Input("interval-component", "n_intervals")],
    )
    def update_graphs(_):
        ctfdata = read_csv(logfile)
        xaxis_view_width = 500
        n = len(ctfdata["index"])
        if n > xaxis_view_width:
            xaxis = dict(range=[n - xaxis_view_width, n])
        else:
            xaxis = dict(range=[0, n])

        updated_graphs = [
            dcc.Graph(
                style={"height": 300},
                id="defocus",
                figure=dict(
                    data=[
                        dict(name="defocus1", x=ctfdata["index"], y=ctfdata["defocus1"]),
                        dict(name="defocus2", x=ctfdata["index"], y=ctfdata["defocus2"],),
                    ],
                    layout=dict(
                        title="Defocus 1 and 2, um",
                        showlegend=True,
                        legend=dict(x=0, y=1.0),
                        margin=dict(l=40, r=10, t=60, b=30),
                        yaxis=dict(range=[0, 4]),
                        xaxis=xaxis,
                    ),
                ),
            ),
            dcc.Graph(
                style={"height": 300},
                id="astig",
                figure=dict(
                    data=[dict(x=ctfdata["index"], y=ctfdata["astig"],),],
                    layout=dict(
                        title="Amount of Astigmatism = abs(defocus1 - defocus2), nm",
                        margin=dict(l=40, r=10, t=60, b=30),
                        yaxis=dict(range=[0, 200]),
                        xaxis=xaxis,
                    ),
                ),
            ),
            dcc.Graph(
                style={"height": 300},
                id="azimuth_astig",
                figure=dict(
                    data=[dict(x=ctfdata["index"], y=ctfdata["azimuth_astig"],),],
                    layout=dict(
                        title="Azimuth of Astigmatism",
                        margin=dict(l=40, r=10, t=60, b=30),
                        xaxis=xaxis,
                    ),
                ),
            ),
            dcc.Graph(
                style={"height": 300},
                id="phase_shift",
                figure=dict(
                    data=[dict(x=ctfdata["index"], y=ctfdata["phase_shift"],),],
                    layout=dict(
                        title="Phase Shift, Degrees",
                        margin=dict(l=40, r=10, t=60, b=30),
                        yaxis=dict(range=[-20, 100]),
                        xaxis=xaxis,
                    ),
                ),
            ),
            dcc.Graph(
                style={"height": 300},
                id="xcorr",
                figure=dict(
                    data=[dict(x=ctfdata["index"], y=ctfdata["xcorr"],),],
                    layout=dict(
                        title="Cross Correlation",
                        margin=dict(l=40, r=10, t=60, b=30),
                        xaxis=xaxis,
                    ),
                ),
            ),
            dcc.Graph(
                style={"height": 300},
                id="res_fit",
                figure=dict(
                    data=[dict(x=ctfdata["index"], y=ctfdata["res_fit"],),],
                    layout=dict(
                        title="Resolution of Fit, A",
                        margin=dict(l=40, r=10, t=60, b=30),
                        yaxis=dict(range=[0, 10]),
                        xaxis=xaxis,
                    ),
                ),
            ),
        ]

        return updated_graphs

    app.run_server(debug=False)
