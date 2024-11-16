from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from dash import html

df = pd.read_csv("./datasets/cleaned_data_related_jobs.csv")

df = df.rename(columns={'python_yn': 'Py', 'spark_yn': 'Sp', 'azure_yn': 'Az', "aws_yn": "AWS", 'excel_yn': 'Xlsx',
                          'machine_learning_yn': 'ML'})
df = df.copy()
df['seniority'] = df['seniority'].replace({'junior': 'Junior', 'mid': 'Mid'})

salary_summary = {
    "min": df['salary estimate'].min(),
    "25%": df['salary estimate'].quantile(0.25),
    "50%": df['salary estimate'].median(),
    "75%": df['salary estimate'].quantile(0.75),
    "max": df['salary estimate'].max()
}


app = Dash(__name__)

app.layout = html.Div(children=[

    # Main container
    html.Div(className="container", children=[

        # Left container
        html.Div(children=[
            html.Div(className="profile-container", children=[
                html.Div(className="top-row", children=[

                    html.Div(className="profile-pic", children=[
                        html.Img(src="assets/images/profile-pic.png", alt="Profile Picture")
                    ]),

                    html.Div(className="info", children=[
                        html.Div("Wendell Abino", className="name"),
                        html.Label("BS Mathematics Student")
                    ])
                ]),
                html.Div(className="links", children=[
                    html.A(
                    href="https://www.facebook.com/wendell.abino/",
                    target="_blank",
                    children=[
                        html.Div(
                            html.Img(src="/assets/images/fb-logo.png", alt="Facebook"),
                            className="link-box"
                        )
                    ]
                    ),
                    html.A(
                        href="https://www.linkedin.com/in/renz-wendell-abi%C3%B1o-4327322b9/",
                        target="_blank",
                        children=[
                            html.Div(
                                html.Img(src="/assets/images/linkedin-logo.png", alt="LinkedIn"),
                                className="link-box"
                            )
                        ]
                    ),
                    html.A(
                        href="https://drive.google.com/file/d/1lHJrUvcQY3oYiBEf29WUAVkYGuVThZSE/view?usp=sharing",
                        target="_blank",
                        children=[
                            html.Div(
                                html.Img(src="/assets/images/resume.jpg", alt="Resume"),
                                className="link-box"
                            )
                        ]
                    )
                ])

            ]),

            html.Div(className="info-container",
                children=[
                    html.H2("Detailed Information"),
                    html.Div(className="info-item",

                        children=[
                            html.Label("Email Address"),
                            html.Span("renz_abino@dlsu.edu.ph")
                        ]
                    ),

                    html.Div(className="info-item",

                        children=[
                            html.Label("School"),
                            html.Span("De La Salle University")
                        ]
                    ),

                    html.Div(className="info-item",

                         children=[
                             html.Label("Degree Program"),
                             html.Span("Bachelor of Science in Mathematics with Specialization in Computer Applications")
                         ]
                    ),

                    html.Div(className="info-item",

                         children=[
                             html.Label("Knowledge"),
                             html.Ul(
                                 children=[
                                     html.Li("Data Preparation and Integration"),
                                     html.Li("Basic AI Understanding"),
                                     html.Li("Java, Python OOP")
                                 ]
                             )
                         ]
                    ),

                    html.Div(className="info-item",

                         children=[
                             html.Label("Career Goals"),
                             html.Ul(
                                 children=[
                                     html.Li("Explore Data Related Jobs Overseas."),
                                     html.Li("Achieve mastery in the skills acquirable through experience."),
                                     html.Li("Return to the Philippines equipped with advanced expertise and a distinguished position.")
                                 ]
                             )
                         ]
                    ),

                    html.Div(className="info-item",

                         children=[
                             html.Label("Projects"),
                             html.Ul(
                                 children=[
                                    html.Li(html.A("Banach-Mazur Algorithm Paper", href="https://drive.google.com/file/d/15hp-U7yFF3-_tNon19r_B57_KXzB-NaC/view?usp=sharing", target="_blank")),
                                    html.Li(html.A("Linear Modelling", href="https://www.youtube.com/watch?v=yhJ7f54lfb4", target="_blank")),
                                    html.Li(html.A("Tesselation", href="https://www.youtube.com/watch?v=5N_bCNgg0Kc", target="_blank"))
                                 ]
                             )
                         ]
                    ),





            ])
        ]),

        # Right container
        html.Div(children=[

            html.Div(className="dataset-container", children=[
                html.Div("Data Related Jobs Dataset", className="header"),

                html.Div(className="dataset-content", children=[
                    html.Div(children=[
                        html.H3("Information"),
                        html.P("This dataset comprises around 1700 job postings from Glassdoor, focusing on roles in data-related fields only. It includes salary, company information, whether it pays hourly, company ratings, skills required for Python, Spark, AWS, Azure, Excel, and machine learning, or job category and seniority.")
                    ],

                    className="left-box"),

                    html.Div(children=[
                        html.H3("Importance"),
                        html.P("It contains data jobs: data science, data analysis, data engineering, machine learning that I am interested in exploring. Using other columns such as company, location, salary estimate, or rating of the company could provide a valuable insight that could help decide where to apply.")
                    ],
                    className="right-box")

                ])
            ]),

            html.Div(className="map-graph-container", children=[

                html.Div(className="map-container", children=[

                    # Mapbox container
                    html.Div(className="mapbox", children=[
                        dcc.Graph(
                            id = 'scatter_mapbox',
                            figure={},
                            style={
                                'height': '100%',
                                'width': '100%',
                                'border-radius' : '10px',
                                'overflow' : 'hidden'}
                        )
                    ]),

                    # Mapbox Controller Container
                    html.Div(className="mapbox-controller", children=[
                        # row 1: Jobs dropdown menu

                        html.Div(className="filter-row", children=[
                            dcc.Dropdown(
                                id='jobs-dropdown',
                                options=[
                                    {'label' : 'Data Scientist', 'value' : 'data scientist'},
                                    {'label' : 'Data Analyst', 'value' : 'data analyst'},
                                    {'label' : 'Data Engineer', 'value' : 'data engineer'},
                                    {'label' : 'ML Engineer', 'value' : 'machine learning engineer'}
                                ],
                                placeholder="Select Jobs",
                                className="fixed-dropdown"
                            )
                        ]),


                        # row 3: Salary range
                        html.Div(className="filter-row", children=[
                            html.Label("Salary Slider", id="salary-range-label"),
                            dcc.RangeSlider(
                                id='salary-range',
                                min=5000,
                                max=270000,
                                step=5000,
                                value=[5000, 270000],
                                marks={
                                    5000: "$5k",

                                    107800: "$107k",

                                    270000: "$270k"
                                },
                                tooltip={"placement": "bottom", "always_visible": False},

                            )
                        ]),


                        # Row 4: Company Rating range
                        html.Div(className="filter-row", children=[
                            html.Label("Company Rating", id="rating-range-label"),

                            dcc.RangeSlider(
                                id='company-rating-range',
                                min=df['rating'].min(),
                                max=df['rating'].max(),
                                step=0.1,
                                value=[0, 5],
                                marks={i: str(i) for i in range(1, 6)},
                                pushable=True
                            )
                        ])

                    ])
                ]),

                html.Div(className="graphs-container", children=[
                    html.Div(className="graph1", children=[
                        dcc.Graph(
                            id = 'bar_graph',
                            figure={},
                            style={
                                'height': '100%',
                                'width': '100%',
                                'border-radius' : '10px',
                                'overflow' : 'hidden'}
                        )
                    ]),
                    html.Div(className="graph2", children=[
                        dcc.Graph(
                            id = 'box_plot',
                            figure={},
                            style={
                                'height': '100%',
                                'width': '100%',
                                'border-radius' : '10px',
                                'overflow' : 'hidden'}
                        )
                    ])
                ])
            ])

        ])
    ]
    )
])

