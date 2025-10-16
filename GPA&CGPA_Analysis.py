import streamlit as st

st.title("📘 GPA & CGPA Calculator (with Credit Hours)")

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

# Input marks and credit hours for each subject
marks_list = []
credits_list = []
for i in range(int(num_subjects)):
    mark = st.number_input(f"Marks for Subject {i+1}:", min_value=0.0, max_value=100.0)
    credit = st.number_input(f"Credit Hours for Subject {i+1}:", min_value=0.5, step=0.5)
    marks_list.append(mark)
    credits_list.append(credit)

# GPA Calculation
if st.button("Calculate GPA"):
    grade_points = [marks_to_gpa(m) for m in marks_list]
    weighted_points = [gp * cr for gp, cr in zip(grade_points, credits_list)]
    total_credits = sum(credits_list)
    gpa = sum(weighted_points) / total_credits if total_credits > 0 else 0
    st.success(f"Your GPA for this semester is: {gpa:.2f}")

# CGPA Calculation
st.subheader("📚 CGPA Calculator")
prev_semesters = st.number_input("Enter number of previous semesters:", min_value=0, step=1)

prev_gpas = []
prev_credits = []
for i in range(int(prev_semesters)):
    g = st.number_input(f"GPA for Semester {i+1}:", min_value=0.0, max_value=4.0)
    c = st.number_input(f"Total Credit Hours for Semester {i+1}:", min_value=1.0, step=0.5)
    prev_gpas.append(g)
    prev_credits.append(c)

if st.button("Calculate CGPA"):
    total_weighted_gpa = sum([g * c for g, c in zip(prev_gpas, prev_credits)])
    total_credits_all = sum(prev_credits)
    if 'gpa' in locals():
        total_weighted_gpa += gpa * total_credits
        total_credits_all += total_credits
    cgpa = total_weighted_gpa / total_credits_all if total_credits_all > 0 else 0
    st.success(f"Your CGPA is: {cgpa:.2f}")

