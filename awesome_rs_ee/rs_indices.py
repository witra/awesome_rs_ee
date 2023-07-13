def ndvi_img(img, satellite_name):
    """
    Generate ndvi image from the multi-spectral satellite image.
    Formula:  NDVI = (NIR - red) / (NIR + red)
    Parameters
    ----------
    img: ee.image

    Returns
    -------
    ndvi img: ee.Image
    """
    if satellite_name == 'COPERNICUS/S2_SR_HARMONIZED':
        return img.normalizedDifference(['B8', 'B4']).rename('NDVI');
    else:
        raise Exception('The NDVI calculation for the specified satellite image is not provided yet or not available')
