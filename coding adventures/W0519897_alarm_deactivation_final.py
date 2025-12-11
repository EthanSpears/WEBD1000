import sys
import time
import getpass
import os

PASSWORD_FILE = "passwords.txt" 
MAX_ATTEMPTS = 3               
LOCKOUT_SECONDS = 20            

def load_passcodes(path: str):
    codes = set()
    if not os.path.exists(path):
        print(f"Password file not found: {path}")
        return codes

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue
            code = raw.replace(" ", "") 
            if len(code) == 5 and code.isdigit():
                codes.add(code)
            else:
                print(f"Skipping invalid code in file: '{raw}' (must be 5 digits)")
    return codes

def prompt_for_code(hidden: bool = True) -> str:
    """Prompt user for a 5-digit code; input is hidden if possible."""
    prompt = "\nEnter 5-digit passcode: "
    if hidden:
        try:
            code = getpass.getpass(prompt)
        except Exception:
            code = input(prompt)
    else:
        code = input(prompt)
    return code.strip()

def run_alarm():
    valid_codes = load_passcodes(PASSWORD_FILE)
    if not valid_codes:
        print("No valid passcodes loaded. Add 5-digit codes to passwords.txt and try again.")
        return

    print(f"Alarm ACTIVE! {len(valid_codes)} passcode(s) loaded. Enter 5-digit code to disarm.")

    attempts = 0
    while True:
        code = prompt_for_code(hidden=True)
        if len(code) != 5 or not code.isdigit():
            print("Invalid format. Passcode must be exactly 5 digits.")
            continue

        if code in valid_codes:
            print("\nCorrect code. Alarm disarmed.")
            break
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"Wrong code. Attempts left: {remaining}.")
            else:
                print(f"Too many failed attempts. Locked for {LOCKOUT_SECONDS} seconds.")
                lockout_end = time.time() + LOCKOUT_SECONDS
                while time.time() < lockout_end:
                    remaining_lock = int(lockout_end - time.time())
                    sys.stdout.write(f"\rLockout: {remaining_lock} seconds remaining ")
                    sys.stdout.flush()
                    time.sleep(0.5)
                print("\nLockout ended. You may try again.")
                attempts = 0  

    print("Program finished.")

if __name__ == "__main__":
    try:
        run_alarm()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")

