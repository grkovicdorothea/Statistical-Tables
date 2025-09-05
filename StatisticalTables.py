import streamlit as st
import numpy as np
from scipy import stats

st.title("Statistical Tables Aoo")

st.sidebar.header("Select Functionality")
option = st.sidebar.selectbox(
    "Choose calculation",
    ["Normal Distribution", "t-distribution", "Chi-squared distribution", "F-distribution", "Durbin-Watson statistic"]
)

# ---------------- Normal Distribution ----------------
if option == "Normal Distribution":
    st.header("Normal Distribution")
    mean = st.number_input("Mean (μ)", value=0.0)
    std = st.number_input("Standard deviation (σ)", value=1.0, min_value=0.0001)
    alpha = st.number_input("Significance level (α)", value=0.05, step=0.01)
    
    tail = st.radio("Tail type", ["Two-tailed", "One-tailed"])
    
    if st.button("Calculate Normal Critical Value"):
        if tail == "Two-tailed":
            crit = stats.norm.ppf(1 - alpha/2, loc=mean, scale=std)
        else:
            crit = stats.norm.ppf(1 - alpha, loc=mean, scale=std)
        st.success(f"Critical value: {crit:.4f}")

# ---------------- t-distribution ----------------
elif option == "t-distribution":
    st.header("t-Distribution")
    df = st.number_input("Degrees of freedom (df)", min_value=1, step=1)
    alpha = st.number_input("Significance level (α)", value=0.05, step=0.01)
    tail = st.radio("Tail type", ["Two-tailed", "One-tailed"])
    
    if st.button("Calculate t Critical Value"):
        if tail == "Two-tailed":
            crit = stats.t.ppf(1 - alpha/2, df)
        else:
            crit = stats.t.ppf(1 - alpha, df)
        st.success(f"Critical value (t): {crit:.4f}")

# ---------------- Chi-squared distribution ----------------
elif option == "Chi-squared distribution":
    st.header("Chi-squared Distribution")
    df = st.number_input("Degrees of freedom (df)", min_value=1, step=1)
    alpha = st.number_input("Significance level (α)", value=0.05, step=0.01)
    
    if st.button("Calculate Chi² Critical Value"):
        crit = stats.chi2.ppf(1 - alpha, df)
        st.success(f"Critical value (Chi²): {crit:.4f}")

# ---------------- F-distribution ----------------
elif option == "F-distribution":
    st.header("F-Distribution")
    df1 = st.number_input("Numerator df (df1)", min_value=1, step=1)
    df2 = st.number_input("Denominator df (df2)", min_value=1, step=1)
    alpha = st.number_input("Significance level (α)", value=0.05, step=0.01)
    
    if st.button("Calculate F Critical Value"):
        crit = stats.f.ppf(1 - alpha, df1, df2)
        st.success(f"Critical value (F): {crit:.4f}")

# ---------------- Durbin-Watson ----------------
elif option == "Durbin-Watson statistic":
    st.header("Durbin-Watson Statistic")
    st.write("Input residuals separated by commas, e.g., 1, -0.5, 0.3")
    res_input = st.text_area("Residuals")
    
    if st.button("Calculate Durbin-Watson"):
        try:
            residuals = np.array([float(x.strip()) for x in res_input.split(",")])
            diff = np.diff(residuals)
            dw = np.sum(diff**2) / np.sum(residuals**2)
            st.success(f"Durbin-Watson statistic: {dw:.4f}")
        except:
            st.error("Invalid input. Make sure residuals are numeric and comma-separated.")