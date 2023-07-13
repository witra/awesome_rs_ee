import ee
from awesome_rs_ee.rs_indices import ndvi_img

try:
    from keys import sensitive
    key = "../keys/ee_keys.json"
    service = sensitive.service_account
    credentials = ee.ServiceAccountCredentials(service, key)
    ee.Initialize(credentials, opt_url='https://earthengine-highvolume.googleapis.com')
except:
    ee.Authenticate()
    ee.Initialize()

def sample_img(img, xy=[45, 45]):
    # ref: https://developers.google.com/earth-engine/apidocs/ee-image-arraymask
    point = ee.Geometry.Point([xy[0], xy[1]])
    return img.toArray().sample(point, 100).first().get('array')
def test_ndvi_img():
    nir = ee.Image(5).rename("B8")
    red = ee.Image(15).rename("B4")
    sat_img = nir.addBands(red)
    sat_path = 'COPERNICUS/S2_SR_HARMONIZED'
    dividend = nir.subtract(red)
    divisor = nir.add(red)
    ndvi_true = dividend.divide(divisor)
    ndvi = ndvi_img(sat_img, sat_path)
    assert sample_img(ndvi_true, [10, 10]).getInfo() == sample_img(ndvi, [10, 10]).getInfo()
