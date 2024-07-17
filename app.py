import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    """
    Fetches the movie poster from The Movie Database (TMDb) API.

    Parameters:
    movie_id (int): The unique ID of the movie.

    Returns:
    str: The full URL to the movie poster image.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    return None

def recommend(movie):
    """
    Recommends movies similar to the given movie.

    Parameters:
    movie (str): The title of the movie for which recommendations are needed.

    Returns:
    tuple: A tuple containing two lists - 
           1. recommended_movie_names: List of recommended movie titles.
           2. recommended_movie_posters: List of URLs to the recommended movie posters.
    """
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# Load precomputed movie list and similarity matrix
movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: black;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: blue;
        color: white;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .header {
        background-color: maroon;
        padding: 10px;
        border-radius: 5px;
    }
    .header h1 {
        color: white;
    }
    .movie-container {
        padding: 20px;
        background-color: white;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True
)

# App layout and styling
st.markdown('<div class="header"><h1>Movie Recommender System</h1></div>', unsafe_allow_html=True)
st.subheader('Using Machine Learning')
st.markdown("""
    This application provides movie recommendations based on your selection. 
    It uses a machine learning model to suggest movies that you might like.
    Simply select a movie from the dropdown menu, and the app will recommend similar movies.
""")

# Sidebar for additional options
st.sidebar.title('Navigation')
st.sidebar.subheader('Options')

# Movie selection
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

# Show recommendations when the button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    st.header('Recommended Movies')
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f'<div class="movie-container"><h4>{recommended_movie_names[i]}</h4><img src="{recommended_movie_posters[i]}" width="100%"></div>', unsafe_allow_html=True)
