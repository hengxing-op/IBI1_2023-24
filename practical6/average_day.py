import matplotlib.pyplot as plt

#Create a dictionary with activities and hours
activities = {
    "Sleeping": 8,
    "Classes": 6,
    "Studying": 3.5,
    "TV": 2,
    "Music": 1
}

#Calculate 'Other' category hours and add it to the dictionary
total_hours_accounted = sum(activities.values())
activities["Other"] = 24 - total_hours_accounted

#Print the activities dictionary
print("Activities dictionary:", activities)

#Generate and display a pie chart
labels = activities.keys()
sizes = activities.values()
plt.figure()
plt.pie(sizes, labels=labels, startangle=90)
plt.title('Average Day of a University Student')
plt.show()

#Print hours spent on a specific activity (modify this variable to test)
requested_activity = "Studying"  # Modify this line for different activities
print(f"Hours spent on {requested_activity}: {activities[requested_activity]}")