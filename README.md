# GrimGrim

_GrimGrim_ converts an image into cartoon style with openCV.

This python project is based on the following feature:
1. Decrease the noise through GaussianBlur and BilateralFilter.
2. Detect the edge with Canny algorithm.
3. Apply Kmeans algorithm to cluster the color. (K=7)
4. Apply the color to the edge. (bitwise_and)
5. Here's the cartoon-styled image!

## Condition of cartoon style
> The cel-shading process starts with a typical 3D model. Where cel-shading differs from conventional rendering is in its non-photorealistic shading algorithm. Conventional smooth lighting values are calculated for each pixel and then quantized to a small number of discrete shades to create the characteristic "flat look", where the shadows and highlights appear as blocks of color rather than being smoothly mixed in a gradient.
> _- Wikipedia, 'cel shading'_

Cartoon style generally refers to a way of depicting real-world images as if they were drawn, by simplifying the numerous shades created by natural shading into a limited number of colors and adding outlines that do not exist in reality. Although the term “cartoon rendering” is primarily used in 3D graphics, the concept applies to 2D images as well. However, if the color simplification is overly abstract, it may become difficult to recognize the shape and shading of objects. Similarly, an excessive number of outlines can distort the object’s form. Therefore, a well-converted cartoon-style image should have an appropriate number of color variations and outlines.

## Good example of cartoonizing
![cartoon](https://raw.githubusercontent.com/fallingflow/GrimGrim/refs/heads/main/data/image1.jpg)
![cartoon](https://raw.githubusercontent.com/fallingflow/GrimGrim/refs/heads/main/screenshots/image1_screenshot.png)
_“image1.jpg”_ is a good example of a well-applied cartoon style. The background and objects are clearly distinguished, and the object’s colors are free from excessive noise. As a result, the overall number of shading colors and outlines is appropriately balanced.

## Bad example of cartoonizing
![cartoon](https://raw.githubusercontent.com/fallingflow/GrimGrim/refs/heads/main/data/image2.jpg)
![cartoon](https://raw.githubusercontent.com/fallingflow/GrimGrim/refs/heads/main/screenshots/image2_screenshot.png)
_“image2.jpg”_ is a bad example of a cartoon style. The background and objects are not clearly distinguished, and the object’s colors are noisy. The excessive number of shading colors and outlines makes it difficult to recognize the object’s form.

## Limitations
An issue arose where outlines appeared even in areas where the color changes were not particularly extreme. For example, in _“image2.jpg”_, although the colors fall within the same color category and appear relatively uniform to the human eye, outlines are still generated at every striped boundary. As a result, when converted to a cartoon style, the image appears excessively noisy. This issue could be resolved by improving the algorithm so that outlines are created only when the color change around a reference point is significant, while avoiding unnecessary outlines in areas with subtle color variations.