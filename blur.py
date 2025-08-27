import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image1.jpg")

blur = cv2.GaussianBlur(img, (15, 15), 0)
blur = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

plt.imshow(blur)
plt.axis("off")
plt.show()
