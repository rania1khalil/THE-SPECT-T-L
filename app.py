import streamlit as st
import pandas as pd

st.set_page_config(page_title="מערכת ניתוח משובים", page_icon="📊", layout="centered")

st.title("📊 מערכת ניתוח משובים – פסגת ירכא")
st.markdown("המערכת מאפשרת העלאת קבצי משוב וניתוח אוטומטי לפי תחומים.")

uploaded_file = st.file_uploader("העלאת קובץ משוב (Excel)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("✅ הקובץ נטען בהצלחה!")
    st.subheader("תצוגה מקדימה:")
    st.dataframe(df)
    
    st.subheader("ממוצעים לדוגמה לפי שאלות:")
    numeric_cols = df.select_dtypes(include="number").columns
    if not numeric_cols.empty:
        means = df[numeric_cols].mean().round(2)
        st.write(means)
    else:
        st.info("לא נמצאו עמודות מספריות לחישוב ממוצע.")
