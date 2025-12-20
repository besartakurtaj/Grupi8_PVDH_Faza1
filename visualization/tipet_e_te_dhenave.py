import streamlit as st
import pandas as pd
import plotly.express as px

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(
    page_title="Data Visualization Dashboard",
    layout="wide"
)

st.title("📊 Data Visualization Dashboard")

# ======================================
# LOAD DATA
# ======================================
df = pd.read_csv("../data/cleaned_dataset.csv")

# Identify data types
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

# ======================================
# NAVIGATION
# ======================================
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "📌 Data Types Overview",
        "🔢 Numerical Data",
        "🏷️ Categorical Data",
        "📈 Multidimensional"
    ]
)

# ======================================
# PAGE 1: DATA TYPES
# ======================================
if page == "📌 Data Types Overview":
    st.header("📌 Data Types Overview")
    st.caption("Struktura e dataset-it sipas tipeve të të dhënave")

    c1, c2, c3 = st.columns(3)
    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Numerical Columns", len(numerical_cols))

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔢 Numerical Columns")
        st.dataframe(
            pd.DataFrame(numerical_cols, columns=["Column"]),
            use_container_width=True,
            height=350
        )

    with col2:
        st.subheader("🏷️ Categorical Columns")
        st.dataframe(
            pd.DataFrame(categorical_cols, columns=["Column"]),
            use_container_width=True,
            height=350
        )

# ======================================
# PAGE 2: NUMERICAL DATA
# ======================================
elif page == "🔢 Numerical Data":
    st.header("🔢 Numerical Data")

    num_col = st.sidebar.selectbox("Select numerical column", numerical_cols)

    c1, c2, c3 = st.columns(3)
    c1.metric("Min", round(df[num_col].min(), 2))
    c2.metric("Mean", round(df[num_col].mean(), 2))
    c3.metric("Max", round(df[num_col].max(), 2))

    fig = px.violin(
        df,
        y=num_col,
        box=True,
        points="outliers",
        title=f"Distribution of {num_col}"
    )
    st.plotly_chart(fig, use_container_width=True)

# ======================================
# PAGE 3: CATEGORICAL DATA
# ======================================
elif page == "🏷️ Categorical Data":
    st.header("🏷️ Categorical Data")

    cat_col = st.sidebar.selectbox("Select categorical column", categorical_cols)

    counts = df[cat_col].value_counts().reset_index()
    counts.columns = [cat_col, "Count"]

    fig = px.bar(
        counts,
        x=cat_col,
        y="Count",
        text="Count",
        title=f"Distribution of {cat_col}"
    )

    fig.update_layout(xaxis_title="", yaxis_title="Count")
    st.plotly_chart(fig, use_container_width=True)

# ======================================
# PAGE 4: MULTIDIMENSIONAL
# ======================================
elif page == "📈 Multidimensional":
    st.header("📈 Multidimensional Visualization")

    x_col = st.sidebar.selectbox("X Axis", numerical_cols, index=0)
    y_col = st.sidebar.selectbox("Y Axis", numerical_cols, index=1)
    size_col = st.sidebar.selectbox("Bubble Size", numerical_cols, index=2)
    color_col = st.sidebar.selectbox("Color (Category)", categorical_cols)

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        size=size_col,
        color=color_col,
        opacity=0.7,
        title="Multidimensional Relationship"
    )

    st.plotly_chart(fig, use_container_width=True)
