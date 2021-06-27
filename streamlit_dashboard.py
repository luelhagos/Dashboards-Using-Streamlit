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

def text_category(p):
    """
    A function  that takes a value p and returns, depending on the value of p, 
    a string 'positive', 'negative' or 'neutral'
    """
    if p > 0 : return 'positive'
    elif p == 0: return 'neutral'
    return 'negative'

# Count the number of positive, neutral, and negative
def polarity_count():
    df = loadData()
    df['score'] = df['polarity'].apply(text_category) 
    sc = list(df['score'])
    return { 'positive': sc.count('positive'), 'neutral': sc.count('neutral'),
                            'negative': sc.count('negative')  }


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
  
# draws bar chart of the polarity
def barChart():
    st.title('BarChart')
    count = polarity_count()
    data = pd.DataFrame({
    'index': list(count.keys()),
    'total': [count[key] for key in count.keys()],
                }).set_index('index')
    st.bar_chart(data)
  
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
  
