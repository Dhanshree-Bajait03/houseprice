import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/550?api_key=e85bc81b4e51495da7b105b4e24934a0",format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://images.tmdb.org/t/p/w500/" + poster_path

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

#creater a dropdower to select a movie
selected_movie = st.selectbox("select a movie:", movies_list)

import streamlit.components.v1 as components

def recommend(movie):
    index = movie[movie['ttle']== movie].index[0]
    distancec = sorted(list(enumrate(similarity[index])), reverse=True, Key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_movie.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster 

if st.button("show Recommend"):
    movie_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
