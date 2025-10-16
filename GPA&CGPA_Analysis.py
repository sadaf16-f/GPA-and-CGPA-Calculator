import streamlit as st

# Title
st.title("🎓 GPA & CGPA Calculator")

# Sidebar for instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
- Enter your marks for each subject.
- GPA is calculated based on current semester.
- CGPA is calculated using previous semesters' GPA and current GPA.
""")

# Function to convert marks to grade points
def marks_to_gpa(marks):
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 60:
        return 2.3
    elif marks >= 55:
        return 2.0
    elif marks >= 50:
        return 1.7
    else:
        return 0.0

# Input number of subjects
num_subjects = st.number_input("Enter number of subjects this semester:", min_value=1, step=1)

# Input marks for each subject
marks_list = []
for i in range(int(num_subjects)):
    mark = st.number_input(f"Enter marks for Subject {i+1}:", min_value=0.0, max_value=100.0)
    marks_list.append(mark)

# GPA Calculation
if st.button("Calculate GPA"):
    grade_points = [marks_to_gpa(m) for m in marks_list]
    gpa = sum(grade_points) / len(grade_points)
    st.success(f"Your GPA for this semester is: {gpa:.2f}")

# CGPA Calculation
st.subheader("📚 CGPA Calculator")
prev_semesters = st.number_input("Enter number of previous semesters:", min_value=0, step=1)

prev_gpas = []
for i in range(int(prev_semesters)):
    g = st.number_input(f"GPA for Semester {i+1}:", min_value=0.0, max_value=4.0)
    prev_gpas.append(g)

if st.button("Calculate CGPA"):
    all_gpas = prev_gpas + [gpa] if 'gpa' in locals() else prev_gpas
    if all_gpas:
        cgpa = sum(all_gpas) / len(all_gpas)
        st.success(f"Your CGPA is: {cgpa:.2f}")
    else:
        st.warning("Please enter GPA values to calculate CGPA.")

