import random
import csv

# Read the event dataset from a CSV file
event_dataset = []
with open('event_dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    event_dataset = list(reader)

# Read the events dataset from a CSV file
events_dataset = []
with open('events.csv', 'r') as file:
    reader = csv.DictReader(file)
    events_dataset = list(reader)

# Function to recommend events based on a person's information
def recommend_events(person_info, events_data, num_recommendations=5):
    recommended_events = []

    # Find person's interests and skills from the event dataset
    person_interests = []
    person_skills = []
    for person in event_dataset:
        if person['Name'] == person_info['Name']:
            person_interests = person['Interests'].split(', ')
            person_skills = person['Skills'].split(', ')
            break

    # Recommend events based on person's interests and skills
    for event in events_data:
        if event['Category'] in person_interests:
            recommended_events.append(event)

    random.shuffle(recommended_events)  # Shuffle the recommendations
    return recommended_events[:num_recommendations]

# Input person's name
person_name = input("Enter the person's name: ")

# Find person's information from the event dataset
person_info = None
for person in event_dataset:
    if person['Name'] == person_name:
        person_info = person
        break

# Recommend events for the person
if person_info:
    recommendations = recommend_events(person_info, events_dataset)

    # Generate HTML output
    html_output = "<html>\n<head>\n<title>Event Recommendations</title>\n</head>\n<body>\n"
    html_output += "<h1>Event Recommendations for {}</h1>\n".format(person_name)
    if recommendations:
        html_output += "<ul>\n"
        for event in recommendations:
            html_output += "<li>\n"
            html_output += "<strong>Event Name:</strong> {}\n".format(event["Event Name"])
            html_output += "<strong>Category:</strong> {}\n".format(event["Category"])
            html_output += "<strong>Date:</strong> {}\n".format(event["Date"])
            html_output += "<strong>Location:</strong> {}\n".format(event["Location"])
            html_output += "<strong>Description:</strong> {}\n".format(event["Description"])
            html_output += "</li>\n"
        html_output += "</ul>\n"
    else:
        html_output += "<p>No relevant events found for {}.</p>\n".format(person_name)
    html_output += "</body>\n</html>"

    # Save the HTML output to a file
    output_file = "event_recommendations.html"
    with open(output_file, "w") as file:
        file.write(html_output)

    print("Event recommendations generated and saved to '{}'.".format(output_file))
else:
    print("Person information not found for {}.".format(person_name))
