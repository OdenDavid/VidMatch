"""
In an environment with streamlit installed,
Run with `streamlit run App.py`
"""
import pandas as pd
import streamlit as st
from PIL import Image
import os
import random


# ============= PAGE SETUP ============
st.set_page_config(page_title="VidMatch", page_icon="🔻", layout="wide")

image = Image.open('Images/logo.png')
st.image(image)

# ============== Session States/Pages ==================
if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage():
    st.session_state.page += 1 # Go to next page

def restart(): st.session_state.page = 0 # Go back to beginning

placeholder = st.empty() # Initialize a container widget to hold entire page contents

# ================= Page 1: Home Page ==================
if st.session_state.page == 0:
    with placeholder.container():
        c1, c2, c3 = st.columns([3,8,2])
        with c2:
            st.header("Say Goodbye to Boring Feeds")
            st.subheader("Find youtube videos based on your interests")
            st.caption("VidMatch is powered by efficient recommendation algorithms, populating your feeds with what you love ❤️")

        # ================ Image Grid =====================
        image_files = [f for f in os.listdir("Images/thumbnails")] # List of all images in folder
        random_images = random.sample(image_files, 15) # 15 random images
        image_paths = [os.path.join("Images/thumbnails", image) for image in random_images] # List of 15 image paths
        # First Row
        c1, c2, c3 = st.columns([2,8,2])
        with c2:
            c21, c22, c23 = st.columns(3)
            with c21:
                st.image(Image.open(image_paths[0]))
            with c22:
                st.image(Image.open(image_paths[1]))
            with c23:
                st.image(Image.open(image_paths[2]))
        # Second And Third Row
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        with c1:
            st.image(Image.open(image_paths[3]))
            st.image(Image.open(image_paths[4]))
        with c2:
            st.image(Image.open(image_paths[5]))
            st.image(Image.open(image_paths[6]))
        with c3:
            st.image(Image.open(image_paths[7]))
            st.image(Image.open(image_paths[8]))
        with c4:
            st.image(Image.open(image_paths[9]))
            st.image(Image.open(image_paths[10]))
        with c5:
            st.image(Image.open(image_paths[11]))
            st.image(Image.open(image_paths[12]))
        with c6:
            st.image(Image.open(image_paths[13]))
            st.image(Image.open(image_paths[14]))

        st.write("")
        st.write("")
        # ========== CTA ============
        c1, c2, c3 = st.columns([4,4,4])
        with c2:
            if st.button("Get Started", type="primary",use_container_width=True):
                nextpage()
# ================= Page 2: Login/Sign Up Page ==================
if st.session_state.page == 1:
    with placeholder.container():
        c1, c2, c3 = st.columns([3,8,3])
        with c2:
            st.write("")
            t1, t2 = st.tabs(["Login","Sign Up"])
            with t1: # Login
                st.write("")
                st.write("")
                st.subheader("Login")
                c1, c2, c3 = st.columns([2,4,2])
                with c2:
                    st.text_input("User ID",type="password",placeholder="4 digit pin (1234)")
                    if st.button("login",type="primary",use_container_width=True):
                        pass
            with t2: # Sign Up
                st.write("")
                st.write("")
                st.subheader("Tell us a little about your interests")
                c1, c2, c3 = st.columns([2,4,2])
                with c2:
                    categories = ['Film & Animation', 'Autos & Vehicles', 'Music', 'Pets & Animals', 'Sports', 'Short Movies', 'Travel & Events', 'Gaming', 'Videoblogging', 'People & Blogs', 'Comedy', 'Entertainment', 'News & Politics', 'Howto & Style', 'Education', 'Science & Technology', 'Nonprofits & Activism', 'Movies', 'Anime/Animation', 'Action/Adventure', 'Classics', 'Comedy', 'Documentary', 'Drama', 'Family', 'Foreign', 'Horror', 'Sci-Fi/Fantasy', 'Thriller', 'Shorts', 'Shows', 'Trailers']
                    countries = ["USA","Canada","France","UK"]
                    interests = st.multiselect('What are you interested in?',options=categories, placeholder="Select as many categories")
                    countries = st.multiselect('From what countries?',options=countries, placeholder="Select one or more countries")
                    st.write("")
                    st.write("")
                    st.text_input("Auto-Generated User ID (You can type yours)",value=str(random.randint(1000, 9999)),type="password")
                    if st.button("Sign Up",type="primary",use_container_width=True):
                        pass
# ================= Page 3: Feed Page ==================
if st.session_state.page == 2:
    pass