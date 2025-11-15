# APRA – Adaptive Password Risk Analyzer

APRA (Adaptive Password Risk Analyzer) is a cybersecurity tool that evaluates password risk using entropy analysis, leaked-pattern detection, human-behavior pattern recognition, keyboard-sequence checks, dictionary weaknesses, and brute-force cracking time simulation.

It generates:
- A **Risk Score (0–100)**
- A **Risk Category (Low / Medium / High)**
- Detailed **flags** explaining weaknesses
- Estimated **crack time** for CPU, GPU, and botnet-level attacks

---

## 🔒 Features

- **Entropy-based strength evaluation**
- **Detection of leaked/common password patterns**
- **Human behavior pattern analysis**
  - Starts with uppercase
  - Ends with numbers
- **Keyboard sequence detection** (qwerty, asdf, zxcv, 1234)
- **Repetition pattern detection** (aaa, 111, $$$)
- **Dictionary word detection**
- **Brute-force crack time estimation** for:
  - CPU
  - GPU
  - Botnet (distributed attack)
- **Final risk score & category** with explanations

---

## 🛠️ Installation

Ensure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/HimanshuBhat001/adaptive-password-risk-analyzer
```

Navigate into the project:

```bash
cd adaptive-password-risk-analyzer
```

---

## ▶️ How to Run

Execute the main analyzer script:

```bash
python src/password_risk_analyzer.py
```

Enter a password when prompted.

---

## 📄 Sample Output

```
=== ADAPTIVE PASSWORD RISK REPORT ===
Risk Category: Medium Risk
Risk Score: 62
Entropy: 41.2 bits

Flags:
- Contains dictionary word
- Human pattern: Ends with numbers

Estimated crack time:
CPU: 44.53 seconds
GPU: <1 second
Botnet: <1 second
```

More examples can be found in `/examples/sample_output.txt`.

---

## 🧠 Project Structure

```
adaptive-password-risk-analyzer/
│
├── src/
│   └── password_risk_analyzer.py      # Main analyzer script
│
├── docs/
│   └── overview.md                    # Technical explanation
│
├── examples/
│   └── sample_output.txt              # Sample output from tool
│   └── .keep
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📘 Documentation

A detailed technical overview is available at:

```
docs/overview.md
```

Covers:
- Entropy calculation logic  
- Pattern detection methods  
- Risk scoring algorithm  
- Attack simulation model  

---

## 🚀 Future Enhancements

- GUI-based desktop version  
- Web interface using Flask  
- Integration with real leaked-password APIs  
- Machine-learning based password prediction patterns  

---

## 👤 Author

**Himanshu Bhat**  
Cybersecurity | Python | Networking | Cloud  

---

## 📄 License

Licensed under the **MIT License**.

