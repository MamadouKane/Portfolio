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

    # Add a custom style for input fields
    # st.markdown(
    #     """
    #     <style>
    #     input, textarea {
    #         background-color: #f0d6fd !important;
    #         color: black !important;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )

    with st.container():
        # col1, col2,col3 = st.columns([1,3,1])
        # with col2:
        #     # Form
        #     with st.form("contact_form"):
        #         sender_email = st.text_input("Your Email Address", placeholder="Enter your email")
        #         subject = st.text_input("Subject", placeholder="Enter the subject of your message")
        #         message_content = st.text_area("Message", placeholder="Write your message here...")
        #         attachment = st.file_uploader("Attach a file (optional)", type=["pdf", "png", "jpg", "jpeg", "docx"])
        #         submit_button = st.form_submit_button(label="Send Message")

        #         if submit_button:
        #             if sender_email and subject and message_content:
        #                 success = send_email(sender_email, subject, message_content, attachment)
        #                 if success:
        #                     st.success("Your message has been sent successfully!")
        #                 else:
        #                     st.error("Failed to send your message. Please try again later.")
        #             else:
        #                 st.warning("Please fill out all required fields before submitting.")

        contact()




            
        
        
        
        