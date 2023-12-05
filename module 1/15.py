import cv2
import requests

image_url = 'https://tumen.biskvitdvor.ru/upload/resize_cache/iblock/d35/498_400_0/d35c4f9135ad3fe4b95066f73843d077.jpg'
img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

image = cv2.imread('image_name.jpg', 0)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Binary Image', binary_image)
cv2.imwrite('binary_image.jpg', binary_image)

canny_image = cv2.Canny(image, 50, 150)

cv2.imshow('Canny Image', canny_image)
cv2.imwrite('canny_image.jpg', canny_image)

median_img = cv2.medianBlur(image, 5)

cv2.imshow('Blurred Image', median_img)
cv2.imwrite('blurred_image.jpg', median_img)

cv2.waitKey(0)
cv2.destroyAllWindows()