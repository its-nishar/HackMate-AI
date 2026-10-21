# ============================================================
# HACKMATE AI
# Team SyncMind
# ============================================================

# ============================================================
# IMPORTS
# ============================================================

import streamlit as st
import pandas as pd

from datetime import datetime
from zoneinfo import ZoneInfo

from matcher import calculate_match
from ai_agent import analyze_hackathons

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HackMate AI",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# REGISTRATION STATE
# ============================================================

if "registrations" not in st.session_state:
    st.session_state.registrations = {}

if "ticket_ids" not in st.session_state:
    st.session_state.ticket_ids = {}

# ============================================================
# AI RECOMMENDATION STATE
# ============================================================

if "ai_recommendation" not in st.session_state:
    st.session_state.ai_recommendation = ""

# ============================================================
# SEARCH RESULTS STATE
# ============================================================

if "search_results" not in st.session_state:
    st.session_state.search_results = []

# ============================================================
# VIEW HACKATHON STATE
# ============================================================

if "selected_hackathon" not in st.session_state:
    st.session_state.selected_hackathon = None

# ============================================================
# 2.LOAD HACKATHON DATA
# ============================================================

hackathons = pd.read_csv("hackathons.csv")


# ============================================================
# 3. PROFESSIONAL NAVY + CYAN + VIOLET THEME
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       MAIN PAGE
       -------------------------------------------------------- */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(56, 189, 248, 0.12),
                transparent 25%
            ),
            radial-gradient(
                circle at 85% 15%,
                rgba(139, 92, 246, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 50% 90%,
                rgba(56, 189, 248, 0.06),
                transparent 30%
            ),
            #050816;
    }


    /* --------------------------------------------------------
       PAGE WIDTH
       -------------------------------------------------------- */

    .block-container {
        max-width: 1100px;
        padding-top: 40px;
        padding-bottom: 60px;
    }


    /* --------------------------------------------------------
       BACKGROUND GLOW
       -------------------------------------------------------- */

    .stApp::before {
        content: "";

        position: fixed;

        width: 280px;
        height: 280px;

        left: -100px;
        top: 15%;

        background: rgba(56, 189, 248, 0.08);

        border-radius: 50%;

        filter: blur(90px);

        animation: cyanGlow 7s ease-in-out infinite alternate;

        pointer-events: none;
    }


    .stApp::after {
        content: "";

        position: fixed;

        width: 300px;
        height: 300px;

        right: -100px;
        bottom: 10%;

        background: rgba(139, 92, 246, 0.08);

        border-radius: 50%;

        filter: blur(95px);

        animation: violetGlow 8s ease-in-out infinite alternate;

        pointer-events: none;
    }


    @keyframes cyanGlow {

        0% {
            transform: translate(0, 0);
            opacity: 0.35;
        }

        100% {
            transform: translate(45px, -25px);
            opacity: 0.75;
        }
    }


    @keyframes violetGlow {

        0% {
            transform: translate(0, 0);
            opacity: 0.30;
        }

        100% {
            transform: translate(-40px, 25px);
            opacity: 0.70;
        }
    }


    /* --------------------------------------------------------
       HERO TITLE
       -------------------------------------------------------- */

    .hero-title {
        text-align: center;

        color: #38BDF8;

        font-size: 58px;

        font-weight: 800;

        letter-spacing: -2px;

        line-height: 1.1;

        margin-top: 5px;

        margin-bottom: 0;

        text-shadow:
            0 0 12px rgba(56, 189, 248, 0.45),
            0 0 30px rgba(139, 92, 246, 0.20);
    }


    /* --------------------------------------------------------
       HERO SUBTITLE
       -------------------------------------------------------- */

    .hero-subtitle {
        text-align: center;

        color: #CBD5E1;

        font-size: 30px;

        font-weight: 700;

        line-height: 1.25;

        margin-top: 15px;

        margin-bottom: 0;
    }


    /* --------------------------------------------------------
       HERO TAGLINE
       -------------------------------------------------------- */

    .hero-tagline {
        text-align: center;

        color: #64748B;

        font-size: 17px;

        font-weight: 500;

        margin-top: 18px;
    }


    /* --------------------------------------------------------
       HERO DESCRIPTION
       -------------------------------------------------------- */

    .hero-description {
        text-align: center;

        color: #94A3B8;

        font-size: 17px;

        font-weight: 400;

        line-height: 1.6;

        margin-top: 35px;

        margin-bottom: 25px;
    }


    /* --------------------------------------------------------
       SECTION HEADINGS
       -------------------------------------------------------- */

    h2 {
        color: #E2E8F0 !important;

        font-weight: 750 !important;
    }


    h3 {
        color: #CBD5E1 !important;

        font-weight: 650 !important;
    }


    /* --------------------------------------------------------
       NORMAL TEXT
       -------------------------------------------------------- */

    p {
        color: #94A3B8;
    }


    /* --------------------------------------------------------
       FORM LABELS
       -------------------------------------------------------- */

    label {
        color: #CBD5E1 !important;

        font-weight: 600 !important;
    }


    /* --------------------------------------------------------
       TEXT INPUT
       -------------------------------------------------------- */

    .stTextInput input {

        background-color: #0B1224 !important;

        color: #E2E8F0 !important;

        border: 1px solid #243554 !important;

        border-radius: 12px !important;

        min-height: 46px;

        transition: 0.25s ease;
    }


    .stTextInput input:focus {

        border-color: #38BDF8 !important;

        box-shadow:
            0 0 0 1px rgba(56, 189, 248, 0.30),
            0 0 18px rgba(56, 189, 248, 0.12) !important;
    }


    /* --------------------------------------------------------
       NUMBER INPUT
       -------------------------------------------------------- */

    .stNumberInput input {

        background-color: #0B1224 !important;

        color: #E2E8F0 !important;

        border: 1px solid #243554 !important;

        border-radius: 12px !important;
    }


    /* --------------------------------------------------------
       SELECT BOX
       -------------------------------------------------------- */

    div[data-baseweb="select"] > div {

        background-color: #0B1224 !important;

        color: #E2E8F0 !important;

        border: 1px solid #243554 !important;

        border-radius: 12px !important;
    }


    /* --------------------------------------------------------
       DATE INPUT
       -------------------------------------------------------- */

    .stDateInput input {

        background-color: #0B1224 !important;

        color: #E2E8F0 !important;

        border: 1px solid #243554 !important;

        border-radius: 12px !important;
    }


    /* --------------------------------------------------------
       SEARCH BUTTON
       -------------------------------------------------------- */

    .stButton > button {

        width: 100%;

        min-height: 54px;

        border-radius: 13px;

        border: 1px solid #38BDF8;

        background:
            linear-gradient(
                90deg,
                #0369A1,
                #2563EB,
                #7C3AED
            );

        color: white;

        font-size: 16px;

        font-weight: 700;

        letter-spacing: 0.2px;

        box-shadow:
            0 5px 25px rgba(56, 189, 248, 0.12);

        transition: all 0.3s ease;
    }


    .stButton > button:hover {

        border-color: #8B5CF6;

        background:
            linear-gradient(
                90deg,
                #0891B2,
                #2563EB,
                #8B5CF6
            );

        box-shadow:
            0 0 20px rgba(56, 189, 248, 0.25),
            0 0 35px rgba(139, 92, 246, 0.15);

        transform: translateY(-2px);
    }


    /* --------------------------------------------------------
   HACKATHON CARD CONTENT
   -------------------------------------------------------- */

