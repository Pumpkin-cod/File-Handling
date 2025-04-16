#!/usr/bin/env python3
import time
import psutil
from mailjet_rest import Client

# Mailjet credentials
api_key = "31f1a73cba6668109b37120323477246"
api_secret = "825dfe9350eb9cb715d2bceae43c794e"

#Defining system thresholds
CPU_THRESHOLD = 2  # Percentage
RAM_THRESHOLD = 10  # Percentage
DISK_THRESHOLD = 50  # Percentage

#Function to send threshold email alerts
def send_alert(subject, message):
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    
    data = {
        'Messages': [{
            "From": {
                "Email": "catherine.gyamfi@amalitechtraining.org",
                "Name": "24/7 System Monitor"
            },
            "To": [{
                "Email": "catherine.gyamfi@amalitechtraining.org",
                "Name": "Admin"
            }],
            "Subject": subject,
            "HTMLPart": f"<h3>{message}</h3>"
        }]
    }
    
    try:
        response = mailjet.send.create(data=data)
        print(f"Email sent: {response.status_code}")
    except Exception as e:
        print(f"Email failed: {str(e)}")

# Getting formatted time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

# Collect metrics
cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# Build alert message
alert_message = ""
if cpu_usage > CPU_THRESHOLD:
    alert_message += f"🚨 CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"

if ram_usage > RAM_THRESHOLD:
    alert_message += f"🚨 RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"

if disk_usage > DISK_THRESHOLD:
    alert_message += f"🚨 Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}%)\n"

# Send alert if needed
if alert_message:
    send_alert(f"System Alert - {formatted_time}", alert_message)
else:
    print(f"{formatted_time} - All systems normal")
