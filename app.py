import streamlit as st
from itinerary_generator import generate_itinerary
from web_search import search_activities

st.title("AI Travel Planner 🌍✈️")

destination = st.text_input("Where are you traveling?")
budget = st.selectbox("Budget?", ["Budget-friendly", "Mid-range", "Luxury"])
duration = st.slider("How many days?", 1, 14, 5)
interests = st.text_input("What do you want to explore? (Food, Culture, Adventure)")

if st.button("Generate Itinerary"):
    activities = search_activities(destination, interests)
    itinerary = generate_itinerary({
        "destination": destination,
        "budget": budget,
        "duration": duration
    }, activities)

    st.write(itinerary)
