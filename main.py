import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# Load the image
image_path = 'C:\\Users\\hp\\Desktop\\k\\1.PNG'
output_path = 'C:\\Users\\hp\\Desktop\\k\\out'

# Read the image
image = cv2.imread(image_path)

# Function to apply filters and save images
def apply_filters(image, output_path):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path + 'gray.png', gray)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)
    cv2.imwrite(output_path + 'equalized.png', equalized)

    # Apply Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imwrite(output_path + 'gaussian_blur.png', gaussian_blur)

    # Apply median blur
    median_blur = cv2.medianBlur(gray, 5)
    cv2.imwrite(output_path + 'median_blur.png', median_blur)

    # Apply bilateral filter
    bilateral_filter = cv2.bilateralFilter(gray, 9, 75, 75)
    cv2.imwrite(output_path + 'bilateral_filter.png', bilateral_filter)

    # Enhance the image using PIL
    pil_image = Image.open(image_path)
    
    # Enhance sharpness
    enhancer = ImageEnhance.Sharpness(pil_image)
    enhanced_image = enhancer.enhance(2.0)
    enhanced_image.save(output_path + 'sharpness.png')

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(pil_image)
    enhanced_image = enhancer.enhance(2.0)
    enhanced_image.save(output_path + 'contrast.png')

    # Enhance brightness
    enhancer = ImageEnhance.Brightness(pil_image)
    enhanced_image = enhancer.enhance(2.0)
    enhanced_image.save(output_path + 'brightness.png')

    # Apply edge enhancement filter
    edge_enhance = pil_image.filter(ImageFilter.EDGE_ENHANCE)
    edge_enhance.save(output_path + 'edge_enhance.png')

    # Apply detail filter
    detail = pil_image.filter(ImageFilter.DETAIL)
    detail.save(output_path + 'detail.png')

    # Apply unsharp mask
    unsharp_mask = pil_image.filter(ImageFilter.UnsharpMask())
    unsharp_mask.save(output_path + 'unsharp_mask.png')

# Apply filters
apply_filters(image, output_path)
