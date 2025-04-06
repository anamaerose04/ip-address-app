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

# Function to get geolocation information (Mock Data Placeholder) - Ana
def get_mock_geolocation(ip):
    mock_data = {
        "192.168.0.1": {"country": "US", "city": "New York", "org": "Local Network"},
        "8.8.8.8": {"country": "US", "city": "Mountain View", "org": "Google"},
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334": {"country": "US", "city": "Los Angeles", "org": "Google"}
    }
    return mock_data.get(ip, {"country": "Unknown", "city": "Unknown", "org": "Unknown"})

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
