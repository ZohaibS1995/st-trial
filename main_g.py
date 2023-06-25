#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 5/31/2023 1:52 PM
# @Author : Yi Chen
# @File : Main_page.py

import streamlit as st
import time
import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import os
from datetime import datetime 


import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# INSERT YOUR CODE 



# 创建计时器
#start_time = st.empty()
#elapsed_time = st.empty()
#
# if start_time.button("开始计时"):
#     start = time.time()
#     while True:
#         elapsed = time.time() - start
#         elapsed_time.text(f"已过时间: {elapsed:.2f} 秒")

path_clinical_data = r"./trial/clinical_variables.csv"
path_orig_images = r"./trial/test_set_selected_original/"
path_reconstructed = r"./trial/counterfactual_reconstructed_image/"
path_counterfactual = r"./trial/counterfactual/"
path_preprocessed = r"./trial/test_set_selected_preprocessed/"
path_model_prediction = r"./trial/model_predicted_result.csv"
path_global_explanation = r"./trial/global_lrp.png"
path_lrp_local = r"./trial/local LRP/"

st_file_name = "default"


def plus_one():
    #st.session_state.page_no = 1
    st.session_state.time_taken[st.session_state.image_names[st.session_state.id]] = "{}".format(datetime.now() - st.session_state.start_time)

    if st.session_state.id < len(st.session_state.image_names):
        st.session_state.id += 1
        st.session_state.pred_mod_page1 = False
    if st.session_state.id == len(st.session_state.image_names):
        st.session_state.page_no = 7
    return

def plus_one_ai():
    #st.session_state.page_no = 1
    st.session_state.time_taken[st.session_state.image_names[st.session_state.id]] = "{}".format(datetime.now() - st.session_state.start_time)

    if st.session_state.id < len(st.session_state.image_names):
        st.session_state.id += 1
        st.session_state.pred_mod_page1 = False
    if st.session_state.id == len(st.session_state.image_names):
        st.session_state.page_no = 8
    return

def plus_one_ai_exp():
    #st.session_state.page_no = 1
    st.session_state.time_taken[st.session_state.image_names[st.session_state.id]] = "{}".format(datetime.now() - st.session_state.start_time)

    if st.session_state.id < len(st.session_state.image_names):
        st.session_state.id += 1
        st.session_state.pred_mod_page1 = False
    if st.session_state.id == len(st.session_state.image_names):
        st.session_state.page_no = 9
    return

def plus_one_u():
    st.session_state.time_taken[st.session_state.image_names[st.session_state.id]] = "{}".format(datetime.now() - st.session_state.start_time)

    st.session_state.page_no = 1
    if st.session_state.id < 6: #len(st.session_state.image_names) - 1 :
        st.session_state.id += 1
        st.session_state.pred_mod_page1 = False
    if st.session_state.id == 6: #len(st.session_state.image_names) - 1:
        st.session_state.page_no = 10
    return

def plus_one_cu():
    st.session_state.page_no = 7
    return

def question_page():
    st.session_state.page_no = 5
    return

def minus_one():
    if st.session_state.id > 0:
        st.session_state.id -= 1
        st.session_state.pred_mod_page1 = False
    return

def explainability_disp():
    st.session_state.page_no = 4
    return

def explainability_disp_t():
    st.session_state.page_no = 6

def back_return_u():
    st.session_state.page_no = 1

def back_return_t():
    st.session_state.page_no = 3

def sel_usability():
    st.session_state.start_time = datetime.now() 
    st.session_state.page_no = 1

def sel_ai_trial():
    st.session_state.start_time = datetime.now() 
    st.session_state.page_no = 2

def sel_ai_exp_trial():
    st.session_state.start_time = datetime.now() 
    st.session_state.page_no = 3

def go_to_landing_page():
    if st.session_state["name"] == "" or st.session_state["nationality"] == "" or st.session_state["hospital"] == "" or st.session_state["department"] == "" or st.session_state["years_of_experience"] == "" or st.session_state["speciality"] == "":
        st.session_state.page_no = -1
        st.session_state.required_flag = True  
    else:
        st.session_state.page_no = 0
        st.session_state.name_user = st.session_state.name
        st.session_state.nationality_user = st.session_state.nationality
        st.session_state.hospital_user = st.session_state.hospital
        st.session_state.department_user = st.session_state.department
        st.session_state.years_of_experience_user = st.session_state.years_of_experience
        st.session_state.speciality_user = st.session_state.speciality
        st.session_state.required_flag = False
    return  


