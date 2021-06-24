import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

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
df_sentences = pd.read_csv ("Sentences_All.csv", encoding='latin1')

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


#to add info about length

df_keywords1 = pd.read_csv ("Keywords_All.csv", index_col = "Keyword")
#print (df_keywords1)

rows10 = df_keywords1.iloc [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1]] #keyword and length from Book 1
#print (rows10)

fr_dic10 = rows10.to_dict()
#print(fr_dic10)

flat10 = dict(ele for sub in fr_dic10.values() for ele in sub.items()) 
#print (flat10)

keys10 = flat10.keys() 
values10 = flat10.values() 
#print (list(keys10))
#print (list(values10)) #length from Book 1



df_keywords2 = pd.read_csv ("Keywords_All.csv", index_col = "Keyword")

rows20 = df_keywords2.iloc [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1]] #keyword and length from Book 2
#print (rows20)

fr_dic20 = rows20.to_dict()
#print(fr_dic20)

flat20 = dict(ele for sub in fr_dic20.values() for ele in sub.items()) 
#print (flat20)

keys20 = flat20.keys() 
values20 = flat20.values() 
#print (list(keys10))
#print (list(values20)) #length from Book 2


fig = make_subplots(specs=[[{"secondary_y": True}]])

app.layout = html.Div(children=[
	html.H1(children='Assignment 3 by Lubov Novozhilova'),
	html.Div(children='Graph 1'),
	dcc.Graph(figure=fig)
	])

#Vizualization for keywords and their frequencies from Book 1 and Book 2
fig.add_trace(
	go.Bar(x=list(keys1), y=list(values1), marker=dict(color="navy"), name="Frequency(Muller)"),
	#secondary_y=False,
)

fig.add_trace(
    go.Bar(x=list(keys2), y=list(values2), marker=dict(color="purple"), name="Frequency(Sapir)"),
	#secondary_y=True,
)

fig.add_trace(
	go.Bar(x=list(keys1), y=list(values10), marker=dict(color="blue"), name="Length(Muller)"),
	#secondary_y=False,
)

fig.add_trace(
    go.Bar(x=list(keys2), y=list(values20), marker=dict(color="violet"), name="Length(Sapir)"),
	#secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="<b>Frequency and length of top 10 keywords in Muller and Sapir </b>", hovermode='x', barmode="stack" 
)

# Set x-axis title
fig.update_xaxes(title_text="<b>Words</b>")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Frequency</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Length</b>", secondary_y=True)

fig.show()

# if __name__=='__main__':
# 	app.run_server(debug=True) 










