# ============================================================
# HACKMATE AI - SKILL RELATIONSHIPS
# ============================================================

SKILL_ALIASES = {

    "ml": "machine learning",

    "ai": "artificial intelligence",

    "js": "javascript",

    "node": "node.js",

    "nodejs": "node.js",

    "k8s": "kubernetes",

    "aws cloud": "aws",

    "gcp": "google cloud"
}


def normalize_skill(skill):

    skill = skill.lower().strip()

    return SKILL_ALIASES.get(
        skill,
        skill
    )


def are_related(skill1, skill2):

    skill1 = normalize_skill(skill1)
    skill2 = normalize_skill(skill2)

    return skill1 == skill2