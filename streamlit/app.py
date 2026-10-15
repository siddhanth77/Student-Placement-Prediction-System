import sys
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Student Placement Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add project root so that from src.X imports work
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# Add the _pages directory for existing page imports
_pages_dir = str(Path(__file__).resolve().parent / "_pages")
if _pages_dir not in sys.path:
    sys.path.insert(0, _pages_dir)

# Existing dashboard pages
from home import render_home_page
from upload import render_upload_page
from analysis import render_analysis_page
from training import render_training_page
from prediction import render_prediction_page
from explanation import render_explanation_page
from settings import render_settings_page
from chatbot import render_chatbot_page

# Authentication and authorization
from login import render_login
from src.auth import logout_user
from src.authorization import can_access


def load_css():
    css_path = Path(__file__).resolve().parent / "css" / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )


load_css()

# --------------------------------------------------
# AUTHENTICATION GATE
# --------------------------------------------------

if not st.session_state.get("authenticated", False):
    st.session_state.pop("page", None)
    render_login()
    st.stop()

user_role = st.session_state.get("user_role", "student")
user_name = st.session_state.get("user_name", "User")

# Map visible menu labels to permission names and render functions
pages = {
    "🏠 Home": ("Home", render_home_page),
    "📂 Upload Dataset": ("Upload Dataset", render_upload_page),
    "📊 Data Analysis": ("Analysis", render_analysis_page),
    "🤖 Train Models": ("Training", render_training_page),
    "🎯 Predict Placement": ("Prediction", render_prediction_page),
    "🧠 Explain Prediction": ("Explanation", render_explanation_page),
    "💬 AI Placement Assistant": ("Chatbot", render_chatbot_page),
    "⚙ Settings": ("Settings", render_settings_page),
}

# Only show pages allowed for this user's role
available_pages = [
    label
    for label, (permission_name, _) in pages.items()
    if can_access(user_role, permission_name)
]

# Safety fallback if the role is invalid or has no permitted pages
if not available_pages:
    st.error("Your account has no permitted pages. Please contact an administrator.")
    if st.button("Logout"):
        logout_user()
        st.rerun()
    st.stop()

# Set a permitted default page
if st.session_state.get("page") not in available_pages:
    st.session_state.page = "🏠 Home"

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h2 style="color: #FFFFFF; font-weight: 800; font-size: 1.5rem;
    letter-spacing: -0.05em; margin-bottom: 4px;">
        Placement Portal
    </h2>
</div>
""", unsafe_allow_html=True)

st.sidebar.write(f"Welcome, **{user_name}**")
st.sidebar.caption(f"Role: {user_role.title()}")

if st.sidebar.button("Logout", use_container_width=True):
    logout_user()
    st.session_state.pop("page", None)
    st.rerun()

st.sidebar.divider()
st.sidebar.subheader("Navigation")

menu_selection = st.sidebar.radio(
    label="Go to page",
    options=available_pages,
    index=available_pages.index(st.session_state.page),
    label_visibility="collapsed",
    key="navigation_menu"
)

st.session_state.page = menu_selection

# --------------------------------------------------
# RENDER SELECTED PAGE
# --------------------------------------------------

active_page = st.session_state.page
permission_name, render_function = pages[active_page]

# Check permission again before rendering the page
if can_access(user_role, permission_name):
    render_function()
else:
    st.error("You do not have permission to access this page.")

# --------------------------------------------------
# SIDEBAR FOOTER
# --------------------------------------------------

st.sidebar.write("---")
st.sidebar.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 0.8rem;
font-weight: 500;">
    Student Placement Portal<br>
    © 2026 All Rights Reserved
</div>
""", unsafe_allow_html=True)