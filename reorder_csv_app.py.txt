import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="CSV Column Reorder", layout="centered")
st.title("🔀 CSV Column Reorder Tool")

uploaded_file = st.file_uploader("📤 Upload a CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        columns = list(df.columns)

        st.write("### ✏️ Reorder the Columns")
        new_order = st.multiselect(
            label="Drag to reorder the columns",
            options=columns,
            default=columns,
            key="reorder",
        )

        if set(new_order) != set(columns):
            st.warning("⚠️ You must include all original columns (no duplicates or omissions).")
        else:
            reordered_df = df[new_order]

            buffer = io.StringIO()
            reordered_df.to_csv(buffer, index=False)
            buffer.seek(0)

            st.success("✅ Columns reordered!")
            st.download_button(
                label="📥 Download Reordered CSV",
                data=buffer,
                file_name="reordered.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
