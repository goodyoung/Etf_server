import pathlib
import re,os
import json
from datetime import datetime

import matplotlib.colors as mcolors

import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot

import pandas as pd
import numpy as np
import sqlalchemy as sqla
from sqlalchemy import text
import pymysql

from dateutil import relativedelta
from wordcloud import WordCloud, STOPWORDS

from naver_blog import naver_blog_search, concat_blog_description
import nltk
from nltk.corpus import stopwords
from konlpy.tag import Kkma, Okt, Hannanum, Komoran

# dash 2.x above
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dash_table, html, dcc, Input, Output, callback
from dash.dash_table import DataTable
from dash.dash_table import FormatTemplate
from dash.dash_table.Format import Format, Group, Prefix, Scheme, Symbol

import requests

# ROOT_PATH = '/home/qkboo/'
# print('asdf',os.getcwd())
os.chdir("/Users/goodyoung/Desktop/대학교/Dash")
font_path = '/Users/goodyoung/Library/Fonts/NanumGothic.otf'
# print('asdf',os.getcwd())
# ROOT_PATH = 'E:/Jupyter-Finance2/'
# DATA_PATH = pathlib.Path(__name__).parent.resolve()

## rest - api 대체
with open(f'./.api_keys/secret_homedb.json') as f:
    secrets = json.loads(f.read())

DB_USER, DB_PW = secrets['stockmart']['userid'], secrets['stockmart']['password']
CLIENT_ID, CLIENT_SECRET = secrets['naver_search_api']['client_id'], secrets['naver_search_api']['client_secret']
engine = sqla.create_engine(f'mysql+pymysql://{DB_USER}:{DB_PW}@220.121.140.51:3030/financedb')  

# query =  sqla.text("select d.종목코드, d.종목명,  e.지급기준일, e.`분배금(원)`, e.DC_R `분배율(%)` "\
# " from etf_details d, etf_profit_payout e "\
# " where e.종목코드=d.종목코드 "\
# " and d.PAY_CLASS='MONTLY' " \
# # " and e.지급기준일 like '2023-02%' "\
# " order by e.DC_R desc")

# df1 = pd.read_sql(query, con=engine)
url = 'http://127.0.0.1:8000/api/test/'
req = requests.get(url).json()
j = json.loads(req['data'])
df1 = pd.DataFrame(j)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
'''
    main function
'''

def plotly_wordcloud2(wc:WordCloud):
    word_list=[]
    freq_list=[]
    fontsize_list=[]
    position_list=[]
    orientation_list=[]
    color_list=[]

    for (word, freq), fontsize, position, orientation, color in wc.layout_:
        word_list.append(word)
        freq_list.append(freq)
        fontsize_list.append(fontsize)
        position_list.append(position)
        orientation_list.append(orientation)
        color_list.append(color)
        
    # get the positions
    x=[ i[0] for i in position_list]
    y=[ i[1] for i in position_list]
            
     # get the relative occurence frequencies
    new_freq_list = [ (i*100) for i in freq_list ]
    new_freq_list
    
    trace = go.Scatter(x=x, 
                       y=y, 
                       textfont = dict(size=new_freq_list,
                                       color=color_list),
                       hoverinfo='text',
                       hovertext=['{0} {1:.2%}'.format(w, f) for w, f in zip(word_list, freq_list)],
                       mode="text",  
                       text=word_list
                      )
    
    layout = go.Layout(
                       xaxis=dict(showgrid=False, 
                                  showticklabels=False,
                                  zeroline=False,
                                  automargin=True),
                       yaxis=dict(showgrid=False,
                                  showticklabels=False,
                                  zeroline=False,
                                  automargin=True)
                      )
    
    fig = go.Figure(data=[trace], layout=layout)
    
    return fig

def getWordcloud(name, font_path = font_path):
    STOCK_NAME = str(name)
    ## data crawling
    items = naver_blog_search(CLIENT_ID, CLIENT_SECRET, STOCK_NAME, 2, 100)
    contents = concat_blog_description(items)
    ## data preprocessing
    korm = Komoran()
    tokens_ko = korm.nouns(contents)
    tokens_ko = nltk.regexp_tokenize(contents, r'(\w+)')\
    
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM kr_words"))
        ko_stops = result.all()
    en_stops = stopwords.words('english')
    ko_stopwords = ko_stops[0][2]
    tokens_ko = [w for w in tokens_ko if len(w) > 1]
    # tokens_stopped = [word for word in tokens_ko if word in ko_stopwords]
    tokens_ko = [word for word in tokens_ko if word not in ko_stopwords]
    tokens_ko = [word for word in tokens_ko if word.lower() not in en_stops]
    # 형태소 분석을 통해 필요한 단어 추가!!!
    MORE_STOPS = ['미래에셋', 'TIGER', '타이거', STOCK_NAME]
    tokens_ko = [word for word in tokens_ko if word not in MORE_STOPS]
    komorph = nltk.Text(tokens_ko, name=STOCK_NAME)
    #data analize
    most_common_words = komorph.vocab().most_common(30)
    wordcloud = WordCloud(
                          font_path = font_path,
                          relative_scaling = 0.2,
                          background_color='white',
    ).generate_from_frequencies(dict(most_common_words))
    return wordcloud


