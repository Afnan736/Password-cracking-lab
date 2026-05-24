# Password-cracking-lab
A hands-on lab simulating a corporate data breach. Generated MD5, SHA256, and bcrypt password hashes for 20 fictional users, cracked them using Hashcat and John the Ripper with the rockyou wordlist, and analysed the results from a purple team perspective including defensive recommendations on password storage, policies, and detection
## Purple Team Analysis – JTR and Hashcat

## Overview
A simulated company data breach scenario where 20 user password hashes 
were extracted and cracked to analyse the real-world impact of weak 
hashing algorithms and poor password choices.

---

## Tools Used
- Python 3 (hashlib, bcrypt) — hash generation
- John the Ripper (JTR) — dictionary cracking
- Hashcat — GPU-accelerated cracking
- rockyou.txt — wordlist
- Kali Linux — attack environment

---

## Scenario
A fictional company database of 20 users was compromised.
Passwords were stored using MD5, SHA256, and bcrypt.
This lab simulates what an attacker would do with stolen hashes 
and the real defensive impact of each algorithm.

---
# Project Structure

```bash
Password-cracking-lab/
├── hashgen.py                 # Generates password hashes
├── hashes_md5.txt             # MD5 hash dataset
├── hashes_sha256.txt          # SHA256 hash dataset
├── hashes_bcrypt.txt          # bcrypt hash dataset
├── results/
│   ├── jtr_results.txt        # John the Ripper cracking results
│   └── hashcat_results.txt    # Hashcat cracking results
├── screenshots/               # Terminal screenshots and evidence
└── README.md
```

---
## Results
```
| Algorithm | Tool    | Cracked | Total | Speed        | Time            |
|-----------|---------|---------|-------|--------------|-----------------|
| MD5       | JTR     | 13      | 20    | Extremely fast | Seconds       |
| SHA256    | JTR     | 13      | 20    | Very fast    | Seconds         |
| bcrypt    | JTR     | 10      | 20    | Very slow    | ~6 minutes      |
| MD5       | Hashcat | 13      | 20    | ~7433 kH/s   | ~2 seconds      |
| SHA256    | Hashcat | 13      | 20    | ~6270 kH/s   | ~3 seconds      |
| bcrypt    | Hashcat | 8       | 20    | ~31 H/s      | 63–72 days est. |

**Key finding: 65% of accounts compromised in seconds using a 
standard dictionary attack on a personal laptop.**
```
---

## Why Attackers Want Password Hashes
Hashes can become real credentials. Cracked hashes give attackers:
- Direct account access
- Password reuse across other platforms
- Privilege escalation opportunities
- Credential stuffing at scale

The hash database is often more valuable than the application itself.

---

## Pattern Analysis
Passwords that cracked shared predictable patterns:
```
| Pattern                   | Example          |
|---------------------------|---------         |
| Keyboard patterns         | qwerty           |
| Sequential numbers        | 123456           |
| Dictionary words          | monkey, football |
| Simple suffixes           | abc123           |
| Weak complexity tricks    | password123      |
| Basic capitalisation      | Welcome1         |
| Predictable substitutions | P@ssw0rd         |

**Key insight: Complexity alone does not equal strength.
Attackers already expect @ instead of a, 0 instead of o.**
```
---

## Simulated Real-World Impact

**Within seconds:** All MD5 and SHA256 weak passwords cracked

**Within minutes:** Employee email, VPN, and admin account access gained

**Within hours:** Ransomware deployment, internal phishing, data theft

At 65% compromise rate, lateral movement becomes trivial.

---

## Why bcrypt Resisted
```
| Algorithm |          Speed        |    Security Leve     |
|-----------|-----------------------|----------------------|
| MD5       | ~7,433,000 hashes/sec | Weak                 |
| SHA256    | ~6,270,000 hashes/sec | Weak without salting |
| bcrypt    | ~31 hashes/sec        |Strong                |
```
bcrypt is intentionally slow, automatically salted, and supports 
configurable work factors. Estimated full crack time: 63–72 days.

Real attackers abandoned bcrypt because the ROI was too low.
That is the goal — economically painful security, not impossible security.

---

## Why Salting Matters
Without salts:
- Identical passwords produce identical hashes
- Rainbow table attacks become trivial
- One crack applies to multiple users

With bcrypt salting:
- Each hash is unique even for identical passwords
- Precomputed attacks become ineffective
- Cracking must be done per user

---

## Purple Team Analysis

### What went wrong
- Passwords stored as unsalted MD5 and SHA256
- No password policy blocking common passwords
- No detection of the breach or unusual access patterns

### What companies should do
- Use bcrypt with cost factor 12 or higher
- Add unique salts to every password hash
- Enforce minimum 12+ character passwords
- Block known leaked passwords on registration
- Implement MFA — cracked passwords become less useful
- Consider Argon2id as the modern gold standard

### How to detect credential stuffing
- Alert on 5+ failed logins from the same IP
- Flag successful login after multiple failures
- Monitor for impossible travel patterns
- Detect automated user-agent patterns
- Correlate login spikes with breach intelligence feeds

---

## Limitations of This Lab
- Dataset of 20 users is small
- No GPU acceleration demonstrated
- No Argon2 or scrypt comparison
- No entropy scoring
- No rule-based mutation attacks

Future improvements: entropy analysis, GPU benchmarks, 
Argon2 comparison, credential stuffing simulation, SIEM log examples.

---

## Lessons Learned
- MD5 and SHA256 are unsuitable for password storage
- bcrypt resists cracking because it is deliberately slow
- Password length and randomness matter more than complexity rules
- Even bcrypt cannot protect trivially weak passwords
- Human password behaviour is predictable and exploitable

# Disclaimer

This project was created for:
- cybersecurity education
- defensive security research
- password security awareness

No unauthorized systems or real credentials were targeted.
