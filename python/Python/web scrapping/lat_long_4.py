import requests
geo_url = 'http://maps.googleapis.com/maps/api/geocode/json'
address = {'address':"Pride Appartments,  Banerghatta Main Road, Bengaluru, Karnataka, India", 'language':'en'}
resp = requests.get(geo_url, params=address)
print(resp.text)