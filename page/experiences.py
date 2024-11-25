import streamlit as st
from streamlit_lottie import st_lottie
import json, os
import base64


def lottie_file(filepath):
    with open(filepath, 'r',encoding='utf-8') as file:
        return json.load(file)

lottie_filepath= os.path.join('static', 'lottie.json')
research_filepath= os.path.join('static','research.json')


lottie_json= lottie_file(lottie_filepath)
resarch_json= lottie_file(research_filepath)

# Convert image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
   

def experiences():

    st.header('Professional Experience')
    with st.container():
        st.write('---')
        leftcolumn, rightcolum = st.columns([3,2])
        with leftcolumn:

            franfinance_logo_base64 = image_to_base64("data/logo_franfinance.png")  
            
            # Display aligned with HTML and CSS
            st.markdown(
                f"""
                <div style="display: flex; align-items: center;">
                    <img src="data:image/png;base64,{franfinance_logo_base64}" style="width: 90px; margin-right: 15px;">
                    <h2 style="color:#007DC5; margin: 0;">FRANFINANCE</h2>
                </div>
                """,
                unsafe_allow_html=True
            )
            # st.markdown("""<h2><span style ="color:#007DC5;">FRANFINANCE</span></h2> """, unsafe_allow_html=True)
            # st.write('####')
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('''<h6> <em>April 2024 - 30 September 2024</em></h6>''',unsafe_allow_html=True)
            st.markdown("""<h3><span style="color: #C0C0C0;">Role :</span> 
                        <span style="color: #94ffeb;">Data scientist</span></h3>""",unsafe_allow_html=True
            )
            st.markdown(
                '''  
                - Development of a predictive Deep Learning model for the recovery of bank loans.
                - This involves : Analysis of existing data (structured and unstructured). 
                  Processing millions of lines of data. Implementation of NLP techniques (Topic modeling). 
                  Building predictive model using Deep Learning. Model evaluation.
                - This allows the bank to prioritize and optimize its recovery strategies and enhances the ability to analyze large volumes of data, 
                  leading to more informed decision-making and reduced financial losses.
    
                '''
            )
            st.markdown("""<h3><span style="color: #C0C0C0;">Tools :</span></h3>""",unsafe_allow_html=True)

            # https://img.shields.io
            st.markdown("""
                ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
                ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
                ![Pytorch](https://img.shields.io/badge/pytorch-8A2BE2.svg?style=for-the-badge&logo=pytorch&logoColor=orange)
                ![LSTM](https://img.shields.io/badge/LSTM-black.svg?style=for-the-badge)
                ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-red.svg?style=for-the-badge)
                ![Neural Network](https://img.shields.io/badge/Neural%20Network-yellow.svg?style=for-the-badge)
                ![GitLab](https://img.shields.io/badge/GitLab-8A2BE2.svg?style=for-the-badge&logo=gitlab&logoColor=orange)
                ![MLFlow](https://img.shields.io/badge/MlFlow-red.svg?style=for-the-badge&logo=mlflow&logoColor=white)
                ![SAS](https://img.shields.io/badge/SAS-8A2BE2.svg?style=for-the-badge&logo=SAS&logoColor=white)
                ![SQL](https://img.shields.io/badge/SQL-fedcba.svg?style=for-the-badge&logo=SQL&logoColor=white)
                ![Polars](https://img.shields.io/badge/Polars-8A2BE2.svg?style=for-the-badge&logo=Polars&logoColor=white)
                ![Pandas](https://img.shields.io/badge/Pandas-purpe.svg?style=for-the-badge&logo=Pandas&logoColor=white)
                ![Jupyter](https://img.shields.io/badge/Jupyter-3670A0?style=for-the-badge&logo=Jupyter&logoColor=ffdd54)
                ![SCRUM agile method](https://img.shields.io/badge/SCRUM%20agile%20method-E34F26.svg?style=for-the-badge)
                ![NLP](https://img.shields.io/badge/NLP-marron.svg?style=for-the-badge)
                ![Spacy](https://img.shields.io/badge/Spacy-white.svg?style=for-the-badge&logo=Spacy&logoColor=blue)
                ![Time Series](https://img.shields.io/badge/Time%20Series-yellow.svg?style=for-the-badge)
            """)
        
        with rightcolum:
            st_lottie(lottie_json, speed=1, width=800, height=400, key="lottie_animation")

    st.write('---')    



    # ********************************************** 2 **************************************************************
    with st.container():
        leftcolumn, rightcolum = st.columns(2)
        with leftcolumn:
            
            franfinance_logo_base64 = image_to_base64("data/logo_MSN.png")  
            
            # Display Center
            st.markdown(
                f"""
                <div style="display: flex; align-items: center;">
                    <img src="data:image/png;base64,{franfinance_logo_base64}" style="width: 200px; margin-right: 15px;">
                    <h2 style="color:#007DC5; margin: 0;">LaMSN</h2>
                </div>
                """,
                unsafe_allow_html=True
            )
           
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('''<h6> <em>May 2022 -  July 2022</em></h6>''',unsafe_allow_html=True)
            st.markdown("""<h3><span style="color: #C0C0C0;">Role :</span> 
                        <span style="color: #94ffeb;">Developper | Robotics programming</span></h3>""",unsafe_allow_html=True
            )
            st.markdown(
                '''  
                - Program the movement of a robotic arm which will help gain precision in carpal tunnel surgery.
                - In collaboration with a surgeon and M2 data scientist students.  
                - The robot is equipped with a camera. With this camera, ML techniques are applied to target areas. 
                    The coordinates under the three XYZ axes of these zones and the characteristics of the robot's rotary motor are used 
                    to calculate the number of rotations required of the cylinder along each axis to reach these zones. 
                '''
            )
            st.markdown("""<h3><span style="color: #C0C0C0;">Tools :</span></h3>""",unsafe_allow_html=True)
            st.markdown("""
                ![Arduino](https://img.shields.io/badge/Arduino-3670A0?style=for-the-badge&logo=Arduino&logoColor=ffdd54)
                ![C](https://img.shields.io/badge/C-3670A0?style=for-the-badge&logo=C&logoColor=ffdd54)
                ![Mechanics](https://img.shields.io/badge/Mechanics-FF4B4B.svg?style=for-the-badge&logo=mechanics&logoColor=white)
                ![Git](https://img.shields.io/badge/Git-black.svg?style=for-the-badge&logo=Git&logoColor=white)
                ![SCRUM agile method](https://img.shields.io/badge/SCRUM%20agile%20method-E34F26.svg?style=for-the-badge)
                ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
                  
            """)

            with rightcolum:
                st_lottie(resarch_json, speed=1, width=800, height=400, key="research_animation")
