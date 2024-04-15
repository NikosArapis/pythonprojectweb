import streamlit as st
from students import Student, Classroom


def app(my_class_room):
    st.title("Student Grades Modifier")
    # Input for the student ID
    updated = False
    student_id = st.number_input("Enter Student ID", min_value=1, value=1)
    student = my_class_room.get_student_by_id(student_id)
    # Button to search for the student
    if st.button("Search"):
        student = my_class_room.get_student_by_id(student_id)
    if student:
        st.write(f"Found : {student.fname} {student.lname}")
        update_values(student)
        st.success('successfully update')
    else :
        st.write(f'There is not student with id {student_id}')

def update_values(student):
    with st.form(key = "gradeform"):
        courses = student.courses
        math_grade = st.number_input('grade for math',min_value=0, max_value=100, value=courses['Math'])
        history_grade = st.number_input('grade for history',min_value=0, max_value=100, value=courses['History'])
        physics_grade = st.number_input('grade for physics',min_value=0, max_value=100, value=courses['Physics'])
        english_grade = st.number_input('grade for english',min_value=0, max_value=100, value=courses['English'])
        biology_grade = st.number_input('grade for biology',min_value=0, max_value=100, value=courses['Biology'])
        submitted = st.form_submit_button('update grades')

    if submitted:
        student.add_grade('Math',math_grade)
        student.add_grade('History',history_grade)
        student.add_grade('Physics',physics_grade)
        student.add_grade('English',english_grade)
        student.add_grade('Biology',biology_grade)
