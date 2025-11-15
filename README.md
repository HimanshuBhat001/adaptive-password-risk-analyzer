# Adaptive Password Risk Analyzer (APRA)

A cybersecurity project that analyzes password strength using entropy, leaked-pattern detection, human-behavior analysis, keyboard-sequence recognition, and brute-force cracking time simulation.  
This tool generates a risk score (0–100) and categorizes passwords as **Low**, **Medium**, or **High Risk**.

---

## 🔍 Features

- Entropy-based password evaluation  
- Detection of leaked/common password patterns  
- Identification of human behavior patterns  
  - Starts with uppercase  
  - Ends with numbers  
- Keyboard-sequence detection (qwerty, asdf, zxcv, 1234, etc.)  
- Repetition pattern detection (aaa, 111, $$$)  
- Dictionary word detection  
- Estimation of brute-force crack time on:
  - CPU-level cracking  
  - GPU-level cracking  
  - Botnet-scale cracking  
- Final Risk Score (0–100)  
- Risk Category Classification (Low / Medium / High)

---

## 🛠️ Installation

Make sure Python 3 is installed.

Clone the repository:

