
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
            pass  # create empty file

    with open(file_path, "r") as f:
        for line in f:
            p = line.strip()
            if p.isdigit() and len(p) == 4:
                passwords.append(p)
            elif p:  # show malformed entries but continue
                print(f"[WARN] Ignoring malformed password in file: '{p}' (must be 4 digits)")
    return passwords

def display_status(alarm_status: str, alarm_armed_status: str):
    print(f"\n--- System Status ---")
    print(f"alarm_status       : {alarm_status}")
    print(f"alarm_armed_status : {alarm_armed_status}")
    print(f"---------------------\n")

def main():
    # 1) Initialization per flowchart
    alarm_status = "OFF"         # Alarm initially calm
    alarm_armed_status = "ON"    # System is armed and expects a password
    password_attempts = 3        # User gets 3 tries

    passwords_file = "passwords.txt"
    valid_passwords = load_passwords(passwords_file)

    # If no passwords exist, we can optionally seed one for demo purposes.
    if not valid_passwords:
        demo_password = "1234"
        with open(passwords_file, "a") as f:
            f.write(demo_password + "\n")
        valid_passwords.append(demo_password)
        print(f"[INFO] No passwords found. Seeded demo password: {demo_password}")

    # 2) Prompt user per flowchart
    print("Enter your 4-digit password:")

    while True:
        # Early exit conditions (alarm triggered or disarmed)
        if alarm_status == "ON":
            # Alarm already active; display and end
            display_status(alarm_status, alarm_armed_status)
            break
        if alarm_armed_status == "OFF":
            # System already disarmed; display and end
            display_status(alarm_status, alarm_armed_status)
            break

        raw = input("> ").strip()

        # 3) Convert Keyboard ASCII to number (we still keep string to preserve leading zeros)
        # Validate format (4 digits only)
        is_valid_number = raw.isdigit() and len(raw) == 4

        if not is_valid_number:
            # 4) Display "Invalid Password" (format error)
            print("Invalid Password (must be 4 digits).")
            # 5) Decrement attempts
            password_attempts -= 1
        else:
            # Valid 4-digit number entered
            # 6) Reset the password_attempts counter? 
            # The flowchart shows a "Reset the password_attempts counter" box connected to "Valid Number".
            # Interpretation: reset only after a successful match; otherwise decrement on wrong code.
            # We'll proceed to check; if wrong, we decrement; if right, we disarm (and attempts don't matter).
            pass

            # 7) Create/Load password list (already loaded), then check password
            entered_password = raw  # keep string to preserve leading zeros
            if entered_password in valid_passwords:
                # Password Match
                alarm_status = "OFF"          # 1) set alarm_status to off
                alarm_armed_status = "OFF"    # 2) set alarm_armed_status to off
                print("Password accepted. System disarmed.")
                display_status(alarm_status, alarm_armed_status)
                break
            else:
                # Incorrect Password
                print("Incorrect Password.")
                password_attempts -= 1

        # 8) Password Attempts check
        if password_attempts <= 0:
            # set alarm_status to ON and display
            alarm_status = "ON"
            print("Too many failed attempts. Alarm ACTIVATED!")
            display_status(alarm_status, alarm_armed_status)
            break
        else:
            # Show remaining attempts for user feedback
            print(f"Attempts remaining: {password_attempts}")

if __name__ == "__main__":
