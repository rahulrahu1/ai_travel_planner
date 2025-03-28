import requests

def search_activities(destination, interest):
    # Simulating a web search by returning sample activities
    return [
        {"morning": f"Visit {destination}'s famous landmark", "afternoon": f"Explore a {interest} museum", "evening": "Try local cuisine"},
        {"morning": "Go on a city walking tour", "afternoon": "Relax in a popular park", "evening": "Attend a cultural show"},
        [
            {"morning": f"Visit {destination}'s famous landmark", "afternoon": f"Explore a {interest} museum",
             "evening": "Try local cuisine"},
            {"morning": "Go on a city walking tour", "afternoon": "Relax in a popular park",
             "evening": "Attend a cultural show"},
            {"morning": "Enjoy a scenic hike", "afternoon": "Visit a historic site",
             "evening": "Taste street food specialties"},
            {"morning": "Take a guided architecture tour", "afternoon": "Shop at a local market",
             "evening": "Join a cooking class"},
            {"morning": f"Explore {destination}'s botanical gardens", "afternoon": "Visit an art gallery or exhibition",
             "evening": "Attend a live music performance"},
            {"morning": "Embark on a boat or ferry ride", "afternoon": "Discover a lesser-known neighborhood",
             "evening": "Dine at a rooftop restaurant"},
            {"morning": "Go wildlife watching or birdwatching",
             "afternoon": "Enjoy an outdoor adventure like ziplining", "evening": "Relax at a spa"},
            {"morning": "Take a food tour", "afternoon": "Visit a quirky or unusual museum",
             "evening": "Watch a sunset at a viewpoint"},
            {"morning": "Participate in a local festival or event",
             "afternoon": "Take a day trip to nearby attractions", "evening": "Experience nightlife hotspots"},
            {"morning": f"Walk along {destination}'s waterfront or promenade",
             "afternoon": "Join a photography workshop", "evening": "Discover hidden gems on a night tour"},
            {"morning": "Explore historical neighborhoods", "afternoon": "Engage in watersports or activities",
             "evening": "Savor dessert specialties"},
            {"morning": "Visit a famous library or bookshop", "afternoon": "Learn a traditional craft or skill",
             "evening": "Enjoy open-air cinema or theater"},
            {"morning": "Discover ancient ruins or monuments", "afternoon": "Ride a scenic train or bus route",
             "evening": "Attend a local storytelling event"},
            {"morning": "Take a cultural dance or music lesson",
             "afternoon": "Visit a science center or interactive museum",
             "evening": "Try food fusion at a modern restaurant"},
            {"morning": "Go stargazing or on a sunrise trek", "afternoon": "Take a self-guided audio tour",
             "evening": "Reflect on the journey with a relaxing dinner"},
        ]
    ]
