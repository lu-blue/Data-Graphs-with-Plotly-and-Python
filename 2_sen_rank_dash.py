import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#unpacking csv and preparing for plotly
#Keywords_All
df_keywords = pd.read_csv ("Keywords_All.csv", index_col = "Keyword")

rows1 = df_keywords.iloc [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0]] #keywords and frequency from Book 1
fr_dic1 = rows1.to_dict() #converting into dictionary
flat1 = dict(ele for sub in fr_dic1.values() for ele in sub.items()) #removing top level of dictionary
keys1 = flat1.keys() #splitting into keys and values
values1 = flat1.values() 
#print (list(keys1)) #keys as a list
#print (list(values1))

rows2 = df_keywords.iloc [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0]] #keywords and frequency from Book 2
fr_dic2 = rows2.to_dict() #converting into dictionary
flat2 = dict(ele for sub in fr_dic2.values() for ele in sub.items()) #removing top level of dictionary
keys2 = flat2.keys() #splitting into keys and values
values2 = flat2.values() 
#print (list(keys2)) #keys as a list
#print (list(values2)) #values as a list

#Sentences_All
df_sentences = pd.read_csv ("Sentences_All.csv", encoding='latin1', index_col = "Ranking")

rows1_sen = df_sentences.iloc [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0]] #sentence length and ranking from Book 1
fr_dic1_sen = rows1_sen.to_dict() #converting into dictionary
flat1_sen = dict(ele for sub in fr_dic1_sen.values() for ele in sub.items()) #removing top level of dictionary
keys1_sen = flat1_sen.keys() #splitting into keys and values
values1_sen = flat1_sen.values() 
#print (list(keys1_sen)) #keys as a list
#print (list(values1_sen)) #values as a list

rows2_sen = df_sentences.iloc [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0]] #length and ranking from Book 2
fr_dic2_sen = rows2_sen.to_dict() #converting into dictionary
flat2_sen = dict(ele for sub in fr_dic2_sen.values() for ele in sub.items()) #removing top level of dictionary
keys2_sen = flat2_sen.keys() #splitting into keys and values
values2_sen = flat2_sen.values() 
#print (list(keys2_sen)) #keys as a list
#print (list(values2_sen)) #values as a list


fig = make_subplots(specs=[[{"secondary_y": True}]])

app.layout = html.Div(children=[
	html.H1(children='Assignment 3 by Lubov Novozhilova'),
	html.Div(children='Graph 2'),
	dcc.Graph(id="graph2",
		figure=fig)
	])

#Vizualization for sentence length and ranking from Book 1 and Book 2
fig.add_trace(
	go.Bar(x=list(keys1_sen), y=list(values1_sen), marker=dict(color="limegreen"), name="Muller"),
	#secondary_y=False,
)

fig.add_trace(
    go.Bar(x=list(keys2_sen), y=list(values2_sen), marker=dict(color="dodgerblue"), name="Sapir"),
	#secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="<b>Length of top 10 ranked sentences in Muller and Sapir</b>", hovermode='x'#barmode="stack"
)

# Set x-axis title
fig.update_xaxes(title_text="<b>Rank of top 10 sentences</b>")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Number of words per sentence</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Number of words per sentence</b>", secondary_y=True)

fig.show()

#if __name__=='__main__':
	#app.run_server(debug=True)