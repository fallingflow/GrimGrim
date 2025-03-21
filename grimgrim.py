import cv2
import numpy as np
import matplotlib.pyplot as plt


# Load the image
img = cv2.imread('data/image1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Designate the edge thickness
edge_thickness = 2
kernel = np.ones((edge_thickness, edge_thickness), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)
edges = cv2.erode(edges, kernel, iterations=1)

# Convert the image to color
color = img.reshape((-1, 3))
color = np.float32(color)

# Apply KMeans algorithm to cluster colors
K = 7
_, labels, centers = cv2.kmeans(color, K, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2), 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(img.shape)

# Combine the color image with the edges mask
cartoon = cv2.bitwise_and(segmented_image, segmented_image, mask=edges)

# Display the cartoon imag
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()