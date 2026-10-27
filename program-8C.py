
import pandas as pd
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer as NLTKVADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as StandaloneVADER

nltk.download("vader_lexicon", quiet=True)

df = pd.read_csv("reviews.csv")
df["review"] = df["review"].fillna("").astype(str)

nltk_analyzer = NLTKVADER()
vader_analyzer = StandaloneVADER()

def classify(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    return "Neutral"

nltk_scores = df["review"].apply(nltk_analyzer.polarity_scores)

df["nltk_positive"] = nltk_scores.apply(lambda x: x["pos"])
df["nltk_negative"] = nltk_scores.apply(lambda x: x["neg"])
df["nltk_neutral"] = nltk_scores.apply(lambda x: x["neu"])
df["nltk_compound"] = nltk_scores.apply(lambda x: x["compound"])

vader_scores = df["review"].apply(vader_analyzer.polarity_scores)

df["vader_positive"] = vader_scores.apply(lambda x: x["pos"])
df["vader_negative"] = vader_scores.apply(lambda x: x["neg"])
df["vader_neutral"] = vader_scores.apply(lambda x: x["neu"])
df["vader_compound"] = vader_scores.apply(lambda x: x["compound"])

df["nltk_sentiment"] = df["nltk_compound"].apply(classify)
df["vader_sentiment"] = df["vader_compound"].apply(classify)

print(df[[
    "review",
    "nltk_compound",
    "nltk_sentiment",
    "vader_compound",
    "vader_sentiment"
]].head(10).to_string(index=False))

print("\nNLTK sentiment distribution:")
print(df["nltk_sentiment"].value_counts())

print("\nStandalone VADER sentiment distribution:")
print(df["vader_sentiment"].value_counts())

df.to_csv("sentiment_analysis_results.csv", index=False)
print("\nResults saved to sentiment_analysis_results.csv")
