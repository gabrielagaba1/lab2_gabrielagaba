#!/bin/bash

FILE="twitter_dataset.csv"

if [ ! -f "$FILE" ]; then
    echo "Error: Dataset '$FILE' not found."
    exit 1
fi

echo "Top 5 Most Active Users:"
tail -n +2 "$FILE" | cut -d',' -f2 | sort | uniq -c | sort -nr | head -n 5