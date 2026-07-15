def run_pipeline():

    import requests
    import pandas as pd

    import streamlit as st
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    from llm_filter import is_relevant
    from newsletter import generate_newsletter
    from preprocess import (
        remove_exact_duplicates,
        remove_near_duplicates,
        add_credibility_score
    )

    # News API Endpoint
    url = "https://newsapi.org/v2/everything"

    # Query Parameters
    params = {
        "q": "FMCG",
        "pageSize": 100,
        "language": "en"
    }

    # Authentication
    headers = {
        "X-API-KEY": API_KEY
    }

    # Fetch News
    response = requests.get(
        url=url,
        params=params,
        headers=headers
    )

    print("Status Code:", response.status_code)

    # JSON -> Python Dictionary
    data = response.json()

    # Create DataFrame
    news = []

    for article in data["articles"]:
        news.append({
            "source": article["source"]["name"],
            "title": article["title"],
            "description": article["description"],
            "publishedAt": article["publishedAt"],
            "url": article["url"]
        })

    df = pd.DataFrame(news)
    df.to_csv("data/news.csv", index=False)

    # Remove Duplicates
    print("Original Articles:", len(df))

    clean_df = remove_exact_duplicates(df)
    print("After Exact Duplicate Removal:", len(clean_df))

    clean_df = remove_near_duplicates(clean_df)
    print("After Near Duplicate Removal:", len(clean_df))

    clean_df.to_csv("data/clean_news.csv", index=False)

    # LLM Filtering
    relevant_news = []

    for _, row in clean_df.iterrows():

        if is_relevant(
            row["title"],
            row["description"]
        ):
            relevant_news.append(row)

    relevant_df = pd.DataFrame(relevant_news)

    print("Relevant Articles:", len(relevant_df))

    # Credibility Score
    ##relevant_df = add_credibility_score(relevant_df)

    # Generate Newsletter
    newsletter = generate_newsletter(relevant_df)

    print(newsletter)

    # Save Newsletter
    with open("newsletter.md", "w", encoding="utf-8") as f:
        f.write(newsletter)

    print("Newsletter saved successfully!")

    return newsletter
