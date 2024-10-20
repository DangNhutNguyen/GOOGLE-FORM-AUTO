import requests
import time

# Function to read form data from a text file
def read_form_data(file_path):
    form_data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            if key == 'form_id':
                form_id = value
            else:
                form_data[key] = value
    return form_id, form_data

# Specify the path to your text file
file_path = 'form_data.txt'  # Change this if your file is in a different location

# Read the form ID and data from the file
form_id, form_data = read_form_data(file_path)

# Construct the form URL
form_url = f'https://docs.google.com/forms/d/e/{form_id}/formResponse'

# Ask the user for the number of submissions
num_submissions = int(input("Enter the number of times to submit the form: "))

# Loop for the specified number of submissions
for i in range(num_submissions):
    # Send the POST request to the Google Form
    response = requests.post(form_url, data=form_data)

    # Check the response
    if response.status_code == 200:
        print(f'Form submitted successfully! Submission {i + 1}/{num_submissions}')
    else:
        print('Failed to submit the form. Status code:', response.status_code)

    # Optional: Wait for a few seconds before the next submission
    time.sleep(0)  # Adjust the delay time as needed
