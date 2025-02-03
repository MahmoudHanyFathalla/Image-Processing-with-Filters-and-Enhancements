# Image Processing with Filters and Enhancements

This Python script applies various filters and enhancements to an image using OpenCV and PIL (Pillow). The filters include converting to grayscale, applying histogram equalization, Gaussian blur, and bilateral filter. Additionally, it enhances the image's sharpness, contrast, brightness, and details using PIL. All processed images are saved in a specified output directory.

## Features

- **Grayscale Conversion**: Converts the image to grayscale.
- **Histogram Equalization**: Applies histogram equalization to improve the image's contrast.
- **Gaussian Blur**: Applies Gaussian blur to reduce image noise.
- **Median Blur**: Uses median blur for noise reduction while preserving edges.
- **Bilateral Filter**: Applies bilateral filtering for edge-preserving smoothing.
- **Sharpness Enhancement**: Increases the sharpness of the image.
- **Contrast Enhancement**: Increases the contrast of the image.
- **Brightness Enhancement**: Adjusts the brightness of the image.
- **Edge Enhancement**: Applies an edge enhancement filter to highlight edges in the image.
- **Detail Enhancement**: Enhances the fine details of the image.
- **Unsharp Masking**: Applies unsharp masking to sharpen the image.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- OpenCV
- Pillow (PIL)
- NumPy

To install the required libraries, run:

```bash
pip install opencv-python pillow numpy
```

## Usage

1. **Set Input and Output Paths**: 
   - Change the `image_path` variable to the path of your input image.
   - Change the `output_path` variable to the directory where you want to save the processed images. Ensure that the output path ends with a backslash (`\\`).

2. **Run the Script**:
   - The script will apply multiple filters and save the resulting images to the output directory.

### Example Code Snippet:

```python
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# Load the image
image_path = 'C:\\Users\\hp\\Desktop\\k\\1.PNG'
output_path = 'C:\\Users\\hp\\Desktop\\k\\out\\'

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
```

## Output

The script will generate and save the following filtered images in the specified output directory:

- `gray.png`: Grayscale version of the input image.
- `equalized.png`: Histogram equalized version of the input image.
- `gaussian_blur.png`: Image with Gaussian blur applied.
- `median_blur.png`: Image with median blur applied.
- `bilateral_filter.png`: Image with bilateral filter applied.
- `sharpness.png`: Image with enhanced sharpness.
- `contrast.png`: Image with enhanced contrast.
- `brightness.png`: Image with enhanced brightness.
- `edge_enhance.png`: Image with edge enhancement filter applied.
- `detail.png`: Image with detail enhancement filter applied.
- `unsharp_mask.png`: Image with unsharp mask applied.

## Notes

- Ensure the image path and output path are correctly specified in the script.
- The script applies multiple filters to the same image, which may result in large files being generated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
