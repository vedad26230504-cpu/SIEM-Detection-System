# install library 
pip install geoip2

# add ip-api 
import requests

def get_country(ip):
    if ip.startswith("192.") or ip.startswith("10.") or ip.startswith("172."):
        return "Private Network"
    
    try:
        import requests
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        
        return data.get("country", "Unknown")
    
    except:
        return "Unknown"

#test ip - API 
print(get_country("8.8.8.8"))

