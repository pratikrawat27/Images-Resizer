import cv2

#Show you the image
# i = cv2.imread("unnamed.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",i)
# cv2.waitKey(0)

#Resizing
i = cv2.imread("unnamed.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title",i)

#Percentage by which the image is resize
scalePercentage = 200

#Cal the 50 percentage of original dimensions
newwidth = int(i.shape[1] * scalePercentage/100)
newheight = int(i.shape[0] * scalePercentage/100)

#dSize
dSize = (newwidth,newheight)

# resizing image
output = cv2.resize(i,dSize)
cv2.imwrite('newimage.png',output)
cv2.waitKey(0)