# info  
def info_page():
    st.session_state.page_no = -1

    col1, col2, col3 = st.columns([2, 4, 2])

    with col2: 
        st.title("*In silico* Clinical and Usability Trial")
        st.subheader("Enter Details Below")
        with st.form("form1"):
            st.text_input("Full Name", key="name")
            st.text_input("Nationality", key = "nationality")
            st.text_input("Hospital", key = "hospital")
            st.text_input("Department", key = "department")
            st.text_input("Years of Working Experience", key = "years_of_experience")
            st.text_input("Speciality", key= "speciality")
            st.form_submit_button("Submit", on_click=go_to_landing_page)
    
        if st.session_state.required_flag:
            st.write("**:red[Please fill all the fields]**")
    

# this is the landing page
def landing_page():

    st.markdown("<h1 style='text-align: center;'>"
                "Post-Hepatectomy Liver Failure Prediction Based on 2D-SWE images and Clinical Variables with"
                " an Interpretable Deep Learning Framework"
                "</h1>", unsafe_allow_html=True)

    
    st.markdown("<h4 style='text-align: center;color: red;'>"
                    "The Timer will start when you click the button."
                    "</h4>", unsafe_allow_html=True)


    st.markdown("""<style>
                    div[class*="stButton"] > label > div[data-testid="stMarkdownContainer"] > p {
                        font-size: 32px;
                    }
                        </style>
                """, unsafe_allow_html=True)
    
    
    st.markdown("""
     <style>
     div.stButton > button:first-child {
        font-size:28px !important;
        margin: auto;
        display: block;
        height: 2em; 
        width: 20em; }
         </style>""", unsafe_allow_html=True)
    
    st.markdown(
                """<style>
            div[class*="stButton"] > button > div[data-testid="stMarkdownContainer"] > p {
                font-size: 28px;
                margin: auto;
                display: block;
                height: 2em; 
                width: 20em;
            }
                </style>
                """, unsafe_allow_html=True)

    button1 = st.button("Usability test", on_click=sel_usability, key="s_u")
    button2 = st.button("Clinical trial: only AI", on_click = sel_ai_trial, key="s_a")
    button3 = st.button("Clinical trial: AI+explanation", on_click= sel_ai_exp_trial, key="s_ex_a")


    col1, col2, col3 = st.columns([2, 4, 2])

    with col2:   
        video_file = open('./video_instructions.mp4', 'rb')
        video_bytes = video_file.read()
    
        st.markdown("<h2 style='text-align: center;'>"
                    "Please go through the video before you begin the trial"
                    "</h2>", unsafe_allow_html=True)
        st.video(video_bytes)

    return 


def pred_mod():
    st.session_state.pred_mod_page1 = True
    return

def usability_page():
    st.markdown(
        """<style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 24px;
    }
        </style>
        """, unsafe_allow_html=True)

    st.markdown(
        """<style>
    div[class*="stRadio"] {
        background-color: #FEA09A;
        border: 3px solid;
    }
        </style>
        """, unsafe_allow_html=True)  

    st.session_state.page_no = 1

    st.write("## Usability Trial: " + str(st.session_state.id+1) + "/6")

    st.write("---")

    col1, col2 = st.columns([4, 5])


    with col1:
        st.write("**Top: SWE Image, Bottom: B-mode Ultrasound**")
        image = Image.open(path_orig_images + "{:03d}".format(int(st.session_state.u_name[st.session_state.id])) + ".png")
        st.image(image)


    with col2:
        df = pd.read_csv(path_clinical_data)
        keys_n = list(df.columns)[2:]
        val_w_k = list(df.iloc[st.session_state.u_id[st.session_state.id], 2:].to_numpy())

        np_v = np.vstack((keys_n, val_w_k)).transpose()
                        
        v_df = pd.DataFrame(np_v, columns = ["Clinical Variable", "Value"])
        st.table(v_df)
        st.write("##### For explanation of clinical variables, click [here](https://docs.google.com/spreadsheets/d/13gx5gZnqBapxq4_5cgQXWx8jH5iJiPTq/edit?usp=sharing&ouid=109860958973286366025&rtpof=true&sd=true)")

    df_pred = pd.read_csv(path_model_prediction, delimiter = ";")

    if  not st.session_state.pred_mod_page1:
        st.markdown('<p class="big-font"> Press the button to reveal the model prediction</p>', unsafe_allow_html=True)

    st.button("1- Model Prediction Results of PHLF Risk", on_click=pred_mod, key="disp_pred_mod")

    if  st.session_state.pred_mod_page1:
            val_w_k = df_pred.iloc[st.session_state.u_id[st.session_state.id], 1:].to_numpy()
            st.markdown("#### The AI model prediction is :red["+ str(val_w_k[0])+ "] with a probability of :red["+ str(val_w_k[1])+ "]")

    explainability_page = st.button("2- Explainability", on_click=explainability_disp, key="exp_page")

    col1, col2, col3 = st.columns([4,4,4])

    with col1:
        st.radio("3- Select your prediction of PHLF Risk", ("High risk of PHLF", "low risk of PHLF"), key="u_pred")

    st.session_state.usability_pred["{:03d}".format(int(st.session_state.u_name[st.session_state.id])) + ".png"] = st.session_state.u_pred

    col1, col2, col3 = st.columns([1,7,1])

    with col1:
        button_back = st.button("Back", on_click=minus_one, key="minus_one")
    with col3:
        button_next = st.button("Next", on_click=question_page, key="q_page")
    return

