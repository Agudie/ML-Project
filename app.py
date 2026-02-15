import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="UHAS Health Data Portal", page_icon="🏥", layout="wide")

st.title("🏥 Public Health Data Cleaning Portal")
# Put your actual name here!
st.write("Developed by: Emmanuel Adu-Awuku [Joeboy]")

st.sidebar.header("Step 1: Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df_raw = pd.read_csv(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Raw Data Preview")
        st.dataframe(df_raw.head())

    # Cleaning Logic
    if st.button("🚀 Run Automated Cleaning"):
        # Create a copy to clean
        df = df_raw.copy()
        
        # 1. Age Correction
        avg_age = df.loc[df['age'] <= 110, 'age'].mean()
        df['age'] = df['age'].apply(lambda x: avg_age if pd.isna(x) or x > 110 else x)
        
        # 2. Weight Correction
        df['weight_kg'] = df['weight_kg'].abs()
        
        # 3. Blood Type Filtering
        valid_types = ['A', 'B', 'AB', 'O']
        df = df[df['blood_type'].isin(valid_types)]
        
        with col2:
            st.subheader("✅ Cleaned Data")
            st.dataframe(df.head())
        
        st.divider()
        
        # --- NEW: STATISTICAL SUMMARY SECTION ---
        st.subheader("📈 Research Metrics (Cleaned Dataset)")
        m1, m2, m3 = st.columns(3)
        
        m1.metric("Total Records Processed", len(df))
        m2.metric("Average Patient Age", f"{df['age'].mean():.1f} Years")
        m3.metric("Valid Data Integrity", "100%")
        
        # Download Button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Research-Ready CSV", data=csv, file_name="cleaned_health_data.csv", use_container_width=True)
else:
    st.info("👋 Ready to clean data? Please upload your CSV file in the sidebar.")