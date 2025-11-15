import re
import math
import time

common_patterns = [
    "2024", "2023", "1234", "abcd", "password", "welcome",
    "user", "admin", "qwerty", "iloveyou", "letmein",
    "spring", "summer", "winter", "fall",
]

keyboard_sequences = ["qwerty", "asdf", "zxcv", "1234", "7890"]

def entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[@$!%*?&]", password): charset += 10
    if charset == 0: return 0
    return round(len(password) * math.log2(charset), 2)

def crack_time(ent):
    guesses_per_sec = {
        'CPU': 1e6,
        'GPU': 1e9,
        'Botnet': 1e12
    }
    times = {}
    for device, speed in guesses_per_sec.items():
        seconds = (2 ** ent) / speed
        if seconds < 1: times[device] = "<1 second"
        else: times[device] = f"{seconds:.2f} seconds"
    return times

def risk_score(ent, flags):
    base = 100 - ent
    base += len(flags) * 5
    return min(100, round(base, 2))

def analyze(password):
    flags = []

    # basic patterns
    for p in common_patterns:
        if p in password.lower():
            flags.append(f"Contains weak or leaked pattern: {p}")
            break

    # keyboard patterns
    for seq in keyboard_sequences:
        if seq in password.lower():
            flags.append("Contains keyboard pattern")
            break

    # human behavior patterns
    if password[0].isupper():
        flags.append("Human behavior pattern: Start with uppercase")
    if password[-1].isdigit():
        flags.append("Human pattern: Ends with numbers")

    # repetition
    if re.search(r"(.)\1\1", password):
        flags.append("Repetitive characters detected")

    # dictionary word
    dictionary_words = ["love", "god", "hello", "world", "test"]
    for word in dictionary_words:
        if word in password.lower():
            flags.append("Contains dictionary word")

    ent = entropy(password)
    cracking = crack_time(ent)
    score = risk_score(ent, flags)

    if score <= 40:
        category = "Low Risk (Strong)"
    elif score <= 70:
        category = "Medium Risk"
    else:
        category = "High Risk"

    return {
        "entropy": ent,
        "risk_score": score,
        "risk_category": category,
        "flags": flags,
        "cracking_time": cracking
    }

pwd = input("Enter password: ")
result = analyze(pwd)

print("\n=== ADAPTIVE PASSWORD RISK REPORT ===")
print("Risk Category:", result["risk_category"])
print("Risk Score:", result["risk_score"])
print("Entropy:", result["entropy"])
print("\nFlags:")
for f in result["flags"]:
    print("-", f)
print("\nEstimated crack time:")
for k, v in result["cracking_time"].items():
    print(k + ": " + v)
