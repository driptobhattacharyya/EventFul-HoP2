import csv

# Function to read data from CSV file
def read_data(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        data = []
        for row in reader:
            data.append(row)
    return data

# Function to recommend teammates based on desired skills and ratings
def recommend_teammates(data, desired_skills):
    matching_teammates = {}
    
    for row in data:
        person, skill, rating = row
        if person in matching_teammates:
            if skill in desired_skills and int(rating) >= desired_skills[skill]:
                matching_teammates[person].append((skill, rating))
        else:
            if skill in desired_skills and int(rating) >= desired_skills[skill]:
                matching_teammates[person] = [(skill, rating)]
    
    # Sort the matching teammates based on the number of matching skills (descending order)
    sorted_teammates = sorted(matching_teammates.items(), key=lambda x: (len(x[1]), max([rating for _, rating in x[1]])), reverse=True)
    
    return sorted_teammates

# Function to generate HTML output from recommendations
def generate_html_output(recommendations):
    html = "<html><body>"
    for person, skills in recommendations:
        html += "<p><strong>{}</strong></p>".format(person)
        for skill, rating in skills:
            html += "<p>{}, Rating: {}</p>".format(skill, rating)
    html += "</body></html>"
    return html
# Main function
def main():
    # Read data from CSV file
    data = read_data("dataset1.csv")
    
    # Get user input for desired skills and ratings
    desired_skills = {}

    skill_input = input("Enter desired skills and ratings (skill1:rating1, skill2:rating2, skill3:rating3): ")
    skill_pairs = skill_input.split(", ")

    for pair in skill_pairs:
        skill, rating = pair.split(":")
        desired_skills[skill.strip()] = int(rating.strip())

    # Recommend teammates based on desired skills and ratings
    recommended_teammates = recommend_teammates(data, desired_skills)

    # Generate HTML output from recommendations
    html_output = generate_html_output(recommended_teammates)

    # Write HTML output to file
    with open("recommendations.html", "w") as file:
        file.write(html_output)

    print("Recommendations generated successfully. Please check 'recommendations.html' file.")

if __name__ == '__main__':
    main()

