import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import pathlib
import plotly.express as px

PATH = pathlib.Path(__file__).parent

DATA_PATH = PATH.joinpath("../data").resolve()

dalian = pd.read_csv(DATA_PATH.joinpath("lianjia_processed.csv"))

colors = dict(background='#787878', text='#7FDBFF')

mapbox_access_token = "pk.eyJ1Ijoia2VrZWluZyIsImEiOiJjazRjZ3Njc3owbmh1M2xvMmZrbHczNmd1In0.A51yo2likAVjYj4qRepeog"

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server


def map():
    fig = px.scatter_mapbox(dalian, lat="lat", lon="lon", hover_name="xiaoqu",
                            hover_data=["address", "deal_totalPrice", "deal_unitPrice"],
                            color_discrete_sequence=["fuchsia"], height=900, )

    fig.update_layout(autosize=True,
                      hovermode='closest',
                      mapbox_style="open-street-map",
                      # mapbox_style="dark",
                      mapbox=dict(
                          accesstoken=mapbox_access_token,
                          bearing=0,
                          center=dict(
                              lat=38.9146,
                              lon=121.619
                          ),
                          pitch=0,
                          zoom=9
                      ), )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 10})
    return fig


def heatmap():
    fig = px.density_mapbox(dalian, lat='lat', lon='lon', z='deal_totalPrice', hover_data=["xiaoqu","address", "deal_totalPrice","deal_unitPrice"],
                            radius=10)
    fig.update_layout(autosize=True,
                      hovermode='closest',
                      mapbox_style="stamen-watercolor",
                      mapbox=dict(
                          accesstoken=mapbox_access_token,
                          bearing=0,
                          center=dict(
                              lat=38.9146,
                              lon=121.619
                          ),
                          pitch=0,
                          zoom=9,
                      ),
                      )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


def allscatter():
    fig = px.scatter(dalian, x="gross_area", y="deal_totalPrice", color="region",
                     hover_data=["address", "deal_totalPrice", "deal_unitPrice"])

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


def unitscatter():
    fig = px.scatter(dalian, x="gross_area", y="deal_unitPrice", color="region",
                     hover_data=["address", "deal_totalPrice", "deal_unitPrice"])

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


def scatter():
    fig = px.scatter(dalian, x="gross_area", y="deal_totalPrice", color="deal_totalPrice", facet_col="region",
                     color_continuous_scale=px.colors.sequential.Viridis, render_mode="webgl")
    return fig


def housenum():
    district_number = dalian.region.value_counts().reset_index().sort_values(by='region', ascending=False)
    housenum = px.line(district_number, x='index', y='region')
    return housenum


def housetype():
    houseuse = dalian.house_usage.value_counts().reset_index().sort_values(by='house_usage', ascending=False)
    houseusefig = px.bar(houseuse, y='index', x='house_usage', orientation='h')
    return houseusefig


def pie():
    fig = px.pie(dalian, names='household_style')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 10})

    return fig


def piet():
    fig = px.pie(dalian, names='house_decoration')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


def cmap_one():
    dalian_one = pd.read_csv(DATA_PATH.joinpath("clustering_one.csv"))

    fig = px.density_mapbox(dalian_one, lat='lat', lon='lon', z='deal_totalPrice',
                            hover_data=["xiaoqu", "address", "deal_totalPrice", "deal_unitPrice"],
                            radius=10)
    fig.update_layout(autosize=True,
                      hovermode='closest',
                      mapbox_style="open-street-map",
                      mapbox=dict(
                          accesstoken=mapbox_access_token,
                          bearing=0,
                          center=dict(
                              lat=38.9146,
                              lon=121.619
                          ),
                          pitch=0,
                          zoom=9,
                      ),
                      )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 10})
    return fig


def cmap_two():
    dalian_two = pd.read_csv(DATA_PATH.joinpath("clustering_two.csv"))

    fig = px.density_mapbox(dalian_two, lat='lat', lon='lon', z='deal_totalPrice',
                            hover_data=["xiaoqu", "address", "deal_totalPrice", "deal_unitPrice"],
                            radius=10)
    fig.update_layout(autosize=True,
                      hovermode='closest',
                      mapbox_style="open-street-map",
                      mapbox=dict(
                          accesstoken=mapbox_access_token,
                          bearing=0,
                          center=dict(
                              lat=38.9146,
                              lon=121.619
                          ),
                          pitch=0,
                          zoom=9,
                      ),
                      )


    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 10})
    return fig


def cmap_three():
    dalian_three = pd.read_csv(DATA_PATH.joinpath("clustering_three.csv"))

    fig = px.density_mapbox(dalian_three, lat='lat', lon='lon', z='deal_totalPrice',
                            hover_data=["xiaoqu", "address", "deal_totalPrice", "deal_unitPrice"],
                            radius=10)
    fig.update_layout(autosize=True,
                      hovermode='closest',
                      mapbox_style="open-street-map",
                      mapbox=dict(
                          accesstoken=mapbox_access_token,
                          bearing=0,
                          center=dict(
                              lat=38.9146,
                              lon=121.619
                          ),
                          pitch=0,
                          zoom=9,
                      ),
                      )


    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 10})
    return fig


app.layout = html.Div(
    # style=dict(backgroundColor=colors['background']),
    className="app_main_content",
    children=[
        html.Div(
            className="banner",
            children=[
                html.H3(
                    children="DaLian链家二手房源信息",
                ),
                html.Img(src=app.get_asset_url("plotly_logo.png")),
            ],
        ),
        html.Div(
            html.H6('大连二手房屋分布地图'),
            style=dict(textAlign='center', color=colors['text']),
        ),
        html.Div(
            children=dcc.Loading(
                children=dcc.Graph(
                    id="flights_time_series",
                    figure=map(),
                )
            ),
        ),
        html.Div(
            children=[
                html.H6(children='大连二手房屋总价热力图',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=heatmap(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连二手房总价-面积散点图',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=allscatter(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连二手房单价-面积散点图',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=unitscatter(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='各区房屋面积-总价散点图',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=scatter(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连各区二手房屋数量图',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=housenum(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连各区二手房屋类型图',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=housetype(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连二手房房屋户型占比图',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=pie(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连二手房房屋户型占比图',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=piet(),
                        ),
                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连二手房屋聚类一',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=cmap_one(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连二手房屋聚类二',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=cmap_two(),
                        ),

                    ),
                ),
            ]
        ),
        html.Div(
            children=[
                html.H6(children='大连二手房屋聚类三',
                        style=dict(textAlign='center', color=colors['text']),
                        ),
                html.Div(
                    children=dcc.Loading(
                        children=dcc.Graph(
                            figure=cmap_three(),
                        ),

                    ),
                ),
            ]
        ),

    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
