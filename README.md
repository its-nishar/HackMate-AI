# 🚀 HackMate-AI

### AI-Powered Hackathon Discovery, Matching & Registration Assistant

HackMate-AI is an AI-powered web application that helps students and developers discover hackathons that best match their **skills, team size, location, availability, and registration requirements**.

Instead of manually searching through multiple hackathon platforms, users can enter their profile once and receive personalized hackathon recommendations with an explainable match score.

---

## 🌟 Key Features

### 🔎 1. Smart Hackathon Discovery

HackMate-AI searches the available hackathon dataset and identifies opportunities that match the user's profile.

Users can provide:

- 🧠 Technical skills
- 👥 Team size
- 🌍 Preferred location
- 📅 Availability

---

### 🎯 2. Intelligent Match Scoring

Each hackathon receives a compatibility score based on multiple factors:

- 🧠 Skill compatibility
- 👥 Team-size eligibility
- 🌍 Location compatibility
- 📅 Deadline / availability compatibility

The results are ranked so users can quickly identify their strongest opportunities.

---

### 🤖 3. AI-Powered Recommendation

HackMate-AI uses Gemini to analyze the matching results and recommend the most suitable hackathon.

The recommendation explains:

- Why the hackathon is suitable
- Matching skills
- Missing skills
- Team compatibility
- Registration information
- Deadline information

This makes the recommendation more transparent instead of simply displaying a score.

---

### 🧠 4. Skill Gap Analysis

The application identifies both:

**Matching Skills**

Skills that the user already has.

**Skill Gaps**

Skills required by the hackathon that may be missing from the user's profile.

This helps users understand what they may need to learn before participating.

---

### 👥 5. Team Eligibility

HackMate-AI checks whether the user's team size satisfies the hackathon's minimum and maximum team requirements.

For example:

```text
Required Team Size: 2–4

User Team Size: 3

✓ Eligible
```

---

### 💰 6. Registration Fee Review

The system displays the registration fee when it is available.
If the fee is unknown, the application provides a review flow:

```text
Registration Fee
      ↓
Unknown
      ↓
Review Registration Fee
      ↓
Fee Reviewed
      ↓
Approval
      ↓
Registration
```
This demonstrates a human-in-the-loop approach rather than automatically assuming that an unknown fee is free.

---

### 🎫 7. Registration & Ticket Generation

After the registration process is approved, HackMate-AI generates a unique ticket ID.
Example:
HM-H009-A3F92C

The application also displays the registration status.

---

### 🔗 8. View Hackathon

Each recommendation contains a View Hackathon button that takes the user to the corresponding hackathon source/listing.

```text

### 🏗️ System Architecture
                    ┌──────────────────────┐
                    │      User Profile    │
                    │──────────────────────│
                    │ Skills               │
                    │ Team Size            │
                    │ Location             │
                    │ Availability         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Matcher Engine     │
                    │──────────────────────│
                    │ Skill Matching        │
                    │ Team Matching         │
                    │ Location Matching     │
                    │ Deadline Matching     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Match Score Engine  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Ranked Hackathons   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Gemini AI        │
                    │ Recommendation Engine │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
             View          Register       Ticket ID
           Hackathon       Review          Generation
```

---

### ⚙️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Pandas | Hackathon dataset processing |
| Google Gemini | AI-powered recommendations |
| CSV | Hackathon data storage |
| Git & GitHub | Version control and project hosting |

---

### 📂 File Description

**`app.py`**  
Main Streamlit application containing the user interface, search workflow, recommendations, registration flow, and ticket generation.

**`ai_agent.py`**  
Handles the Gemini AI integration and generates personalized hackathon recommendations.

**`matcher.py`**  
Contains the matching and scoring logic used to compare the user's profile with hackathon requirements.

**`skill_map.py`**  
Contains skill-related mappings used by the matching system.

**`hackathons.csv`**  
Stores hackathon information such as:

- Hackathon name
- Required skills
- Team size
- Location
- Deadline
- Registration fee
- Source
- URL

**`requirements.txt`**  
Contains the Python dependencies required to run the application.

**`.gitignore`**  
Prevents unnecessary files such as virtual environments, Python cache files, and secret configuration files from being uploaded.

