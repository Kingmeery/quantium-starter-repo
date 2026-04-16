import pandas as pd
from pathlib import Path
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
base_path = Path(__file__).parent
df = pd.read_csv(base_path / "output.csv")
df["date"] = pd.to_datetime(df["date"])

# Create app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    style={
        "backgroundColor": "#f5f5f5",
        "padding": "20px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#333"}
        ),

        html.Div(
            [
                html.Label("Select Region:", style={"fontWeight": "bold"}),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "South", "value": "south"},
                        {"label": "East", "value": "east"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginBottom": "20px"}
                ),
            ],
            style={"textAlign": "center"}
        ),

        dcc.Graph(id="sales-graph")
    ]
)

# Callback to update graph
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    filtered_df = filtered_df.sort_values("date")

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Sales Over Time ({selected_region.upper()})"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)