import os, socket, json

def ip_track(ip):
    if ip == "":
        ip = socket.gethostbyname(socket.gethostname())
    else:
        ip = ip
    ip_response = json.loads(requests.get("http://ip-api.com/json/"+ip).content.decode("utf-8"))
	
    ipTrack = ""
    ipTrack += "IP: " + ip_response["query"] + "\n"
    ipTrack += "Country: " + ip_response["country"] + "\n"
    ipTrack += "Country Code: " + ip_response["countryCode"] + "\n"
    ipTrack += "Region: " + ip_response["regionName"] + "\n"
    ipTrack += "City: " + ip_response["city"] + "\n"
    ipTrack += "Zip: " + ip_response["zip"] + "\n"
    ipTrack += "Time Zone: " + ip_response["timezone"] + "\n"
    ipTrack += "ISP: " + ip_response["isp"] + "\n"
    ipTrack += "Organization: " + ip_response["org"] + "\n"
    ipTrack += "AS: " + ip_response["isp"] + "\n"
    ipTrack += "Latitude: " + str(ip_response["lat"]) + "\n"
    ipTrack += "Longitude : " + str(ip_response["lon"]) + "\n"
    print(ipTrack)

os.system("clear")
ipAddress = input("Enter IP Address: ")
ip_track(ipAddress)
