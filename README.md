# 🤖 AI Job Agent

An AI-powered job matching application that analyzes a user's resume and recommends relevant job opportunities based on their skills and experience.

## 🚀 Features

* 📄 Resume input
* 🤖 AI-powered resume analysis
* 🔎 Job matching
* 📊 Match percentage
* ✅ Matching skills
* ❌ Missing skills
* 💡 Reason why the job matches
* 📝 Short job summary
* 🌐 Streamlit web application

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini AI
* Google GenAI SDK

## 📂 Project Structure

```text
AI-Job-Agent/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. User pastes their resume.
2. The application analyzes the resume using Gemini AI.
3. Available job opportunities are compared with the candidate's skills.
4. The AI identifies relevant jobs.
5. The application displays:

   * Match percentage
   * Matching skills
   * Missing skills
   * Why the job matches
   * Job summary

## ▶️ Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🔐 API Key

The Gemini API key should **not** be stored directly in `app.py` or uploaded to GitHub.

For Streamlit deployment, add the key using Streamlit Secrets:

```text
GEMINI_API_KEY = "your_api_key_here"
```

## 📌 Current Version

The current version uses sample job data for demonstrating the AI matching workflow.

Future versions can connect the agent to real-time job listings and automatically collect relevant opportunities.

## 🎯 Future Improvements

* Real-time job search
* Automatic daily job updates
* Job application links
* Resume upload
* Email notifications
* Advanced skill matching
* Personalized job recommendations

## 👩‍💻 Author

**Vanga Harshitha**

B.Tech Computer Science & Engineering (AI & ML)

GitHub: `harshitha-vanga`
