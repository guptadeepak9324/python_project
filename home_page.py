import streamlit as st

st.set_page_config(
    page_title="My Website",
    page_icon="🐍",
    layout="wide"
)

# Navigation
st.sidebar.title("My Website")
st.sidebar.markdown("---")
st.sidebar.write("Home")
st.sidebar.write("About")
st.sidebar.write("Services")
st.sidebar.write("Contact")

# Main heading
st.title("Welcome to My Website 👋")
st.subheader("Explore the world of Python!")

st.markdown("---")

# About section
st.header("About Us")

st.write("""
Welcome to our website!

We are learning Python and building interesting
applications using modern technologies.
""")

# Services section
st.header("Our Services")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🐍 Python")
    st.write("Learn Python programming.")

with col2:
    st.subheader("🌐 Web Development")
    st.write("Explore web development.")

with col3:
    st.subheader("💡 Projects")
    st.write("Build real-world projects.")

st.markdown("---")

# Footer
st.markdown(
    "<center>© 2026 My Website | All Rights Reserved</center>",
    unsafe_allow_html=True
)