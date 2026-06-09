import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6IUXbDRBZ0EdhD1luPxX--y4D9h_JIdAFy00m8H_nliPw")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the question:")
if st.button("submit"):
    res=model.generate_content(qns+"you are the smart email writer,writes to email. ")
    st.write(res.text)
    