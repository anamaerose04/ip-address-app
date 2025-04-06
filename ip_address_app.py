# Team Name: SIMS
# Members:
# Ana Mae Rose Cagang
# Adona Eve Hijara
# Kimberly Mahilum
# Nica Mapula

import requests
import ipaddress
import json

# Function to validate IP address (IPv4/IPv6)
def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Feature 1: Real Geolocation – Fetch Geolocation from IPInfo API - Ana
def get_real_geolocation(ip):
    access_token = '993c1395f3847f'  # Your IPInfo API token
    url = f"https://ipinfo.io/{ip}/json?token={access_token}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            country = data.get('country', 'Unknown')
            city = data.get('city', 'Unknown')
            org = data.get('org', 'Unknown')
            return {"country": country, "city": city, "org": org}
        else:
            print(f"Failed to retrieve geolocation for {ip}. Status Code: {response.status_code}")
            return {"country": "Unknown", "city": "Unknown", "org": "Unknown"}
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return {"country": "Unknown", "city": "Unknown", "org": "Unknown"}

# Feature 2: Output as JSON – Print Results in JSON Format - Adona
def output_as_json(geo_info):
    return json.dumps(geo_info, indent=4)

# Feature 3: Save Search History – Save the IP Search Results to a File - Nica
def save_search_history(ip, geo_info):
    with open("geo_history.txt", "a") as f:
        f.write(f"IP: {ip} - Geolocation: {output_as_json(geo_info)}\n")
    print("Search history saved.")

# Feature 4: Search History Display – View the Saved Search History - Kim
def display_search_history():
    try:
        with open("geo_history.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No search history found.")

# Feature 5: Use OpenStreetMap Nominatim to Reverse Geocode Coordinates
def reverse_geocode(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}"
    headers = {
        "User-Agent": "IP-Geolocation-App"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            address = data.get("address", {})
            city = address.get("city") or address.get("town") or address.get("village") or "Unknown"
            country = address.get("country", "Unknown")
            return {"city": city, "country": country}
        else:
            print(f"Failed to reverse geocode coordinates. Status Code: {response.status_code}")
            return {"city": "Unknown", "country": "Unknown"}
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return {"city": "Unknown", "country": "Unknown"}

# Main function
def main():
    print("=== IP Geolocation App ===")
    while True:
        ip_input = input("Enter an IP address (IPv4 or IPv6) or 'exit' to quit: ")

        if ip_input.lower() == 'exit':
            print("Exiting the application.")
            break

        if validate_ip(ip_input):
            geo_info = get_real_geolocation(ip_input)
            print(output_as_json(geo_info))  # Print geolocation as JSON
            save_search_history(ip_input, geo_info)  # Save search history
        else:
            print("Invalid IP address.")

        show_history = input("Would you like to see the search history? (yes/no): ").lower()
        if show_history == "yes":
            display_search_history()

        if input("Would you like to reverse geocode coordinates? (yes/no): ").lower() == "yes":
            lat = input("Enter latitude: ")
            lon = input("Enter longitude: ")
            geo_info = reverse_geocode(lat, lon)
            print(output_as_json(geo_info))

# Run the main function
if __name__ == "__main__":
    main()