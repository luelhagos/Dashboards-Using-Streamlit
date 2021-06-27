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

# draws bar chart of the polarity
def barChart():
    st.title('Bar Chart')
    count = polarity_count()
    data = pd.DataFrame({
    'Sentiment': list(count.keys()),
    'Tweets': [count[key] for key in count.keys()],
                })
    bar_fig = px.bar(data, x='Sentiment', y='Tweets')
    st.plotly_chart(bar_fig)

# draws pie chart of the polarity
def pieChart():
    st.title('Pie Chart')
    count = polarity_count()
    pie_fig = px.pie(values=[count[key] for key in count.keys()], names=list(count.keys()))
    st.plotly_chart(pie_fig)
    

# topic modeling
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

#st.title("Data Visualizations")
random_tweet = st.sidebar.selectbox('Visualizations', 
                ('Topic Modeling','Bar Chart','Pie Chart'))
if random_tweet == 'Topic Modeling':
    wordCloud()
elif random_tweet == 'Bar Chart':
    barChart()
elif random_tweet == 'Pie Chart':
    pieChart()
