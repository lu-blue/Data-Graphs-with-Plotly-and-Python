import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#unpacking csv and preparing for plotly
#Sentences_All
df_sentences = pd.read_csv ("Sentences_All.csv", encoding='latin1', index_col = "Length")

rows10_sen = df_sentences.iloc [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0]] #length and content from Book 1
#print (rows10_sen)

fr_dic10_sen = rows10_sen.to_dict()
#print(fr_dic10_sen)
print("\n")


rows20_sen = df_sentences.iloc [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0]] #length and content from Book 2

fr_dic20_sen = rows20_sen.to_dict()
#print (fr_dic20_sen)

#removed top level of dictionary
flat10_sen = dict(ele for sub in fr_dic10_sen.values() for ele in sub.items()) 
#print (flat1_sen)

flat20_sen = dict(ele for sub in fr_dic20_sen.values() for ele in sub.items()) 
#print (flat2_sen)

keys10_sen = flat10_sen.keys() 
values10_sen = flat10_sen.values() 
#print (list(keys10_sen))
#print (list(values10_sen))

keys20_sen = flat20_sen.keys() 
values20_sen = flat20_sen.values() 
#print (list(keys20_sen))
#print (list(values20_sen))


fig = make_subplots(specs=[[{"secondary_y": True}]])

app.layout = html.Div(children=[
	html.H1(children='Assignment 3 by Lubov Novozhilova'),
	html.Div(children='Graph 3'),
	dcc.Graph(id="graph3",
		figure=fig)
	])

#Vizualization for sentence length and ranking from Book 1 and Book 2
fig.add_trace(
	go.Scatter(x=list(values10_sen), y=list(keys10_sen), marker=dict(color="crimson", size=14),
    mode="markers", name="Muller"),
	#secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=list(values20_sen), y=list(keys20_sen), marker=dict(color="gold", size=14),
    mode="markers", name="Sapir"),
	#secondary_y=True,
)

# Add figure title
fig.update_layout(
	title_text="<b>Content and length of top 10 ranked sentences in Muller and Sapir</b>", title_font_size=22, title_font_color="red", hovermode='x'#barmode="stack"
)

# Set x-axis title
fig.update_xaxes(title_text="<b>Rank of top 10 sentences</b>", title_font_size=17, title_font_color="blue")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Number of words per sentence</b>", title_font_size=17, title_font_color="blue", secondary_y=False)
fig.update_yaxes(title_text="<b>Number of words per sentence</b>", title_font_size=17, title_font_color="blue", secondary_y=True)

fig.show()

#if __name__=='__main__':
	#app.run_server(debug=True)