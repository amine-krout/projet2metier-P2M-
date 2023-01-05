from re import X
import socket
import string
import sys
from struct import unpack
import json
from time import time
from tkinter import Y
import matplotlib.pyplot as plt

from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px


def messageclean(message):
    message2 = ""
    for i in range(len(message)):
        if message[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ","]:
            message2 += message[i]
    return[float(message2[0:4]), float(message2[5:])]


x = []
y = []
i = 0

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig, ax = plt.subplots()

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '0.0.0.0', 65000
server_address = (host, port)

print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)

while True:
    # Wait for message
    message, address = sock.recvfrom(4096)
    socket.setdefaulttimeout(5)
    # Print message
    message = message.decode('utf8').replace("'", '"')
    print(message)
    x.append(messageclean(message)[1])
    y.append(messageclean(message)[0])
    print(x[i], y[i])
    i += 1
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    plt.show()
