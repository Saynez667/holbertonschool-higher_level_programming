import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return
    
    # Iterate over attendees and generate invitation files
    for i, attendee in enumerate(attendees, start=1):
        output_content = template
        
        # Replace placeholders with actual values, use 'N/A' if missing
        output_content = output_content.replace("{name}", attendee.get("name", "N/A"))
        output_content = output_content.replace("{event_title}", attendee.get("event_title", "N/A"))
        output_content = output_content.replace("{event_date}", attendee.get("event_date", "N/A") or "N/A")
        output_content = output_content.replace("{event_location}", attendee.get("event_location", "N/A"))
        
        # Write to output file
        file_name = f"output_{i}.txt"
        with open(file_name, "w") as file:
            file.write(output_content)
        print(f"Generated: {file_name}")
        