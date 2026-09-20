# T37 Wealth (wealth.t37.in)

> **Finshots-inspired financial journalism platform** covering Markets, Crypto, Personal Finance, and Algorithmic Trading with 3-minute, actionable, easy-to-understand reads.

Live URL: [https://wealth.t37.in](https://wealth.t37.in)

---

## 🌟 Features

- **Finshots Visual Design**: Clean, crisp typography, high-impact editorial illustrations, and responsive 3-column card grid.
- **5 Navigation Sections**:
  1. **Latest**: Dynamically aggregates the 20 most recent articles across all categories.
  2. **Markets**: Indian and global equities, IPOs, macroeconomics, FII/DII fund flows.
  3. **Crypto**: Blockchain infrastructure, Layer 2 scaling, Bitcoin ETFs, DeFi real yield, regulation.
  4. **Personal Finance**: Mutual funds (Direct vs Regular), insurance fine print, tax optimization, budgeting.
  5. **Algo Trading**: Quantitative models, pairs trading, VWAP order flow, risk management, execution engines.
- **Deep-Linkable Reader**: Seamless article modal with "In a nutshell" key takeaways, social share buttons (WhatsApp, X, LinkedIn), and related recommendations.
- **Instant Search**: Client-side full-text search across titles, summaries, content, authors, and categories.
- **Hidden Content Studio (`editor.html`)**: A private authoring portal not exposed in the public navigation.

---

## ✍️ How to Publish New Articles

### Method 1: Ask Antigravity Directly (Easiest)
Whenever you have a new article in Microsoft Word, Google Docs, or plain text:
1. Simply paste the text or attach your document in Antigravity chat:
   > *"Antigravity, please publish this new article under Algo Trading: [Paste Title & Content]"*
2. Antigravity will automatically:
   - Clean the text and generate semantic HTML.
   - Assign an appropriate SVG thumbnail from `assets/thumbnails/`.
   - Calculate reading time and generate a clean slug.
   - Prepend the article to `data/articles.json`.
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
├── index.html              # Main Finshots-style blog landing page & article reader
├── editor.html             # Hidden content studio & Word paste converter
├── styles.css              # Custom editorial stylesheet
├── script.js               # Category switching, 20-item feed, search, reader modal
├── vercel.json             # Vercel deployment configuration
├── package.json            # Project metadata
├── README.md               # Documentation
├── data/
│   └── articles.json       # Article database (20 starter articles)
├── assets/
│   ├── logo.png            # T37 Logo
│   ├── favicons/           # Complete favicon suite
│   └── thumbnails/         # 20 custom SVG financial illustrations
└── scripts/
    ├── publish_article.py  # Automation script for publishing new articles
    ├── generate_thumbnails.py # SVG thumbnail generator
    └── generate_initial_articles.py # Article generator
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
