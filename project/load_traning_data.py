import string

def load_photos(filename):
    with open(filename, 'r') as file:
        text = file.read()
    image_list = text.split('\n')
    
    return image_list

def load_clean_descriptions(filename, photos):
    with open(filename, 'r') as file:
        text = file.read()
    image_list = text.split('\n')
    
    # Initialize an empty list to store the filtered lines
    filtered_lines = []

    for image in image_list:
        # Split the line into image name and caption using the tab character as the delimiter
        parts = image.split('\t')
        
        # Check if the line has at least two parts (image name and caption)
        if len(parts) >= 2:
            image_name = parts[0]
            caption = parts[1]
            
            # Check if the image name is in the provided list
            if image_name in photos:
                # Add <start> and <end> tags to the caption
                tagged_caption = f"<start>{caption}<end>"
                
                # Reconstruct the line with the tagged caption
                filtered_line = f"{image_name}\t{tagged_caption}"
                
                # Add the filtered line to the filtered lines list
                filtered_lines.append(filtered_line)

    # Write back to the text file 
    with open(filename, 'w') as file:
        file.writelines(filtered_line)
    
