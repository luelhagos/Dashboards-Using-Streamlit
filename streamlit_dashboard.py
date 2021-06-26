import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px
from add_data import db_execute_fetch

st.title('Topic Modeling and Sentiment Analysis')

st.write("## Topic modeling and sentimet anlysis of twiteer data")


# loads the data fromm the db based on query
def loadData():
    query = "select * from Tweet"
    df = db_execute_fetch(query, dbName="db_tweets", rdf=True)
    return df


def wordCloud():
  """
  To be implemented..
  """
  pass
  
def barChart():
  """
  To be implemented..
  """
  pass
  
def pieChart():
  """
  To be implemented..
  """
  pass
    
def selectPolarity():
  """
  To be implemented..
  """
  pass
  
