import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = movies['title'].values
st.set_page_config(layout='wide',page_icon="🎞",page_title="Movie Recommander")
st.header("**Movie Recommandation System** 📽")
selected_movie = st.selectbox('**Select your favorite movie from the dropdown**',movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2fd08e9e5c5e3e1e7a88e46016449e73&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def recommandation(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda vector:vector[1])
    recommeded_movies = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommeded_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommeded_movies,recommend_poster
import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)

if st.button("Show Recommanded"):
    movie_recommended,movie_poster = recommandation(selected_movie)
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(movie_recommended[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_recommended[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_recommended[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_recommended[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_recommended[4])
        st.image(movie_poster[4])
    st.success("**Enjoy** 🎉 ")