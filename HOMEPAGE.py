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
st.title("Welcome to my project")

# Sidebar with a success message
st.sidebar.success("Select an  project from the sidebar")

# Description
description = """
This Streamlit app showcases my project for the Samsung Innovation Campus. 
Feel free to explore and interact with the different features and functionalities.
"""

# Display the description
st.write(description)

# Paragraph
paragraph = """
In my projects, I've developed two applications. 
The first project employs ImageNet EfficientNet 
pretrained convolutional neural networks (CNNs) 
for image classification. Leveraging EfficientNet's 
pretraining, this system accurately categorizes images
into various classes, enhancing automated image understanding. 
The second project involves building a YouTube comment sentiment analyzer. 
It extracts comments from specified URLs and performs sentiment analysis, categorizing 
the sentiments as positive, negative, or neutral. This analysis provides valuable insights
into audience reactions to YouTube content."""

# Display the paragraph
st.write(paragraph)
