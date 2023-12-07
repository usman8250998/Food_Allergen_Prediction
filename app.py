from predict import predictions
import streamlit as st

st.title("Predicting the ingredients of input food image")
allergen = st.text_input("Enter the allergen you want to avoid (give commas seprated values)", "milk,egg")
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    st.write("Analyzing...")
    with open('temp.jpg', 'wb') as f:
        f.write(uploaded_file.getbuffer())
    output = predictions(image_path="temp.jpg")
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    allergen_list = allergen.split(',')
    allergen_found_list = [concept.name for concept in output.data.concepts if concept.name in allergen_list]
    if len(allergen_found_list) > 0:
        st.write("Allergen found in the image are: ", allergen_found_list)
    else:
        st.write("Allergen not found in the image")
            