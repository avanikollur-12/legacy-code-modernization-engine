import streamlit as st
from modernization import modernize_code, detect_language

st.set_page_config(page_title="Legacy Code Modernization Engine")

st.title("🚀 Legacy Code Modernization Engine")
st.write("Convert legacy code into modern coding standards instantly.")

# Input box
code = st.text_area("Paste your legacy code here", height=250)

if st.button("Modernize Code"):

    if code.strip():

        # Detect language
        language = detect_language(code)
        st.info(f"Detected Language: {language}")

        original, modern = modernize_code(code)

        # Side-by-side comparison
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🧾 Legacy Code")
            st.code(original)

        with col2:
            st.subheader("✨ Modern Code")
            st.code(modern)

        # Download button
        st.download_button(
            label="📥 Download Modern Code",
            data=modern,
            file_name="modern_code.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please enter code.")
