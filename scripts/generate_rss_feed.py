import json
import os
from datetime import datetime, timezone
import email.utils

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_PATH = os.path.join(ROOT_DIR, "data", "articles.json")
FEED_PATH = os.path.join(ROOT_DIR, "feed.xml")
RSS_PATH = os.path.join(ROOT_DIR, "rss.xml")

with open(ARTICLES_PATH, "r", encoding="utf-8") as f:
    articles = json.load(f)

def to_rfc822(dt_str):
    try:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        return email.utils.format_datetime(dt)
    except Exception:
        return email.utils.format_datetime(datetime.now(timezone.utc))

now_rfc822 = email.utils.format_datetime(datetime.now(timezone.utc))

rss_items = []
for a in articles:
    title = a.get("title", "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    slug = a.get("slug", "")
    url = f"https://wealth.t37.in/#article/{slug}"
    excerpt = a.get("excerpt", "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    author = a.get("author", "T37 Editor Desk")
    category = a.get("category", "Markets")
    pub_date = to_rfc822(a.get("datetime", ""))
    thumb = f"https://wealth.t37.in/{a.get('thumbnail', '')}"
    content = a.get("content", "")

    # Clean description / content
    item_xml = f"""    <item>
      <title>{title}</title>
      <link>{url}</link>
      <guid isPermaLink="true">{url}</guid>
      <pubDate>{pub_date}</pubDate>
      <dc:creator><![CDATA[{author}]]></dc:creator>
      <category><![CDATA[{category}]]></category>
      <description><![CDATA[{excerpt}]]></description>
      <content:encoded><![CDATA[{content}]]></content:encoded>
      <enclosure url="{thumb}" type="image/svg+xml" length="1024" />
    </item>"""
    rss_items.append(item_xml)

rss_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" 
     xmlns:dc="http://purl.org/dc/elements/1.1/" 
     xmlns:content="http://purl.org/rss/1.0/modules/content/" 
     xmlns:atom="http://www.w3.org/2005/Atom"
     xmlns:media="http://search.yahoo.com/mrss/">
  <channel>
    <title>T37 Wealth | Financial Journalism &amp; Market Intelligence</title>
    <link>https://wealth.t37.in</link>
    <atom:link href="https://wealth.t37.in/feed.xml" rel="self" type="application/rss+xml" />
    <description>3-minute actionable, verified financial journalism covering Indian &amp; global markets, macroeconomics, and personal finance strategies.</description>
    <language>en-us</language>
    <copyright>Copyright 2026 T37 Consulting</copyright>
    <lastBuildDate>{now_rfc822}</lastBuildDate>
    <docs>https://cyber.harvard.edu/rss/rss.html</docs>
    <generator>T37 Wealth RSS Generator</generator>
    <image>
      <url>https://wealth.t37.in/assets/logo.png</url>
      <title>T37 Wealth</title>
      <link>https://wealth.t37.in</link>
    </image>
{chr(10).join(rss_items)}
  </channel>
</rss>"""

with open(FEED_PATH, "w", encoding="utf-8") as f:
    f.write(rss_xml)

with open(RSS_PATH, "w", encoding="utf-8") as f:
    f.write(rss_xml)

print(f"Generated {FEED_PATH} and {RSS_PATH} with {len(articles)} articles!")
