import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screentime-App-Details.csv")
print(data.head())

# Analyzing the screen time of user
figure = px.bar(data_frame=data, x="Date", y="Usage", color="App", title="Usage")
figure.show()