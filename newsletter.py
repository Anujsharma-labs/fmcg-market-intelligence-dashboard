from google import genai
import streamlit as st
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_newsletter(df):

    articles = []

    # Convert each row into readable text
    for _, row in df.iterrows():

        article = f"""
Title:
{row["title"]}

Source:
{row["source"]}

Description:
{row["description"]}
"""

        articles.append(article)

    # Combine all articles into one text block
    newsletter_text = "\n\n".join(articles)

    # Prompt for Gemini
    prompt = f"""
You are an FMCG Market Intelligence Analyst.

Using the following news articles, generate a professional daily newsletter.

Include:

- Newsletter Title
- Top Headlines
- Executive Summary
- Key Takeaways

Return the output in Markdown format.

Articles:

{newsletter_text}
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
         import traceback
         return f"Newsletter generation failed.\n\n{traceback.format_exc()}"