"""
    Page Layouts
"""

_LOGO_URL = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSu9xFbA6COOd9Wq-koFEoAFD7wpFgbvdz6Q&usqp=CAU'
_TITLE = 'ETF 분배율 (이익금분배 종목)'

NAVBAR = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=_LOGO_URL, height="30px")),
                    dbc.Col(
                        dbc.NavbarBrand(_TITLE, className="ml-2")
                    ),
                ],
                align="center",
                # no_gutters=True,
            ),
            href="https://blog.thinkbee.kr",
        )
    ],
    color="dark",
    dark=True,
    sticky="top",
)


#
# WordCoud 블럭
#
WORDCLOUD_PLOTS = [
    dbc.CardHeader(html.H5("Wordcloud")),
    dbc.Alert(
        "Not enough data to render these plots, please adjust the filters",
        id="no-data-alert",
        color="warning",
        style={"display": "none"},
    ),
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                        dcc.Loading(
                            id="loading-wordcloud",
                            children=[
                                dcc.Graph(id="bank-wordcloud")
                            ],
                            type="default",
                        )
                        ],
                        # md=8, # md???
                    ),
                ]
            )
        ]
    ),
]


'''
    Wordcloud Callback
'''

@callback(Output("bank-wordcloud", "figure",allow_duplicate=True), 
          Input('datatable-paging', 'active_cell'),
         prevent_initial_call=True)
def update_graphs(active_cell):
    s = df1.loc[active_cell['row'], active_cell['column_id']]
    wc = getWordcloud(s)
    fig = plotly_wordcloud2(wc)
    return fig



#  분배율
#
new_columns = [' index', '종목코드', '종목명', '지급기준일', '분배금(원)', '분배율(%)']
PAGE_SIZE = 15

df1[' index'] = range(1, len(df1) + 1)
df1 = df1[new_columns]

# fmt_money = FormatTemplate.money(2)
# fmt_percentage = FormatTemplate.percentage(2)
fmt_percentage = Format(precision=2, scheme=Scheme.decimal)
fmt_money = Format(symbol=Symbol.yes, symbol_prefix='₩')

columns = [{"name": i, "id": i} for i in df1.columns]
columns[4]['format'] = fmt_money
columns[5]['format'] = fmt_percentage

columns[4]['type'] = 'numeric'
columns[5]['type'] = 'numeric'

    
DATATABLE = [
    dbc.CardHeader(html.H5( '2023년 1~4월 ETF 분배율 (이익금분배 종목)')),
    dbc.CardBody(
        [
            dash_table.DataTable(
                id='datatable-paging',
                columns=columns,
                page_current=0,
                page_size=PAGE_SIZE,
                page_action='custom',


                sort_action='custom',
                sort_mode='multi',
                sort_by=[]
            ),
            dbc.Alert(id='datatable-alert'),

        ]
    )
]


"""
#  분배율 Callbacks
"""

@app.callback(
    Output('datatable-paging', 'data'),
    Input('datatable-paging', "page_current"),
    Input('datatable-paging', "page_size"),
    Input('datatable-paging', "sort_by")
)
def update_table(page_current, page_size, sort_by):
    if len(sort_by):
        dff = df1.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = df1
    return dff.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')

"""
# BODY
"""

BODY = dbc.Container(
    [
        dbc.Row([dbc.Col(dbc.Card(DATATABLE)),], style={"marginTop": 20}),
        dbc.Card(WORDCLOUD_PLOTS,style={"marginTop": 20}),
        # dbc.Row([dbc.Col(dbc.Card(WORDCLOUD_PLOTS)),], style={"marginTop": 20}),
        
    ]
)

app.layout = html.Div(children=[NAVBAR, BODY])


if __name__ == "__main__":
    app.run_server(debug=False, port=53062)
