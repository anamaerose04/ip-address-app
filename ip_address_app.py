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

# Feature 1: Mock Geolocation - Ana
def get_mock_geolocation(ip):
    mock_data = {
        "192.168.0.1": {"country": "US", "city": "New York", "org": "Local Network"},
        "8.8.8.8": {"country": "US", "city": "Mountain View", "org": "Google"},
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334": {"country": "US", "city": "Los Angeles", "org": "Google"}
    }
    return mock_data.get(ip, {"country": "Unknown", "city": "Unknown", "org": "Unknown"})

# Feature 2: Output as JSON - Adona Eve
def output_as_json(geo_info):
    return json.dumps(geo_info, indent=4)

# Feature 3: Save Search History
def save_search_history(ip, geo_info):
    with open("geo_history.txt", "a") as f:
        f.write(f"IP: {ip} - Geolocation: {output_as_json(geo_info)}\n")
    print("Search history saved.")

# Feature 3: Search History Display
def display_search_history():
    try:
        with open("geo_history.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No search history found.")
    
# Function to print geolocation information
def print_geolocation(geo_info):
    print(output_as_json(geo_info))

# Main function
def main():
    print("=== IP Geolocation App ===")
    while True:
        ip_input = input("Enter an IP address (IPv4 or IPv6) or 'exit' to quit: ")

        if ip_input.lower() == 'exit':
            print("Exiting the application.")
            break

        if validate_ip(ip_input):
            geo_info = print_geolocation(ip_input)
            print_geolocation(geo_info)
            save_search_history(ip_input, geo_info)
        else:
            print("Invalid IP address.")
            show_history = input("Would you like to see the search history? (yes/no): ").lower()
            if show_history == "yes":
                display_search_history()
            
# Run the main function
main()
