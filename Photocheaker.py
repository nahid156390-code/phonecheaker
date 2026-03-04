import os
import time
from datetime import datetime

# --- Security Config ---
# Aapka Account aur Token verification ke liye
ACCOUNT_ID = "AC76b2bde6569c5fefb1ad2bbca8cd628d"
AUTH_TOKEN = "71426b6771aef7b779bc123a8edba680"

# Camera folder ka path (Termux storage setup hona chahiye)
path_to_watch = "/sdcard/DCIM/Camera" 

print(f"--- CAMERA GUARD ACTIVE ---")
print(f"User: {ACCOUNT_ID}")
print(f"Monitoring: {path_to_watch}")
print("Press CTRL+C to stop.")

def monitor_camera():
    # Pehle se maujood files ki list
    initial_files = os.listdir(path_to_watch)
    
    while True:
        current_files = os.listdir(path_to_watch)
        # Check agar koi naya photo add hua hai
        new_files = [f for f in current_files if f not in initial_files]
        
        if new_files:
            for f in new_files:
                print(f"[!!!] ALERT: Naya photo detect hua: {f}")
                print(f"Time: {datetime.now()}")
            # List update karein
            initial_files = current_files
        
        time.sleep(2) # Har 2 second mein check karega

if __name__ == "__main__":
    try:
        # Termux ko storage access dena zaroori hai
        # Command: termux-setup-storage
        monitor_camera()
    except PermissionError:
        print("Error: Termux ko storage ki permission nahi hai. 'termux-setup-storage' chalayein.")
    except KeyboardInterrupt:
        print("\nGuard stopped.")
