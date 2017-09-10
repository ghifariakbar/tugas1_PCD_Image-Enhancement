import cv2
image = cv2.imread('E:\my collection picture\my\New folder\hahah.jpg')
cv2.normalize(image, image, alpha=20, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.imwrite('kucing2CS.jpg', image)
