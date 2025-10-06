import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns


st.title(" CORD-19 Research Data Explorer")
st.write("Explore global COVID-19 research trends interactively.")

# Load data
df = pd.read_csv('metadata.csv', low_memory=False)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Sidebar filters
year_range = st.slider("Select Year Range", 2019, 2023, (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
st.bar_chart(year_counts)

st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)

st.subheader("Word Cloud of Titles")
text = ' '.join(filtered['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

st.subheader("Sample Data")
st.dataframe(filtered.head(10))