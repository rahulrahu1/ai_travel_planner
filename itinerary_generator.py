def generate_itinerary(user_preferences, activities):
    itinerary = []
    for day in range(user_preferences["duration"]):
        itinerary.append({
            "day": day + 1,
            "morning": activities[day]["morning"] if day < len(activities) else "Free morning",
            "afternoon": activities[day]["afternoon"] if day < len(activities) else "Free afternoon",
            "evening": activities[day]["evening"] if day < len(activities) else "Free evening"
        })
    return itinerary
