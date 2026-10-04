# T37 Wealth (wealth.t37.in)

> **Finshots-inspired financial journalism platform** covering Markets and Personal Finance with 3-minute, actionable, easy-to-understand reads.

Live URL: [https://wealth.t37.in](https://wealth.t37.in)

---

## 🌟 Features

- **Finshots Visual Design**: Clean, crisp typography, high-impact editorial illustrations, and responsive 3-column card grid.
- **3 Navigation Sections**:
  1. **Latest**: Dynamically aggregates recent articles across all categories.
  2. **Markets**: Indian and global equities, IPOs, macroeconomics, FII/DII fund flows.
  3. **Personal Finance**: Mutual funds (Direct vs Regular), insurance fine print, tax optimization, budgeting, and risk management.
- **Google News & E-E-A-T Architecture**:
  - Valid RSS 2.0 / Media RSS feeds (`feed.xml` and `rss.xml`) with full `<content:encoded>` excerpts, RFC 822 timestamps, and categories.
  - Dedicated Google News XML sitemap (`news-sitemap.xml`) with `<news:news>` and `<news:publication>` tags.
  - Comprehensive `NewsMediaOrganization` & `NewsArticle` Schema.org JSON-LD.
  - Institutional E-E-A-T Transparency: Editorial policy, primary source fact-checking (NSE, BSE, RBI, SEBI), transparent corrections policy, and statutory YMYL non-advisory disclosures.
  - Explicit crawl access for `Googlebot` and `Googlebot-News` in `robots.txt`.
- **Deep-Linkable Reader**: Seamless article modal with "In a nutshell" key takeaways, Google News follow button, verified byline, and related recommendations.
- **Instant Search**: Client-side full-text search across titles, summaries, content, authors, and categories.
- **Hidden Content Studio (`editor.html`)**: A private authoring portal not exposed in the public navigation.

---

## 📰 Google Publisher Center Submission Guide

To get fast-tracked into Google News as an authorized publication:
1. Go to [Google Publisher Center](https://publishercenter.google.com/) and click **"Add Publication"**.
2. **Publication Name**: `T37 Wealth`
3. **Primary Website Property**: `https://wealth.t37.in` (Verify via Google Search Console).
4. **Location**: India • **Primary Language**: English
5. **Content Sections**:
   - Section 1 (Feed): Name: `Markets` • Feed URL: `https://wealth.t37.in/feed.xml`
   - Section 2 (Feed): Name: `Personal Finance` • Feed URL: `https://wealth.t37.in/rss.xml`
6. **Square Logo**: Upload `assets/logo.png` (512x512px).
7. Submit for review! Feeds will automatically synchronize new articles.

---

## ✍️ How to Publish New Articles

### Method 1: Ask Antigravity Directly (Easiest)
Whenever you have a new article in Microsoft Word, Google Docs, or plain text:
1. Simply paste the text or attach your document in Antigravity chat:
   > *"Antigravity, please publish this new article under Markets: [Paste Title & Content]"*
2. Antigravity will automatically:
   - Clean the text and generate semantic HTML.
   - Assign an appropriate SVG thumbnail from `assets/thumbnails/`.
   - Calculate reading time and generate a clean slug.
   - Prepend the article to `data/articles.json`.
   - Automatically regenerate `sitemap.xml`, `news-sitemap.xml`, `feed.xml`, and `rss.xml`.
   - Commit and push to GitHub so it appears on `wealth.t37.in` immediately.

### Method 2: Hidden Content Studio (`editor.html`)
1. Open `editor.html` in your browser (or visit `https://wealth.t37.in/editor.html`).
2. Fill in:
   - **Title**, **Category**, **Author**, **Date & Time**.
   - Pick a thumbnail from the preset vector illustrations or upload an image.
   - Paste content from Microsoft Word into the **Word Paste Box** and click **"✨ Clean & Convert Word Content"**.
3. Use the **Live Preview** tab to review the exact card and full reader view.
4. Click **"Copy Antigravity Publishing Prompt"** to copy the formatted prompt into Antigravity, or click **"Download JSON"**.

### Method 3: Python CLI Script
You can publish articles from your terminal:
```bash
# Publish from JSON file
python scripts/publish_article.py --json-file my_article.json --push

# Publish directly via command line
python scripts/publish_article.py \
  --title "RBI Monetary Policy Outlook 2026" \
  --category "Markets" \
  --content-file draft.html \
  --push
```

---

## 📁 Repository Structure

```
wealth/
├── index.html              # Main Finshots-style blog landing page, editorial strip & modals
├── editor.html             # Hidden content studio & Word paste converter
├── styles.css              # Custom editorial stylesheet (trust strips, badges, cards)
├── script.js               # Category switching, 20-item feed, search, reader modal, schemas
├── robots.txt              # Crawler permissions for Googlebot, Googlebot-News & sitemaps
├── sitemap.xml             # Main XML sitemap
├── news-sitemap.xml        # Dedicated Google News XML sitemap (<news:news>)
├── feed.xml                # Google Publisher Center RSS 2.0 Feed
├── rss.xml                 # Alternate RSS 2.0 Feed
├── vercel.json             # Vercel deployment & feed MIME configuration
├── data/
│   └── articles.json       # Article database (Markets & Personal Finance)
├── assets/
│   ├── logo.png            # T37 Logo
│   ├── favicons/           # Complete favicon suite
│   └── thumbnails/         # Custom SVG financial illustrations
└── scripts/
    ├── publish_article.py  # Automation script for publishing new articles
    ├── generate_sitemap.py # Sitemap & Google News sitemap generator
    ├── generate_rss_feed.py# RSS 2.0 & Media RSS feed generator
    └── generate_thumbnails.py # SVG thumbnail generator
```

---

## 🚀 Local Development

To run the site locally:
```bash
# Using Python
python -m http.server 3000

# Using Node.js
npx serve .
```
Open [http://localhost:3000](http://localhost:3000) in your browser.
