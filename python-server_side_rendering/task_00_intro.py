import os


def generate_invitations(template, attendees):
    # Step 1: Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list):
        if not all(isinstance(attendee, dict) for attendee in attendees):
            print("Error: Attendees must be a list of dictionaries.")
        return

    # Step 2: Handle empty inputs
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Step 3: Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data
        # Use "N/A" for missing values
        personalized_content = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            value_to_replace = value if value else "N/A"
            placeholder_tag = f"{{{placeholder}}}"
            personalized_content = personalized_content.replace(
                placeholder_tag, value_to_replace
            )

        # Step 4: Generate output files
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(personalized_content)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
