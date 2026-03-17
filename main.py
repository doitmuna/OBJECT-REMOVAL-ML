import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("test.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create mask (same height & width)
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Mark region to remove (rectangle)
mask[200:400, 300:500] = 255

# Show mask
plt.imshow(mask, cmap='gray')
plt.title("Mask (White = Remove)")
plt.axis("off")
plt.show()