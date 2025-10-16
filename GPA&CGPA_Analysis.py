import streamlit as st
import pandas as pd

st.set_page_config(page_title="COMSATS GPA & CGPA Calculator", layout="centered")

st.title("🎓 COMSATS GPA & CGPA Calculator")

st.write("""
Enter your marks and credit hours for each subject.
This calculator follows **COMSATS University Islamabad** official grading scale.
""")

# Step 1: Number of subjects
num_subjects = st.number_input("Enter number of subjects:", min_value=1, max_value=15, value=5, step=1)

subjects, marks, credits = [], [], []

st.subheader("📘 Enter Subject Details")
for i in range(int(num_subjects)):
    col1, col2, col3 = st.columns(3)
    with col1:
        subjects.append(st.text_input(f"Subject {i+1} Name", f"Subject {i+1}"))
    with col2:
        marks.append(st.number_input(f"Marks (0-100) for {subjects[i]}", min_value=0.0, max_value=100.0, step=0.5))
    with col3:
        credits.append(st.number_input(f"Credit Hours for {subjects[i]}", min_value=1.0, max_value=5.0, value=3.0))

# Step 2: COMSATS grading system
def grade_point(mark):
    if mark >= 85:
        return 4.00, "A"
    elif mark >= 80:
        return 3.67, "A-"
    elif mark >= 75:
        return 3.33, "B+"
    elif mark >= 70:
        return 3.00, "B"
    elif mark >= 65:
        return 2.67, "B-"
    elif mark >= 61:
        return 2.33, "C+"
    elif mark >= 58:
        return 2.00, "C"
    elif mark >= 55:
        return 1.67, "C-"
    elif mark >= 50:
        return 1.00, "D"
    else:
        return 0.00, "F"

# Step 3: GPA Calculation
if st.button("Calculate GPA & CGPA"):
    data = []
    total_points = 0
    total_credits = 0

    for i in range(int(num_subjects)):
        gp, grade = grade_point(marks[i])
        points = gp * credits[i]
        data.append([subjects[i], marks[i], credits[i], grade, gp])
        total_points += points
        total_credits += credits[i]

    gpa = total_points / total_credits if total_credits > 0 else 0

    df = pd.DataFrame(data, columns=["Subject", "Marks", "Credit Hours", "Grade", "Grade Point"])
    st.subheader("📊 Semester Results")
    st.dataframe(df, use_container_width=True)

    st.success(f"🎯 Your Semester GPA is: **{gpa:.2f}**")

    # Step 4: CGPA Section
    st.subheader("🏆 CGPA Calculation")
    first_sem = st.radio("Is this your first semester?", ("Yes", "No"))

    if first_sem == "No":
        prev_cgpa = st.number_input("Enter your Previous CGPA:", min_value=0.0, max_value=4.0, value=0.0)
        prev_credits = st.number_input("Enter your Total Completed Credit Hours (before this semester):", min_value=0.0, value=0.0)
        if prev_credits > 0:
            cgpa = ((prev_cgpa * prev_credits) + (gpa * total_credits)) / (prev_credits + total_credits)
            st.info(f"✅ Your Updated CGPA is: **{cgpa:.2f}**")
        else:
            st.info(f"Your Current CGPA is same as GPA: **{gpa:.2f}**")
    else:
        st.info(f"🎓 Your CGPA (1st semester) = **{gpa:.2f}**")

st.caption("Developed by Sadaf 🌸 — Data Science Student (COMSATS Grading Standard)")
