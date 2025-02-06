import string

def load_photos(filename):
    with open(filename, 'r') as file:
        text = file.read()
    image_list = text.split('\n')
    
    return image_list

