
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
df = pd.read_csv("reviews.csv")
df["review"] = df["review"].fillna("").astype(str)
analyzer = SentimentIntensityAnalyzer()
def classify_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    return "Neutral"
df["sentiment"] = df["review"].apply(classify_sentiment)
def generate_wordcloud(text, title, filename):
    if not text.strip():
        print("No text available for:", title)
        return
    cloud = WordCloud(
        width=1200,
        height=600,
        background_color="white",
        max_words=150,
        collocations=False
    ).generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.show()
all_text = " ".join(df["review"])
generate_wordcloud(all_text, "WordCloud - All Reviews", "wordcloud_all.png")
positive_text = " ".join(df.loc[df["sentiment"] == "Positive", "review"])
generate_wordcloud(positive_text, "WordCloud - Positive Reviews", "wordcloud_positive.png")
negative_text = " ".join(df.loc[df["sentiment"] == "Negative", "review"])
generate_wordcloud(negative_text, "WordCloud - Negative Reviews", "wordcloud_negative.png")
df.to_csv("product_reviews_analyzed.csv", index=False)
print(df["sentiment"].value_counts())
print("WordCloud images saved successfully.")
