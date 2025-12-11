
import os

def load_passwords(file_path: str) -> list[str]:
    """
    Reads a list of valid 4-digit passwords from passwords.txt.
    Ignores empty lines and trims whitespace. Enforces 4-digit format.
    """
    passwords = []
    if not os.path.exists(file_path):
        print(f"[WARN] '{file_path}' not found. Creating an empty file.")
        with open(file_path, "w") as f:
            pass  

    with open(file_path, "r") as f:
        for line in f:
            p = line.strip()
            if p.isdigit() and len(p) == 4:
                passwords.append(p)
            elif p:  
                print(f"[WARN] Ignoring malformed password in file: '{p}' (must be 4 digits)")
    return passwords


def display_status(alarm_status: str, alarm_armed_status: str):
    print(f"\n--- System Status ---")
    print(f"alarm_status       : {alarm_status}")
    print(f"alarm_armed_status : {alarm_armed_status}")
    print(f"---------------------\n")

def main():
alarm_status = "OFF"      
alarm_armed_status = "ON"    
password_attempts = 3        
    
passwords_file = "passwords.txt"
valid_passwords = load_passwords(passwords_file)

print("Enter your 5-digit password:")
    
while True:
        if alarm_status == "ON":
            display_status(alarm_status, alarm_armed_status)
            break
        if alarm_armed_status == "OFF":
            display_status(alarm_status, alarm_armed_status)
            break

raw = input("> ").strip()
        
is_valid_number = raw.isdigit() and len(raw) == 5

if not is_valid_number:
            print("Invalid Password (must be 5 digits).")
            password_attempts -= 1
else:
    pass
    entered_password = raw  # keep string to preserve leading zeros
    if entered_password in valid_passwords:
        alarm_status = "OFF"          # 1) set alarm_status to off
        alarm_armed_status = "OFF"    # 2) set alarm_armed_status to off
        print("Password accepted. System disarmed.")
        display_status(alarm_status, alarm_armed_status)
        
    else:
                print("Incorrect Password.")
                password_attempts -= 1

    if password_attempts <= 0:
            # set alarm_status to ON and display
            alarm_status = "ON"
            print("Too many failed attempts. Alarm ACTIVATED!")
            display_status(alarm_status, alarm_armed_status)
            
    else:
            # Show remaining attempts for user feedback
            print(f"Attempts remaining: {password_attempts}")

if __name__ == "__main__":
     main()