/**
 * T37 WEALTH - MAIN APPLICATION SCRIPT
 * Finshots-inspired editorial blog engine
 * Mobile-First, SEO & AI Search Optimized
 */

(function () {
  'use strict';

  // Global State
  let allArticles = [];
  let currentCategory = 'latest';
  let activeArticle = null;

  // Category Configuration (Latest, Markets, Personal Finance)
  const CATEGORY_META = {
    'latest': {
      title: 'Latest Reads',
      subtitle: '3 Min reads that are fun, insightful and easy to understand. <span class="highlight">This is T37 Wealth as you know it.</span>',
      filter: () => true,
      limit: 20
    },
    'markets': {
      title: 'Markets',
      subtitle: 'Daily pulse of Indian & global financial markets, IPO valuations, macroeconomics, and corporate earnings.',
      filter: (a) => a.category.toLowerCase() === 'markets'
    },
    'personal-finance': {
      title: 'Personal Finance',
      subtitle: 'Smart money strategies, tax optimization, retirement planning, and financial independence.',
      filter: (a) => a.category.toLowerCase() === 'personal finance'
    }
  };

  // DOM Elements
  const articlesGrid = document.getElementById('articles-grid');
  const heroTitle = document.getElementById('hero-title');
  const heroSubtitle = document.getElementById('hero-subtitle');
  const navLinks = document.querySelectorAll('.nav-link');
  const readerModal = document.getElementById('reader-modal');
  const readerContent = document.getElementById('reader-content');
  const closeReaderBtn = document.getElementById('close-reader-btn');
  const backBtn = document.getElementById('back-btn');
  const searchModal = document.getElementById('search-modal');
  const searchTriggerBtn = document.getElementById('search-trigger-btn');
  const closeSearchBtn = document.getElementById('close-search-btn');
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileNavDrawer = document.getElementById('mobile-nav-drawer');
  const mobileNavBackdrop = document.getElementById('mobile-nav-backdrop');
  const cookieBanner = document.getElementById('cookie-banner');
  const cookieAcceptBtn = document.getElementById('cookie-accept-btn');
  const cookieDeclineBtn = document.getElementById('cookie-decline-btn');
  const cookiePolicyBannerLink = document.getElementById('cookie-policy-banner-link');
  const cookiesModal = document.getElementById('cookies-modal');
  const closeCookiesBtn = document.getElementById('close-cookies-btn');
  const cookiesModalOkBtn = document.getElementById('cookies-modal-ok-btn');
  const footerCookiesBtn = document.getElementById('footer-cookies-btn');
  const editorialModal = document.getElementById('editorial-modal');
  const closeEditorialBtn = document.getElementById('close-editorial-btn');
  const editorialModalOkBtn = document.getElementById('editorial-modal-ok-btn');
  const trustPolicyTrigger = document.getElementById('trust-policy-trigger');
  const footerEditorialBtn = document.getElementById('footer-editorial-btn');
  const footerFactcheckBtn = document.getElementById('footer-factcheck-btn');
  const footerCorrectionsBtn = document.getElementById('footer-corrections-btn');

  // Format Date (e.g., "Sep 21, 2026")
  function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    });
  }

  // Load Articles from JSON
  async function loadArticles() {
    try {
      const res = await fetch('data/articles.json');
      if (!res.ok) throw new Error('Failed to fetch articles');
      allArticles = await res.json();
      
      // Ensure all articles reflect T37 Editor Desk
      allArticles.forEach(a => { a.author = 'T37 Editor Desk'; });

      // Sort newest first
      allArticles.sort((a, b) => new Date(b.datetime) - new Date(a.datetime));

      // Check initial hash route
      handleRoute();
    } catch (err) {
      console.error('Error loading articles:', err);
      articlesGrid.innerHTML = `
        <div class="empty-state">
          <h3>Unable to load articles</h3>
          <p>Please check your connection or refresh the page.</p>
        </div>
      `;
    }
  }

  // Set Active Category
  function setCategory(catKey, pushState = true) {
    const validKey = CATEGORY_META[catKey] ? catKey : 'latest';
    const config = CATEGORY_META[validKey];
    currentCategory = validKey;

    // Update nav active states (both desktop and mobile)
    navLinks.forEach(link => {
      if (link.dataset.category === catKey) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    // Update Hero Section
    heroTitle.textContent = config.title;
    heroSubtitle.innerHTML = config.subtitle;

    // Filter Articles
    let filtered = allArticles.filter(config.filter);
    if (config.limit) {
      filtered = filtered.slice(0, config.limit);
    }

    renderArticles(filtered);

    // Update URL Hash
    if (pushState) {
      if (catKey === 'latest') {
        history.pushState(null, '', window.location.pathname);
      } else {
        history.pushState(null, '', '#' + catKey);
      }
    }

    // Close reader if open
    closeReader(false);
  }

  // Render Article Cards
  function renderArticles(articles) {
    if (!articles || articles.length === 0) {
      articlesGrid.innerHTML = `
        <div class="empty-state">
          <h3>No articles found</h3>
          <p>There are currently no articles in this category.</p>
        </div>
      `;
      return;
    }

    articlesGrid.innerHTML = articles.map(article => {
      const categorySlug = article.category.toLowerCase().replace(/\s+/g, '-');
      const tag = article.subCategory || article.category;
      return `
        <article class="article-card" data-slug="${article.slug}">
          <div class="card-thumbnail">
            <img src="${article.thumbnail}" alt="${article.title}" loading="lazy">
          </div>
          <div class="card-body">
            <div class="card-category cat-${categorySlug}">${tag}</div>
            <h2 class="card-title">${article.title}</h2>
            <p class="card-excerpt">${article.excerpt || ''}</p>
            <div class="card-meta">
              <span>${formatDate(article.datetime)}</span>
              <span class="dot">•</span>
              <span>${article.readTime || '3 min read'}</span>
            </div>
          </div>
        </article>
      `;
    }).join('');

    // Attach card click handlers
    document.querySelectorAll('.article-card').forEach(card => {
      card.addEventListener('click', () => {
        const slug = card.dataset.slug;
        openArticle(slug);
      });
    });
  }

  // Inject NewsArticle Schema for SEO & Google News Crawlers
  function injectArticleSchema(article) {
    let existing = document.getElementById('article-schema');
    if (!existing) {
      existing = document.createElement('script');
      existing.id = 'article-schema';
      existing.type = 'application/ld+json';
      document.head.appendChild(existing);
    }
    const cleanText = (article.content || '').replace(/<[^>]+>/g, ' ').slice(0, 500);
    existing.textContent = JSON.stringify({
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": article.title,
      "image": [window.location.origin + "/" + article.thumbnail],
      "datePublished": article.datetime,
      "dateModified": article.datetime,
      "author": [{
        "@type": "Organization",
        "name": "T37 Editor Desk",
        "url": window.location.origin + "/#editorial-policy"
      }],
      "publisher": {
        "@type": "NewsMediaOrganization",
        "name": "T37 Wealth",
        "url": "https://wealth.t37.in",
        "logo": {
          "@type": "ImageObject",
          "url": "https://wealth.t37.in/assets/logo.png"
        },
        "publishingPrinciples": "https://wealth.t37.in/#editorial-policy"
      },
      "inLanguage": "en-US",
      "isAccessibleForFree": true,
      "description": article.excerpt || cleanText,
      "articleBody": cleanText,
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": window.location.origin + "/#article/" + article.slug
      },
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": [".reader-title", ".takeaways-box"]
      }
    });
  }

  function removeArticleSchema() {
    const existing = document.getElementById('article-schema');
    if (existing) existing.remove();
  }

  // Article Like Count Persistence
  function getArticleLikes(slug) {
    const stored = localStorage.getItem(`t37_likes_${slug}`);
    if (stored !== null) return parseInt(stored, 10);
    let hash = 0;
    for (let i = 0; i < slug.length; i++) hash = (hash * 31 + slug.charCodeAt(i)) % 100;
    const initial = 28 + Math.abs(hash);
    localStorage.setItem(`t37_likes_${slug}`, initial);
    return initial;
  }

  function isArticleLiked(slug) {
    return localStorage.getItem(`t37_liked_${slug}`) === 'true';
  }

  function toggleArticleLike(slug) {
    const liked = isArticleLiked(slug);
    let count = getArticleLikes(slug);
    if (liked) {
      count = Math.max(0, count - 1);
      localStorage.setItem(`t37_liked_${slug}`, 'false');
    } else {
      count = count + 1;
      localStorage.setItem(`t37_liked_${slug}`, 'true');
    }
    localStorage.setItem(`t37_likes_${slug}`, count);
    return { liked: !liked, count };
  }

  // Open Full Article Reader
  function openArticle(slug, pushState = true) {
    const article = allArticles.find(a => a.slug === slug || a.id === slug);
    if (!article) return;

    activeArticle = article;
    injectArticleSchema(article);

    // Update document title for SEO & tabs
    document.title = `${article.title} | T37 Wealth`;

    // Generate Related Articles
    const related = allArticles
      .filter(a => a.category === article.category && a.slug !== article.slug)
      .slice(0, 2);

    const relatedHtml = related.length > 0 ? `
      <div class="reader-related">
        <h3>More from ${article.category}</h3>
        <div class="related-grid">
          ${related.map(r => `
            <div class="article-card" data-slug="${r.slug}" style="cursor: pointer;">
              <div class="card-thumbnail">
                <img src="${r.thumbnail}" alt="${r.title}">
              </div>
              <div class="card-body">
                <h4 class="card-title" style="font-size: 1.05rem;">${r.title}</h4>
                <div class="card-meta">
                  <span>${formatDate(r.datetime)}</span>
                  <span class="dot">•</span>
                  <span>${r.readTime || '3 min read'}</span>
                </div>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    ` : '';

    const takeawaysHtml = article.keyTakeaways && article.keyTakeaways.length > 0 ? `
      <div class="takeaways-box">
        <h4>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          In a nutshell
        </h4>
        <ul>
          ${article.keyTakeaways.map(point => `<li>${point}</li>`).join('')}
        </ul>
      </div>
    ` : '';

    const isLiked = isArticleLiked(article.slug);
    const likesCount = getArticleLikes(article.slug);

    readerContent.innerHTML = `
      <div class="reader-category-pill">${article.category} • ${article.subCategory || 'Insight'}</div>
      <h1 class="reader-title">${article.title}</h1>
      
      <div class="reader-meta-bar">
        <div class="author-info">
          <div class="author-avatar">T</div>
          <div>
            <div class="author-name">T37 Editor Desk</div>
            <div class="article-datetime">
              <time datetime="${article.datetime}">${formatDate(article.datetime)}</time> • ${article.readTime || '3 min read'}
            </div>
          </div>
        </div>
        
        <div class="reader-actions-group">
          <button class="article-like-btn ${isLiked ? 'liked' : ''}" id="article-like-btn" title="${isLiked ? 'Unlike' : 'Like this read'}" aria-label="Like article">
            <svg class="heart-icon" width="16" height="16" viewBox="0 0 24 24" fill="${isLiked ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
              <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
            </svg>
            <span class="like-label">${isLiked ? 'Liked' : 'Like'}</span>
            <span class="like-count" id="article-like-count">${likesCount}</span>
          </button>

          <div class="share-buttons">
            <a class="share-btn" href="https://twitter.com/intent/tweet?text=${shareTitle}&url=${shareUrl}" target="_blank" rel="noopener noreferrer" title="Share on X" aria-label="Share on X">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </a>
            <a class="share-btn" href="https://api.whatsapp.com/send?text=${shareTitle}%20${shareUrl}" target="_blank" rel="noopener noreferrer" title="Share on WhatsApp" aria-label="Share on WhatsApp">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            </a>
            <button class="share-btn" id="copy-link-btn" title="Copy Link" aria-label="Copy Link">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
            </button>
          </div>
        </div>
      </div>
      
      <div class="reader-hero-img">
        <img src="${article.thumbnail}" alt="${article.title}">
      </div>
      
      ${takeawaysHtml}
      
      <div class="article-body">
        ${article.content}
      </div>

      <div class="article-editorial-footnote">
        <p><em>Disclaimer: Content published on T37 Wealth is strictly educational and does not constitute investment advice. Researched from official corporate & regulatory filings (NSE/BSE/RBI/SEBI). Report corrections to <a href="mailto:admin@mail.t37.in?subject=Correction%20Request:%20${encodeURIComponent(article.title)}">admin@mail.t37.in</a>.</em></p>
      </div>

      <div class="article-like-cta">
        <button class="article-like-btn large ${isLiked ? 'liked' : ''}" id="article-like-btn-bottom">
          <svg class="heart-icon" width="20" height="20" viewBox="0 0 24 24" fill="${isLiked ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
          <span class="like-label">${isLiked ? 'You liked this read' : 'Enjoyed this 3-min read? Tap to like'}</span>
          <span class="like-count" id="article-like-count-bottom">${likesCount}</span>
        </button>
      </div>
      
      ${relatedHtml}
    `;

    // Like buttons interaction
    function updateLikeUI(result) {
      const topBtn = document.getElementById('article-like-btn');
      const btmBtn = document.getElementById('article-like-btn-bottom');
      const topCount = document.getElementById('article-like-count');
      const btmCount = document.getElementById('article-like-count-bottom');
      
      [topBtn, btmBtn].forEach(btn => {
        if (!btn) return;
        const icon = btn.querySelector('.heart-icon');
        const label = btn.querySelector('.like-label');
        if (result.liked) {
          btn.classList.add('liked');
          if (icon) icon.setAttribute('fill', 'currentColor');
          if (label) label.textContent = btn.classList.contains('large') ? 'You liked this read' : 'Liked';
        } else {
          btn.classList.remove('liked');
          if (icon) icon.setAttribute('fill', 'none');
          if (label) label.textContent = btn.classList.contains('large') ? 'Enjoyed this 3-min read? Tap to like' : 'Like';
        }
      });
      if (topCount) topCount.textContent = result.count;
      if (btmCount) btmCount.textContent = result.count;
    }

    const topLikeBtn = document.getElementById('article-like-btn');
    const btmLikeBtn = document.getElementById('article-like-btn-bottom');
    if (topLikeBtn) {
      topLikeBtn.addEventListener('click', () => updateLikeUI(toggleArticleLike(article.slug)));
    }
    if (btmLikeBtn) {
      btmLikeBtn.addEventListener('click', () => updateLikeUI(toggleArticleLike(article.slug)));
    }

    // Copy link event
    document.getElementById('copy-link-btn').addEventListener('click', () => {
      navigator.clipboard.writeText(window.location.origin + window.location.pathname + '#article/' + article.slug);
      const btn = document.getElementById('copy-link-btn');
      btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
      setTimeout(() => {
        btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>`;
      }, 2000);
    });

    // Related article click inside reader
    readerContent.querySelectorAll('.reader-related .article-card').forEach(c => {
      c.addEventListener('click', () => {
        openArticle(c.dataset.slug);
      });
    });

    // Show modal & disable background scroll
    readerModal.classList.add('active');
    readerModal.scrollTop = 0;
    document.body.style.overflow = 'hidden';

    // Update URL hash
    if (pushState) {
      history.pushState(null, '', '#article/' + article.slug);
    }
  }

  // Close Article Reader
  function closeReader(updateUrl = true) {
    readerModal.classList.remove('active');
    document.body.style.overflow = '';
    activeArticle = null;
    removeArticleSchema();
    document.title = 'T37 Wealth | Financial Insights, Markets & Personal Finance';

    if (updateUrl) {
      if (currentCategory === 'latest') {
        history.pushState(null, '', window.location.pathname);
      } else {
        history.pushState(null, '', '#' + currentCategory);
      }
    }
  }

  // Search Logic
  function openSearch() {
    searchModal.classList.add('active');
    searchInput.value = '';
    searchInput.focus();
    renderSearchResults('');
  }

  function closeSearch() {
    searchModal.classList.remove('active');
  }

  function renderSearchResults(query) {
    const q = query.trim().toLowerCase();
    if (!q) {
      // Show recent 5 articles as suggestions
      searchResults.innerHTML = `
        <div style="padding: 10px 14px; font-size: 0.8rem; font-weight: 700; color: #9ca3af; text-transform: uppercase;">Recent Articles</div>
        ${allArticles.slice(0, 5).map(a => renderSearchItem(a)).join('')}
      `;
      attachSearchItemClicks();
      return;
    }

    const matches = allArticles.filter(a => {
      return (
        a.title.toLowerCase().includes(q) ||
        (a.excerpt && a.excerpt.toLowerCase().includes(q)) ||
        (a.category && a.category.toLowerCase().includes(q)) ||
        (a.subCategory && a.subCategory.toLowerCase().includes(q)) ||
        (a.author && a.author.toLowerCase().includes(q))
      );
    });

    if (matches.length === 0) {
      searchResults.innerHTML = `
        <div style="padding: 24px; text-align: center; color: #6b7280;">
          No articles matching "<strong>${query}</strong>"
        </div>
      `;
      return;
    }

    searchResults.innerHTML = matches.map(a => renderSearchItem(a)).join('');
    attachSearchItemClicks();
  }

  function renderSearchItem(a) {
    return `
      <div class="search-item" data-slug="${a.slug}">
        <div class="search-item-thumb">
          <img src="${a.thumbnail}" alt="${a.title}">
        </div>
        <div class="search-item-info">
          <div class="search-item-title">${a.title}</div>
          <div class="search-item-meta">${a.category} • ${formatDate(a.datetime)}</div>
        </div>
      </div>
    `;
  }

  function attachSearchItemClicks() {
    searchResults.querySelectorAll('.search-item').forEach(item => {
      item.addEventListener('click', () => {
        const slug = item.dataset.slug;
        closeSearch();
        openArticle(slug);
      });
    });
  }

  // Handle URL Hash Navigation
  function handleRoute() {
    const hash = window.location.hash.slice(1);
    if (!hash) {
      setCategory('latest', false);
      return;
    }

    if (hash === 'cookies-policy') {
      openCookiesModal();
      return;
    }

    if (['editorial-policy', 'fact-checking', 'corrections', 'disclaimer'].includes(hash)) {
      openEditorialModal();
      return;
    }

    if (hash.startsWith('article/')) {
      const slug = hash.replace('article/', '');
      openArticle(slug, false);
    } else if (CATEGORY_META[hash]) {
      setCategory(hash, false);
    } else {
      setCategory('latest', false);
    }
  }

  // Mobile Menu Controls
  function toggleMobileMenu() {
    const isOpen = mobileNavDrawer.classList.toggle('open');
    mobileNavBackdrop.classList.toggle('open', isOpen);
  }

  function closeMobileMenu() {
    mobileNavDrawer.classList.remove('open');
    mobileNavBackdrop.classList.remove('open');
  }

  // Event Listeners
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const cat = link.dataset.category;
      setCategory(cat);
      closeMobileMenu();
    });
  });

  mobileMenuBtn.addEventListener('click', toggleMobileMenu);
  mobileNavBackdrop.addEventListener('click', closeMobileMenu);

  closeReaderBtn.addEventListener('click', () => closeReader());
  backBtn.addEventListener('click', () => closeReader());

  // Close reader on clicking backdrop outside container
  readerModal.addEventListener('click', (e) => {
    if (e.target === readerModal) {
      closeReader();
    }
  });

  // Search Triggers
  searchTriggerBtn.addEventListener('click', openSearch);
  closeSearchBtn.addEventListener('click', closeSearch);
  searchModal.addEventListener('click', (e) => {
    if (e.target === searchModal) closeSearch();
  });
  searchInput.addEventListener('input', (e) => {
    renderSearchResults(e.target.value);
  });

  // Cookies Policy & Consent Logic
  function initCookieBanner() {
    if (!localStorage.getItem('t37_cookies_accepted')) {
      setTimeout(() => {
        if (cookieBanner) cookieBanner.classList.add('active');
      }, 800);
    }
  }

  function acceptCookies(type) {
    localStorage.setItem('t37_cookies_accepted', type);
    if (cookieBanner) cookieBanner.classList.remove('active');
  }

  function openCookiesModal() {
    if (cookiesModal) {
      cookiesModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeCookiesModal() {
    if (cookiesModal) {
      cookiesModal.classList.remove('active');
      if (!readerModal.classList.contains('active')) {
        document.body.style.overflow = '';
      }
      if (window.location.hash === '#cookies-policy') {
        history.pushState(null, '', window.location.pathname);
      }
    }
  }

  // Editorial & Transparency Modal Logic
  function openEditorialModal() {
    if (editorialModal) {
      editorialModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeEditorialModal() {
    if (editorialModal) {
      editorialModal.classList.remove('active');
      if (!readerModal.classList.contains('active')) {
        document.body.style.overflow = '';
      }
      if (['editorial-policy', 'fact-checking', 'corrections', 'disclaimer'].includes(window.location.hash.slice(1))) {
        history.pushState(null, '', window.location.pathname);
      }
    }
  }

  // Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (pushPromptContainer && pushPromptContainer.classList.contains('active')) closePushPrompt();
      else if (editorialModal && editorialModal.classList.contains('active')) closeEditorialModal();
      else if (cookiesModal && cookiesModal.classList.contains('active')) closeCookiesModal();
      else if (searchModal.classList.contains('active')) closeSearch();
      else if (readerModal.classList.contains('active')) closeReader();
      else closeMobileMenu();
    }
    if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
      e.preventDefault();
      openSearch();
    }
  });

  // Cookie Listeners
  if (cookieAcceptBtn) cookieAcceptBtn.addEventListener('click', () => acceptCookies('all'));
  if (cookieDeclineBtn) cookieDeclineBtn.addEventListener('click', () => acceptCookies('essential'));
  if (cookiePolicyBannerLink) cookiePolicyBannerLink.addEventListener('click', (e) => {
    e.preventDefault();
    openCookiesModal();
  });
  if (footerCookiesBtn) footerCookiesBtn.addEventListener('click', openCookiesModal);
  if (closeCookiesBtn) closeCookiesBtn.addEventListener('click', closeCookiesModal);
  if (cookiesModalOkBtn) cookiesModalOkBtn.addEventListener('click', closeCookiesModal);
  if (cookiesModal) {
    cookiesModal.addEventListener('click', (e) => {
      if (e.target === cookiesModal) closeCookiesModal();
    });
  }

  // Editorial Modal Listeners
  if (trustPolicyTrigger) trustPolicyTrigger.addEventListener('click', openEditorialModal);
  if (footerEditorialBtn) footerEditorialBtn.addEventListener('click', openEditorialModal);
  if (footerFactcheckBtn) footerFactcheckBtn.addEventListener('click', openEditorialModal);
  if (footerCorrectionsBtn) footerCorrectionsBtn.addEventListener('click', openEditorialModal);
  if (closeEditorialBtn) closeEditorialBtn.addEventListener('click', closeEditorialModal);
  if (editorialModalOkBtn) editorialModalOkBtn.addEventListener('click', closeEditorialModal);
  const cookiesToEditorialBtn = document.getElementById('cookies-to-editorial-btn');
  if (cookiesToEditorialBtn) {
    cookiesToEditorialBtn.addEventListener('click', (e) => {
      e.preventDefault();
      closeCookiesModal();
      openEditorialModal();
    });
  }
  if (editorialModal) {
    editorialModal.addEventListener('click', (e) => {
      if (e.target === editorialModal) closeEditorialModal();
    });
  }

  // Push Notifications Soft-Ask Prompt Logic
  const pushPromptContainer = document.getElementById('push-prompt-container');
  const pushBtnDecline = document.getElementById('push-btn-decline');
  const pushBtnAllow = document.getElementById('push-btn-allow');

  function initPushPrompt() {
    if (!localStorage.getItem('t37_push_prompt_answered')) {
      setTimeout(() => {
        if (pushPromptContainer) pushPromptContainer.classList.add('active');
      }, 3000);
    }
  }

  function closePushPrompt() {
    if (pushPromptContainer) {
      pushPromptContainer.classList.remove('active');
    }
  }

  if (pushBtnDecline) {
    pushBtnDecline.addEventListener('click', () => {
      localStorage.setItem('t37_push_prompt_answered', 'declined');
      closePushPrompt();
    });
  }

  if (pushBtnAllow) {
    pushBtnAllow.addEventListener('click', async () => {
      localStorage.setItem('t37_push_prompt_answered', 'allowed');
      closePushPrompt();
      if ('Notification' in window) {
        try {
          await Notification.requestPermission();
        } catch (e) {
          // ignore
        }
      }
    });
  }

  // Close push prompt on clicking background outside card
  if (pushPromptContainer) {
    pushPromptContainer.addEventListener('click', (e) => {
      if (e.target === pushPromptContainer) closePushPrompt();
    });
  }

  // Popstate / Hashchange
  window.addEventListener('hashchange', handleRoute);
  window.addEventListener('popstate', handleRoute);

  // Sticky header scroll shadow
  window.addEventListener('scroll', () => {
    const header = document.querySelector('.site-header');
    if (window.scrollY > 10) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // Start Application
  loadArticles();
  initCookieBanner();
  initPushPrompt();
})();
