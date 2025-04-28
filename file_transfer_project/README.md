# 🚀 Automated File Download & Upload using Selenium and OS Module

## 📌 Objective
This mini project demonstrates automation of:
- Downloading a file using Selenium
- Detecting the latest downloaded file using the `os` module
- Uploading the detected file back to another website using Selenium

All operations are performed **automatically** without any manual interaction!

---

## 🛠️ Technologies Used
- Python 3
- Selenium WebDriver
- OS module
- Firefox Browser + GeckoDriver

---

## 📂 Project Structure
```
file-transfer-project/
│
├── file_transfer_automation.py   # Main automation script
└── README.md                     # Project documentation
```

---

## ▶️ How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/file-transfer-project.git
   cd selenium-file-transfer-project
   ```

2. Install required packages:
   ```bash
   pip install selenium
   ```

3. Make sure GeckoDriver is installed and added to PATH or provide its location manually.

4. Run the script:
   ```bash
   python file_transfer_automation.py
   ```

---

## 🌐 Websites Used
- [Download File Website](https://demoqa.com/upload-download)
- [Upload File Website](https://the-internet.herokuapp.com/upload)

---

## 📸 Project Flow

- Open a website and **download a sample file**.
- Automatically **detect the latest downloaded file** in the Downloads folder.
- Open another website and **upload the detected file**.
- **Print confirmation** of successful download and upload.

---

## ✨ Bonus Features
- Dynamic detection of the latest downloaded file.
- Clean error handling with `try-finally` block to always close the browser.

---

## 📢 Author

**Durga Devi**  
[GitHub: DurgaDevi-tester](https://github.com/DurgaDevi-tester)
