import streamlit as st
from streamlit_lottie import st_lottie
import json, os
from PIL import Image
import base64


RAG=Image.open('data/rag.jpg')
# archi_language_detection_model = Image.open('data/language-detection.drawio.png')
# archi_scoring = Image.open('data/scoring_archi.png')

# Convert image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def projects():
    st.header("🚀 My Projects")
    st.write('---') 


    # ********************************************************** PROJECT 1 *************************************************************

    with st.container():     
        
        st.header("💬 RAG chat with your pdf")
        st.subheader("Overview")
        st.markdown("""
            ### 🤖 Chat with PDF locally using Ollama + LangChain

            A powerful local RAG (Retrieval Augmented Generation) application that lets you chat with your PDF documents using Ollama and LangChain. This project includes both a Jupyter notebook for experimentation and a Streamlit web interface for easy interaction.

            ### ✨ Features

            - 🔒 Fully local processing - no data leaves your machine
            - 📄 PDF processing with intelligent chunking
            - 🧠 Multi-query retrieval for better context understanding
            - 🎯 Advanced RAG implementation using LangChain
            - 🖥️ Clean Streamlit interface
            - 📓 Jupyter notebook for experimentation
        """)

        st.markdown('''<h6> <em>Tools : </h6>''',unsafe_allow_html=True)
        st.markdown("""
            ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
            ![Ollama](https://img.shields.io/badge/Ollama-red.svg?style=for-the-badge&logo=Ollama&logoColor=white)
            ![LLM](https://img.shields.io/badge/LLM-purpe.svg?style=for-the-badge&logo=LLM&logoColor=white)
            ![Jupyter](https://img.shields.io/badge/Jupyter-3670A0?style=for-the-badge&logo=Jupyter&logoColor=ffdd54)
            ![Chroma](https://img.shields.io/badge/Chroma-yellow.svg?style=for-the-badge&logo=Chroma&logoColor=white)
            ![Embedding model](https://img.shields.io/badge/Embedding%20model-ffdd54.svg?style=for-the-badge)
            ![Streamlit](https://img.shields.io/badge/Streamlit-black.svg?style=for-the-badge&logo=Streamlit&logoColor=red)
            ![LangChain](https://img.shields.io/badge/LangChain-blue.svg?style=for-the-badge&logo=LangChain&logoColor=ffdd54)
            
        """)

        # with st.container():
        # st.subheader("Project architecture")
        # st.image(archi_scoring) # , width=300

       
        with st.container():
            st.subheader("APP UI")
            # center image
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64('data/st_app_ui.png')}" alt="app UI" style="max-width: 95%; height: auto;">
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display: flex; justify-content: center; gap: 20px;">
                <a href="https://github.com/MamadouKane/RAG_chat_with_your_pdf" target="_blank">
                    <button style="padding:10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                        View code on GitHub
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )



    # ********************************************************** PROJECT 2 *************************************************************
    st.write('---')
    with st.container():     
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(RAG, width=300)
        with text_column:
            st.header("Prediction of bank loan defaults")
            st.subheader("Overview")
            st.markdown("""
                - Build a machine learning model that predicts whether a customer will default on the bank loan or not based on the characteristics provided.
                - That involves : Data Cleaning, Exploratory Data Analysis, Features Engineering, ML Classifications Models, Cross-validation, Optimization, Deployment. 
            """)

            st.markdown('''<h6> <em>Tools : </h6>''',unsafe_allow_html=True)
            st.markdown("""
                ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
                ![scikit Learn](https://img.shields.io/badge/scikit%20Learn-red.svg?style=for-the-badge&logo=scikit-Learn&logoColor=white)
                ![Pandas](https://img.shields.io/badge/Pandas-purpe.svg?style=for-the-badge&logo=Pandas&logoColor=white)
                ![Jupyter](https://img.shields.io/badge/Jupyter-3670A0?style=for-the-badge&logo=Jupyter&logoColor=ffdd54)
                ![Numpy](https://img.shields.io/badge/Numpy-yellow.svg?style=for-the-badge&logo=numpy&logoColor=white)
                ![Matplotlib](https://img.shields.io/badge/Matplotlib-ffdd54.svg?style=for-the-badge)
                ![Streamlit](https://img.shields.io/badge/Streamlit-black.svg?style=for-the-badge&logo=Streamlit&logoColor=red)
                ![joblib](https://img.shields.io/badge/joblib-white.svg?style=for-the-badge)
                       
            """)

            st.markdown(
                """
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <a href="https://github.com/MamadouKane/bank-loan-default/tree/main" target="_blank">
                        <button style="padding:10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                            View code on GitHub
                        </button>
                    </a>
                    <a href="https://bank-loan-default-mk.streamlit.app/" target="_blank">
                        <button style="padding:10px 20px; background-color: #28a745; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                            Visit the wep App
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

            
            
    # ********************************************************** PROJECT 3 *************************************************************
    st.write('---')
    with st.container():     
        
        st.header("Language detection model")
        st.subheader("Overview")
        st.markdown("""
            - Implementation of a machine learning model for text classification. The model takes text as input and predicts the language of the text. 
                With FastApi an API is created to use the model. The model supports 17 languages.
            - That involves : Data preprocessing, text vectorization, API creation, ML Model Deployment, containerization. 
        """)

        st.markdown('''<h6> <em>Tools : </h6>''',unsafe_allow_html=True)
        st.markdown("""
            ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
            ![scikit Learn](https://img.shields.io/badge/scikit%20Learn-red.svg?style=for-the-badge&logo=scikit-Learn&logoColor=white)
            ![Pandas](https://img.shields.io/badge/Pandas-purpe.svg?style=for-the-badge&logo=Pandas&logoColor=white)
            ![Jupyter](https://img.shields.io/badge/Jupyter-3670A0?style=for-the-badge&logo=Jupyter&logoColor=ffdd54)
            ![Numpy](https://img.shields.io/badge/Numpy-yellow.svg?style=for-the-badge&logo=numpy&logoColor=white)
            ![Matplotlib](https://img.shields.io/badge/Matplotlib-ffdd54.svg?style=for-the-badge)
            ![Docker](https://img.shields.io/badge/Docker-white.svg?style=for-the-badge&logo=Docker&logoColor=blue)
            ![Pickle](https://img.shields.io/badge/Pickle-pink.svg?style=for-the-badge)
            ![FastAPI](https://img.shields.io/badge/FastAPI-black.svg?style=for-the-badge&logo=FastAPI&logoColor=red)
            ![Seaborn](https://img.shields.io/badge/Seaborn-ffdd54.svg?style=for-the-badge)
            ![NLP](https://img.shields.io/badge/NLP-green.svg?style=for-the-badge)
        """)

        with st.container():
            st.subheader("Project architecture")
            # center image
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64('data/language-detection.drawio.png')}" alt="Architecture" style="max-width: 100%; height: auto;">
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display: flex; justify-content: center; gap: 20px;">
                <a href="https://github.com/MamadouKane/language-detection-model/tree/main" target="_blank">
                    <button style="padding:10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                        View code on GitHub
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )


        
    # ********************************************************** PROJECT 4 *************************************************************
    st.write('---')
    with st.container():     
        
        st.header("Credit score and customer segmentation")
        st.subheader("Overview")
        st.markdown("""
            - Credit scoring aims to determine the creditworthiness of individuals based on their credit profiles. 
                By analyzing factors such as payment history, credit utilization ratio, and number of credit accounts, 
                we can assign a credit score to each individual, providing a quantitative measure of their creditworthiness.
            - The process of calculating credit scores and segmenting customers based on their credit scores involves several steps. 
                Firstly, relevant data about borrowers is collected and organized. Then, using complex algorithms and statistical models, 
                the collected data is analyzed to generate credit scores for each borrower.
            - Once the credit scores are calculated, customers are segmented into different risk categories or credit tiers based on 
                predefined thresholds. This segmentation helps financial institutions assess the credit risk associated with each customer 
                and make informed decisions regarding loan approvals, interest rates, and credit limits. By categorizing customers into segments, 
                financial institutions can better manage their lending portfolios and effectively mitigate the risk of potential defaults.
        """)

        st.markdown('''<h6> <em>Tools : </h6>''',unsafe_allow_html=True)
        st.markdown("""
            ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
            ![scikit Learn](https://img.shields.io/badge/scikit%20Learn-red.svg?style=for-the-badge&logo=scikit-Learn&logoColor=white)
            ![Pandas](https://img.shields.io/badge/Pandas-purpe.svg?style=for-the-badge&logo=Pandas&logoColor=white)
            ![Jupyter](https://img.shields.io/badge/Jupyter-3670A0?style=for-the-badge&logo=Jupyter&logoColor=ffdd54)
            ![Numpy](https://img.shields.io/badge/Numpy-yellow.svg?style=for-the-badge&logo=numpy&logoColor=white)
            ![Matplotlib](https://img.shields.io/badge/Matplotlib-ffdd54.svg?style=for-the-badge)
            ![Streamlit](https://img.shields.io/badge/Streamlit-black.svg?style=for-the-badge&logo=Streamlit&logoColor=red)
            ![Clustering](https://img.shields.io/badge/Clustering-blue.svg?style=for-the-badge)
            ![Plotly](https://img.shields.io/badge/Plotly-green.svg?style=for-the-badge&logo=Plotly&logoColor=red)
        """)

        # with st.container():
        # st.subheader("Project architecture")
        # st.image(archi_scoring) # , width=300

       
        with st.container():
            st.subheader("Project architecture")
            # center image
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64('data/scoring_archi.png')}" alt="Architecture" style="max-width: 100%; height: auto;">
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display: flex; justify-content: center; gap: 20px;">
                <a href="https://github.com/MamadouKane/credit-scoring-customers-segmentation" target="_blank">
                    <button style="padding:10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                        View code on GitHub
                    </button>
                </a>
                <a href="https://credit-scoring-customers-segmentation.streamlit.app/" target="_blank">
                        <button style="padding:10px 20px; background-color: #28a745; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                            Visit the wep App
                        </button>
                    </a>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ********************************************************** PROJECT 5 *************************************************************
    st.write('---')
    with st.container():     
        
        st.header("End to end Data Engineering - Sales analysis")
        st.subheader("Overview")
        st.markdown("""
            - The use case for this project is building an end to end solution by ingesting the tables from on-premise SQL Server database 
                using Azure Data Factory and then store the data in Azure Data Lake.
            - Then Azure databricks is used to transform the RAW data to the most cleanest form of data 
                    and finally using Microsoft Power BI to build an interactive dashboard.
        """)

        st.markdown('''<h6> <em>Tools : </h6>''',unsafe_allow_html=True)
        st.markdown("""
            ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
            ![Pandas](https://img.shields.io/badge/Pandas-purpe.svg?style=for-the-badge&logo=Pandas&logoColor=white)
            ![Jupyter](https://img.shields.io/badge/Jupyter-3670A0?style=for-the-badge&logo=Jupyter&logoColor=ffdd54)
            ![Numpy](https://img.shields.io/badge/Numpy-yellow.svg?style=for-the-badge&logo=numpy&logoColor=white)
            ![Matplotlib](https://img.shields.io/badge/Matplotlib-red.svg?style=for-the-badge)
            ![Seaborn](https://img.shields.io/badge/Seaborn-ffdd54.svg?style=for-the-badge)
            ![Pyspark](https://img.shields.io/badge/Pyspark-3670A0?style=for-the-badge&logo=pache-Spark&logoColor=#E25A1C)
            ![Databricks](https://img.shields.io/badge/Databricks-orange?style=for-the-badge&logo=Databricks&logoColor=#E25A1C)
            ![Seaborn](https://img.shields.io/badge/Seaborn-ffdd54.svg?style=for-the-badge)
            ![Power BI](https://img.shields.io/badge/Power%20BI-white.svg?style=for-the-badge)
            ![SQL Server](https://img.shields.io/badge/SQL%20Server-black.svg?style=for-the-badge)
            ![MS AZURE](https://img.shields.io/badge/MS%20AZURE-red.svg?style=for-the-badge)
        """)

        with st.container():
            st.subheader("Dashboard")
            # center image
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64('data/dashboard.png')}" alt="Architecture" style="max-width: 90%; height: auto;">
                </div>
                """,
                unsafe_allow_html=True
            )

        with st.container():
            st.subheader("Project architecture")
            # center image
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64('data/sales_analysis_steps.png')}" alt="Architecture" style="max-width: 90%; height: auto;">
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display: flex; justify-content: center; gap: 20px;">
                <a href="https://github.com/MamadouKane/pizza_sales_analysis" target="_blank">
                    <button style="padding:10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                        View code on GitHub
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ********************************************************** PROJECT 6 *************************************************************
    st.write('---')
    with st.container():     
        
        st.header("AWS Football-API ETL pipeline")
        st.subheader("Overview")
        st.markdown("""
            - This project implements an ETL (Extract, Transform, Load) pipeline to fetch football data from the API Sports, 
                    transform it using Python, and then load it into a data lake on Amazon S3. 
                    The pipeline is orchestrated by Apache Airflow, deployed on an Amazon EC2 instance.
        """)

        st.markdown('''<h6> <em>Tools : </h6>''',unsafe_allow_html=True)
        st.markdown("""
            ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
            ![Pandas](https://img.shields.io/badge/Pandas-purpe.svg?style=for-the-badge&logo=Pandas&logoColor=white)
            ![Numpy](https://img.shields.io/badge/Numpy-yellow.svg?style=for-the-badge&logo=numpy&logoColor=white)
            ![Amazon S3](https://img.shields.io/badge/Amazon%20S3-black.svg?style=for-the-badge&logo=Amazon-S3&logoColor=red)
            ![Amazon EC2](https://img.shields.io/badge/Amazon%20EC2-white.svg?style=for-the-badge&logo=Amazon-EC2&logoColor=red)
            ![Apache airflow](https://img.shields.io/badge/Apache%20airflow-3670A0.svg?style=for-the-badge&logo=Apache-airflow&logoColor=white)
            
        """)

        with st.container():
            st.subheader("Project architecture")
            # center image
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64('data/archi_football_API.png')}" alt="Architecture" style="max-width: 100%; height: auto;">
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display: flex; justify-content: center; gap: 20px;">
                <a href="https://github.com/MamadouKane/AWS_Football-API_pipeline" target="_blank">
                    <button style="padding:10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                        View code on GitHub
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ***************************************** Others projects ***********************************************
    with st.container():
        st.write('---')
        st.markdown(
                """
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <a href="https://github.com/MamadouKane?tab=repositories" target="_blank">
                        <button style="padding:10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; font-size:16px; cursor:pointer;">
                            View the reste of my projects on GitHub
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
