import streamlit as st
import json, os
from streamlit_option_menu import option_menu

from page.aboutMe import about_me
from page.experiences import *
from page.projects import projects
from page.contact import contact

st.set_page_config(page_title="MK portfolio", page_icon='📋', layout='wide')


with st.container():
    selected = option_menu(
        menu_title="",
        options= ["Home","Experiences","Projects", "Contact"],
        icons= ["house", "briefcase", "book", 'envelope'],
        default_index=0,
        orientation="horizontal"
    ) 


# ***************************************************** ABOUT ME ********************************
if selected=='Home':
    # _,col2,_ = st.columns([1,8,1])
    # with col2:
    # About me
    about_me()


# ***************************************************** EXPERIENCES ********************************  
if selected=='Experiences':
    experiences()


# ***************************************************** PROJECTS *********************************** 
if selected=='Projects':
    projects()        
    

# ***************************************************** CONTACT ************************************      
if selected== 'Contact':
    # Section Contact

    st.header("Contact Me 📨 ")
    st.write("Feel free to reach out to me using the form below!")

    with st.container():
        contact()




            
        
        
        
        