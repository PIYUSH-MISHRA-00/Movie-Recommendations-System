import streamlit as st
import pickle
import pandas as pd
import requests
import gdown

# Function to fetch the poster of a movie
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""
    return full_path

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_posters = []
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movie_posters

# Download the models from Google Drive
@st.cache_data
def load_models():
    movie_dict_url = 'https://drive.google.com/uc?id=1rB8Nk9ZsY7bJoP2CiVyas3LfGHEVudu1'
    similarity_url = 'https://drive.google.com/uc?id=1_Q7WrH6vkliUQ089c5XE6DGSxxnwP610'

    # Download the movie dictionary
    gdown.download(movie_dict_url, 'movie_dict.pkl', quiet=False)
    # Download the similarity matrix
    gdown.download(similarity_url, 'similarity.pkl', quiet=False)

    # Load the models
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return pd.DataFrame(movies_dict), similarity

# Load the movie dictionary and similarity matrix
movies, similarity = load_models()

# Streamlit UI
st.title('Movie Recommender System')

# Movie selection box
selected_movie_name = st.selectbox('Select the movie', movies['title'].values)

# Show recommendations when the button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    
    # Display recommendations
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
