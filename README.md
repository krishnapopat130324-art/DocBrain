# 📄 Important DocBrain

A simple Python-based application that helps users track important document expiry dates and receive notifications before expiration.

---

## 🚀 Features
- Add important documents with expiry dates
- View document status (Valid / Expiring Soon / Expired)
- Local data storage using JSON
- Desktop notification alerts
- Simple terminal-based interface

---

## 🛠️ Technologies Used
- Python 3
- JSON for data storage
- Plyer (for desktop notifications)

---

## 📂 Project Structure

python-project/
├── main.py
├── storage.py
├── checker.py
├── documents.json
├── README.md


---

## ▶️ How to Run the Project

### Step 1: Install Python
Download Python from:
https://www.python.org/downloads/

Make sure Python is added to PATH.

---

### Step 2: Install Required Library
```bash
pip install plyer

Step 3: Run the Application
python main.py

Sample Output
===== IMPORTANT DocBrain =====
1. Add new document
2. View document status
3. Exit
Choose an option:

🔐 Data Storage

All document data is stored locally in documents.json.
No internet connection is required.

👨‍💻 Author

Krishna