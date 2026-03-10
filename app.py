import streamlit as st
from modernization import modernize_code

st.title("Legacy Code Modernization Engine")

st.write("Convert legacy code into modern coding standards.")

code = st.text_area("Paste your legacy code here")

if st.button("Modernize Code"):

    if code.strip():
        result = modernize_code(code)

        st.subheader("Modernized Code")
        st.code(result)

    else:
        st.warning("Please enter code.")