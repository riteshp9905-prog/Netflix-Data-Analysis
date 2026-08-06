import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

print("=" * 50)
print("🎬 NETFLIX DATA ANALYSIS")
print("=" * 50)

df = pd.read_csv("data/netflix_titles.csv")

print("\n Dataset Loaded Successfully!")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())


# ==========================================
# DATASET INFORMATION
# ==========================================

print("\n" + "=" * 50)
print("📊 DATASET INFORMATION")
print("=" * 50)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Info:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# MOVIES VS TV SHOWS
# ==========================================

print("\n" + "=" * 50)
print("🎬 MOVIES VS TV SHOWS")
print("=" * 50)

content = df["type"].value_counts()

print(content)


plt.figure(figsize=(6,5))

content.plot(
    kind="bar",
    color=["red", "blue"]
)

plt.title("Netflix Content Type")

plt.xlabel("Type")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig("images/content_type.png")

plt.show()

print(" Content Type Graph Saved!")

# ==========================================
# TOP COUNTRIES
# ==========================================

print("\n" + "=" * 50)
print("🌍 TOP 10 COUNTRIES")
print("=" * 50)

countries = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
)

top_country = countries.value_counts().head(10)

print(top_country)


plt.figure(figsize=(10,6))

top_country.plot(kind="bar")

plt.title("Top 10 Countries on Netflix")

plt.xlabel("Country")

plt.ylabel("Titles")

plt.tight_layout()

plt.savefig("images/top_countries.png")

plt.show()

print(" Top Countries Graph Saved!")

# ==========================================
# RELEASE YEAR ANALYSIS
# ==========================================

print("\n" + "=" * 50)
print("📅 RELEASE YEAR ANALYSIS")
print("=" * 50)

release = df["release_year"].value_counts().sort_index()

print(release.tail(15))

plt.figure(figsize=(12,6))

release.plot()

plt.title("Netflix Releases Over the Years")

plt.xlabel("Year")

plt.ylabel("Number of Titles")

plt.grid(True)

plt.tight_layout()

plt.savefig("images/release_year.png")

plt.show()

print(" Release Year Graph Saved!")


# ==========================================
# RATINGS ANALYSIS
# ==========================================

print("\n" + "=" * 50)
print("⭐ RATINGS")
print("=" * 50)

ratings = df["rating"].value_counts()

print(ratings)

plt.figure(figsize=(10,6))

ratings.head(10).plot(kind="bar", color="purple")

plt.title("Top Netflix Ratings")

plt.xlabel("Rating")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig("images/ratings.png")

plt.show()

print(" Ratings Graph Saved!")


# ==========================================
# TOP GENRES
# ==========================================

genres = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
)

top_genres = genres.value_counts().head(10)

print("\nTop Genres")

print(top_genres)


plt.figure(figsize=(12,6))

top_genres.plot(kind="bar", color="green")

plt.title("Top 10 Netflix Genres")

plt.xlabel("Genre")

plt.ylabel("Titles")

plt.tight_layout()

plt.savefig("images/top_genres.png")

plt.show()

print(" Genres Graph Saved!")


# ==========================================
# PROJECT SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("🎬 NETFLIX DATA ANALYSIS SUMMARY")
print("=" * 60)

print(f" Total Titles       : {len(df)}")
print(f" Movies             : {content.get('Movie',0)}")
print(f" TV Shows           : {content.get('TV Show',0)}")
print(f" Total Countries    : {countries.nunique()}")
print(f" Total Genres       : {genres.nunique()}")

print("\n🏆 Top Country")
print(top_country.head(1))

print("\n🎭 Top Genre")
print(top_genres.head(1))

print("\n⭐ Most Common Rating")
print(ratings.head(1))

print("\n🎉 Analysis Completed Successfully!")

# ==========================================
# SAVE REPORT
# ==========================================

with open("Netflix_Report.txt", "w", encoding="utf-8") as file:

    file.write("NETFLIX DATA ANALYSIS REPORT\n")
    file.write("=" * 45 + "\n\n")

    file.write(f"Total Titles : {len(df)}\n")
    file.write(f"Movies : {content.get('Movie',0)}\n")
    file.write(f"TV Shows : {content.get('TV Show',0)}\n")
    file.write(f"Countries : {countries.nunique()}\n")
    file.write(f"Genres : {genres.nunique()}\n\n")

    file.write("Top 10 Countries\n")
    file.write(str(top_country))
    file.write("\n\n")

    file.write("Top 10 Genres\n")
    file.write(str(top_genres))

print(" Report Saved Successfully!")


