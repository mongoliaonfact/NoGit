from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from pandas import read_pickle
from datetime import datetime 
from sklearn import preprocessing

df = read_pickle("../data/main_table.pickle")
df["difference"] = df["sentiment_pos"] - df["sentiment_neg"]
df["year"] = df.date.apply(lambda x: x.year)
#print(df.year.min())


app = Dash(__name__)

app.layout = html.Div([dcc.Graph(id="graph-with-slider"), 
                       dcc.Slider(df["year"].min(),
                                  df["year"].max(),
                                  step=None,
                                  value=df["year"].min(),
                                  marks={str(aday):str(aday) for aday in df["year"].unique()},
                                  id="year-slider"
                                  ) 
                       ])

@app.callback(
    Output("graph-with-slider", "figure"),
    Input("year-slider", "value"))
def update_figure(selected_year):
    filtered_date = df[df["year"] == selected_year]
    fig = px.scatter(filtered_date, x="sentiment_pos", y="sentiment_neg",
                  size="difference", hover_name="ticker", color="ticker",
                  log_x=True, title="Sentiment Scores")
    #fig.update_layout(transition_duration=500)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)