# Vulnerable OTP Authentication System
import random
import time

# Simulated user database
users = {"user1": {"phone": "+923409777222", "otp": None, "otp_time": None}}

# Generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Send OTP (simulated)
def send_otp(phone):
    otp = generate_otp()
    users["user1"]["otp"] = otp
    users["user1"]["otp_time"] = time.time()
    print(f"OTP sent to {phone}: {otp}")
    return otp

# Vulnerable OTP validation
def validate_otp(username, input_otp):
    user = users.get(username)
    if not user:
        return False
    # Flaw 1: No rate limiting on OTP attempts
    # Flaw 2: OTP not tied to user session
    # Flaw 3: Long OTP expiration time (e.g., 10 minutes)
    if user["otp"] == input_otp and (time.time() - user["otp_time"]) < 600:
        print("OTP validated successfully!")
        return True
    return False

# Simulate hacker exploiting the system
def exploit_otp_bypass(username, phone):
    # Step 1: Trigger OTP generation
    send_otp(phone)
    
    # Step 2: Brute-force OTP (no rate limiting)
    for guess in range(100000, 1000000):  # Trying all 6-digit OTPs
        if validate_otp(username, str(guess)):
            print(f"Success! Bypassed OTP: {guess}")
            return True
    print("Failed to bypass OTP")
    return False

# Example usage
if __name__ == "__main__":
    username = "user1"
    phone = users[username]["phone"]
    
    # Simulate legitimate user flow
    print("Legitimate user flow:")
    otp = send_otp(phone)
    validate_otp(username, otp)
    
    # Simulate hacker exploiting the system
    print("\nHacker exploiting system:")
    exploit_otp_bypass(username, phone)