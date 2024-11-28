# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import numpy as np     
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from ast import literal_eval





# # page_bg_color = """
# # <style>
# # [data-testid="stAppViewContainer"] {
# #     background-color: #00011; /* Light beige background */
# #     color: black; /* Text color */
# # }

# # [data-testid="stSidebar"] {
# #     background-color: #f0f8ff; /* Light blue sidebar */
# # }
# # </style>
# # """

# # st.markdown(page_bg_color, unsafe_allow_html=True)










# # Title for the app
# st.title("Travel Suggestion App")

# df = pickle.load(open('hotel.pkl', 'rb'))

# # # Input fields
# # city = st.text_input("Enter City", placeholder="e.g., Paris")
# # food = st.text_input("Enter Preferred Food", placeholder="e.g., Pizza")
# # price = st.number_input("Enter Your Budget", min_value=0, step=1)



# def recommend_restaurant(city, cuisine, cost):
#     cuisine = cuisine.lower()

#     # Filtering the cuisine set
#     stop_words = set(stopwords.words('english'))
#     filtered = {word for word in word_tokenize(cuisine) if word not in stop_words}

#     # Filtering the dataset based on input city and cost
#     city_df = df[df['City'].str.lower() == city.lower()]
#     city_df = city_df[city_df['Cost'] <= int(cost)]
#     city_df = city_df.set_index(np.arange(city_df.shape[0]))

#     cos = []
#     for i in range(city_df.shape[0]):
#         temp_token = word_tokenize(city_df["Cuisine"][i])
#         temp_set = {word for word in temp_token if word not in stop_words}
#         vector = temp_set.intersection(filtered)
#         cos.append(len(vector))
    
#     # Assigning similarity scores
#     city_df['similarity'] = cos

#     # Sorting based on similarity and rating
#     city_df = city_df.sort_values(by=['similarity', 'Rating'], ascending=[False, False])
#     city_df.reset_index(drop=True, inplace=True)
    
#     return city_df[["Name", "Location", "Rating"]].head()


# # User Inputs
# city = st.text_input("Enter City:", "")
# cuisine = st.text_input("Enter Cuisine:", "")
# cost = st.number_input("Enter Maximum Cost:", min_value=0, value=500)

# # Recommend Button
# if st.button("Recommend"):
#     if city and cuisine and cost:
#         try:
#             recommendations = recommend_restaurant(city, cuisine, cost)
#             if recommendations.empty:
#                 st.write("No recommendations found. Try different inputs.")
#             else:
#                 st.write("Here are the top recommendations:")
#                 st.dataframe(recommendations)
#         except Exception as e:
#             st.error(f"Error: {e}")
#     else:
#         st.warning("Please provide all inputs!")

















import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np     
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')  # for word_tokenize
nltk.download('stopwords')  # for stopwords

# Title for the app
st.title("Travel Suggestion App")

df = pickle.load(open('hotel.pkl', 'rb'))

def recommend_restaurant(city, cuisine, cost):
    cuisine = cuisine.lower()

    # Filtering the cuisine set
    stop_words = set(stopwords.words('english'))
    filtered = {word for word in word_tokenize(cuisine) if word not in stop_words}

    # Filtering the dataset based on input city and cost
    city_df = df[df['City'].str.lower() == city.lower()]
    city_df = city_df[city_df['Cost'] <= int(cost)]
    city_df = city_df.set_index(np.arange(city_df.shape[0]))

    cos = []
    for i in range(city_df.shape[0]):
        temp_token = word_tokenize(city_df["Cuisine"][i])
        temp_set = {word for word in temp_token if word not in stop_words}
        vector = temp_set.intersection(filtered)
        cos.append(len(vector))
    
    # Assigning similarity scores
    city_df['similarity'] = cos

    # Sorting based on similarity and rating
    city_df = city_df.sort_values(by=['similarity', 'Rating'], ascending=[False, False])
    city_df.reset_index(drop=True, inplace=True)
    
    return city_df[["Name", "Location", "Rating"]].head()


# User Inputs
city = st.text_input("Enter City:", "")
cuisine = st.text_input("Enter Cuisine:", "")
cost = st.number_input("Enter Maximum Cost:", min_value=0, value=500)

# Recommend Button
if st.button("Recommend"):
    if city and cuisine and cost:
        try:
            recommendations = recommend_restaurant(city, cuisine, cost)
            if recommendations.empty:
                st.write("No recommendations found. Try different inputs.")
            else:
                st.write("Here are the top recommendations:")
                st.dataframe(recommendations)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please provide all inputs!")