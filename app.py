
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="EduPro Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("edupro_processed_data.csv")

df = load_data()

# ---------------- DASHBOARD HEADER ----------------
st.title("📊 EduPro Analytics Dashboard")
st.markdown(
    "### Learner Demographics and Course Enrollment Behavior Analysis"
)

st.divider()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Filter Data")

age_options = sorted(df["AgeGroup"].dropna().unique().tolist())
gender_options = sorted(df["Gender"].dropna().unique().tolist())
category_options = sorted(
    df["CourseCategory"].dropna().unique().tolist()
)
type_options = sorted(df["CourseType"].dropna().unique().tolist())

selected_age = st.sidebar.multiselect(
    "Select Age Group",
    age_options,
    default=age_options
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    gender_options,
    default=gender_options
)

selected_category = st.sidebar.multiselect(
    "Select Course Category",
    category_options,
    default=category_options
)

selected_type = st.sidebar.multiselect(
    "Select Course Type",
    type_options,
    default=type_options
)

# ---------------- FILTER DATA ----------------
filtered_df = df[
    df["AgeGroup"].isin(selected_age)
    & df["Gender"].isin(selected_gender)
    & df["CourseCategory"].isin(selected_category)
    & df["CourseType"].isin(selected_type)
].copy()

st.caption(
    f"Showing {len(filtered_df):,} enrollment records "
    f"out of {len(df):,} total records."
)