def ai_trial():
    st.markdown(
        """<style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 24px;
    }
        </style>
        """, unsafe_allow_html=True)

    st.markdown(
        """<style>
    div[class*="stRadio"] {
        background-color: #FEA09A;
        border: 3px solid;
    }
        </style>
        """, unsafe_allow_html=True)  

    st.session_state.page_no = 2

    st.write("## AI + Clinicians Trial: " + str(st.session_state.id+1) + "/" + str(len(st.session_state.image_names)))
    st.write("---")


    col1, col2 = st.columns([4, 5])


    with col1:
        st.write("**Top: SWE Image, Bottom: B-mode Ultrasound**")
        image = Image.open(path_orig_images + st.session_state.image_names[st.session_state.id])
        st.image(image)


    with col2:
        df = pd.read_csv(path_clinical_data)
        keys_n = list(df.columns)[2:]
        val_w_k = list(df.iloc[st.session_state.id, 2:].to_numpy())

        np_v = np.vstack((keys_n, val_w_k)).transpose()
                        
        v_df = pd.DataFrame(np_v, columns = ["Clinical Variable", "Value"])
        st.table(v_df)
        st.write("##### For explanation of clinical variables, click [here](https://docs.google.com/spreadsheets/d/13gx5gZnqBapxq4_5cgQXWx8jH5iJiPTq/edit?usp=sharing&ouid=109860958973286366025&rtpof=true&sd=true)")

    df_pred = pd.read_csv(path_model_prediction, delimiter = ";")

    if  not st.session_state.pred_mod_page1:
        st.markdown('<p class="big-font"> Press the button to reveal the model prediction</p>', unsafe_allow_html=True)

    st.button("1- Model Prediction Results of PHLF Risk", on_click=pred_mod, key="disp_pred_mod")

    if  st.session_state.pred_mod_page1:
            val_w_k = df_pred.iloc[st.session_state.id, 1:].to_numpy()
            st.markdown("#### The AI model prediction is :red["+ str(val_w_k[0])+ "] with a probability of :red["+ str(val_w_k[1])+ "]")

    col1, col2, col3 = st.columns([4,4,4])

    with col1:
        st.radio("2- Select your prediction of PHLF Risk", ("High risk of PHLF", "low risk of PHLF"), key="ai_pred")

    st.session_state.ai_trial[st.session_state.image_names[st.session_state.id]] = st.session_state.ai_pred

    col1, col2, col3 = st.columns([1,7,1])

    with col1:
        button_back = st.button("Back", on_click=minus_one, key="minus_one")
    with col3:
        button_next = st.button("Next", on_click=plus_one_ai, key="plus_one_ai")
    return   

def ai_trial_explanations():
    st.markdown(
        """<style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 24px;
    }
        </style>
        """, unsafe_allow_html=True)

    st.markdown(
        """<style>
    div[class*="stRadio"] {
        background-color: #FEA09A;
        border: 3px solid;
    }
        </style>
        """, unsafe_allow_html=True)  
    st.session_state.page_no = 3

    st.write("## AI + Clinicians + Explanations Trial: " + str(st.session_state.id+1) + "/" + str(len(st.session_state.image_names)))
    st.write("---")


    #st.write("---")

    col1, col2 = st.columns([4, 5])


    with col1:
        st.write("**Top: SWE Image, Bottom: B-mode Ultrasound**")
        image = Image.open(path_orig_images + st.session_state.image_names[st.session_state.id])
        st.image(image)


    with col2:
        df = pd.read_csv(path_clinical_data)
        keys_n = list(df.columns)[2:]
        val_w_k = list(df.iloc[st.session_state.id, 2:].to_numpy())

        np_v = np.vstack((keys_n, val_w_k)).transpose()
                        
        v_df = pd.DataFrame(np_v, columns = ["Clinical Variable", "Value"])
        st.table(v_df)
        st.write("##### For explanation of clinical variables, click [here](https://docs.google.com/spreadsheets/d/13gx5gZnqBapxq4_5cgQXWx8jH5iJiPTq/edit?usp=sharing&ouid=109860958973286366025&rtpof=true&sd=true)")
      
    df_pred = pd.read_csv(path_model_prediction, delimiter = ";")

    if  not st.session_state.pred_mod_page1:
        st.markdown('<p class="big-font"> Press the button to reveal the model prediction</p>', unsafe_allow_html=True)

    st.button("1- Model Prediction Results of PHLF Risk", on_click=pred_mod, key="disp_pred_mod")

    if  st.session_state.pred_mod_page1:
            val_w_k = df_pred.iloc[st.session_state.id, 1:].to_numpy()
            st.markdown("#### The AI model prediction is :red["+ str(val_w_k[0])+ "] with a probability of :red["+ str(val_w_k[1])+ "]")

    explainability_page = st.button("2- Explainability", on_click=explainability_disp_t, key="exp_page")

    col1, col2, col3 = st.columns([4,4,4])

    with col1:
        st.radio("3- Select your prediction of PHLF Risk", ("High risk of PHLF", "low risk of PHLF"), key="ai_exp_pred")

    st.session_state.ai_exp_trial[st.session_state.image_names[st.session_state.id]] = st.session_state.ai_exp_pred
    
    col1, col2, col3 = st.columns([1,7,1])

    with col1:
        button_back = st.button("Back", on_click=minus_one, key="minus_one")
    with col3:
        button_next = st.button("Next", on_click=plus_one_ai_exp, key="plus_one_ai_exp")
    return   


