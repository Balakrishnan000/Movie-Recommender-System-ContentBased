from datetime import datetime

import streamlit as st
import pickle 
import pandas as pd
import requests
import streamlit.components.v1 as components

COMMENT_TEMPLATE_MD = """{} - {}
> {}"""


my_api_key = '4051077e7188c536fc7feb16b656bbd0'

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id,my_api_key))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']


movie_dict = pickle.load(open('movie_dict.pkl','rb'))
#new df is now here via the file - as dict
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System - Content Based')
selected_movie_name = st.selectbox(
     'Hey, It\'s so simple, just type out a movie name that you have seen or with respect to which you need to see the results, then click on \'Recommend Me\'  ',
     movies['title'].values)
st.write('You selected:', selected_movie_name)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] #Way to get index with name
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x : x[1])[1:6]
    #as top is the 1 and its the same movie
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list :
        movie_id = movies.iloc[i[0]].movie_id #here u get movie id - to see look at iloc 
        #fetch poster from an API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

if st.button('Recommend Me'):
    with st.spinner("Loading..."):
        names,posters = recommend(selected_movie_name)

        st.write("**Hooray! Here are the Top 5 Recommendations from our Recommendation Model:**")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text("1. "+names[0])
            st.image(posters[0])
        with col2:
            st.text("2. "+names[1])
            st.image(posters[1])
        with col3:
            st.text("3. "+names[2])
            st.image(posters[2])
        with col4:
            st.text("4. "+names[3])
            st.image(posters[3])
        with col5:
            st.text("5. "+names[4])
            st.image(posters[4])

embedcmp = { 'linkedin': """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script> <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="balakrishnan-r-906404184" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/balakrishnan-r-906404184?trk=profile-badge">Balakrishnan R</a></div>"""
}

with st.sidebar:
    
    st.subheader("To Know More: ")
    st.write("Feel free to contact the Developer: ")
    components.html(embedcmp['linkedin'],height=350)

#CONTACT ME FORM WHICH WILL MAIL ME
contact_form = """<form action="https://formsubmit.co/devbala2022@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Working Email to get reply back" required>
     <textarea name="message" placeholder="Your Message or Feedback - Positive or Negative - Both welcomed"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown("***")

st.subheader("Contact Form:")
st.write("*Here your message reaches to my mailbox directly. (24 hours avg reply time)*")
st.markdown(contact_form,unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#Removeing the made by 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
