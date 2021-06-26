import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px
from add_data import db_execute_fetch

st.title('Topic Modeling and Sentiment Analysis')

st.write("## Topic modeling and sentimet anlysis of twiteer data")
