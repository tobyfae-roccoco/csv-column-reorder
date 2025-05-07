import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="CSV Reorder by Template", layout="centered")
st.title("🔄 Reorder CSV Columns by Template")

# Upload the template file
st.header("1. Upload Template CSV")
template_file = st.file_uploader("📤 Upload a CSV file that defines the correct column order", type="csv", key="template")

# Upload the source file
st.header("2. Upload CSV to Reorder")
source_file = st.file_uploader("📥 Upload the CSV file you want to convert", type="csv", key="source")

if template_file and source_file:
    try:
        template_df = pd.read_csv(template_file)
        source_df = pd.read_csv(source_file)

        template_columns = list(template_df.columns)

        # Check if all required columns are in the source
        missing = [col for col in template_columns if col not in source_df.columns]

        if missing:
            st.error(f"❌ The following columns from the template are missing in the uploaded CSV: {', '.join(missing)}")
        else:
            # Reorder source_df to match template
            reordered_df = source_df[template_columns]

            buffer = io.StringIO()
            reordered_df.to_csv(buffer, index=False)
            buffer.seek(0)

            st.success("✅ Source CSV reordered to match the template!")
            st.download_button(
                label="📥 Download Reordered CSV",
                data=buffer,
                file_name="reordered.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"⚠️ An error occurred while processing the files: {e}")
