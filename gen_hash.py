import hashlib
import bcrypt

user_pass = [
    ("alice", "password123"),
    ("bob", "Summer2024!"),
    ("charlie", "qwerty"),
    ("diana", "iloveyou"),
    ("edward", "P@ssw0rd"),
    ("fatima", "123456"),
    ("george", "Tr0ub4dor&3"),
    ("hannah", "letmein"),
    ("ibrahim", "Monday1!"),
    ("jessica", "correct-horse-battery"),
    ("karen", "abc123"),
    ("liam", "Welcome1"),
    ("maria", "sunshine"),
    ("noah", "Dragon2023!"),
    ("olivia", "monkey"),
    ("peter", "Xk9#mP2$vL"),
    ("queen", "football"),
    ("rachel", "Qr7!nX2@wP9"),
    ("sam", "pass"),
    ("tanya", "MyD0g$N4me!"),
]

print("=" * 60)
print("COMPANY USER HASH DATABASE - SIMULATED BREACH")
print("=" * 60)

with open("hashes_md5.txt", "w") as md5_file:
    for username, password in user_pass:
        md5 = hashlib.md5(password.encode()).hexdigest()
        md5_file.write(f"{username}:{md5}\n")

with open("hashes_sha256.txt", "w") as sha256_file:
    for username, password in user_pass:
        sha256 = hashlib.sha256(password.encode()).hexdigest()
        sha256_file.write(f"{username}:{sha256}\n")

with open("hashes_bcrypt.txt", "w") as bcrypt_file:
    for username, password in user_pass:
        bcrypt_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()
        ).decode()
        bcrypt_file.write(f"{username}:{bcrypt_hash}\n")

print(f"\n{'Username':<12} {'MD5':<35} {'SHA256':<65} {'bcrypt'}")
print("-" * 160)
for username, password in user_pass:
    md5 = hashlib.md5(password.encode()).hexdigest()
    sha256 = hashlib.sha256(password.encode()).hexdigest()
    bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print(f"{username:<12} {md5:<35} {sha256:<65} {bcrypt_hash}")

print("\n Files created:")
print("    hashes_md5.txt    — for Hashcat and John")
print("    hashes_sha256.txt — for Hashcat and John")
print("    hashes_bcrypt.txt — for Hashcat and John")
print("\n Hash generation complete.")