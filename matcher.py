from datetime import date
from skill_map import are_related


def calculate_match(
    user_skills,
    team_size,
    location,
    available_date,
    hackathon
):

    # ========================================================
    # 1. USER SKILLS
    # ========================================================

    user_skill_list = [
        skill.strip().lower()
        for skill in str(user_skills).split(",")
        if skill.strip()
    ]


    # ========================================================
    # 2. HACKATHON REQUIRED SKILLS
    # ========================================================

    hackathon_skill_list = [
        skill.strip().lower()
        for skill in str(hackathon["skills"]).split(",")
        if skill.strip()
    ]


    # ========================================================
    # 3. SKILL MATCH
    # ========================================================

    matching_skills = []
    matched_required_skills = set()

    for hackathon_skill in hackathon_skill_list:

        for user_skill in user_skill_list:

            if are_related(user_skill, hackathon_skill):

                matching_skills.append(user_skill)

                matched_required_skills.add(
                    hackathon_skill
                )

                break


    matching_skills = list(
        dict.fromkeys(matching_skills)
    )


    # ========================================================
    # 4. SKILL SCORE
    # ========================================================

    total_required_skills = len(
        set(hackathon_skill_list)
    )

    total_matched_skills = len(
        matched_required_skills
    )

    if total_required_skills > 0:

        skill_score = (
            total_matched_skills
            / total_required_skills
        ) * 50

    else:

        skill_score = 0


    # ========================================================
    # 5. TEAM SIZE MATCH
    # ========================================================

    team_min = int(
        hackathon["team_min"]
    )

    team_max = int(
        hackathon["team_max"]
    )

    if team_min <= team_size <= team_max:

        team_score = 20
        team_match = True

    else:

        team_score = 0
        team_match = False


    # ========================================================
    # 6. LOCATION MATCH
    # ========================================================

    hackathon_location = str(
        hackathon["location"]
    ).strip().lower()

    user_location = str(
        location
    ).strip().lower()

    if (
        hackathon_location == user_location
        or hackathon_location == "global"
    ):

        location_score = 15
        location_match = True

    else:

        location_score = 0
        location_match = False


    # ========================================================
    # 7. DATE MATCH
    # ========================================================

    try:

        deadline = date.fromisoformat(
            str(hackathon["deadline"])
        )

        if available_date <= deadline:

            date_score = 15
            date_match = True

        else:

            date_score = 0
            date_match = False

    except (ValueError, TypeError):

        date_score = 0
        date_match = False


    # ========================================================
    # 8. FINAL SCORE
    # ========================================================

    final_score = (
        skill_score
        + team_score
        + location_score
        + date_score
    )


    # ========================================================
    # 9. RETURN RESULT
    # ========================================================

    return {

        "score": round(final_score),

        "matching_skills": matching_skills,

        "team_match": team_match,

        "location_match": location_match,

        "date_match": date_match,

        "skill_score": round(skill_score),

        "team_score": team_score,

        "location_score": location_score,

        "date_score": date_score
    }