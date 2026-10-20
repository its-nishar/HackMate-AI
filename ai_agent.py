import os
from google import genai


# ============================================================
# GEMINI API CONFIGURATION
# ============================================================

api_key = os.getenv("GEMINI_API_KEY")

client = None

if api_key:

    try:

        client = genai.Client(
            api_key=api_key
        )

    except Exception:

        client = None


# ============================================================
# ANALYZE HACKATHONS
# ============================================================

def analyze_hackathons(
    student_skills,
    team_size,
    location,
    available_date,
    hackathons
):

    # ========================================================
    # CHECK GEMINI AVAILABILITY
    # ========================================================

    if client is None:

        return (
            "⚠️ Gemini AI is currently unavailable."
        )


    # ========================================================
    # CREATE PROMPT
    # ========================================================

    prompt = f"""
You are HackMate-AI, an intelligent hackathon
recommendation agent.

Student Skills:
{student_skills}

Team Size:
{team_size}

Preferred Location:
{location}

Available Date:
{available_date}

Hackathons:
{hackathons}

Analyze the hackathons and recommend the best
opportunity.

Explain:

1. Best hackathon
2. Why it matches
3. Matching skills
4. Skill gaps
5. Team eligibility
6. Location compatibility
7. Registration fee
8. Deadline
9. Recommendation
10. Next step

Do not register for anything automatically.
Human approval is required before registration.
"""


    # ========================================================
    # CALL GEMINI WITH RETRY
    # ========================================================

    max_attempts = 3


    for attempt in range(max_attempts):

        try:

            response = client.models.generate_content(

                model="gemini-3.8-flash",

                contents=prompt
            )

            if response and response.text:

                return response.text


        except Exception:

            if attempt == max_attempts - 1:

                return (
                    "⚠️ Gemini AI is temporarily unavailable."
                )


    return (
        "⚠️ Gemini AI is temporarily unavailable."
    )