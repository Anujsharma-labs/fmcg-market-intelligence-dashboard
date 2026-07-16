from google import genai
import streamlit as st

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_newsletter(df):

    # If no relevant articles found
    if df.empty:
        return "# No relevant FMCG news found today."

    # Send only top 5 articles to Gemini
    df = df.head(5)

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

    # Combine all articles
    newsletter_text = "\n\n".join(articles)

    # Prompt
    prompt = f"""
You are an FMCG Market Intelligence Analyst.

Using the following news articles, generate a concise professional newsletter.

Include:

# FMCG Daily Intelligence Newsletter

## Top Headlines
- Bullet points

## Executive Summary
(3-4 sentences)

## Key Takeaways
- Bullet points

Keep the response concise, professional, and suitable for business executives.

Articles:

{newsletter_text}
"""

    try:

        response = client.models.generate_content(
            model="models/gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        if "429" in str(e):
            return """
# Gemini API Quota Exceeded

The free-tier Gemini API quota has been exhausted.

Please try again after the quota resets or use another API key.
"""

        elif "503" in str(e):
            return """
# Gemini Service Busy

Gemini is currently experiencing high demand.

Please try again after a few minutes.
"""

        else:
            import traceback
            return f"Newsletter generation failed.\n\n{traceback.format_exc()}"