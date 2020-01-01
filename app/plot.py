import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    mapbox_access_token = "pk.eyJ1Ijoia2VrZWluZyIsImEiOiJjazRjZ3Njc3owbmh1M2xvMmZrbHczNmd1In0.A51yo2likAVjYj4qRepeog"
    dalian = pd.read_csv(r'../data/lianjia_processed.csv', sep=',')

    fig = px.scatter_mapbox(dalian, lat="lat", lon="lon", hover_name="xiaoqu",
                            hover_data=["address", "deal_totalPrice", "deal_unitPrice"],
                            color_discrete_sequence=["fuchsia"], height=900, )

    fig.update_layout(autosize=True,
                      hovermode='closest',
                      mapbox_style="carto-positron",
                      mapbox=dict(
                          accesstoken=mapbox_access_token,
                          bearing=0,
                          center=dict(
                              lat=38.9146,
                              lon=121.619
                          ),
                          pitch=0,
                          zoom=10
                      ), )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()
