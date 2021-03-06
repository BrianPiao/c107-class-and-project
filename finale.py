import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")

#df.loc will help us filter out all the rows with the given student id
studentdef = df.loc [df["student_id"] == "TRL_zet"]

fig = go.Figure(go.Bar(
     x = studentdef.groupby("level")["attempt"].mean() , 
     y = ['Level 1' , "Level 2" , 'Level 3' , 'Level 4'],
     orientation = 'h'
))

fig.show ()