import psutil
import time
from plyer import notification
import platform

def check_battery_status():
    # Check if the system has a battery
    if not hasattr(psutil.sensors_battery(), 'percent'):
        print("This system doesn't have a battery.")
        return False
    
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged
    
    print(f"Current battery level: {percent}% | Plugged in: {plugged}")
    
    if plugged and percent >= 100:
        return True
    return False

def send_notification():
    title = "Battery Fully Charged"
    message = "Your system battery has reached 100%. Please unplug the charger."
    
    notification.notify(
        title=title,
        message=message,
        app_name="Battery Monitor",
        timeout=10
    )

def main():
    print("Battery monitor started. Waiting for 100% charge...")
    
    while True:
        if check_battery_status():
            send_notification()
            print("Notification sent for 100% charge!")
            # Wait for 30 minutes before checking again to avoid spamming
            time.sleep(1800)
        else:
            # Check every 30 second
            time.sleep(30)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBattery monitor stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