div[data-testid="stVerticalBlockBorderWrapper"] h3 {
    color: #38BDF8 !important;
    font-size: 24px !important;
    font-weight: 750 !important;
    margin-bottom: 8px !important;
}


/* --------------------------------------------------------
   CARD TEXT
   -------------------------------------------------------- */

div[data-testid="stVerticalBlockBorderWrapper"] p {
    color: #CBD5E1 !important;
}


/* --------------------------------------------------------
   CARD CAPTIONS
   -------------------------------------------------------- */

div[data-testid="stVerticalBlockBorderWrapper"] small {
    color: #64748B !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px;
}


/* --------------------------------------------------------
   MATCH SCORE
   -------------------------------------------------------- */

div[data-testid="stMetric"] {

    background:
        rgba(56, 189, 248, 0.05);

    border:
        1px solid rgba(56, 189, 248, 0.15);

    border-radius: 14px;

    padding: 8px;

}


/* --------------------------------------------------------
   MATCH SCORE VALUE
   -------------------------------------------------------- */

div[data-testid="stMetricValue"] {

    color: #38BDF8 !important;

    font-size: 28px !important;

    font-weight: 800 !important;

    text-shadow:
        0 0 12px rgba(56, 189, 248, 0.35);
}


/* --------------------------------------------------------
   MATCH SCORE LABEL
   -------------------------------------------------------- */

div[data-testid="stMetricLabel"] {

    color: #94A3B8 !important;

    font-weight: 700 !important;
}


/* --------------------------------------------------------
   LINK BUTTON
   -------------------------------------------------------- */

div[data-testid="stVerticalBlockBorderWrapper"]
a {

    border-radius: 10px !important;

    font-weight: 700 !important;
}


/* --------------------------------------------------------
   RESULT SPACING
   -------------------------------------------------------- */