@app.callback(
    [Output(component_id='scatter_mapbox', component_property='figure'),
     Output(component_id='bar_graph', component_property='figure'),
     Output(component_id='box_plot', component_property='figure'), ],
    Input(component_id='jobs-dropdown', component_property='value'),
    Input(component_id='salary-range', component_property='value'),
    Input(component_id='company-rating-range', component_property='value')
)
def updateGraphs(job, salary_range, rating_range):
    df_update = df
    df_filt1 = df_update[df_update['job_simpl'] == job]
    df_filt2 = df_filt1[(df_filt1['salary estimate'] >= salary_range[0]) & (df_filt1['salary estimate'] <= salary_range[1])]
    df_filtered = df_filt2[(df_filt2['rating'] >= rating_range[0]) & (df_filt2['rating'] <= salary_range[1])]

    # Mapbox
    fig1 = px.scatter_mapbox(
                  df_filtered,
                  lat='Latitude', lon='Longitude',
                  mapbox_style = 'carto-positron',
                  zoom = 1,)

    fig1.update_layout(
        mapbox=dict(center=dict(lat=df["Latitude"].mean(), lon=df["Longitude"].mean())),
                      margin={"r": 0, "t": 0, "l": 0, "b": 0}
                      )

    fig1.update_traces(marker_color='#056676')
    # Bar plot
    skills_df = df_filtered[['Py', 'Sp', 'Az', 'AWS', 'Xlsx', 'ML']]



    skills_count = skills_df.sum().reset_index()
    skills_count.columns = ['Skill', 'Count']

    fig2 = px.bar(skills_count,

                 x=skills_count['Skill'],
                 y=skills_count['Count'],)

    fig2.update_xaxes(title_text='')
    fig2.update_yaxes(title_text='')
    fig2.update_layout(margin=dict(l=0, r=25, t=25, b=0))
    fig2.update_traces(marker_color='#056676')

    # Box plot



    fig3 = px.box(df_filtered,
                  x="seniority", y="salary estimate"
                  )


    fig3.update_xaxes(title_text='')
    fig3.update_yaxes(title_text='')
    fig3.update_layout(margin=dict(l=0, r=25, t=25, b=0))
    fig3.update_traces(marker_color='#056676')

    return fig1, fig2, fig3

if __name__ == '__main__':
    app.run_server(debug=True)