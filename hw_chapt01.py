# Purpose: Streamlit app to draw rectangles on an image and save the coordinates to a json file
# Refer andrie folder "receipt2_app.py" for some of the codes here
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
# pip install git+https://github.com/abelembaye/streamlit-drawable4testing.git
#from streamlit_drawable4testing import st_canvas
import json
import os
import fn4authen_app  # as auth?

st.set_page_config(
    page_title="Your Page Title",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

#st.title("HW Chapter 1")

q01_holder = "This question has been attempted by me!"
#student_name = st.text_input("Full NAME", placeholder="John Doe")
q01 = st.text_input("Q01. What is the best course you are taking",
                    placeholder=q01_holder, key=1)
st.write("Q02. For the following question, please draw on the canvas below")

drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "line", #"rect", "circle",
                      #"curve", "text", "transform")
                     )
)

# stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider(
        "Point display radius: ", 1, 25, 3)
# stroke_color = st.sidebar.color_picker("Stroke color hex: ")
# bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
# bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

realtime_update = st.sidebar.checkbox("Update in realtime", True)

# docImg = Image.open("img01b.png")

if 'saved_state' not in st.session_state or st.session_state.saved_state is None:
    # print('NEW SESSION')
    if os.path.exists("saved_state0.json"):
        with open("saved_state0.json", "r") as f:
            saved_state = json.load(f)
    else:
        saved_state = {}  # Initialize an empty state if the file doesn't exist
        with open("saved_state.json", "w") as f:
            json.dump(saved_state, f)  # Create the file
    st.session_state['saved_state'] = saved_state
else:
    # print('OLD SESSION')
    saved_state = st.session_state['saved_state']

# mode="transform" if st.checkbox("Move ROIS", False) else "rect"
# mode = "transform" if st.checkbox("Move ROIS", False) else "line"

canvas_result01 = st_canvas(
    fill_color="rgba(0, 151, 255, 0.3)",
    stroke_width=2,
    stroke_color="rgba(0, 50, 255, 0.7)",
    # background_image=docImg,
    # background_color=bg_color,
    initial_drawing=saved_state,  # this the beginning jason data and drawings
    # height=720,
    # width=512,
    height=400,
    width=400,
    drawing_mode=drawing_mode,
    display_toolbar=True,
    update_streamlit=True,
    key="graph01"
)

# start with an image data you want
# canvas_result01.image_data
if canvas_result01.json_data is not None:
    # need to convert obj to str because PyArrow
    objects = pd.json_normalize(canvas_result01.json_data["objects"])
    for col in objects.select_dtypes(include=['object']).columns:
        objects[col] = objects[col].astype("str")
    st.dataframe(objects)  # displays the drawing dataframe
    # st.write(canvas_result01.json_data) #displays the drawing json data-- ugly
    with st.form(key="fields_form"):
        submit_button = st.form_submit_button(label="save")
        if submit_button:
            # to write json to drive file
            # with open('saved_state.json', 'w') as outfile:
            #     json.dump(canvas_result01.json_data, outfile, indent=2)
            # st.write(canvas_result01.json_data)
            # this is printed to the st page
            st.image(canvas_result01.image_data)
            file_path = os.path.join(
                os.getcwd(), "test.jpeg")  # Write image to disk
            # print(file_path)
            img06 = Image.fromarray(canvas_result01.image_data)
            img06 = img06.convert("RGB")  # Convert to RGB mode
            img06.save(file_path, "JPEG")  # to disck

q03 = st.text_input("Q03. Question 3 is answered below",
                    placeholder="place holder to TBA", key=3)

canvas_result02 = st_canvas(
    fill_color="rgba(0, 151, 255, 0.3)",
    stroke_width=2,
    stroke_color="rgba(0, 50, 255, 0.7)",
    # background_image=docImg,
    # background_color=bg_color,
    initial_drawing=saved_state,  # this the beginning jason data and drawings
    # height=720,
    # width=512,
    height=400,
    width=400,
    drawing_mode=drawing_mode,
    display_toolbar=True,
    update_streamlit=True,
    key="graph02"
)

# start with an image data you want
# canvas_result02.image_data
if canvas_result02.json_data is not None:
    # need to convert obj to str because PyArrow
    objects = pd.json_normalize(canvas_result02.json_data["objects"])
    for col in objects.select_dtypes(include=['object']).columns:
        objects[col] = objects[col].astype("str")
    st.dataframe(objects)  # displays the drawing dataframe
    # st.write(canvas_result02.json_data) #displays the drawing json data-- ugly
    with st.form(key="fields_form2"):
        submit_button = st.form_submit_button(label="save2")
        if submit_button:
            # to write json to drive file
            # with open('saved_state.json', 'w') as outfile:
            #     json.dump(canvas_result02.json_data, outfile, indent=2)
            # st.write(canvas_result02.json_data)
            # this is printed to the st page
            st.image(canvas_result02.image_data)
            file_path = os.path.join(
                os.getcwd(), "test.jpeg")  # Write image to disk
            # print(file_path)
            img06 = Image.fromarray(canvas_result02.image_data)
            img06 = img06.convert("RGB")  # Convert to RGB mode
            img06.save(file_path, "JPEG")  # to disck

# conda activate cvenv4st
# streamlit run hw_chapt01.py