div[data-testid="stVerticalBlockBorderWrapper"] {
    margin-bottom: 22px;
}


    /* --------------------------------------------------------
       METRIC
       -------------------------------------------------------- */

    [data-testid="stMetricValue"] {

        color: #38BDF8 !important;

        font-weight: 800 !important;
    }


    [data-testid="stMetricLabel"] {

        color: #94A3B8 !important;
    }


    /* --------------------------------------------------------
       ALERTS
       -------------------------------------------------------- */

    div[data-testid="stAlert"] {

        border-radius: 13px;
    }


    /* --------------------------------------------------------
       DIVIDER
       -------------------------------------------------------- */

    hr {

        border-color:
            rgba(56, 189, 248, 0.12) !important;
    }


    /* --------------------------------------------------------
       CAPTION
       -------------------------------------------------------- */

    .stCaption {

        color: #64748B !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 4. HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero-title">
        🚀 HackMate AI
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="hero-subtitle">
        Find Hackathons That Match Your Potential
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="hero-tagline">
        Intelligent opportunity discovery for ambitious students
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="hero-description">
        Discover hackathons based on your skills,
        team size, preferred location and availability.
    </div>
    """,
    unsafe_allow_html=True
)


st.divider()


# ============================================================
# 5. PROFILE SECTION
# ============================================================

st.header("🎯 Build Your Hackathon Profile")

st.write(
    "Tell HackMate AI about yourself and we'll "
    "find opportunities that fit your profile."
)


st.write("")


# ============================================================
# 6. SKILLS
# ============================================================

skills = st.text_input(
    "💻 Your Skills",
    placeholder="Python, AI, Machine Learning, Data Science..."
)


# ============================================================
# 7. TEAM SIZE + LOCATION
# ============================================================

col1, col2 = st.columns(2)


with col1:

    team_size = st.number_input(
        "👥 Team Size",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )


with col2:

    location = st.selectbox(
        "🌍 Preferred Location",
        [
            "India",
            "Global",
            "Asia",
            "Europe"
        ]
    )


# ============================================================
# 8. AVAILABILITY
# ============================================================

available_date = st.date_input(
    "📅 Available From"
)


st.write("")


# ============================================================
# 9. SEARCH BUTTON
# ============================================================

search = st.button(
    "🔎  Find Matching Hackathons",
    use_container_width=True
)

# ============================================================
# DEADLINE TIMEZONE CONVERSION
# ============================================================

def convert_deadline_to_ist(deadline):

    try:

        deadline = str(deadline).strip()

        # PST
        if deadline.endswith("PST"):

            date_part = deadline.replace(" PST", "")

            dt = datetime.strptime(
                date_part,
                "%Y-%m-%d %H:%M"
            )

            dt = dt.replace(
                tzinfo=ZoneInfo("America/Los_Angeles")
            )

        # PDT
        elif deadline.endswith("PDT"):

            date_part = deadline.replace(" PDT", "")

            dt = datetime.strptime(
                date_part,
                "%Y-%m-%d %H:%M"
            )

            dt = dt.replace(
                tzinfo=ZoneInfo("America/Los_Angeles")
            )

        # Already normal/IST
        else:

            return deadline

        # Convert to IST
        ist_time = dt.astimezone(
            ZoneInfo("Asia/Kolkata")
        )

        return ist_time.strftime(
            "%Y-%m-%d %I:%M %p IST"
        )

    except Exception:

        return str(deadline)


# ============================================================
# 10. FIND HACKATHONS
# ============================================================


# ============================================================
# 10.1 GENERATE RULE-BASED FALLBACK RECOMMENDATION
# ============================================================

def generate_fallback_recommendation(results):

    """
    Generates a recommendation using the existing
    HackMate matching engine when Gemini is unavailable.
    """

    if not results:

        return (
            "## 🤖 HackMate-AI Recommendation\n\n"
            "No suitable hackathons were found."
        )


    # --------------------------------------------------------
    # GET BEST MATCH
    # --------------------------------------------------------

    best = results[0]


    # --------------------------------------------------------
    # REQUIRED SKILLS
    # --------------------------------------------------------

    required_skills = [

        skill.strip().lower()

        for skill in str(
            best["skills"]
        ).split(",")

        if skill.strip()
    ]


    # --------------------------------------------------------
    # MATCHED SKILLS
    # --------------------------------------------------------

    matched_skills = [

        skill.strip().title()

        for skill in best["matching_skills"]

        if skill.strip()
    ]


    # --------------------------------------------------------
    # FIND MISSING SKILLS
    # --------------------------------------------------------

    matched_lower = [

        skill.strip().lower()

        for skill in best["matching_skills"]
    ]


    missing_skills = [

        skill.strip().title()

        for skill in required_skills

        if skill not in matched_lower
    ]


    # --------------------------------------------------------
    # TEAM STATUS
    # --------------------------------------------------------

    if best["team_match"]:

        team_status = (
            f"Eligible — your team size of "
            f"{team_size} fits the required range "
            f"of {best['team_min']}-{best['team_max']}."
        )

    else:

        team_status = (
            f"Not eligible — this event requires "
            f"{best['team_min']}-{best['team_max']} members."
        )


    # --------------------------------------------------------
    # LOCATION STATUS
    # --------------------------------------------------------

    if best["location_match"]:

        location_status = (
            f"Compatible — {best['location']} "
            f"matches your preference."
        )

    else:

        location_status = (
            "Location may not match your preference."
        )


    # --------------------------------------------------------
    # REGISTRATION FEE
    # --------------------------------------------------------

    fee_value = str(
        best["fee"]
    ).strip().lower()


    if fee_value in [
        "unknown",
        "unk",
        "na",
        "n/a",
        "",
        "none"
    ]:

        fee_status = "Unknown"

    elif fee_value == "0":

        fee_status = "Free"

    else:

        try:

            fee_status = f"₹{int(float(fee_value))}"

        except:

            fee_status = str(
                best["fee"]
            )


    # --------------------------------------------------------
    # SKILL GAP
    # --------------------------------------------------------

    if missing_skills:

        skill_gap = ", ".join(
            missing_skills
        )

    else:

        skill_gap = "None"


    # --------------------------------------------------------
    # CREATE RECOMMENDATION
    # --------------------------------------------------------

    recommendation = f"""
## 🤖 HackMate-AI Recommendation

🏆 **Best Hackathon:**
{best['name']}

### Why it matches

This hackathon has the strongest overall match score of
**{best['score']}%** among the shortlisted opportunities.
Your skills, team size and preferred location were considered
by the HackMate matching engine.

🧠 **Matching Skills:**
{", ".join(matched_skills) if matched_skills else "None"}

⚠️ **Skill Gaps:**
{skill_gap}

👥 **Team:**
{team_status}

🌍 **Location:**
{location_status}

💰 **Registration:**
{fee_status}

📅 **Deadline:**
{convert_deadline_to_ist(best['deadline'])}

⭐ **Recommendation:**
This is currently your strongest shortlisted opportunity
based on the HackMate matching score.

➡️ **Next Step:**
Review the hackathon details and registration requirements
before proceeding.
"""

    return recommendation


# ============================================================
# 10.2 RUN SEARCH
# ============================================================

if search:

    # --------------------------------------------------------
    # RESET PREVIOUS RESULTS
    # --------------------------------------------------------

    st.session_state.search_results = []

    st.session_state.ai_recommendation = ""


    # --------------------------------------------------------
    # CHECK SKILLS
    # --------------------------------------------------------

    if not skills.strip():

        st.warning(
            "⚠️ Please enter your skills to discover "
            "matching hackathons."
        )


    else:

        # ----------------------------------------------------
        # CREATE RESULTS LIST
        # ----------------------------------------------------

        results = []


        # ----------------------------------------------------
        # CHECK EACH HACKATHON
        # ----------------------------------------------------

        for _, hackathon_data in hackathons.iterrows():

            # ------------------------------------------------
            # CALCULATE MATCH
            # ------------------------------------------------

            match = calculate_match(

                skills,

                team_size,

                location,

                available_date,

                hackathon_data
            )


            # ------------------------------------------------
            # KEEP EVENTS WITH MATCHING SKILLS
            # ------------------------------------------------

            if not match["matching_skills"]:

                continue


            # ------------------------------------------------
            # CREATE CLEAN RESULT
            # ------------------------------------------------

            results.append({

                "id":
                    hackathon_data["id"],

                "name":
                    hackathon_data["name"],

                "skills":
                    hackathon_data["skills"],

                "team_min":
                    hackathon_data["team_min"],

                "team_max":
                    hackathon_data["team_max"],

                "location":
                    hackathon_data["location"],

                "deadline":
                    hackathon_data["deadline"],

                "fee":
                    hackathon_data["fee"],

                "source":
                    hackathon_data["source"],

                "source_id":
                    hackathon_data["source_id"],

                "url":
                    hackathon_data["url"],

                "score":
                    match["score"],

                "matching_skills":
                    match["matching_skills"],

                "team_match":
                    match["team_match"],

                "location_match":
                    match["location_match"],

                "date_match":
                    match["date_match"],

                "skill_score":
                    match["skill_score"],

                "team_score":
                    match["team_score"],

                "location_score":
                    match["location_score"],

                "date_score":
                    match["date_score"]
            })


        # ----------------------------------------------------
        # SORT BY MATCH SCORE
        # ----------------------------------------------------

        results = sorted(

            results,

            key=lambda x: x["score"],

            reverse=True
        )


        # ----------------------------------------------------
        # SAVE RESULTS
        # ----------------------------------------------------

        st.session_state.search_results = results


        # ====================================================
        # 10.3 AI RECOMMENDATION
        # ====================================================

        if results:

            with st.spinner(
                "🤖 HackMate-AI is analyzing your "
                "matching hackathons..."
            ):

                try:

                    # ----------------------------------------
                    # CALL GEMINI AI AGENT
                    # ----------------------------------------

                    ai_result = analyze_hackathons(

                        student_skills=skills,

                        team_size=team_size,

                        location=location,

                        available_date=available_date,

                        hackathons=results
                    )


                    # ----------------------------------------
                    # CHECK AI RESULT
                    # ----------------------------------------

                    if (
                        ai_result
                        and
                        not ai_result.startswith("⚠️")
                    ):

                        st.session_state.ai_recommendation = (
                            ai_result
                        )

                    else:

                        st.session_state.ai_recommendation = (
                            generate_fallback_recommendation(
                                results
                            )
                        )


                except Exception:

                    # ----------------------------------------
                    # GEMINI ERROR
                    # ----------------------------------------

                    st.session_state.ai_recommendation = (
                        generate_fallback_recommendation(
                            results
                        )
                    )


# ============================================================
# 10.4 LOAD SAVED RESULTS
# ============================================================

results = st.session_state.search_results


# ============================================================
# 10.5 DISPLAY RESULTS
# ============================================================

if results:

    # --------------------------------------------------------
    # SUCCESS MESSAGE
    # --------------------------------------------------------

    st.success(
        f"🎯 Found {len(results)} matching hackathons!"
    )


    # ========================================================
    # MATCH SUMMARY
    # ========================================================

    st.markdown(
        "### 📊 Your Hackathon Match Summary"
    )


    total_hackathons = len(results)


    top_score = max(
        hackathon["score"]
        for hackathon in results
    )


    average_score = round(

        sum(
            hackathon["score"]
            for hackathon in results
        )
        /
        len(results)
    )


    excellent_matches = sum(

        1

        for hackathon in results

        if hackathon["score"] >= 80
    )


    # --------------------------------------------------------
    # SUMMARY CARDS
    # --------------------------------------------------------

    m1, m2, m3, m4 = st.columns(4)


    with m1:

        st.metric(
            "🏆 Hackathons",
            total_hackathons
        )


    with m2:

        st.metric(
            "🎯 Top Match",
            f"{top_score}%"
        )


    with m3:

        st.metric(
            "📊 Average Match",
            f"{average_score}%"
        )


    with m4:

        st.metric(
            "✨ Excellent Matches",
            excellent_matches
        )


    # ========================================================
    # 10.6 TOP 3
    # ========================================================

    st.markdown("---")

    st.markdown(
        "### 🏆 Top 3 Best Matches"
    )


    top_3 = results[:3]


    top_columns = st.columns(
        len(top_3)
    )


    for i, hackathon in enumerate(top_3):

        with top_columns[i]:

            if i == 0:

                medal = "🥇"

            elif i == 1:

                medal = "🥈"

            else:

                medal = "🥉"


            st.markdown(
                f"### {medal}"
            )


            st.write(
                f"**{hackathon['name']}**"
            )


            st.metric(
                "Match",
                f"{hackathon['score']}%"
            )


            if hackathon["matching_skills"]:

                skills_text = ", ".join(

                    skill.title()

                    for skill in hackathon[
                        "matching_skills"
                    ]
                )


                st.caption(
                    f"🧠 {skills_text}"
                )


    # ========================================================
    # 10.7 AI AGENT RECOMMENDATION
    # ========================================================

    st.markdown("---")

    if st.session_state.ai_recommendation:

        # Avoid displaying the heading twice
        recommendation = (
            st.session_state.ai_recommendation
        )

        recommendation = recommendation.replace(
            "## 🤖 HackMate-AI Recommendation",
            "",
            1
        ).strip()


        st.markdown(
            "## 🤖 HackMate-AI Recommendation"
        )


        st.markdown(
            recommendation
        )

    else:

        st.info(
            "🤖 AI recommendation is not available "
            "for this search."
        )


    # ========================================================
    # 10.8 RECOMMENDED HACKATHONS
    # ========================================================

    st.markdown("---")

    st.markdown(
        "## 🚀 Recommended Hackathons"
    )


    # ========================================================
    # DISPLAY EACH HACKATHON
    # ========================================================

    for hackathon in results:

        with st.container(border=True):

            # =================================================
            # TITLE + SCORE
            # =================================================

            title_col, score_col = st.columns(
                [4, 1]
            )


            with title_col:

                st.markdown(
                    f"### 🚀 {hackathon['name']}"
                )


            with score_col:

                st.metric(
                    "MATCH",
                    f"{hackathon['score']}%"
                )


            # =================================================
            # BASIC INFORMATION
            # =================================================

            st.write(
                f"🧠 **Required Skills:** "
                f"{hackathon['skills']}"
            )


            # =================================================
            # REGISTRATION FEE
            # =================================================

            fee_value = str(
                hackathon["fee"]
            ).strip().lower()


            if fee_value in [
                "unknown",
                "unk",
                "na",
                "n/a",
                "",
                "none"
            ]:

                st.warning(
                    "💰 **Registration Fee:** Unknown"
                )

            elif fee_value in [
                "0",
                "0.0"
            ]:

                st.write(
                    "💰 **Registration Fee:** Free"
                )

            else:

                try:

                    display_fee = int(
                        float(fee_value)
                    )

                    st.write(
                        f"💰 **Registration Fee:** "
                        f"₹{display_fee}"
                    )

                except:

                    st.write(
                        f"💰 **Registration Fee:** "
                        f"{hackathon['fee']}"
                    )


            # =================================================
            # TEAM / LOCATION / DEADLINE
            # =================================================

            info1, info2, info3 = st.columns(3)


            with info1:

                st.caption(
                    "👥 TEAM SIZE"
                )

                st.write(
                    f"{hackathon['team_min']} - "
                    f"{hackathon['team_max']} members"
                )


            with info2:

                st.caption(
                    "🌍 LOCATION"
                )

                st.write(
                    hackathon["location"]
                )


            with info3:

                st.caption(
                    "📅 DEADLINE"
                )

                st.write(
                    convert_deadline_to_ist(
                        hackathon["deadline"]
                    )
                )


            # =================================================
            # MATCH QUALITY
            # =================================================

            if hackathon["score"] >= 80:

                st.success(
                    "✨ Excellent Match"
                )

            elif hackathon["score"] >= 60:

                st.info(
                    "✓ Good Match"
                )

            else:

                st.warning(
                    "△ Partial Match"
                )


            # =================================================
            # 10.9 REGISTRATION
            # =================================================

            st.markdown(
                "#### 📝 Registration"
            )


            hackathon_id = hackathon["id"]


            registration_status = (
                st.session_state.registrations.get(
                    hackathon_id,
                    "not_registered"
                )
            )


            # =================================================
            # ALREADY REGISTERED
            # =================================================

            if registration_status == "registered":

                st.success(
                    "✅ Registration completed"
                )


                if hackathon_id in (
                    st.session_state.ticket_ids
                ):

                    ticket_id = (
                        st.session_state.ticket_ids[
                            hackathon_id
                        ]
                    )


                    st.info(
                        f"🎫 **Ticket ID:** "
                        f"{ticket_id}"
                    )


            # =================================================
            # FEE REVIEWED
            # =================================================

            elif registration_status == "fee_reviewed":

                # ------------------------------------------------
                # SIMULATED DISCOVERED FEE
                # ------------------------------------------------

                reviewed_fee = 500


                st.success(
                    "🔎 Registration fee reviewed."
                )


                st.info(
                    f"💰 **Registration Fee:** "
                    f"₹{reviewed_fee}"
                )


                st.caption(
                    "The fee was discovered during the "
                    "registration review step."
                )


                st.warning(
                    "⚠️ Human approval is required "
                    "before registration."
                )


                # ------------------------------------------------
                # APPROVE REGISTRATION
                # ------------------------------------------------

                approve_button = st.button(

                    "✅ Approve Registration",

                    key=f"approve_reviewed_{hackathon_id}"
                )


                if approve_button:

                    st.session_state.registrations[
                        hackathon_id
                    ] = "registered"


                    ticket_id = (
                        f"HM-{hackathon_id}-"
                        f"{team_size}"
                    )


                    st.session_state.ticket_ids[
                        hackathon_id
                    ] = ticket_id


                    st.success(
                        "🎉 Registration approved!"
                    )


                    st.info(
                        f"🎫 **Ticket ID:** "
                        f"{ticket_id}"
                    )


                    st.rerun()


            # =================================================
            # PENDING APPROVAL
            # =================================================

            elif registration_status == "pending":

                st.warning(
                    "⏳ Registration paused. "
                    "Human approval is required."
                )


                approve_button = st.button(

                    "✅ Approve Registration",

                    key=f"approve_{hackathon_id}"
                )


                if approve_button:

                    st.session_state.registrations[
                        hackathon_id
                    ] = "registered"


                    ticket_id = (
                        f"HM-{hackathon_id}-"
                        f"{team_size}"
                    )


                    st.session_state.ticket_ids[
                        hackathon_id
                    ] = ticket_id


                    st.success(
                        "🎉 Registration approved!"
                    )


                    st.info(
                        f"🎫 **Ticket ID:** "
                        f"{ticket_id}"
                    )


                    st.rerun()


            # =================================================
            # NOT REGISTERED
            # =================================================

            else:

                team_eligible = (

                    hackathon["team_min"]
                    <= team_size
                    <= hackathon["team_max"]
                )


                # =============================================
                # TEAM SIZE NOT ELIGIBLE
                # =============================================

                if not team_eligible:

                    st.error(
                        f"❌ Registration blocked. "
                        f"This event requires "
                        f"{hackathon['team_min']}-"
                        f"{hackathon['team_max']} "
                        f"members, but your team has "
                        f"{team_size} members."
                    )


                # =============================================
                # TEAM SIZE ELIGIBLE
                # =============================================

                else:

                    st.success(
                        "✓ Your team size is eligible."
                    )


                    # =========================================
                    # CHECK FEE TYPE
                    # =========================================

                    fee_value = str(
                        hackathon["fee"]
                    ).strip().lower()


                    is_unknown_fee = fee_value in [
                        "unknown",
                        "unk",
                        "na",
                        "n/a",
                        "",
                        "none"
                    ]


                    is_free = fee_value in [
                        "0",
                        "0.0"
                    ]


                    # =========================================
                    # UNKNOWN FEE
                    # =========================================

                    if is_unknown_fee:

                        st.warning(
                            "💰 Registration fee is "
                            "**currently unknown**."
                        )


                        review_button = st.button(

                            "🔍 Review Registration Fee",

                            key=f"review_fee_{hackathon_id}"
                        )


                        if review_button:

                            st.session_state.registrations[
                                hackathon_id
                            ] = "fee_reviewed"


                            st.rerun()


                    # =========================================
                    # FREE EVENT
                    # =========================================

                    elif is_free:

                        st.success(
                            "💰 Registration Fee: Free"
                        )


                        register_button = st.button(

                            "📝 Register for this Hackathon",

                            key=f"register_{hackathon_id}"
                        )


                        if register_button:

                            st.session_state.registrations[
                                hackathon_id
                            ] = "registered"


                            ticket_id = (
                                f"HM-{hackathon_id}-"
                                f"{team_size}"
                            )


                            st.session_state.ticket_ids[
                                hackathon_id
                            ] = ticket_id


                            st.success(
                                "🎉 Registration completed!"
                            )


                            st.info(
                                f"🎫 **Ticket ID:** "
                                f"{ticket_id}"
                            )


                            st.rerun()


                    # =========================================
                    # PAID EVENT
                    # =========================================

                    else:

                        try:

                            known_fee = int(
                                float(fee_value)
                            )

                        except:

                            known_fee = 500


                        st.warning(
                            f"💰 Registration Fee: "
                            f"₹{known_fee}"
                        )


                        review_button = st.button(

                            "⚠️ Review Paid Registration",

                            key=f"review_paid_{hackathon_id}"
                        )


                        if review_button:

                            st.session_state.registrations[
                                hackathon_id
                            ] = "pending"


                            st.rerun()


            # =================================================
            # 10.10 WHY THIS MATCHES YOU
            # =================================================

            st.markdown(
                "#### 🤖 Why this matches you"
            )


            # ------------------------------------------------
            # REQUIRED SKILLS
            # ------------------------------------------------

            required_skills = [

                skill.strip().lower()

                for skill in str(
                    hackathon["skills"]
                ).split(",")

                if skill.strip()
            ]


            # ------------------------------------------------
            # MATCHED SKILLS
            # ------------------------------------------------

            matched_skills = [

                skill.strip().lower()

                for skill in hackathon[
                    "matching_skills"
                ]

                if skill.strip()
            ]


            # ------------------------------------------------
            # MISSING SKILLS
            # ------------------------------------------------

            missing_skills = [

                skill

                for skill in required_skills

                if skill not in matched_skills
            ]


            # ------------------------------------------------
            # MATCHED SKILLS
            # ------------------------------------------------

            if matched_skills:

                skills_text = ", ".join(

                    skill.title()

                    for skill in matched_skills
                )


                st.write(
                    f"✓ Your skills match: "
                    f"**{skills_text}**"
                )


            # ------------------------------------------------
            # SKILL COVERAGE
            # ------------------------------------------------

            matched_count = len(
                matched_skills
            )


            required_count = len(
                required_skills
            )


            st.write(
                f"🧠 **Skill Coverage:** "
                f"{matched_count}/{required_count}"
            )


            # ------------------------------------------------
            # SKILL SCORE
            # ------------------------------------------------

            st.write(
                f"🎯 **Skill Score:** "
                f"{hackathon['skill_score']}/50"
            )


            # ------------------------------------------------
            # SKILL STATUS
            # ------------------------------------------------

            if matched_count == required_count:

                st.success(
                    "🎉 **Full Skill Match**"
                )

            else:

                st.warning(
                    f"⚠️ **Partial Skill Match** — "
                    f"{matched_count}/{required_count} "
                    f"required skills matched."
                )


            # ------------------------------------------------
            # MISSING SKILLS
            # ------------------------------------------------

            if missing_skills:

                missing_text = ", ".join(

                    skill.title()

                    for skill in missing_skills
                )


                st.warning(
                    f"⚠️ **Missing required skills:** "
                    f"{missing_text}"
                )


                st.info(
                    "💡 **Skill Gap:** "
                    "Learn the missing skills above "
                    "to improve your match."
                )

            else:

                st.success(
                    "🎉 **Skill Complete:** "
                    "You have all the required skills "
                    "for this hackathon."
                )


            # ------------------------------------------------
            # TEAM MATCH
            # ------------------------------------------------

            if hackathon["team_match"]:

                st.write(
                    "✓ Your team size is eligible"
                )


            # ------------------------------------------------
            # LOCATION MATCH
            # ------------------------------------------------

            if hackathon["location_match"]:

                st.write(
                    "✓ Location matches your preference"
                )


            # ------------------------------------------------
            # DATE MATCH
            # ------------------------------------------------

            if hackathon["date_match"]:

                st.write(
                    "✓ Your availability is before "
                    "the deadline"
                )


            # =================================================
            # 10.11 AI MATCH BREAKDOWN
            # =================================================

            st.markdown(
                "#### 📊 AI Match Breakdown"
            )


            b1, b2, b3, b4 = st.columns(4)


            with b1:

                st.metric(
                    "🧠 Skills",
                    f"{hackathon['skill_score']}/50"
                )


            with b2:

                st.metric(
                    "👥 Team",
                    f"{hackathon['team_score']}/20"
                )


            with b3:

                st.metric(
                    "🌍 Location",
                    f"{hackathon['location_score']}/15"
                )


            with b4:

                st.metric(
                    "📅 Availability",
                    f"{hackathon['date_score']}/15"
                )


            # =================================================
            # SOURCE
            # =================================================

            st.caption(
                f"📌 Source: {hackathon['source']} "
                f"• ID: {hackathon['source_id']}"
            )


            # =================================================
            # 10.12 VIEW HACKATHON
            # =================================================

            st.markdown(
                "#### 🔎 Hackathon Resource"
            )


            if hackathon["url"]:

                st.link_button(
                    "🔗 View Source",
                    hackathon["url"],
                    use_container_width=True
                )

            else:

                st.warning(
                    "⚠️ Official hackathon link "
                    "is not available."
                )


    # ========================================================
    # 10.13 REGISTERED HACKATHONS
    # ========================================================

    st.markdown("---")

    st.markdown(
        "## 🎫 Registered Hackathons"
    )


    registered_found = False


    for hackathon in results:

        hackathon_id = hackathon["id"]


        if (
            st.session_state.registrations.get(
                hackathon_id,
                "not_registered"
            )
            == "registered"
        ):

            registered_found = True


            st.success(
                f"🎉 {hackathon['name']}"
            )


            st.write(
                f"📅 **Deadline:** "
                f"{convert_deadline_to_ist(
                    hackathon['deadline']
                )}"
            )


            st.write(
                f"📌 **Source:** "
                f"{hackathon['source']}"
            )


            if hackathon_id in (
                st.session_state.ticket_ids
            ):

                ticket_id = (
                    st.session_state.ticket_ids[
                        hackathon_id
                    ]
                )


                st.write(
                    f"🎫 **Ticket ID:** "
                    f"{ticket_id}"
                )


            # ------------------------------------------------
            # OPEN REGISTERED HACKATHON
            # ------------------------------------------------

            if hackathon["url"]:

                st.link_button(
                    "🔗 Open Source",
                    hackathon["url"]
                )


    if not registered_found:

        st.info(
            "You have not registered for any "
            "hackathon yet."
        )


# ============================================================
# 10.14 NO RESULTS
# ============================================================

elif search:

    st.warning(
        "😕 No hackathons found with at least "
        "one matching skill."
    )


# ============================================================
# 11. HOW IT WORKS
# ============================================================

st.write("")

st.divider()

st.header("⚡ How HackMate AI Works")

st.caption(
    "Three simple steps to discover your next opportunity."
)

st.write("")


step1, step2, step3 = st.columns(3)


with step1:

    st.subheader("01")

    st.write(
        "💻 **Build Profile**"
    )

    st.caption(
        "Enter your skills, team size and preferences."
    )


with step2:

    st.subheader("02")

    st.write(
        "🤖 **Smart Matching**"
    )

    st.caption(
        "HackMate analyses your profile and opportunities."
    )


with step3:

    st.subheader("03")

    st.write(
        "🏆 **Discover**"
    )

    st.caption(
        "Explore hackathons that match your potential."
    )


# ============================================================
# 12. FOOTER
# ============================================================

st.write("")

st.divider()

st.caption(
    "Built with ❤️ by Team SyncMind • HackMate AI"
)