# ---------------- KPI CARDS ----------------
total_learners = filtered_df["UserID"].nunique()
total_courses = filtered_df["CourseID"].nunique()
total_enrollments = filtered_df["TransactionID"].nunique()
total_amount = filtered_df["Amount"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Unique Learners", f"{total_learners:,}")
col2.metric("Courses Enrolled", f"{total_courses:,}")
col3.metric("Enrollment Records", f"{total_enrollments:,}")
col4.metric("Transaction Amount", f"{total_amount:,.2f}")

st.divider()

# ---------------- AGE GROUP CHART ----------------
st.subheader("Learner Age Group Distribution")

age_counts = (
    filtered_df.drop_duplicates("UserID")
    ["AgeGroup"].value_counts()
    .reindex(age_options, fill_value=0)
    .rename_axis("Age Group")
    .reset_index(name="Learners")
)

fig_age = px.bar(
    age_counts,
    x="Age Group",
    y="Learners",
    text="Learners",
    title="Unique Learners by Age Group"
)

st.plotly_chart(fig_age, use_container_width=True)

# ---------------- TOP COURSES ----------------
st.subheader("Top 10 Most Enrolled Courses")

top_courses = (
    filtered_df.groupby("CourseName")["TransactionID"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
    .reset_index(name="Enrollments")
)

fig_courses = px.bar(
    top_courses,
    x="Enrollments",
    y="CourseName",
    orientation="h",
    text="Enrollments",
    title="Top 10 Courses"
)

st.plotly_chart(fig_courses, use_container_width=True)

# ---------------- CATEGORY CHART ----------------
st.subheader("Enrollment by Course Category")

category_counts = (
    filtered_df.groupby("CourseCategory")["TransactionID"]
    .nunique()
    .reset_index(name="Enrollments")
    .sort_values("Enrollments", ascending=False)
)

fig_category = px.bar(
    category_counts,
    x="CourseCategory",
    y="Enrollments",
    title="Course Category Popularity"
)

fig_category.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig_category, use_container_width=True)

# ---------------- FREE VS PAID ----------------
st.subheader("Free vs Paid Course Enrollments")

type_counts = (
    filtered_df.groupby("CourseType")["TransactionID"]
    .nunique()
    .reset_index(name="Enrollments")
)

fig_type = px.pie(
    type_counts,
    names="CourseType",
    values="Enrollments",
    hole=0.4,
    title="Free vs Paid Enrollment Records"
)

st.plotly_chart(fig_type, use_container_width=True)

# ---------------- MONTHLY TREND ----------------
st.subheader("Monthly Enrollment Trend")

monthly_counts = (
    filtered_df.groupby("EnrollmentMonth")["TransactionID"]
    .nunique()
    .reindex(range(1, 13), fill_value=0)
    .rename_axis("Month")
    .reset_index(name="Enrollments")
)

month_names = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

monthly_counts["MonthName"] = monthly_counts["Month"].map(month_names)

fig_month = px.line(
    monthly_counts,
    x="MonthName",
    y="Enrollments",
    markers=True,
    title="Monthly Enrollment Records"
)

st.plotly_chart(fig_month, use_container_width=True)


# ---------------- ADVANCED ANALYTICS ----------------
st.divider()
st.header("Advanced Analytics")

# Chart 1: Average Course Rating by Category
st.subheader("Average Course Rating by Category")

rating_data = (
    filtered_df.groupby("CourseCategory")["CourseRating"]
    .mean()
    .reset_index()
    .sort_values("CourseRating", ascending=False)
)

fig_rating = px.bar(
    rating_data,
    x="CourseCategory",
    y="CourseRating",
    title="Average Course Rating by Category",
    labels={
        "CourseCategory": "Course Category",
        "CourseRating": "Average Rating"
    },
    text_auto=".2f"
)

fig_rating.update_layout(
    xaxis_tickangle=-45,
    yaxis_range=[0, 5]
)

st.plotly_chart(fig_rating, use_container_width=True)


# Chart 2: Monthly Transaction Amount
st.subheader("Monthly Transaction Amount")

monthly_amount = (
    filtered_df.groupby("EnrollmentMonth")["Amount"]
    .sum()
    .reindex(range(1, 13), fill_value=0)
    .rename_axis("Month")
    .reset_index(name="Total Amount")
)

month_names = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

monthly_amount["Month Name"] = (
    monthly_amount["Month"].map(month_names)
)

fig_amount = px.line(
    monthly_amount,
    x="Month Name",
    y="Total Amount",
    markers=True,
    title="Monthly Transaction Amount"
)

st.plotly_chart(fig_amount, use_container_width=True)


# Chart 3: Enrollment by Course Level
st.subheader("Enrollment by Course Level")

level_data = (
    filtered_df.groupby("CourseLevel")["TransactionID"]
    .nunique()
    .reset_index(name="Enrollments")
)

fig_level = px.bar(
    level_data,
    x="CourseLevel",
    y="Enrollments",
    color="CourseLevel",
    text="Enrollments",
    title="Enrollment Records by Course Level"
)

st.plotly_chart(fig_level, use_container_width=True)


# Chart 4: Gender Distribution
st.subheader("Gender Distribution")

gender_data = (
    filtered_df.drop_duplicates("UserID")["Gender"]
    .value_counts()
    .rename_axis("Gender")
    .reset_index(name="Learners")
)

fig_gender = px.pie(
    gender_data,
    names="Gender",
    values="Learners",
    hole=0.4,
    title="Unique Learners by Gender"
)

st.plotly_chart(fig_gender, use_container_width=True)



# ---------------- INSIGHTS AND FINDINGS ----------------
st.divider()
st.header("Insights and Findings")

if not filtered_df.empty:

    # Insight 1: Most popular course
    course_counts = filtered_df["CourseName"].value_counts()

    if not course_counts.empty:
        popular_course = course_counts.idxmax()
        popular_count = course_counts.max()

        st.subheader("1. Most Popular Course")
        st.write(
            f"**{popular_course}** has the highest number "
            f"of enrollment records: **{popular_count:,}**."
        )

    # Insight 2: Most popular category
    category_counts = filtered_df["CourseCategory"].value_counts()

    if not category_counts.empty:
        popular_category = category_counts.idxmax()
        category_count = category_counts.max()

        st.subheader("2. Most Popular Course Category")
        st.write(
            f"**{popular_category}** is the leading category "
            f"with **{category_count:,}** enrollment records."
        )

    # Insight 3: Highest enrollment month
    month_names = {
        1: "January", 2: "February", 3: "March",
        4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December"
    }

    monthly_counts = filtered_df.groupby(
        "EnrollmentMonth"
    )["TransactionID"].nunique()

    if not monthly_counts.empty:
        highest_month = monthly_counts.idxmax()
        highest_month_name = month_names.get(
            int(highest_month), str(highest_month)
        )
        highest_month_count = monthly_counts.max()

        st.subheader("3. Highest Enrollment Month")
        st.write(
            f"**{highest_month_name}** has the highest number "
            f"of enrollment records: **{highest_month_count:,}**."
        )

    # Insight 4: Free vs paid courses
    if "CourseType" in filtered_df.columns:
        type_counts = filtered_df["CourseType"].value_counts()

        if not type_counts.empty:
            most_common_type = type_counts.idxmax()
            type_count = type_counts.max()

            st.subheader("4. Most Common Course Type")
            st.write(
                f"**{most_common_type}** courses account for "
                f"the largest number of records: **{type_count:,}**."
            )

    # Insight 5: Transaction amount
    total_amount = filtered_df["Amount"].sum()

    st.subheader("5. Total Transaction Amount")
    st.write(
        f"The total recorded transaction amount for the "
        f"selected data is **{total_amount:,.2f}**."
    )

else:
    st.warning(
        "No records match the selected filters. "
        "Please change your sidebar filters."
    )




# ---------------- DATA TABLE AND CSV EXPORT ----------------
st.divider()
st.header("Filtered Data and Download")

st.write(
    "View the records based on your selected filters "
    "and download them as a CSV file."
)

# Select columns to display
display_columns = [
    "TransactionID",
    "UserID",
    "UserName",
    "Age",
    "Gender",
    "CourseName",
    "CourseCategory",
    "CourseType",
    "CourseLevel",
    "CoursePrice",
    "CourseRating",
    "EnrollmentMonth",
    "Amount",
    "PaymentMethod"
]

# Keep only columns available in the dataset
display_columns = [
    col for col in display_columns
    if col in filtered_df.columns
]

# Display filtered data
st.subheader("Enrollment Records")

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)

# Show number of records
st.write(f"Total records displayed: {len(filtered_df):,}")

# Convert filtered data into CSV
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

# Download button
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name="edupro_filtered_data.csv",
    mime="text/csv"
)


# ---------------- FOOTER ----------------
st.divider()
st.caption("EduPro Analytics | Academic Data Analysis Project")
