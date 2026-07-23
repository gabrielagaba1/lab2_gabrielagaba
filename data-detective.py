import csv
import sys
import os

def load_raw_data(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    dataset = []
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dataset.append(row)

    return dataset

def clean_data(tweets):
    cleaned = []
    dropped = 0
    fixed = 0

    for item in tweets:
        text = item.get("Text")
        if not text or str(text).strip() == "":
            dropped += 1
            continue

        entry = dict(item)

        likes = str(entry.get("Likes", "")).strip()
        if not likes:
            entry["Likes"] = 0
            fixed += 1
        else:
            entry["Likes"] = int(likes)

        retweets = str(entry.get("Retweets", "")).strip()
        if not retweets:
            entry["Retweets"] = 0
            fixed += 1
        else:
            entry["Retweets"] = int(retweets)

        cleaned.append(entry)

    print(f"Cleaned {len(cleaned)} tweets (Dropped: {dropped}, Fixed: {fixed})")
    return cleaned

def find_viral_tweet(tweets):
    if not tweets:
        return None

    top = tweets[0]
    for item in tweets:
        if item["Likes"] > top["Likes"]:
            top = item

    print(f"Most Viral Tweet by @{top['Username']}: {top['Likes']} likes")
    print(f"Text: {top['Text']}\n")
    return top

def custom_sort_by_likes(tweets):
    sorted_posts = list(tweets)
    n = len(sorted_posts)
    likes_cache = [p["Likes"] for p in sorted_posts]

    for i in range(n - 1):
        highest_pos = i
        highest_val = likes_cache[i]

        for j in range(i + 1, n):
            if likes_cache[j] > highest_val:
                highest_val = likes_cache[j]
                highest_pos = j

        if highest_pos != i:
            likes_cache[i], likes_cache[highest_pos] = likes_cache[highest_pos], likes_cache[i]
            sorted_posts[i], sorted_posts[highest_pos] = sorted_posts[highest_pos], sorted_posts[i]

    return sorted_posts

def search_tweets(tweets, keyword):
    matches = []
    term = keyword.lower().strip()

    for item in tweets:
        if term in item.get("Text", "").lower():
            matches.append(item)

    print(f"Found {len(matches)} tweets matching '{keyword}':")
    for tweet in matches[:3]:
        print(f"@{tweet['Username']}: {tweet['Text']}")

    return matches

if __name__ == "__main__":
    raw_data = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(raw_data)} tweets.")

    clean_feed = clean_data(raw_data)
    find_viral_tweet(clean_feed)

    print("\nTop 10 Most Liked Tweets:")
    sorted_feed = custom_sort_by_likes(clean_feed)
    for pos, tweet in enumerate(sorted_feed[:10], 1):
        print(f"{pos}. @{tweet['Username']} - {tweet['Likes']} likes")

    print("\nSearch:")
    search_word = input("Enter keyword: ")
    if not search_word:
        search_word = "python"
    search_tweets(clean_feed, search_word)
