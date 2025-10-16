import streamlit as st

st.set_page_config(page_title="GPA & CGPA Calculator", layout="centered")

st.title("🎓 GPA & CGPA Calculator")
st.caption("Based on HEC Grading Criteria – COMSATS University Islamabad")

# HEC Grading Criteria Mapping
def percentage_to_gpa(percentage):
    if percentage >= 87:
        return 4.00
    elif 82 <= percentage <= 86:
        return 3.67
    elif 77 <= percentage <= 81:
        return 3.33
    elif 72 <= percentage <= 76:
        return 3.00
    elif 68 <= percentage <= 71:
        return 2.67
    elif 63 <= percentage <= 67:
        return 2.33
    elif 58 <= percentage <= 62:
        return 2.00
    elif 54 <= percentage <= 57:
        return 1.67
    elif 50 <= percentage <= 53:
        return 1.00
    else:
        return 0.00

# GPA Calculation Section
st.header("📘 Semester GPA Calculator")

num_subjects = st.number_input("Number of subjects this semester:", min_value=1, step=1)

subject_data = []
for i in range(int(num_subjects)):
    col1, col2 = st.columns(2)
    with col1:
        marks = st.number_input(f"Marks for Subject {i+1} (%)", min_value=0.0, max_value=100.0, key=f"marks_{i}")
    with col2:
        credit = st.number_input(f"Credit Hours for Subject {i+1}", min_value=0.5, step=0.5, key=f"credit_{i}")
    subject_data.append((marks, credit))

if st.button("Calculate GPA"):
    total_quality_points = 0
    total_credits = 0
    for marks, credit in subject_data:
        gpa = percentage_to_gpa(marks)
        total_quality_points += gpa * credit
        total_credits += credit
    semester_gpa = total_quality_points / total_credits if total_credits > 0 else 0
    st.success(f"✅ Your Semester GPA is: **{semester_gpa:.2f}**")

# CGPA Calculation Section
st.header("📚 CGPA Calculator")

prev_semesters = st.number_input("Number of previous semesters:", min_value=0, step=1)

prev_data = []
for i in range(int(prev_semesters)):
    col1, col2 = st.columns(2)
    with col1:
        prev_gpa = st.number_input(f"GPA for Semester {i+1}", min_value=0.0, max_value=4.0, key=f"prev_gpa_{i}")
    with col2:
        prev_credit = st.number_input(f"Total Credit Hours for Semester {i+1}", min_value=1.0, step=0.5, key=f"prev_credit_{i}")
    prev_data.append((prev_gpa, prev_credit))

if st.button("Calculate CGPA"):
    total_weighted_gpa = sum(g * c for g, c in prev_data)
    total_credits = sum(c for _, c in prev_data)

    # Include current semester if calculated
    if 'semester_gpa' in locals():
        total_weighted_gpa += semester_gpa * total_credits
        total_credits += total_credits

    cgpa = total_weighted_gpa / total_credits if total_credits > 0 else 0
    st.success(f"📊 Your CGPA is: **{cgpa:.2f}**")
