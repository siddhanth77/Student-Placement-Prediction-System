
import streamlit as st
from src.auth import login_user, register_user


def render_login():
    # Identify this page for login-specific CSS
    st.markdown(
        '<div class="login-page-marker"></div>',
        unsafe_allow_html=True
    )

    if "login_view" not in st.session_state:
        st.session_state.login_view = "Login"

    # Center the content
    left, center, right = st.columns([1, 1.5, 1])

    with center:
        st.markdown(
            """
            <div class="login-heading">
                <div class="login-icon">🎓</div>
                <h1>Student Placement <span>Portal</span></h1>
                <p>Sign in or create an account to continue</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Login and Register selectors
        login_col, register_col = st.columns(2)

        with login_col:
            if st.button(
                "Login",
                key="select_login",
                use_container_width=True,
                type=(
                    "primary"
                    if st.session_state.login_view == "Login"
                    else "secondary"
                )
            ):
                st.session_state.login_view = "Login"
                st.rerun()

        with register_col:
            if st.button(
                "Register",
                key="select_register",
                use_container_width=True,
                type=(
                    "primary"
                    if st.session_state.login_view == "Register"
                    else "secondary"
                )
            ):
                st.session_state.login_view = "Register"
                st.rerun()

        # LOGIN FORM
        if st.session_state.login_view == "Login":
            with st.form("login_form"):
                email = st.text_input(
                    "Email address",
                    placeholder="Enter your email address",
                    key="login_email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Enter your password",
                    key="login_password"
                )

                submitted = st.form_submit_button(
                    "Sign in",
                    use_container_width=True
                )

            if submitted:
                if not email.strip() or not password:
                    st.error("Please enter your email and password.")
                else:
                    try:
                        role = login_user(email, password)
                        st.success(
                            f"Login successful! Role: {role.title()}"
                        )
                        st.rerun()
                    except Exception as exc:
                        st.error(str(exc))

        # REGISTRATION FORM
        else:
            with st.form("register_form"):
                name = st.text_input(
                    "Full name",
                    placeholder="Enter your full name",
                    key="register_name"
                )

                email = st.text_input(
                    "Email address",
                    placeholder="Enter your email address",
                    key="register_email"
                )

                password = st.text_input(
                    "Create password",
                    type="password",
                    placeholder="Create a password",
                    key="register_password"
                )

                confirm = st.text_input(
                    "Confirm password",
                    type="password",
                    placeholder="Re-enter your password",
                    key="register_confirm"
                )

                submitted = st.form_submit_button(
                    "Create account",
                    use_container_width=True
                )

            if submitted:
                if not name.strip() or not email.strip():
                    st.error("Name and email are required.")
                elif not password:
                    st.error("Please create a password.")
                elif password != confirm:
                    st.error("Passwords do not match.")
                else:
                    try:
                        result = register_user(name, email, password)

                        if result["confirmation_required"]:
                            st.success(
                                "Account created. Check your email "
                                "to confirm it, then log in."
                            )
                        else:
                            st.success(
                                "Account created. Please log in."
                            )

                    except Exception:
                        st.error(
                            "Registration failed. Check your email, "
                            "password requirements, and Supabase settings."
                        )
