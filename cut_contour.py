import cv2
import numpy as np

image = cv2.imread("chips.jpg")
resized_image = cv2.resize(image, (500, 500))

# convert to RGB
image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
# convert to grayscale
gray = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)


_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# show it
print(resized_image.shape)

# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours
image = cv2.drawContours(resized_image, contours, -1, (0, 255, 0), 2)


idx = 0
for c in contours:
	x,y,w,h = cv2.boundingRect(c)
	if w>50 and h>50:
		idx+=1
		new_img=image[y:y+h,x:x+w]
		cv2.imwrite(str(idx) + '.png', new_img)


cv2.imshow('ed',resized_image)


#cv2.imshow('seryi',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()