import streamlit as st
import base64
from streamlit_pdf_viewer import pdf_viewer


# Convert  PDF file to base64
def get_pdf_download_link(pdf_bytes, filename):
    b64 = base64.b64encode(pdf_bytes).decode() 
    href = f"""
    <a href="data:application/pdf;base64,{b64}" download="{filename}">
        <button style="
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        ">📄 Download my CV</button>
    </a>
    """
    return href

 
def about_me():

    with st.container():

        # CSS styles file
        with open("styles/main.css") as f:
            st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        # Profile image file
        with open("data/profil.jpg", "rb") as img_file:
            img = "data:image/jpg;base64," + base64.b64encode(img_file.read()).decode()

        # PDF CV file
        with open("data/CV_DS_FR.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        st.subheader("Hi! Welcome to my portfolio :wave:")
        # st.title('About Me :)')
        
        

        leftcolumn, rightcolum = st.columns([1, 2])

        with leftcolumn:


            # Image (static and rounded) uncomment it if you prefer this one
            st.write(f"""
            <div style="display: flex; justify-content: center;">
            <img src="{img}" alt="KANE profil" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
            </div>
            """, unsafe_allow_html=True)

            # Subtitle
            st.write(f"""<div class="subtitle" style="text-align: center;">Data scientist</div>""", unsafe_allow_html=True)

            # Social Icons
            social_icons_data = {
                # Platform: [URL, Icon]
                # "Kaggle": ["https://www.kaggle.com/edomingo", "https://www.kaggle.com/static/images/site-logo.svg"],
                "LinkedIn": ["https://www.linkedin.com/in/kanemamadou/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
                "GitHub": ["https://github.com/MamadouKane", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
            }

            social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

            st.write(f"""
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                {''.join(social_icons_html)}
            </div>""", 
            unsafe_allow_html=True)


        with rightcolum:
            # Top title
            st.write(f"""<div class="title"><strong>My name is</strong> Mamadou KANE 😎</div>""", unsafe_allow_html=True)
            st.write("""
                - 🧑‍💻 With a Master's degree in Data Science and Artificial Intelligence, 
                     I have a solid theoretical and practical background in the development and production of Machine Learning and Deep Learning models. 
                     I have acquired skills in the manipulation of textual and auditory models, as well as in the management of large data pipelines. 
                - Enthusiastic and motivated, I'd like to put my knowledge at the service of innovative projects in Machine Learning, Artificial Intelligence and Generative AI. 
                - 📅 Available immediately
                
                - 🏠 France - Belgique
                """
            )

            st.write("--")


    # Download CV button
    st.markdown(get_pdf_download_link(pdf_bytes, "CV_DS_FR.pdf"), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # CV
    
    with st.container():
        _, col2, _ = st.columns([1,6,1])
        with col2:
            st.markdown(
                """
                <style>
                .stContainer > div {
                    width: 55%;
                    margin: auto;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            pdf_viewer("data/CV_DS_FR.pdf")
