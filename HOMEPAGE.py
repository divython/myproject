# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 12:44:00 2023

@author: Divyanshu
"""

import streamlit as st

# Set page title and icon
st.set_page_config(
    page_title='My Project for Samsung Innovation Campus',
    page_icon='🧠'
)

# Main page title
st.title("Main Page")

# Sidebar with a success message
st.sidebar.success("Select an option from the sidebar")

# Description
description = """
This Streamlit app showcases my project for the Samsung Innovation Campus. 
Feel free to explore and interact with the different features and functionalities.
"""

# Display the description
st.write(description)

# Paragraph
paragraph = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec erat ut leo pharetra varius.
Duis at metus nec urna lobortis malesuada. Sed euismod lectus ut elit feugiat, nec accumsan tortor varius.
Praesent ac ligula euismod, sollicitudin purus at, varius orci. Nam fringilla orci eget dui ultricies, 
et bibendum turpis aliquet. Sed vel facilisis libero. Curabitur non neque in turpis vestibulum 
euismod ut id libero. Nullam at tincidunt augue, vel venenatis sapien.
"""

# Display the paragraph
st.write(paragraph)
