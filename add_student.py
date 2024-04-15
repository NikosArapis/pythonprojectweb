import streamlit as st
from students import Student,Classroom
from datetime import datetime

def app(myclassroom):
    st.subheader("Add student")
    with st.form("student_details",clear_on_submit=True):
        id=st.number_input("ID",1,1000)
        fname=st.text_input("Enter first name")
        lname=st.text_input("Enter last name")
        datebirth=st.date_input("Enter your birth date")
        gender=st.radio("Gender",["Male","Female"])
        weight=st.slider("Weight",30,150)
        height=st.slider("Height",125,210)

        submitted=st.form_submit_button("submit",use_container_width=True)
        if submitted:
            stud=Student(id,fname,lname,datebirth,height,weight,gender)
            myclassroom.add_student(stud)
            st.success(f"student {fname} {lname} added successfully")
        else:
            st.warning('No student found')