#!/usr/bin/env python3
"""
T37 Wealth - Automated Article Publisher
Publishes new articles directly into data/articles.json and prepares git deployment.
"""

import sys
import os
import json
import re
import argparse
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
ARTICLES_FILE = os.path.join(PROJECT_ROOT, "data", "articles.json")

def generate_slug(title):
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[\s_-]+', '-', slug)
    return slug.strip('-')

def calculate_read_time(content):
    text = re.sub(r'<[^>]+>', ' ', content)
    words = len(re.findall(r'\w+', text))
    mins = max(1, (words + 199) // 200)
    return f"{mins} min read"

def auto_excerpt(content):
    text = re.sub(r'<[^>]+>', ' ', content)
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 15]
    if len(sentences) >= 2:
        return f"{sentences[0]}. {sentences[1]}."
    elif sentences:
        return f"{sentences[0]}."
    return "Read the complete analysis inside."

def publish_article(article_dict, push_to_git=False):
    if not os.path.exists(ARTICLES_FILE):
        articles = []
    else:
        with open(ARTICLES_FILE, "r", encoding="utf-8") as f:
            articles = json.load(f)

    title = article_dict.get("title", "").strip()
    if not title:
        raise ValueError("Article title is required.")

    slug = article_dict.get("slug") or generate_slug(title)
    category = article_dict.get("category", "Markets")
    content = article_dict.get("content", "").strip()

    article = {
        "id": slug,
        "title": title,
        "slug": slug,
        "category": category,
        "subCategory": article_dict.get("subCategory", category),
        "author": "T37 Editor Desk",
        "datetime": article_dict.get("datetime") or datetime.utcnow().isoformat() + "Z",
        "readTime": article_dict.get("readTime") or calculate_read_time(content),
        "thumbnail": article_dict.get("thumbnail", "assets/thumbnails/markets-nse-ipo.svg"),
        "excerpt": article_dict.get("excerpt") or auto_excerpt(content),
        "keyTakeaways": article_dict.get("keyTakeaways", []),
        "content": content
    }

    # Remove duplicate with same slug if exists
    articles = [a for a in articles if a.get("slug") != slug]
    # Prepend new article so it appears at top of Latest feed
    articles.insert(0, article)

    with open(ARTICLES_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

    print(f" Successfully published article: '{title}' ({slug}) to {ARTICLES_FILE}")

    if push_to_git:
        print("Staging and pushing changes to git origin main...")
        os.system(f'git -C "{PROJECT_ROOT}" add data/articles.json')
        os.system(f'git -C "{PROJECT_ROOT}" commit -m "Publish article: {title}"')
        os.system(f'git -C "{PROJECT_ROOT}" push origin main')
        print(" Pushed to GitHub! Live site wealth.t37.in will update automatically.")

    return article

def main():
    parser = argparse.ArgumentParser(description="Publish an article to T37 Wealth")
    parser.add_argument("--json-file", help="Path to JSON file containing article data")
    parser.add_argument("--json", help="Direct JSON string containing article data")
    parser.add_argument("--title", help="Article title")
    parser.add_argument("--category", choices=["Markets", "Crypto", "Personal Finance"], default="Markets")
    parser.add_argument("--subcategory", help="Sub-category or tag")
    parser.add_argument("--author", default="T37 Editor Desk")
    parser.add_argument("--thumbnail", default="assets/thumbnails/markets-nse-ipo.svg")
    parser.add_argument("--content-file", help="Path to raw text/html/markdown content file")
    parser.add_argument("--push", action="store_true", help="Push to git origin after adding")

    args = parser.parse_args()

    if args.json_file:
        with open(args.json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        publish_article(data, push_to_git=args.push)
    elif args.json:
        data = json.loads(args.json)
        publish_article(data, push_to_git=args.push)
    elif args.title:
        content = ""
        if args.content_file and os.path.exists(args.content_file):
            with open(args.content_file, "r", encoding="utf-8") as f:
                content = f.read()
        data = {
            "title": args.title,
            "category": args.category,
            "subCategory": args.subcategory or args.category,
            "author": "T37 Editor Desk",
            "thumbnail": args.thumbnail,
            "content": content
        }
        publish_article(data, push_to_git=args.push)
    else:
        print("Error: Specify --json-file, --json, or --title to publish an article.")
        sys.exit(1)

if __name__ == "__main__":
    main()
