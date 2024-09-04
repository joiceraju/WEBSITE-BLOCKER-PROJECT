
import time
from datetime import datetime as dt

# Path to the hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Windows path
# hosts_path = "/etc/hosts"  # Mac/Linux path

redirect_ip = "127.0.0.1"
# List of websites to block
websites_to_block = ["www.facebook.com","www.instagram.com"]

# Specify blocking hours (e.g., 8 AM to 4 PM)
start_hour = 15
end_hour = 18

while True:
    # Check current time
    current_time = dt.now()

    if start_hour <= current_time.hour < end_hour:
        print("Working hours... Blocking websites")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in websites_to_block:
                if website not in content:
                    file.write(f"{redirect_ip} {website}\n")
    else:
        print("Outside working hours... Unblocking websites")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_to_block):
                    file.write(line)
            file.truncate()

    # Wait 5 minutes before checking again
        time.sleep(5)