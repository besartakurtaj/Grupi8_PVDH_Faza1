import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titulli
st.title("Vizualizimi sipas tipeve të të dhënave")

# Ngarkimi i dataset-it
df = pd.read_csv("../data/cleaned_dataset.csv")

st.subheader("Pamje e të dhënave")
st.dataframe(df.head())

# Identifikimi i tipeve të kolonave
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = df.select_dtypes(include=["object", "category"]).columns
datetime_cols = df.select_dtypes(include=["datetime64"]).columns

# =========================
# NUMERICAL DATA
# =========================
st.header("Të dhëna numerike")

if len(numerical_cols) > 0:
    num_col = st.selectbox("Zgjidh një kolonë numerike", numerical_cols)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    sns.histplot(df[num_col], kde=True, ax=ax[0])
    ax[0].set_title("Histogram")

    sns.boxplot(x=df[num_col], ax=ax[1])
    ax[1].set_title("Boxplot")

    st.pyplot(fig)
else:
    st.info("Nuk ka kolona numerike.")

# =========================
# CATEGORICAL DATA
# =========================
st.header("Të dhëna kategorike")

if len(categorical_cols) > 0:
    cat_col = st.selectbox("Zgjidh një kolonë kategorike", categorical_cols)

    value_counts = df[cat_col].value_counts()

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax)
    ax.set_title("Frekuenca sipas kategorive")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    st.pyplot(fig)
else:
    st.info("Nuk ka kolona kategorike.")

