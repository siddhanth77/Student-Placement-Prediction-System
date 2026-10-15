
PAGE_PERMISSIONS = {
    "student": [
        "Home",
        "Prediction",
        "Explanation",
        "Settings",
        "Chatbot",
    ],

    "admin": [
        "Home",
        "Upload Dataset",
        "Analysis",
        "Training",
        "Prediction",
        "Explanation",
        "Settings",
        "Chatbot",
    ],
}


def allowed_pages(role):
    return PAGE_PERMISSIONS.get(role, [])


def can_access(role, page):
    return page in allowed_pages(role)
