# MetalGuard 🛡️⚔️

**MetalGuard** is a lightweight Python script designed to demonstrate the fundamentals of **Purple Teaming** by combining a basic network attack simulation (Port Scanning) with a real-time behavioral defense monitor (IDS-lite).

---

## 🚀 About The Project

In cybersecurity, understanding both offensive techniques and defensive mechanisms is crucial. This project runs two concurrent threads:
1. **The Attacker (Red Side):** Simulates rapid connection attempts/port scanning against a target.
2. **The Defender (Blue Side):** Listens on a local socket, tracks incoming connection frequencies, and triggers alerts when suspicious rapid scanning patterns are detected.

---

## ✨ Features

- **Concurrent Execution:** Uses Python's `threading` to run the server (defense) and client (attack) simultaneously.
- **Behavioral Detection:** Tracks request timestamps per IP address to detect aggressive socket flooding rather than relying purely on static signatures.
- **Pure Python Standard Library:** Built entirely using native modules (`socket`, `time`, `threading`) without requiring external heavy dependencies.

---

## 🛠️ How It Works

1. **The Defense Server:** Binds to `127.0.0.1:9999` and accepts incoming TCP connections. It logs every IP and maintains a sliding window of recent connection timestamps. If an IP exceeds a specific threshold (e.g., >4 attempts in 3 seconds), it fires an alert.
2. **The Attack Scanner:** Sends rapid sequential TCP connection probes to the target port with slight delays, simulating a fast reconnaissance scan.

---

## 🚀 Getting Started & Usage

### Prerequisites
Make sure you have **Python 3** installed on your system (Linux, macOS, or Windows).

### Running the Script
Clone the repository and run the script directly using your terminal:

```bash
git clone 
cd MetalGuard
python3 MetalGuard.py