# Making an explainability page
def explainability_page():
    st.title("")
    st.session_state.page_no = 4

    df_pred = pd.read_csv(path_model_prediction, delimiter = ";")
    val_w_k = df_pred.iloc[st.session_state.id, 1:].to_numpy()
    prob = float(val_w_k[1].replace(",","."))

    st.markdown('#### :red[Counterfactual Explanations]')
    st.write("##### For explanation of counterfactual explanation, click [here](https://docs.google.com/presentation/d/1pPZoBA3QWArKC7oc7V4kX2BAXzOMo1gG/edit?usp=drive_link&ouid=113189205428208347942&rtpof=true&sd=true)")
    st.write("##### Model Predicted Probability: :red[", str(prob) +"]")
    col1, col2, col3 = st.columns([5, 5, 5])
    with col1:
        st.write("**Preprocessed Image**")
        image = Image.open(path_preprocessed + "{:03d}".format(int(st.session_state.u_name[st.session_state.id])) + ".png")
        image = image.resize((224,224))
        st.image(image)

    with col2:
        st.write("**Reconstructed Image**")
        image = Image.open(path_reconstructed + "{:03d}".format(int(st.session_state.u_name[st.session_state.id])) + ".png")
        image = image.resize((224,224))
        st.image(image)

    col1, col2, col3 = st.columns([5, 3, 3])
    with col1:
        st.write("**Counterfactual Image**")
        image = Image.open(os.path.join(path_counterfactual + "{:03d}".format(int(st.session_state.u_name[st.session_state.id])),
                                         "0_" + str(int(st.session_state.counterfactual_slider*10)) + ".png"))
        image = image.resize((224,224))
        st.image(image)

    col1, col2, col3 = st.columns([1.5, 5, 5])

    with col1:
        val = st.slider('Select the Counterfactual Probability:', min_value = 0.1, max_value = 0.9, step = 0.1, key="counterfactual_slider")

    st.markdown('#### :red[Layerwise Relevance Propagation (LRP) Explanations]')
    st.write("##### For explanation of layerwise relevance propagation, click [here](https://docs.google.com/presentation/d/1YsvnZTJrwaKeMW1JDVaciEuYttMb9ysv/edit?usp=drive_link&ouid=113189205428208347942&rtpof=true&sd=true)")

    col1, col2 = st.columns([4.5, 5])
    with col1:
        st.write("**Global Explanation**")
        image = Image.open(path_global_explanation)
        st.image(image)

    with col2:
        st.write("**Local Explanation**")
        image = Image.open(path_lrp_local + "{:03d}".format(int(st.session_state.u_name[st.session_state.id])) + ".png")
        st.image(image)

    st.write("##### For explanation of clinical variables, click [here](https://docs.google.com/spreadsheets/d/13gx5gZnqBapxq4_5cgQXWx8jH5iJiPTq/edit?usp=sharing&ouid=109860958973286366025&rtpof=true&sd=true)")
    
    button_back_page = st.button("Back", on_click=back_return_u, key="r_back")

    return 


