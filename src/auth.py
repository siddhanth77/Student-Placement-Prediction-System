
import os

import streamlit as st
from dotenv import load_dotenv
from supabase import create_client, Client


# Load credentials from the project-root .env file
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

load_dotenv(os.path.join(PROJECT_ROOT, ".env"))


def get_supabase() -> Client:
    """Create a Supabase client for the current Streamlit session."""

    if "supabase_client" not in st.session_state:
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")

        if not url or not key:
            raise RuntimeError(
                "SUPABASE_URL or SUPABASE_KEY is missing "
                "from the project-root .env file."
            )

        st.session_state["supabase_client"] = create_client(
            url, key
        )

    return st.session_state["supabase_client"]


def register_user(name: str, email: str, password: str):
    """Register a user. New accounts receive the student role."""

    name = name.strip()
    email = email.strip().lower()

    if not name or not email or not password:
        raise ValueError("All fields are required.")

    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters."
        )

    client = get_supabase()

    response = client.auth.sign_up({
        "email": email,
        "password": password,
        "options": {
            "data": {
                "full_name": name
            }
        },
    })

    if response.user is None:
        raise ValueError("Registration was unsuccessful.")

    # The Supabase database trigger creates the profile
    # with role='student'. Never accept a role from signup.
    return {
        "message": "Registration successful.",
        "confirmation_required": response.session is None,
    }


def login_user(email: str, password: str):
    """Authenticate a user and retrieve their database role."""

    email = email.strip().lower()

    if not email or not password:
        raise ValueError("Enter your email and password.")

    client = get_supabase()

    response = client.auth.sign_in_with_password({
        "email": email,
        "password": password,
    })

    if response.user is None or response.session is None:
        raise ValueError(
            "Login failed. Check your credentials and email confirmation."
        )

    # Verify the authenticated identity with Supabase.
    verified = client.auth.get_user(
        response.session.access_token
    )

    if verified.user is None:
        client.auth.sign_out()
        raise ValueError("User verification failed.")

    user_id = str(verified.user.id)

    # Retrieve the role from the protected profiles table.
    result = (
        client.table("profiles")
        .select("id, full_name, role")
        .eq("id", user_id)
        .limit(1)
        .execute()
    )

    if not result.data:
        client.auth.sign_out()
        raise ValueError(
            "User profile not found. Check the database trigger."
        )

    profile = result.data[0]
    role = profile["role"]

    if role not in ("student", "admin"):
        client.auth.sign_out()
        raise ValueError("Invalid account role.")

    # Store the verified identity and role in this session.
    st.session_state["authenticated"] = True
    st.session_state["user_id"] = user_id
    st.session_state["user_name"] = (
        profile["full_name"] or email
    )
    st.session_state["user_role"] = role

    return role


def logout_user():
    """Sign out and clear local authentication state."""

    client = st.session_state.get("supabase_client")

    try:
        if client is not None:
            client.auth.sign_out()
    finally:
        for key in (
            "authenticated",
            "user_id",
            "user_name",
            "user_role",
            "supabase_client",
        ):
            st.session_state.pop(key, None)
