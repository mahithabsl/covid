import geocoder
import requests	
from ipregistry import IpregistryClient
g = geocoder.ip('me')
print(g.latlng)

def display_ip():
    """  Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})

display_ip()


# client = IpregistryClient("tryout")  
# ipInfo = client.lookup() 
# print(ipInfo)
res=requests.get("https://ipinfo.io/")
data=res.json()
location=data['loc'].split(',')
latitude=location[0]
longitude=location[1]
print(latitude,longitude)
