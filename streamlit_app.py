import streamlit
import pandas

streamlit.title('My parents new healthy dinner')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruits_list = pandas.read.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruits_list)
