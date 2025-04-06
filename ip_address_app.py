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

# Function to get geolocation information (Mock Data Placeholder)
def get_geolocation(ip):
    # Placeholder for future geolocation logic (e.g., API call or mock data)
    geo_info = {"country": "Unknown", "city": "Unknown", "org": "Unknown"}
    return geo_info

# Function to print geolocation information
def print_geolocation(geo_info):
    print(f"Geolocation: {geo_info['country']}, {geo_info['city']}, {geo_info['org']}")

# Main function
def main():
    print("=== IP Geolocation App ===")
    while True:
        ip_input = input("Enter an IP address (IPv4 or IPv6) or 'exit' to quit: ")

        if ip_input.lower() == 'exit':
            print("Exiting the application.")
            break

        if validate_ip(ip_input):
            geo_info = get_geolocation(ip_input)
            print_geolocation(geo_info)
        else:
            print("Invalid IP address.")

# Run the main function
main()
