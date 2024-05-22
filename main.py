import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog","Cow", "Hamster", "Baby"))


pet_color = st.sidebar.text_area(label=f"What color is your {chr(ord(animal_type[0])+97-65)}{animal_type[1:]} name?", max_chars=15)
api_key = st.sidebar.text_area(label="Your openai api key:")
if pet_color and api_key:
    response = lch.generate_pet_name(animal_type, pet_color, api_key)
    st.write(response)
