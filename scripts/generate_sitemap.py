import json
import os
from datetime import datetime, timezone

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_PATH = os.path.join(ROOT_DIR, "data", "articles.json")
SITEMAP_PATH = os.path.join(ROOT_DIR, "sitemap.xml")
NEWS_SITEMAP_PATH = os.path.join(ROOT_DIR, "news-sitemap.xml")

with open(ARTICLES_PATH, "r", encoding="utf-8") as f:
    articles = json.load(f)

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# 1. Main XML Sitemap
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"',
    '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    '  <!-- Main Hub -->',
    '  <url>',
    '    <loc>https://wealth.t37.in/</loc>',
    f'    <lastmod>{today}</lastmod>',
    '    <changefreq>daily</changefreq>',
    '    <priority>1.0</priority>',
    '  </url>'
]

# Categories (Latest, Markets, Personal Finance)
categories = [
    ("latest", "1.0"),
    ("markets", "0.9"),
    ("personal-finance", "0.9")
]

for cat, prio in categories:
    xml_lines.extend([
        '  <url>',
        f'    <loc>https://wealth.t37.in/#{cat}</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>daily</changefreq>',
        f'    <priority>{prio}</priority>',
        '  </url>'
    ])

# Articles
for a in articles:
    date_str = a.get("datetime", "")[:10] or today
    full_iso = a.get("datetime", f"{today}T00:00:00Z")
    slug = a.get("slug", "")
    thumb = a.get("thumbnail", "")
    title = a.get("title", "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    
    xml_lines.extend([
        '  <url>',
        f'    <loc>https://wealth.t37.in/#article/{slug}</loc>',
        f'    <lastmod>{date_str}</lastmod>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.8</priority>',
        '    <news:news>',
        '      <news:publication>',
        '        <news:name>T37 Wealth</news:name>',
        '        <news:language>en</news:language>',
        '      </news:publication>',
        f'      <news:publication_date>{full_iso}</news:publication_date>',
        f'      <news:title>{title}</news:title>',
        '    </news:news>',
        '    <image:image>',
        f'      <image:loc>https://wealth.t37.in/{thumb}</image:loc>',
        f'      <image:title>{title}</image:title>',
        '    </image:image>',
        '  </url>'
    ])

xml_lines.append('</urlset>')

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(xml_lines))

# 2. Dedicated Google News Sitemap
news_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">',
]

for a in articles:
    full_iso = a.get("datetime", f"{today}T00:00:00Z")
    slug = a.get("slug", "")
    title = a.get("title", "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    news_lines.extend([
        '  <url>',
        f'    <loc>https://wealth.t37.in/#article/{slug}</loc>',
        '    <news:news>',
        '      <news:publication>',
        '        <news:name>T37 Wealth</news:name>',
        '        <news:language>en</news:language>',
        '      </news:publication>',
        f'      <news:publication_date>{full_iso}</news:publication_date>',
        f'      <news:title>{title}</news:title>',
        '    </news:news>',
        '  </url>'
    ])

news_lines.append('</urlset>')

with open(NEWS_SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(news_lines))

print(f"Generated {SITEMAP_PATH} and {NEWS_SITEMAP_PATH} with Google News XML tags!")