# Making an explainability page
def explainability_page_trial():
    st.title("")
    st.session_state.page_no = 6

    df_pred = pd.read_csv(path_model_prediction, delimiter = ";")
    val_w_k = df_pred.iloc[st.session_state.id, 1:].to_numpy()
    prob = float(val_w_k[1].replace(",","."))

    st.markdown('#### :red[Counterfactual Explanations]')
    st.write("##### For explanation of counterfactual explanation, click [here](https://docs.google.com/presentation/d/1pPZoBA3QWArKC7oc7V4kX2BAXzOMo1gG/edit?usp=drive_link&ouid=113189205428208347942&rtpof=true&sd=true)")
    st.write("##### Model Predicted Probability: :red[", str(prob) +"]")
    col1, col2, col3 = st.columns([5, 5, 5])
    with col1:
        st.write("**Preprocessed Image**")
        image = Image.open(path_preprocessed + st.session_state.image_names[st.session_state.id])
        image = image.resize((224,224))
        st.image(image)

    with col2:
        st.write("**Reconstructed Image**")
        image = Image.open(path_reconstructed + st.session_state.image_names[st.session_state.id])
        image = image.resize((224,224))
        st.image(image)

    col1, col2, col3 = st.columns([5, 3, 3])
    with col1:
        st.write("**Counterfactual Image**")
        image = Image.open(os.path.join(path_counterfactual + st.session_state.image_names[st.session_state.id].split(".")[0],
                                         "0_" + str(int(st.session_state.counterfactual_slider*10)) + ".png"))
        image = image.resize((224,224))
        st.image(image)

    col1, col2, col3 = st.columns([1.5, 5, 5])

    with col1:
        val = st.slider('Select the Counterfactual Probability:', min_value = 0.1, max_value = 0.9, step = 0.1, key="counterfactual_slider")

    st.markdown('#### :red[Layerwise Relevance Propagation (LRP) Explanations]')
    st.write("##### For explanation of layerwise relevance propagation, click [here](https://docs.google.com/presentation/d/1YsvnZTJrwaKeMW1JDVaciEuYttMb9ysv/edit?usp=drive_link&ouid=113189205428208347942&rtpof=true&sd=true)")

    col1, col2 = st.columns([4.5, 5])
    with col1:
        st.write("**Global Explanation**")
        image = Image.open(path_global_explanation)
        st.image(image)

    with col2:
        st.write("**Local Explanation**")
        image = Image.open(path_lrp_local + st.session_state.image_names[st.session_state.id])
        st.image(image)

    st.write("##### For explanation of clinical variables, click [here](https://docs.google.com/spreadsheets/d/13gx5gZnqBapxq4_5cgQXWx8jH5iJiPTq/edit?usp=sharing&ouid=109860958973286366025&rtpof=true&sd=true)")
    
    button_back_page = st.button("Back", on_click=back_return_t, key="r_back_t")

    return 

