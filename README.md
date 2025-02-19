# Phishy - AI-Powered Phishing Detection Extension

Phishy is a cutting-edge browser extension designed to protect users from phishing attacks and malicious messages. Using AI-powered analysis, it helps detect and prevent access to potentially harmful websites.

## 🚀 Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** FastAPI, Python
- **AI Model:** Mistral (via Groq API)
- **Browser API:** Chrome Extensions API

## Features
- ✅ Real-time phishing detection
- ✅ AI-powered analysis of URLs
- ✅ Safe browsing recommendations
- ✅ Lightweight and easy to use

## 📸 Screenshots
Here are some previews of Phishy in action:

![Phishy Browser Extension](screenshots/screenshot1.png)
*Phishy detecting a phishing website in real-time.*

![Phishy Safe URL Check](screenshots/screenshot2.png)
*Checking a safe website for phishing threats.*

![Phishy Safe URL Check](screenshots/screenshot3.png)
*Checking a unsafe website for phishing threats.*

## Setup Instructions
Follow these steps to set up and use the Phishy extension:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/punithkumar-10/Phishing-detection-extension-using-AI.git
cd Phishing-detection-extension-using-AI
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then, install the required dependencies:
```sh
pip install -r requirements.txt
```

### 3️⃣ Get Groq API Key
1. Visit [Groq API](https://groq.com/) and sign up for an API key.
2. Create a `.env` file in the **Backend** directory.
3. Add the API key to the `.env` file as follows:
   ```sh
   GROQ_API_KEY=your_api_key_here
   ```

### 4️⃣ Start the Backend Server
Navigate to the backend directory and run the FastAPI server using Uvicorn:
```sh
cd Backend
uvicorn main:app --reload
```
The server should now be running on `http://127.0.0.1:8000/`.

### 5️⃣ Load the Chrome Extension
1. Open **Google Chrome** and go to `chrome://extensions/`.
2. Enable **Developer Mode** (toggle in the top right corner).
3. Click **Load Unpacked** and select the **Phishy Extension** folder.
4. The extension is now ready to use! Click on it to check URLs for phishing threats.

## 🔗 GitHub Repository
For more details and updates, visit the official repository:
[Phishy GitHub Repo](https://github.com/punithkumar-10/Phishing-detection-extension-using-AI)

## 🚀 Contribute
Feel free to contribute by submitting issues or pull requests. Let's make the web a safer place together!

---
Made with ❤️ by [Punith Kumar](https://github.com/punithkumar-10/)

