import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


# api key
GROQ_API_KEY = os.getenv("GORQ_API_KEY")

st.title("🍲 Recipe generator")
st.subheader("Provide your ingredients list and get a recipe")

ingredients = st.text_input("Enter Your ingredients", )

#llm-model
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

#promt template

prompt_template = ChatPromptTemplate([
    ("system", '''
     You are a culinary assistant with expertise in Indian and international cuisines. 
     Your primary goal is to generate recipes based on the ingredients provided by the user. 
     Prioritize Indian-style recipes, but also suggest international dishes if they fit the ingredients well. 
     Ensure the recipe includes the following:
        A clear title for the dish.
        A list of ingredients required, including quantities where appropriate.
        Step-by-step preparation and cooking instructions.
        Optional serving suggestions or tips for enhancing flavor.
    If the user requests specific details (e.g., vegetarian-only, fusion dishes, or a specific cooking method), tailor the recipe accordingly.
    '''),
    ("user", '''
     I have the following ingredients: {ingredients}. 
     Suggest an Indian recipe I can make with these, including preparation steps and any additional spices or condiments I might need.
     Create a recipe for''')
])

prompt_template.invoke({"ingredients": ingredients})


chain = prompt_template | llm | StrOutputParser()

if st.button("Generate Recipe"):
    if {ingredients}: 
        response = chain.invoke({"ingredients" : ingredients})
        st.write(response)