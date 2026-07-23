# Lab 2 - Data Detective

This project is about working with a messy Twitter dataset (`twitter_dataset.csv`). I wrote a Python script to clean and analyze the data, and a Bash script to find the most active users.

## Files
- `data-detective.py` – handles all 4 data quests (cleaning, searching, counting, etc.)
- `feed-analyzer.sh` – finds top 5 most active users using bash commands
- `twitter_dataset.csv` – the raw dataset

## How to run

```bash
python3 data-detective.py
```

```bash
chmod +x feed-analyzer.sh
./feed-analyzer.sh
```

## How my sorting algorithm works

I used Selection Sort for Quest 3. It scans through the whole list to find the tweet with the highest likes and swaps it to the front, then repeats for the rest of the list. This way the tweets end up ordered from most liked to least liked without using Python's built-in sort.