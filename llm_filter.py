from google import genai
import streamlit as st
API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=GEMINI_API_KEY)


def is_relevant(title, description):
    prompt = f"""
You are an FMCG Market Intelligence Analyst.

Your task is to determine whether the following news article is related to FMCG:

- Mergers
- Acquisitions
- Investments
- Strategic stake purchases

Analyze both the title and description.

Return ONLY one of the following:

Relevant

Not Relevant

Do not include punctuation or explanation.

Title:
{title}

Description:
{description}
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash-lite",
            contents=prompt
        )

        result = response.text.strip().lower()

        print("Gemini Response:", result)

        if "not relevant" in result:
            return False

        elif "relevant" in result:
            return True

        else:
            print(f"Unexpected Response: {result}")
            return False

    except Exception as e:
        print(f"Gemini Error: {e}")
        return False
