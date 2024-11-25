import streamlit as st
import base64
from streamlit_pdf_viewer import pdf_viewer


# Convert  PDF file to base64
def get_pdf_download_link(pdf_bytes, filename):
    b64 = base64.b64encode(pdf_bytes).decode()  # Encode le fichier en base64
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
        with open("data/profil.png", "rb") as img_file:
            img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

        # PDF CV file
        with open("data/CV_DS1.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        st.subheader("Hi! Welcome to my portfolio :wave:")
        st.title('About Me :)')
        
        # Top title
        st.write(f"""<div class="title"><strong>My name is</strong> Mamadou KANE👋</div>""", unsafe_allow_html=True)

        # Image (static and rounded) uncomment it if you prefer this one
        st.write(f"""
        <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="KANE profil" width="500" height="500" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
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

        # st.write("##")

        # About me section
        # st.subheader("About Me")
        st.write("""
            - 🧑‍💻 I am passionate about technology and always eager to adapt to its advancements. 
                I hold a ***Master's degree in Data Exploration and Decision Making***, with strong skills in ***Machine Learning, Deep Learning, 
                and Business Intelligence***. This background allows me to be a valuable asset to any company.

            - I am looking to continue my career in the data field, particularly as a data scientist.

            - Currently, I am seeking a permanent (CDI) or fixed-term (CDD) contract position to bring my projects to life and contribute my skills to your organization. 
            If you’re looking for a motivated and adaptable professional, feel free to reach out!
            
            - 🏠 France - Belgique
            - 🌏 Languages : 
                - French : Native
                - English : Professional 
            """
        )

        st.write("--")

        # # Download CV button
        # st.download_button(
        #     label="📄 Download my CV",
        #     data=pdf_bytes,
        #     file_name="CV_DS1.pdf",
        #     mime="application/pdf",
        # )

        # Download CV button
        st.markdown(get_pdf_download_link(pdf_bytes, "CV_DS1.pdf"), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # CV
        with st.container():
            col1, col2,col3 = st.columns([1,8,1])
            with col2:
                pdf_viewer("data/CV_DS1.pdf")
