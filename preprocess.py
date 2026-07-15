import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def remove_exact_duplicates(df):

    cleaned_df = df.drop_duplicates(subset = ['title'])

    return cleaned_df
    

# removing duplicate words or news
def remove_near_duplicates(df):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(df['title'])

    similarity_matrix = cosine_similarity(vectors)

    threshold = 0.80

    duplicates = set()

    for i in range (len(df)):
        for j in range (i+1, len(df)):
            if similarity_matrix[i][j] > threshold:
                duplicates.add(j)

    clean_df = df.drop(index = duplicates).reset_index(drop=True)
    return clean_df



def add_credibility_score(df):

    credibility = {
    "Reuters": 10,
    "Bloomberg": 10,
    "CNBC": 9,
    "Financial Times": 9,
    "Economic Times": 8,
    "Mint": 8
    }
    df['credibility_score'] = df['source'].apply(
        lambda x: credibility.get(x , 5)
    )
    return df