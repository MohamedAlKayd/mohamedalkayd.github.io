import os
from datetime import datetime

# Define the path to the _news directory
news_dir = "_news"

# Function to create a news item file
def create_news_item():
    # Ask for the news item title
    title = input("Enter the title of the news item: ").strip()

    # Convert the title to a slug for the filename (lowercase, hyphens instead of spaces)
    slug = title.lower().replace(" ", "_")

    # Ask for the date of the news item (default is today's date)
    date_str = input("Enter the date of the news item (YYYY-MM-DD) [Leave empty for today's date]: ").strip()
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')

    # Ask for the content of the news item
    content = input("Enter the content of the news item: ").strip()

    # Create the filename
    filename = f"{slug}.md"
    filepath = os.path.join(news_dir, filename)

    # Define the content of the Markdown file
    markdown_content = f"""---
layout: post
title: "{title}"
date: {date_str}
---

{content}
"""

    # Write the content to the file
    with open(filepath, 'w') as file:
        file.write(markdown_content)
    
    print(f"News item '{title}' created at: {filepath}")

# Ensure the _news directory exists
if not os.path.exists(news_dir):
    os.makedirs(news_dir)

# Run the script to create a news item
create_news_item()
