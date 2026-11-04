import streamlit as st
import joblib
import numpy as np

model=joblib.load("salary_model.pkl")

st.title("👜 Employee Salary Estimation Portal")

page=st.sidebar.selectbox("Navigation",["Home Page","Input Form"])

if page == "Home Page":
    st.subheader("HR Analytics Suite")
    st.write("Estimate competitive compensation packages based on candidate credentials")
    st.info("Navigate to **Input Form** via the sidebar to run an estimation.")

elif page == "Input Form":
    st.subheader("Candidate Profile Input")
    
    with st.form("salary_form"):
        exp=st.number_input("Years of Experience:",min_value=0.0,max_value=40.0,value=3.0)
        edu=st.selectbox("Education Level:",options=[("Bachelor's(1)",1),("Master's(2)",2),("PhD (3)",3)],format_func=lambda x:x[0])[1]
        certs=st.number_input("Professional Certifications:",min_value=0,max_value=10,value=1)
        score=st.slider("Performance Review Score(0-100):",0,100,75)

        submitted=st.form_submit_button("Calculate Estimated Salary")

        if submitted:
            input_features=np.array([[exp,edu,certs,score]])
            salary=model.predict(input_features)[0]

            st.markdown("-----")
            st.subheader("Estimated Market Valuation")
            st.success(f"💲Estimated Annual Salary:**${salary:.2f}LPA**")
                         
