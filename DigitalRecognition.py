import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Buff4.jpg')

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# Create Gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.blur(gray, (8,8))

# Makes bright pixels much brighter while dark pixels stay dark
img = (img.astype(np.float64)) ** 10

# Scale values back to uint8
img = ((img * 255) / (255 ** 10))
img = img.astype(np.uint8)

# Apply the edge detector
edges = cv2.Canny(img, 100, 200)  # Create Canny edge image

plt.subplot(122), plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()


# initialization
edge = 0
check_x = 0
check_y = 0
upper_x = 0
lower_x = 0

# Check upper two segments
while True:
    if np.any(edges[55, check_x] != 0): # 50 # 40
        edge += 1
        upper_x = check_x

    if check_x == 65: # 85 #72
        break

    check_x = check_x + 1
upper = edge / 2  # two edges make a segment

# reset variables
check_x = 0
edge = 0

# check lower two segments
while True:
    if np.any(edges[80, check_x] != 0): # 90 # 70
        edge += 1
        lower_x = check_x

    if check_x == 65: # 85 # 72
        break

    check_x = check_x + 1
lower = edge / 2  # two edges make a segment

# reset variables
check_x = 0
edge = 0

# checks three middle segments
while True:
    if np.any(edges[check_y, 34] != 0): # 45 # 19
        edge += 1

    if check_y == 100: # 129
        break

    check_y = check_y + 1
vertical = edge / 2  # two edges make a segment

# reset variables
check_y = 0
edge = 0

print "#---------#"
print upper
print lower
print vertical
print "#---------#"

# checks combination of segments to determine number
if upper == 2 and lower == 2 and vertical == 2:
    print "0"

elif upper == 1 and lower == 1 and vertical == 0:
    print "1"

elif upper == 2 and lower == 1 and vertical == 1:
    print "4"

elif upper == 1 and lower == 2 and vertical == 3:
    print "6"

elif upper == 1 and lower == 1 and vertical == 1:
    print "7"

elif upper == 2 and lower == 2 and vertical == 3:
    print "8"

elif upper == 2 and lower == 1 and vertical == 2:
    print "9"

# Three numbers come from this combination
elif upper == 1 and lower == 1 and vertical == 3:
    if upper_x - 20 > lower_x:  # if the upper segment is to the right and lower to the left
        print "2"

    elif upper_x + 20 < lower_x:  # if the upper segment is to the left and lower to the right
        print "5"

    elif abs(upper_x - lower_x) < 15:  # if both upper and lower are on the right
        print "3"


