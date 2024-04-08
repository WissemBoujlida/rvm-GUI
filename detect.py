import requests
def object_detection(img_file):
    URL_TO_OBJECT_DETECTION = "http://192.168.1.16/object_detection"
    response = requests.post(URL_TO_OBJECT_DETECTION, files=img_file)
    return response

def volume_brand_classification(img_file):
  URL_TO_VOLUME_BRAND_CLASSIFICATION = "http://192.168.1.16/volume_brand_classification"
  response = requests.post(URL_TO_VOLUME_BRAND_CLASSIFICATION, files=img_file)
  return response