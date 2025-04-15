from dash import Dash, dcc, html, Input, Output

# Initialize the Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div([
    dcc.Tabs([
        # Tab 1
        dcc.Tab(label="Tab 1", children=[
            html.Div([
                # Dropdown for Tab 1
                dcc.Dropdown(
                    id="tab1-dropdown",
                    options=[
                        {"label": "Tab 1.A", "value": "plot1a.html"},
                        {"label": "Tab 1.B", "value": "plot1b.html"},
                    ],
                    value="plot1a.html",
                    placeholder="Select a plot",
                ),
                # Explanation before the plot
                html.Div(id="tab1-explanation-before", style={"margin-bottom": "20px"}),
                # Embedded plot
                html.Iframe(
                    id="tab1-plot",
                    style={"width": "100%", "height": "600px", "border": "none"}
                ),
                # Explanation after the plot
                html.Div(id="tab1-explanation-after", style={"margin-top": "20px"}),
            ])
        ]),
        # Tab 2
        dcc.Tab(label="Tab 2", children=[
            html.Div([
                # Dropdown for Tab 2
                dcc.Dropdown(
                    id="tab2-dropdown",
                    options=[
                        {"label": "Tab 2.A", "value": "plot2a.html"},
                        {"label": "Tab 2.B", "value": "plot2b.html"},
                    ],
                    value="plot2a.html",
                    placeholder="Select a plot",
                ),
                # Explanation before the plot
                html.Div(id="tab2-explanation-before", style={"margin-bottom": "20px"}),
                # Embedded plot
                html.Iframe(
                    id="tab2-plot",
                    style={"width": "100%", "height": "600px", "border": "none"}
                ),
                # Explanation after the plot
                html.Div(id="tab2-explanation-after", style={"margin-top": "20px"}),
            ])
        ]),
    ])
])

# Define callbacks for Tab 1
@app.callback(
    [Output("tab1-plot", "src"),
     Output("tab1-explanation-before", "children"),
     Output("tab1-explanation-after", "children")],
    Input("tab1-dropdown", "value")
)
def update_tab1_plot(selected_plot):
    explanations = {
        "plot1a.html": ("This is an explanation before Plot 1.A", "This is an explanation after Plot 1.A"),
        "plot1b.html": ("This is an explanation before Plot 1.B", "This is an explanation after Plot 1.B"),
    }
    before, after = explanations.get(selected_plot, ("", ""))
    return f"/assets/{selected_plot}", before, after

# Define callbacks for Tab 2
@app.callback(
    [Output("tab2-plot", "src"),
     Output("tab2-explanation-before", "children"),
     Output("tab2-explanation-after", "children")],
    Input("tab2-dropdown", "value")
)
def update_tab2_plot(selected_plot):
    explanations = {
        "plot2a.html": ("This is an explanation before Plot 2.A", "This is an explanation after Plot 2.A"),
        "plot2b.html": ("This is an explanation before Plot 2.B", "This is an explanation after Plot 2.B"),
    }
    before, after = explanations.get(selected_plot, ("", ""))
    return f"/assets/{selected_plot}", before, after

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)