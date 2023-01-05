################################################################################################################################
# Dependencies & Importations
from tkinter.ttk import Style
from turtle import color, title
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import socket
from struct import unpack
################################################################################################################################

################################################################################################################################
# Clean Message
def messageclean(message):
    message2 = ""
    for i in range(len(message)):
        if message[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ","]:
            message2 += message[i]
    return[float(message2[0:4]), float(message2[5:])]

## Anchors Positions
# Anchor 1 - Initiatior DW532F
x1,y1 = 0,0
# Anchor 2 - DWC1A5
x2,y2 = 2.41,0
# Anchor 3 - DW868D
x3,y3 = 0.44,3.94
################################################################################################################################

################################################################################################################################
# Graph Initialisation
df = pd.DataFrame({'x': [], 'y': []})
fig = px.scatter()
################################################################################################################################

################################################################################################################################
# Starting Dash
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Real-Time Localisation Dashboard",style = {'color':'DarkBlue','text-decoration-line': 'underline'}),
    dcc.Graph(
        id='graph',
        figure=fig,
        style = {'height':'720px','width':'720px','text-align':'center','margin':'auto','display':'flex'}
    ),
    dcc.Interval(
        id='interval-component',
        interval=3*1000,  # in milliseconds
        n_intervals=0
    )
])

# Updating the figure each 3 seconds / may be changed depending on the speed of the data collection
@app.callback(
    Output('graph', 'figure'),
    Input('interval-component', 'n_intervals'))
def update_figure(n):
    ########################################################
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    host, port = '0.0.0.0', 65000
    server_address = (host, port)
    sock.bind(server_address)
    ########################################################

    ########################################################
    # Getting Real Time Data
    while True:
        try:
            # Wait for message
            message, address = sock.recvfrom(4096)
            # Print message
            message = message.decode('utf8').replace("'", '"')
            a = messageclean(message)[1]
            b = messageclean(message)[0]
            sock.close()
        except:
            break
    ########################################################

    ########################################################
    # Updating the figure
    df = pd.DataFrame({'x': [x1,x2,x3,a], 'y': [y1,y2,y3,b], 'Type':['anchor','anchor','anchor','tag']})
    fig = px.scatter(
        df, x="x", y="y",color='Type',range_x=[-1, 4], range_y=[-1, 4], title='Real-Time Localisation')
    return fig
################################################################################################################################

### Starting the App
################################################################################################################################
if __name__ == '__main__':
    app.run_server(debug=True)
################################################################################################################################