def usability_questionaire():
    st.title("")
    st.session_state.page_no = 5
    st.markdown ("### Questionnaire: Counterfactual Explanation")
    st.markdown(
        """
        <style>
        .radio-group > * {
            display: inline-block;
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Block1
    st.markdown('**1. Strongly disagree 2. Disagree 3. Neither agree nor disagree 4. Agree 5. Strongly agree**')
    with st.container():
        st.markdown("**1. Understandability:**")
        option1 = st.radio("I understand how the AI system made the above assessment for PHLF",
                        ("1", "2", "3", "4", "5"), key="radio1", horizontal=True)

    # Block2
    with st.container():
        st.markdown("**2. Classifier’s decision justification:**")

        option2 = st.radio("The changes in the video are related to PHLF", ("1", "2", "3", "4", "5"), key="radio2"
                        , horizontal=True)

    # Block3
    with st.container():
        st.markdown("**3. Visual quality:**")
        option3 = st.radio("Images in the video look like SWE images", ("1", "2", "3", "4", "5"), key="radio3"
                        , horizontal=True)

    # Block4
    with st.container():
        st.markdown("**4. Helpfulness:**")
        option4 = st.radio("The explanation helped me understand the assessment made by the AI system: ",
                        ("1", "2", "3", "4", "5"), key="radio4", horizontal=True)

    # Block5
    with st.container():
        st.markdown("**5. Confidence:**")

        option5 = st.radio("I feel more confident on the model with the explanation:", ("1", "2", "3", "4", "5"),
                        key="radio5", horizontal=True)

        

    st.markdown ("### Questionnaire: LayerWise Relevance Propagation")
    st.markdown(
        """
        <style>
        .radio-group > * {
            display: inline-block;
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Block1
    st.markdown('**1. Strongly disagree 2. Disagree 3. Neither agree nor disagree 4. Agree 5. Strongly agree**')
    with st.container():
        st.markdown("**1. Understandability:**")
        optionl1 = st.radio("I understand which features influence the prediction and how they influence",
                        ("1", "2", "3", "4", "5"), key="radiol1", horizontal=True)

    # Block2
    with st.container():
        st.markdown("**2. Classifier’s decision justification:**")

        optionl2 = st.radio("The feature's contribution are reasonably related to PHLF", ("1", "2", "3", "4", "5"), key="radiol2"
                        , horizontal=True)

    # Block3
    with st.container():
        st.markdown("**3. Helpfulness:**")
        optionl3 = st.radio("The explanation helped me understand the assessment made by the AI system", ("1", "2", "3", "4", "5"), key="radiol3"
                        , horizontal=True)

    # Block4
    with st.container():
        st.markdown("**4. Confidence:**")
        optionl4 = st.radio("I feel more confident on the model with the explanation",
                        ("1", "2", "3", "4", "5"), key="radiol4", horizontal=True)



    col1, col2, col3 = st.columns([1,7,1])

    st.session_state.usability_questionaire[st.session_state.image_names[st.session_state.id]] = [st.session_state.radio1, st.session_state.radio2, st.session_state.radio3, st.session_state.radio4, st.session_state.radio5,
                                                                                                  st.session_state.radiol1, st.session_state.radiol2, st.session_state.radiol3, st.session_state.radiol4]

    with col3:
        button_next = st.button("Next", on_click=plus_one_u, key="add_one_u")

    return 




def system_causability_scale():
    st.title("")
    st.session_state.page_no = 10
    st.markdown ("## Questionnaire about the Interpretability System")
    st.markdown(
        """
        <style>
        .radio-group > * {
            display: inline-block;
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Block1
    st.markdown('**1. Strongly disagree 2. Disagree 3. Neither agree nor disagree 4. Agree 5. Strongly agree**')
    with st.container():
        option1 = st.radio("1. I found that the data included all relevant known causal factors with sufficient precision and granularity",
                        ("1", "2", "3", "4", "5"), key="radio1", horizontal=True)

    # Block2
    with st.container():
        option2 = st.radio("2. I understood the explanations within the context of my work.", ("1", "2", "3", "4", "5"), key="radio2"
                        , horizontal=True)

    # Block3
    with st.container():
        option3 = st.radio("3. I could change the level of detail on demand.", ("1", "2", "3", "4", "5"), key="radio3"
                        , horizontal=True)

    # Block4
    with st.container():
        option4 = st.radio("4. I did not need support to understand the explanations.",
                        ("1", "2", "3", "4", "5"), key="radio4", horizontal=True)

    # Block5
    with st.container():
        option5 = st.radio("5. I found the explanations helped me to understand causality", ("1", "2", "3", "4", "5"),
                        key="radio5", horizontal=True)

        
    # Block6
    with st.container():
        optionl1 = st.radio("6. I was able to use the explanations with my knowledge base.",
                        ("1", "2", "3", "4", "5"), key="radiol1", horizontal=True)

    # Block7
    with st.container():
        optionl2 = st.radio("7. I did not find inconsistencies between explanations", ("1", "2", "3", "4", "5"), key="radiol2"
                        , horizontal=True)

    # Block8
    with st.container():
        optionl3 = st.radio("8. I think that most people would learn to understand the explanations very quickly", ("1", "2", "3", "4", "5"), key="radiol3"
                        , horizontal=True)

    # Block9
    with st.container():
        optionl4 = st.radio("9. I did not need more references in the explanations: e.g., medical guidelines, regulations.",
                        ("1", "2", "3", "4", "5"), key="radiol4", horizontal=True)

    # Block10
    with st.container():
        optionl5 = st.radio("10. I received the explanations in a timely and efficient manner.",
                        ("1", "2", "3", "4", "5"), key="radiol5", horizontal=True)

    col1, col2, col3 = st.columns([1,7,1])

    st.session_state.causability_questionaire[st.session_state.image_names[st.session_state.id]] = [st.session_state.radio1, st.session_state.radio2, st.session_state.radio3, st.session_state.radio4, st.session_state.radio5,
                                                                                                  st.session_state.radiol1, st.session_state.radiol2, st.session_state.radiol3, st.session_state.radiol4, st.session_state.radiol5]

    with col3:
        button_next = st.button("Next", on_click=plus_one_cu, key="add_one_cu")

    return 

def go_home():

    #for key,val in st.session_state.items():
    #    del st.session_state[key]
    st.session_state.id = 0
    st.session_state.page_no = 0
    return 

def final_page_u():
    st.markdown("<h1 style='text-align: center;'>"
            "You finished the Trial!"
            "</h1>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>"
            "Thank you for the participation!"
            "</h1>", unsafe_allow_html=True)
    
    
    st.markdown("<h1 style='text-align: center;'>"
            "Press the home button to go the home page."
            "</h1>", unsafe_allow_html=True)
    

    # Usability Prediction
    keys_t = list(st.session_state.usability_pred.keys())
    values_t = list(st.session_state.usability_pred.values())

    dict_usability = {}
    
    for idx, val in enumerate(keys_t):
        dict_usability[str(val)] = str(values_t[idx])

    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("usability_prediction_results")
    doc_ref.set(dict_usability)

    # Usability Questionaire results
    values_t = list(st.session_state.usability_questionaire.values())
    keys_t = list(st.session_state.usability_pred.keys())
    #keys_t = [str(x) for x in range(len(values_t))]

    dict_trial_questionaire = {}
    
    for idx, val in enumerate(keys_t):
        dict_trial_questionaire[str(val)] = str(values_t[idx])

    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("usability_trial_questionaire")
    doc_ref.set(dict_trial_questionaire)



    # Causability Questionaire results
    values_t = list(st.session_state.causability_questionaire.values())
    keys_t = [str(x) for x in range(len(values_t))]

    dict_causability_questionaire = {}
    
    for idx, val in enumerate(keys_t):
        dict_causability_questionaire[str(val)] = str(values_t[idx])

    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("causability_questionaire")
    doc_ref.set(dict_causability_questionaire)

    # Time taken 

    values_t = list(st.session_state.time_taken.values())
    keys_t = list(st.session_state.usability_pred.keys())
    dict_time = {}
    
    for idx, val in enumerate(keys_t):
        dict_time[str(val)] = str(values_t[idx])
    
    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("usability_trial_time")
    doc_ref.set(dict_time)

    # Saving profile information
    values_t = [
        st.session_state.name_user,
        st.session_state.nationality_user,
        st.session_state.hospital_user,
        st.session_state.department_user, 
        st.session_state.years_of_experience_user,
        st.session_state.speciality_user
    ]
    keys_t = [
        "user_name",
        "nationality_user",
        "hospital_user",
        "department_user",
        "years of experience user",
        "user speciality"
    ]

    dict_profile = {}
    
    for idx, val in enumerate(keys_t):
        dict_profile[str(val)] = str(values_t[idx])
    
    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("usability_profile")
    doc_ref.set(dict_profile)

    col1, col2, col3 , col4, col5, col6 = st.columns([1,1,1,1,1,1])
    with col4:
        button_home = st.button("Home", on_click=go_home, key="go_h")


def final_page_a():
    st.markdown("<h1 style='text-align: center;'>"
            "You finished the Trial!"
            "Press the home button to go the home page."
            "</h1>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>"
            "Thank you for the participation!"
            "</h1>", unsafe_allow_html=True)
    
    
    st.markdown("<h1 style='text-align: center;'>"
            "Press the home button to go the home page."
            "</h1>", unsafe_allow_html=True)
    
    # AI Prediction
    keys_t = list(st.session_state.image_names)
    values_t = list(st.session_state.ai_trial.values())

    dict_ai_trial_pred = {}
    
    for idx, val in enumerate(keys_t):
        dict_ai_trial_pred[str(val)] = str(values_t[idx])

    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("ai_trial_results")
    doc_ref.set(dict_ai_trial_pred)

    st.write(keys_t)
    st.write(values_t)

    # Time taken 

    values_t = list(st.session_state.time_taken.values())
    keys_t = list(st.session_state.image_names)
    dict_time = {}
    
    for idx, val in enumerate(keys_t):
        dict_time[str(val)] = str(values_t[idx])
    
    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("ai_trial_time")
    doc_ref.set(dict_time)

    st.write(keys_t)
    st.write(values_t)

    # Saving profile information
    values_t = [
        st.session_state.name_user,
        st.session_state.nationality_user,
        st.session_state.hospital_user,
        st.session_state.department_user, 
        st.session_state.years_of_experience_user,
        st.session_state.speciality_user
    ]
    keys_t = [
        "user_name",
        "nationality_user",
        "hospital_user",
        "department_user",
        "years of experience user",
        "user speciality"
    ]

    dict_profile = {}
    
    for idx, val in enumerate(keys_t):
        dict_profile[str(val)] = str(values_t[idx])
    
    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("profile")
    doc_ref.set(dict_profile)

    col1, col2, col3 , col4, col5, col6 = st.columns([1,1,1,1,1,1])
    with col4:
        button_home = st.button("Home", on_click=go_home, key="go_h")


def final_page_ex():
    st.markdown("<h1 style='text-align: center;'>"
            "You finished the Trial!"
            "Press the home button to go the home page."
            "</h1>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>"
            "Thank you for the participation!"
            "</h1>", unsafe_allow_html=True)
    
    
    st.markdown("<h1 style='text-align: center;'>"
            "Press the home button to go the home page."
            "</h1>", unsafe_allow_html=True)
    
    # AI Exp Prediction
    keys_t = list(st.session_state.image_names)
    values_t = list(st.session_state.ai_exp_trial.values())

    dict_ai_exp_trial = {}
    
    for idx, val in enumerate(keys_t):
        dict_ai_exp_trial[str(val)] = str(values_t[idx])

    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("ai_exp_trial_results")
    doc_ref.set(dict_ai_exp_trial)


    # Time taken 

    values_t = list(st.session_state.time_taken.values())
    keys_t = list(st.session_state.image_names)
    dict_time = {}
    
    for idx, val in enumerate(keys_t):
        dict_time[str(val)] = str(values_t[idx])
    
    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("ai_exp_trial_time")
    doc_ref.set(dict_time)

    # Saving profile information
    values_t = [
        st.session_state.name_user,
        st.session_state.nationality_user,
        st.session_state.hospital_user,
        st.session_state.department_user, 
        st.session_state.years_of_experience_user,
        st.session_state.speciality_user
    ]
    keys_t = [
        "user_name",
        "nationality_user",
        "hospital_user",
        "department_user",
        "years of experience user",
        "user speciality"
    ]

    dict_profile = {}
    
    for idx, val in enumerate(keys_t):
        dict_profile[str(val)] = str(values_t[idx])
    
    doc_ref = st.session_state["db"].collection(st.session_state["name_user"] ).document("profile")
    doc_ref.set(dict_profile)

    col1, col2, col3 , col4, col5, col6 = st.columns([1,1,1,1,1,1])
    with col4:
        button_home = st.button("Home", on_click=go_home, key="go_h")



import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
if __name__ == "__main__":

    if "firebase" not in st.session_state:
        st.session_state.firebase = True
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate('firestore-key.json')
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred, name="st-trial")
        st.session_state["db"] = firestore.client()
    

    obj1 = {
        "Name": "Zohaib ",
        "Age": "28",
        "Net Worth" : 100000
    }

    obj2 = {"Name": "[0,1,2,3,4]"}

    data = [obj1, obj2]

    for record in data:
        doc_ref = st.session_state["db"].collection(u"Users").document(record["Name"])
        doc_ref.set(record)

    #keys_t = ["Zohaib", "Kiran", "Xian", "Yi"]
    #values_t = [1, 1, 0, 0]

    #for idx, t_key in enumerate(keys_t):
    #    doc_ref = st.session_state.db.collection("test"  + "_" + "Usability_trial_pred").document(t_key)
    #    doc_ref.set(values_t[idx])


    st.set_page_config(page_title='In silico Trial', layout="wide")

    #add_bg_from_local('img.jpg')    

    df = pd.read_csv(path_model_prediction, delimiter = ";")

    st.markdown("""
    <style>
    .css-nqowgj.e1ewe7hr3
    {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)
        
    st.markdown("""
    <style>
    .css-164nlkn.e1g8pov61

    {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)
        
    if "u_name" not in st.session_state:
        st.session_state.u_name = list(np.loadtxt(r"./trial/usability_ID.txt"))

    if "u_id" not in st.session_state:
        temp = [int(x) for x in st.session_state.u_name ]
        st.session_state.u_id = [df[df['ID'] == x].index[0] for x in temp]

    if "page_no" not in st.session_state:
        st.session_state.page_no = -1

    if "id" not in st.session_state:
        st.session_state.id = 0

    if "pred_mod_page1" not in st.session_state:
        st.session_state.pred_mod_page1 = False

    if "image_names" not in st.session_state:
        st.session_state.image_names = os.listdir(path_orig_images)

    if "counterfactual_slider" not in st.session_state:
        st.session_state.counterfactual_slider = 0.1

    if "usability_questionaire" not in st.session_state:
        st.session_state.usability_questionaire = {}

    if "usability_pred" not in st.session_state:
        st.session_state.usability_pred = {}
    
    if "causability_questionaire" not in st.session_state:
        st.session_state.causability_questionaire = {}

    if "ai_trial" not in st.session_state:
        st.session_state.ai_trial = {}

    if "ai_exp_trial" not in st.session_state:
        st.session_state.ai_exp_trial = {}

    if "time_taken" not in st.session_state:
        st.session_state.time_taken = {}

    if "required_flag" not in st.session_state:
        st.session_state.required_flag = False

    if "name_user" not in st.session_state:
        st.session_state.name_user = ""

    if "nationality_user" not in st.session_state:
        st.session_state.nationality_user = ""

    if "department_user" not in st.session_state:
        st.session_state.department_user = ""

    if "years_of_experience_user" not in st.session_state:
        st.session_state.years_of_experience_user = ""

    if "speciality_user" not in st.session_state:
        st.session_state.speciality_user = ""


    if st.session_state.page_no == -1:
        info_page()
    elif st.session_state.page_no == 0:
        landing_page()
    elif st.session_state.page_no == 1:
        usability_page()
    elif st.session_state.page_no == 2:
        ai_trial()
    elif st.session_state.page_no == 3:
        ai_trial_explanations()
    elif st.session_state.page_no == 4:
        explainability_page()
    elif st.session_state.page_no == 5:
        usability_questionaire()
    elif st.session_state.page_no == 6:
        explainability_page_trial()
    elif st.session_state.page_no == 7:
        final_page_u()
    elif st.session_state.page_no == 8:
        final_page_a()
    elif st.session_state.page_no == 9:
        final_page_ex()
    elif st.session_state.page_no == 10:
        system_causability_scale()