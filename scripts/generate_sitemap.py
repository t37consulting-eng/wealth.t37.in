import json
import os
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_PATH = os.path.join(ROOT_DIR, "data", "articles.json")
SITEMAP_PATH = os.path.join(ROOT_DIR, "sitemap.xml")

with open(ARTICLES_PATH, "r", encoding="utf-8") as f:
    articles = json.load(f)

today = datetime.utcnow().strftime("%Y-%m-%d")

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

# Categories
categories = [
    ("latest", "1.0"),
    ("markets", "0.9"),
    ("crypto", "0.9"),
    ("personal-finance", "0.9"),
    ("algo-trading", "0.9")
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
    slug = a.get("slug", "")
    thumb = a.get("thumbnail", "")
    title = a.get("title", "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    
    xml_lines.extend([
        '  <url>',
        f'    <loc>https://wealth.t37.in/#article/{slug}</loc>',
        f'    <lastmod>{date_str}</lastmod>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.8</priority>',
        '    <image:image>',
        f'      <image:loc>https://wealth.t37.in/{thumb}</image:loc>',
        f'      <image:title>{title}</image:title>',
        '    </image:image>',
        '  </url>'
    ])

xml_lines.append('</urlset>')

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(xml_lines))

print(f"Generated {SITEMAP_PATH} with {len(articles) + len(categories) + 1} URLs!")
