"""
In an environment with streamlit installed,
Run with `streamlit run App.py`
"""
import pandas as pd
import streamlit as st
from PIL import Image
import pathlib

import os
import random

import sqlite3

# =========== Initialize SQL ==========
conn = sqlite3.connect("Data.db") # db - database
cursor = conn.cursor() # Cursor object

# Read Data
df_videos = pd.read_sql_query("SELECT * FROM Videos;", conn)

# ============= PAGE SETUP ============
st.set_page_config(page_title="VidMatch", page_icon="🔻", layout="wide")

image = Image.open('Images/logo.png')
st.image(image)

# ============== Session States/Pages ==================
if "page" not in st.session_state:
    st.session_state.page = 0
if "userid" not in st.session_state:
    st.session_state.userid = ""

def nextpage(userid):
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
                placeholder.empty()
                nextpage(userid="")
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
                    id = st.text_input("User ID",type="password",placeholder="4 digit pin (1234)")
                    if st.button("login",type="primary",use_container_width=True):
                        placeholder.empty()
                        nextpage(userid=id)
            with t2: # Sign Up
                st.write("")
                st.write("")
                st.subheader("Tell us a little about your interests")
                c1, c2, c3 = st.columns([2,4,2])
                with c2:
                    categories = ['Entertainment','Music','People & Blogs','News & Politics','Pets & Animals','Education','Science & Technology','Sports','Film & Animation','Travel & Events','Howto & Style','Comedy','Gaming','Autos & Vehicles','Nonprofits & Activism','Shows']
                    countries = ["USA","Canada","France","UK"]
                    interests = st.multiselect('What are you interested in?',options=categories, placeholder="Select as many categories")
                    countries = st.multiselect('From what countries?',options=countries, placeholder="Select one or more countries")
                    st.write("")
                    st.write("")
                    id = st.text_input("Auto-Generated User ID (You can type yours)",value=str(random.randint(1000, 9999)),type="password")
                    if st.button("Sign Up",type="primary",use_container_width=True):
                        placeholder.empty()
                        nextpage(userid=id)

# ================= Page 3: Feed Page ==================
if st.session_state.page == 2:
    with placeholder.container():
        st.subheader("Recommended for you today")
        st.write("")

        # ======= Feeds =========
        st.subheader("Feeds")
        search_input = st.text_input(label="see",label_visibility="hidden",placeholder="Type video or channel name to search", value="")

        # ===============================
        # Filter the dataframe using masks:  Users can search with video or channel name
        m1 = df_videos["title"].str.contains(search_input)
        m2 = df_videos["channel_title"].str.contains(search_input)
        df_search = df_videos[m1 | m2]

        N_cards_per_row = 4
        if search_input:
            for n_row, row in df_search.reset_index().iterrows():
                i = n_row%N_cards_per_row
                if i==0:
                    st.write("---")
                    cols = st.columns(N_cards_per_row, gap="large")
                # draw the card
                with cols[n_row%N_cards_per_row]:
                    url = f"https://www.youtube.com/watch?v={row['video_id']}"
                    clickable_image = f'<a href="{url}" target="_blank"> <img src="https://github.com/OdenDavid/VidMatch/blob/main/Images/logo.png?raw=true" style="{"width:100%;"}"></a>'
                    st.markdown(clickable_image, unsafe_allow_html=True)
                    st.markdown(f"**{row['title']}**")
                    st.caption(f"{row['channel_title']}")
                    st.caption(f"{row['category']} - {row['publish_country']}")
                    st.caption(f"<b>Views:</b> {row['views']} - <b>Likes:</b> {row['likes']}",unsafe_allow_html=True,)
        else:
            df_default = df_videos.sample(n=100, random_state=42)
            for n_row, row in df_default.reset_index().iterrows():
                i = n_row%N_cards_per_row
                if i==0:
                    st.write("---")
                    cols = st.columns(N_cards_per_row, gap="large")
                # draw the card
                with cols[n_row%N_cards_per_row]:
                    url = f"https://www.youtube.com/watch?v={row['video_id']}"
                    clickable_image = f'<a href="{url}" target="_blank"> <img src="https://github.com/OdenDavid/VidMatch/blob/main/Images/logo.png?raw=true" style="{"width:100%;"}"></a>'
                    st.markdown(clickable_image, unsafe_allow_html=True)
                    st.markdown(f"**{row['title']}**")
                    st.caption(f"{row['channel_title']}")
                    st.caption(f"{row['category']} - {row['publish_country']}")
                    st.caption(f"<b>Views:</b> {row['views']} - <b>Likes:</b> {row['likes']}",unsafe_allow_html=True,)
                    
