import streamlit as st
import pickle
import pandas as pd
import base64

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)


def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

set_bg("images/realistic.jpg")



# Load data
df = pickle.load(open("D:\\Movie Reccommendation system\\film.pkl", "rb"))
similarity = pickle.load(open("D:\\Movie Reccommendation system\\similarity.pkl", "rb"))


# Recommendation function
def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = similarity[index]

    movies = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [df.iloc[i[0]]['title'] for i in movies]

# UI
st.markdown("<h1 style='color:white;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

st.markdown("<p style='color:white; font-size:20px;'>Choose a movie</p>", unsafe_allow_html=True)
selected_movie = st.selectbox(
    "",
    df['title'].values
)



if st.button("Recommended for you"):
    for m in recommend(selected_movie):
        st.markdown(f"<b><p style='color:white'>🎬 {m}</p></b>", unsafe_allow_html=True)
    
