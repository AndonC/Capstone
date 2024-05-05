from PIL import Image
import pytesseract
import numpy as np

filename = "The_big_bang.png"

x = 162
x2 = 267
y = 592
y2 = 690
letters = [""]

w, h = 12, 14
arr = []
temp_Array = []

'''
need to create a way to add elements to the 2d array so I then search through it for different word
list of things to do:
2-D array adding elements
function to see words on the right (whole words that still need to be found)
function to solve the word search ( big issue)
create function to then spit out picture with lines on top to show where words are
'''

Matrix = [[0 for x in range(w)] for y in range(h)]


def read_image(x, x2, y, y2, file_name):
    custom_config = '--psm 10 --oem 3'

    try:
        img1 = np.array(Image.open(file_name))

        # Specify region coordinates [y1:y2, x1:x2]
        andon = img1[y:y2, x:x2]

        letter_seen = pytesseract.image_to_string(Image.fromarray(andon), config=custom_config)
        temp_Array.append(letter_seen)
        #print(temp_Array)
        return letter_seen
        # print("Letter Seen:", letter_Seen)
    except Exception as e:
        print("An error occurred:", e)


for i in range(h):
    for j in range(w):
        #print(j)
        Matrix[i][j] = read_image(x, x2, y, y2, filename)
        x = x + 102
        x2 = x2 + 102
    x = 162
    x2 = 267
    y = y + 95
    y2 = y2 + 95

print("the end of the program print\n")
print(Matrix)

'''
iterate through matrix until i find first letter
then check surrounding letters for 2nd letter
then since you know the direction of the letters then check all the letters until whole word is found
if i did not find the word then go back a step until the loop is finished.
if word is still not done then start iterating through the matrix until next would is found
'''