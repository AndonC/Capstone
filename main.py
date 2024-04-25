from PIL import Image
import pytesseract
import numpy as np

filename = "The_big_bang.png"

x = 162
x2 = 267
y = 592
y2 = 690
letters = [""]

array = [[0] * 12] * 14

'''
need to create a way to add elements to the 2d array so I then search through it for different word
list of things to do:
2-D array adding elements
function to see words on the right (whole words that still need to be found)
function to solve the word search ( big issue)
create function to then spit out picture with lines on top to show where words are
'''


def read_image(x, x2, y, y2, file_name):
    custom_config = '--oem 3 --psm 10'

    try:
        img1 = np.array(Image.open(file_name))
        # print("Image opened successfully.")

        # print(x)
        # print(x2)

        # Verify image shape
        # print("Image shape:", img1.shape)

        # Specify region coordinates [y1:y2, x1:x2]
        andon = img1[y:y2, x:x2]

        # Display the image region
        # Image.from-array(andon).show()

        letter_Seen = pytesseract.image_to_string(Image.fromarray(andon), config=custom_config)
        array.add(letter_Seen)
        # print("Letter Seen:", letter_Seen)
    except Exception as e:
        print("An error occurred:", e)


for yaxis in range(14):
    for xaxis in range(12):
        read_image(x, x2, y, y2, filename)
        x = x + 102
        x2 = x2 + 102
    x = 162
    x2 = 267
    y = y + 95
    y2 = y2 + 95

for row in array:
    print(row)

