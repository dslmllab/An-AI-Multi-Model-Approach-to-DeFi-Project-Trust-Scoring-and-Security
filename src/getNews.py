
import requests
import json
import streamlit as st
import genScamSentiment
import getApiKeys



search_api_key = getApiKeys.get_api_keys('searchapi')
engine_id =  getApiKeys.get_api_keys('searchengine')


def google_search(query):

    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": search_api_key, "cx": engine_id, "q": query}
    response = requests.get(url, params=params)
    results = response.json()
    print(results)
    overall_score = []
    items =  results.get('items', [])
    print(items)


    for item in items:
        overall_score.append(genScamSentiment.get_sentimentscore(item['title']))
    print(overall_score)
    neutral_sum = 0
    positive_sum = 0
    negative_sum = 0
    neutral_scores = []
    positive_scores = []
    negative_scores  = []

    print(overall_score)

    for score in overall_score:
        sentiment_data = score[0]
    for sentiment in sentiment_data:
        if sentiment['label'] == 'neutral':
            neutral_sum += sentiment['score']
            neutral_scores.append(sentiment['score'])
        elif sentiment['label'] == 'positive':
            positive_sum += sentiment['score']
            positive_scores.append(sentiment['score'])
        elif sentiment['label'] == 'negative':
            negative_sum += sentiment['score']
            negative_scores.append(sentiment['score'])

    neutral_avg = neutral_sum / len(overall_score)
    positive_avg = positive_sum / len(overall_score)
    negative_avg = negative_sum / len(overall_score)
    display_news(neutral_avg,positive_avg,negative_avg,items)

    return neutral_avg,positive_avg,negative_avg,items




def display_news(neutral_avg,positive_avg,negative_avg,items):
    slice = len(items)/2


    with st.expander("News and social Media"):
        st.write(f"Overall News Sentiment Score Positve: {positive_avg:.2f}")
        st.write(f"Overall News Sentiment Score Neutral: {neutral_avg:.2f}")
        st.write(f"Overall News Sentiment Score Negative: {negative_avg:.2f}")
        tab1, tab2 = st.columns(2)



        with tab1:

            for item in items[:int(slice)]:
                if 'pagemap' in item and 'cse_image' in item['pagemap'] and len(item['pagemap']['cse_image']) > 0:
                    image_url = item['pagemap']['cse_image'][0]['src']
                elif  'pagemap' in item and 'metatags' in item['pagemap'] and len(item['pagemap']['metatags']) > 0 and 'og:image' in data['pagemap']['metatags'][0]:
                    image_url = item['pagemap']['metatags'][0]['og:image']
                else:
                    image_url = None
                if image_url:
                    st.image(image_url,item['title'])
                else:
                    st.write(item['title'])
                st.write(item['link'])
                st.write(item['snippet'])

                st.write("------")
        with tab2:

            for item in items[int(slice):]:
                if 'pagemap' in item and 'cse_image' in item['pagemap'] and len(item['pagemap']['cse_image']) > 0:
                    image_url = item['pagemap']['cse_image'][0]['src']
                elif  'pagemap' in item and 'metatags' in item['pagemap'] and len(item['pagemap']['metatags']) > 0 and 'og:image' in item['pagemap']['metatags'][0]:
                    image_url = item['pagemap']['metatags'][0]['og:image']
                else:
                    image_url = None
                if image_url:
                    st.image(image_url,item['title'])
                else:
                    st.write(item['title'])
                st.write(item['link'])
                st.write(item['snippet'])
                st.write("------")


