import cv2
img = cv2.imread('C:/Users/DongD/Desktop/LKGE_WEEB/123.png')
(b,g,r) = img[10,10]
print(b,'-',g,'-',r)