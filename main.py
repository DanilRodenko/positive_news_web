import streamlit as st

from backend import positive_news

# st.title('Positive news')

for news in positive_news:
    st.subheader(news['title'])
    st.write(news['description'])
    st.markdown("[More info](%s)" % news['url'])
    st.image(news['urlToImage'])

