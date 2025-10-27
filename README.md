# Deadface
All of the challenges I made to DEADFACE CTF. Have fun and keep it legal :)

Challenges are organized by category:
- /web/        → Web exploitation challenges (XSS, SQLi, etc.)
- /pwn/        → Binary exploitation & memory-safety challenges
- /reverse/    → Reverse engineering puzzles
- /crypto/     → Cryptography challenges
- /forensics/  → Log analysis, PCAPs, disk images, etc.
- /misc/       → Everything else that doesn't fit neatly above
- /writeups/   → Official walkthroughs (released after CTF)

Each challenge directory includes:
- Docker compose, Source code or artifacts to deploy/play the challenge
- A README explaining the goal & deployment instructions

---
## 🚀 How to Run a Challenge

Web and SQL challenges support Docker for quick deployment:
```bash
cd web/<challenge_name>
docker compose up --build
```
Look at the .env file for ports.

# Credits
Created by: Bugged System
Originally developed for [DEADFACE CTF](https://ctf.deadface.io/).

Thanks to all testers, organizers, and players!

See LICENSE files for full details.

PEACE!
