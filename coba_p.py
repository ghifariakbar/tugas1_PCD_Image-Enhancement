import cv2
image = cv2.imread('E:\my collection picture\my\New folder\hahah.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('kucing1.jpg', gray)
