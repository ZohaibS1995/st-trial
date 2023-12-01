import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from datetime import datetime

from config import *
from source.utils import * 

def plus_one_no_assist():
    """
    Increments the session state ID to move to the next image in the trial.
    
    This function also captures the time taken by the user to evaluate each image and stores it.
    If all images have been evaluated, the function updates the session state page number to 8.
    """

    # If not the last image, record the time taken and reset the start time
    if st.session_state.id < 80:  
        _record_time_taken()

    # Move to the next image if there are remaining images
    if st.session_state.id < len(st.session_state.image_names) - 1:
        st.session_state.id += 1
        st.session_state.pred_mod_page1 = False

    # If all images have been evaluated, set the page number to 8
    elif st.session_state.id == len(st.session_state.image_names) - 1:
        st.session_state.page_no = 15

def _record_time_taken():
    """
    Helper function to record the time taken to evaluate an image.
    """
    elapsed_time = datetime.now() - st.session_state.start_time
    st.session_state.time_taken[st.session_state.image_names[st.session_state.id]] = elapsed_time
    st.session_state.start_time = datetime.now()

# Function to decrease the value of the counterfactual slider
def decrease_slider():
    st.session_state.confidence_level = max(0, st.session_state.confidence_level - 10)

# Function to increase the value of the counterfactual slider
def increase_slider():
    st.session_state.confidence_level = min(100, st.session_state.confidence_level + 10)

def no_assist_trial():
    """
    Displays the AI + Clinicians Trial page in a Streamlit app.
    
    This function provides a side-by-side view of SWE Images with B-mode Ultrasound, and shows
    clinical data along with model predictions for PHLF Risk. It allows users to make predictions
    based on the displayed images and data.
    """

    # Custom styles for radio buttons
    _inject_style("""
        div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
            font-size: 24px;
        }
        div[class*="stRadio"] {
            background-color: #FEA09A;
            border: 3px solid;
        }
    """)

    # Set current page number and display trial progress
    st.session_state.page_no = 13
    st.write(f"## Clinical Trial - No Assistance: {st.session_state.id+1}/{len(st.session_state.image_names)}")
    st.write("---")

    df_basic_info = pd.read_excel(path_basic_information, engine="openpyxl")
    index_id = df_basic_info.index[df_basic_info['ID'] == int(st.session_state.image_names[st.session_state.id].split(".")[0])].item()
    info = df_basic_info.iloc[index_id, 1:].to_numpy()[0]
    st.write(f"##### Patient's Information: {info}")

    col1, col2 = st.columns([4, 5])

    # Display SWE Image and B-mode Ultrasound
    with col1:
        st.write("**Top: SWE Image, Bottom: B-mode Ultrasound**")
        image = Image.open(path_orig_images + st.session_state.image_names[st.session_state.id])
        st.image(image)

    # Display clinical data
    with col2:
        df = pd.read_excel(path_clinical_data, engine="openpyxl")
        # Iterate over columns and convert if all values are floats
        for col in df.columns:
            # Check if all values in the column can be converted to float
            if df[col].apply(is_float).all():
                df[col] = df[col].astype(float).round(2)
                
        keys_n = list(df.columns)[2:]
        val_w_k = list(df.iloc[df.index[df['ID'] == int(st.session_state.image_names[st.session_state.id].split(".")[0])].item(), 2:].to_numpy())
        normal_range = list(pd.read_csv(path_clinical_normal).to_numpy().transpose())

        data = np.vstack((keys_n, val_w_k, normal_range)).transpose()
        v_df = pd.DataFrame(data, columns=["Clinical Variable", "Value", "Normal Range"])
        hyperlinks = list(pd.read_csv(path_clinical_hyperlinks, delimiter=";")["Hyperlinks"].to_numpy().transpose())
        v_df['Clinical Variable'] = [apply_hyperlink(item, link) for item, link in zip(v_df['Clinical Variable'], hyperlinks)]

    
        styled_df = v_df.style.apply(color_rows, axis=1)

        st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)
        st.write(f"##### For explanation of clinical variables, [click here]({URL_variable_explanation})")


    # User prediction input
    with st.columns([4,4,4])[0]:
        st.radio("Select your prediction of PHLF Risk", ("High risk of PHLF", "Low risk of PHLF"), key="ai_pred")

    # Store user prediction in session state
    st.session_state.no_assist_trial[st.session_state.image_names[st.session_state.id]] = st.session_state.ai_pred

    st.write("### Choose confidence level for your prediction (0 - 100 %):")

    col1, col2, col3, col4 = st.columns([0.4, 4, 0.4, 14])
    with col1:
        st.button(r"\-", on_click=decrease_slider)
    with col2:
        st.slider("", 0, 100, 50, step=10, key="confidence_level")
    with col3:
        st.button(r"\+", on_click=increase_slider)

    st.session_state.ai_no_confidence_level[st.session_state.image_names[st.session_state.id]] = st.session_state.confidence_level

    # Next button
    with st.columns([1,7,1])[2]:
        button_next = st.button("Next", on_click=plus_one_no_assist, key="plus_one_no_assist")
    return

def _inject_style(style_str):
    """
    Helper function to inject custom CSS styles into the Streamlit app.
    """
    st.markdown(f"""<style>{style_str}</style>""", unsafe_allow_html=True)

