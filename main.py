from PIL import Image
import pytesseract
import numpy as np

# Each box is 102 in width and 95 in height
# the idea is to know where the first one starts and then take those number and just add to them
# i.e. 162+102 = top left of next box and 267+102 = bottom right of next box
# then to change the height you do height of box +95 to both the bottom and top to get the respective height numbers

filename = "The_big_bang.png"

x = 162
x2 = 267
y = 592
y2 = 690
letters = [""]


# is supposed to represent the top left corner of a box
# noinspection PyTypeChecker
def read_image(x, x2, y, y2, file_name):
    custom_config = '--oem 3 --psm 10'

    try:
        img1 = np.array(Image.open(file_name))
        print("Image opened successfully.")

        # print(x)
        # print(x2)

        # Verify image shape
        print("Image shape:", img1.shape)

        # Specify region coordinates [y1:y2, x1:x2]
        andon = img1[y:y2, x:x2]

        # Display the image region
        # Image.fromarray(andon).show()

        letter_Seen = pytesseract.image_to_string(Image.fromarray(andon), config=custom_config)
        letters.append(letter_Seen)
        print("Letter Seen:", letter_Seen)
    except Exception as e:
        print("An error occurred:", e)


# read_image(filename)
for yaxis in range(14):
    for xaxis in range(12):
        read_image(x, x2, y, y2, filename)
        x = x + 102
        x2 = x2 + 102
    x = 162
    x2 = 267
    y = y + 95
    y2 = y2 + 95

print(letters)