---

## 🧮 Matching Methodology

HackMate-AI evaluates hackathons using multiple compatibility factors.

The system considers:

```text
Skill Compatibility
        +
Team Compatibility
        +
Location Compatibility
        +
Deadline Compatibility
        =
Overall Match Score
```

The resulting score is used to rank hackathons from the most suitable to the least suitable.

---

## 🤖 AI Recommendation Workflow

The AI recommendation process follows these steps:

```text
1. User enters profile
        ↓
2. Hackathons are filtered
        ↓
3. Match scores are calculated
        ↓
4. Results are ranked
        ↓
5. Gemini analyzes the results
        ↓
6. Best opportunity is recommended
        ↓
7. User receives an explanation
```

The AI recommendation is based on the structured matching results rather than blindly generating a random hackathon suggestion.

---

## 🔐 API Key Security

HackMate-AI does **not** hard-code the Gemini API key in the source code.

The application reads the API key from an environment variable:

```python
api_key = os.getenv("GEMINI_API_KEY")
```

This prevents the secret key from being directly exposed in the GitHub repository.

### Local Setup

Set the environment variable before running the application.

**Windows PowerShell:**

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Then run:

```bash
streamlit run app.py
```

> ⚠️ Never upload your actual Gemini API key to GitHub.

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project

```bash
cd HackMate-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Gemini API Key

**Windows PowerShell:**

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

### 7. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🖥️ Application Workflow

```text
                    HACKMATE-AI
                         │
                         ▼
               Enter Your Profile
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           Skills     Team Size   Location
              │
              ▼
        Find Hackathons
              │
              ▼
        Calculate Matches
              │
              ▼
        Rank Opportunities
              │
              ▼
       AI Recommendation
              │
              ▼
       Review Hackathon
              │
       ┌──────┴──────┐
       ▼             ▼
    Fee Known    Fee Unknown
       │             │
       │       Review Fee
       │             │
       └──────┬──────┘
              ▼
      Approve Registration
              │
              ▼
        Generate Ticket
```

---

## 🎯 Problem Statement

Students and developers often have difficulty finding hackathons that actually match their technical skills, team size, location, deadlines, and budget.

Existing hackathon platforms require users to manually search and compare multiple opportunities.

This creates problems such as:

- Too many irrelevant listings
- Difficulty comparing opportunities
- Missing important deadlines
- Team-size incompatibility
- Unclear registration fees
- Lack of personalized recommendations

---

## 💡 Proposed Solution

HackMate-AI provides a centralized intelligent interface where users can enter their profile once and receive ranked hackathon recommendations.

The system combines:

**Structured Matching + AI Reasoning + Transparent Explanations + User-Controlled Registration**

to make hackathon discovery faster and more useful.

---

## 🚀 Future Enhancements

The current version can be extended with:

- 🌐 Live hackathon data collection
- 🔄 Automatic listing updates
- 🔔 Deadline notifications
- 📧 Email reminders
- 👥 Team member matching
- 🧠 More advanced semantic skill matching
- 📊 User recommendation history
- 🔐 Secure cloud deployment
- 📱 Mobile-friendly interface
- 🏆 Personalized hackathon ranking

---

## ⚠️ Current Data Limitation

The current prototype uses a structured CSV dataset for demonstration and testing.

The data includes sources such as:

- Devfolio
- Unstop
- MLH
- Contest listings

The URLs in the prototype should be treated as **source/listing references**, not as proof that every listed event is currently live or accepting registrations.

A future production version can integrate verified live event APIs or official event feeds.

---

## 🏆 Why HackMate-AI?

HackMate-AI is not just a hackathon listing page.

It combines:

```text
🔎 Discovery
      +
🧠 Skill Matching
      +
🎯 Compatibility Scoring
      +
🤖 AI Recommendation
      +
💰 Fee Review
      +
👥 Team Validation
      +
🎫 Registration Tracking
```

This creates an end-to-end intelligent assistant for hackathon discovery.

---

## 👩‍💻 Author

**Nisha R**
**Siva Priya V**

B.Tech – Artificial Intelligence & Data Science
