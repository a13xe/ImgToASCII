import cv2

ASCII_SIZE = 100
ASCII_CHARS = ['⠀', '⢀', '⠄', '⠤', '⠶', '⡆', '⡖', '⣆', '⣤', '⣶', '⣿']

def resize_image(image, new_width=ASCII_SIZE):
    height, width = image.shape[:2]
    ratio = new_width / float(width)
    new_height = int(height * ratio)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def rgb_to_gray(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def pixels_to_ascii(image):
    ascii_str = ''
    for row in image:
        for pixel_value in row:
            index = pixel_value // 32
            ascii_str += ASCII_CHARS[index]
        ascii_str += '\n'
    return ascii_str

def main(image_path, new_width=ASCII_SIZE):
    try:
        image = cv2.imread(image_path)
    except Exception as e:
        print("Error:", e)
        return

    image = resize_image(image, new_width=new_width)
    gray_image = rgb_to_gray(image)
    ascii_str = pixels_to_ascii(gray_image)

    # Print the ASCII art 
    print(ascii_str)
    
    # Save it to a text file
    with open('ascii_art.txt', 'w') as f:
        f.write(ascii_str)

if __name__ == "__main__":
    image_path = 'image.jpg'
    main(image_path)
