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
    df = loadData()
    # Convert to lowercase
    df['clean_text'] = df['clean_text'].map(lambda x: x.lower())
    # Join the different processed titles together.
    long_string = ','.join(list(df['clean_text'].values))

        # Create a WordCloud object
    wordcloud = WordCloud(background_color="black", width=650, height=450, \
                             min_font_size=5, contour_color='steelblue')
    # Generate a word cloud
    wordcloud.generate(long_string)
    st.title("Tweet Text Word Cloud")
    st.image(wordcloud.to_array())
  
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
  
