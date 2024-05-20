# Import necessary libraries
import matplotlib.pyplot as plt

# Create a dictionary with the given data
activities = {
    'Sleeping': 8,
    'Classes': 6,
    'Studying': 3.5,
    'TV': 2,
    'Music': 1
}

# Add an 'other' category to account for remaining hours
total_hours_in_a_day = 24
hours_spent = sum(activities.values())
activities['Other'] = total_hours_in_a_day - hours_spent

print("Activities dictionary:")
print(activities)

# Plot a pie chart using matplotlib
labels = list(activities.keys())
sizes = list(activities.values())

plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Average Day of a University Student')
plt.show()

# Print the number of hours spent on a specific activity
# For example, let's print hours spent on 'Studying'
requested_activity = 'TV'
print(f"Hours spent on {requested_activity}: {activities[requested_activity]}")