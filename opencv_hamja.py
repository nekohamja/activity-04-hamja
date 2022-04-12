import cv2
filePath = 'album.jpg'
image = cv2.imread(filePath, 1)
cv2.imshow("album", image)
cv2.waitKey(0)
cv2.destroyAllWindows()