import os

os.makedirs(r"C:\Users\T37\Desktop\T37\wealth\assets\thumbnails", exist_ok=True)

THUMBNAILS = {
    "markets-nse-ipo.svg": {
        "title": "NSE IPO Valuation",
        "category": "Capital Markets",
        "bg_start": "#1e3a8a", "bg_end": "#0284c7",
        "accent": "#f59e0b",
        "icon": """
            <!-- Exchange Building & Caliper -->
            <rect x="240" y="160" width="320" height="240" rx="16" fill="#ffffff" opacity="0.95"/>
            <rect x="270" y="220" width="50" height="150" rx="6" fill="#0284c7" opacity="0.3"/>
            <rect x="345" y="220" width="50" height="150" rx="6" fill="#0284c7" opacity="0.3"/>
            <rect x="420" y="220" width="50" height="150" rx="6" fill="#0284c7" opacity="0.3"/>
            <rect x="495" y="220" width="35" height="150" rx="6" fill="#0284c7" opacity="0.3"/>
            <!-- Triangle Roof / Pediment -->
            <polygon points="220,160 400,90 580,160" fill="#ffffff"/>
            <!-- Caliper Measure -->
            <path d="M180,120 L620,120 L620,150 L560,150 L560,280 L520,280 L520,150 L280,150 L280,280 L240,280 L240,150 L180,150 Z" fill="#f59e0b" opacity="0.9"/>
            <!-- Currency Tag -->
            <g transform="translate(540, 240) rotate(15)">
                <polygon points="0,0 80,0 110,35 80,70 0,70" fill="#10b981"/>
                <circle cx="20" cy="35" r="8" fill="#ffffff"/>
                <text x="50" y="45" font-family="system-ui, sans-serif" font-size="28" font-weight="bold" fill="#ffffff" text-anchor="middle">₹?</text>
            </g>
        """
    },
    "markets-treasury-buyback.svg": {
        "title": "US Treasury Buybacks",
        "category": "Macroeconomics",
        "bg_start": "#0f172a", "bg_end": "#334155",
        "accent": "#38bdf8",
        "icon": """
            <!-- Treasury Vault & Yield Curve -->
            <circle cx="400" cy="225" r="140" fill="#1e293b" stroke="#38bdf8" stroke-width="8"/>
            <circle cx="400" cy="225" r="90" fill="none" stroke="#64748b" stroke-dasharray="12 12" stroke-width="4"/>
            <!-- Circular Arrow Buyback Loop -->
            <path d="M400,105 A120,120 0 1,1 285,185" fill="none" stroke="#38bdf8" stroke-width="14" stroke-linecap="round"/>
            <polygon points="280,160 270,210 320,195" fill="#38bdf8"/>
            <!-- Bond Certificate Icon -->
            <rect x="350" y="175" width="100" height="100" rx="12" fill="#ffffff" opacity="0.9"/>
            <line x1="370" y1="205" x2="430" y2="205" stroke="#0f172a" stroke-width="6" stroke-linecap="round"/>
            <line x1="370" y1="225" x2="430" y2="225" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
            <line x1="370" y1="245" x2="410" y2="245" stroke="#10b981" stroke-width="5" stroke-linecap="round"/>
        """
    },
    "markets-semiconductor.svg": {
        "title": "India Semiconductor Push",
        "category": "Industry",
        "bg_start": "#14532d", "bg_end": "#15803d",
        "accent": "#4ade80",
        "icon": """
            <!-- Silicon Microchip -->
            <rect x="280" y="115" width="240" height="220" rx="20" fill="#052e16" stroke="#4ade80" stroke-width="8"/>
            <rect x="330" y="165" width="140" height="120" rx="10" fill="#166534"/>
            <text x="400" y="235" font-family="monospace" font-size="32" font-weight="bold" fill="#4ade80" text-anchor="middle">Si-FAB</text>
            <!-- Chip Pins Top/Bottom/Sides -->
            <g stroke="#86efac" stroke-width="6" stroke-linecap="round">
                <line x1="320" y1="115" x2="320" y2="80"/><line x1="360" y1="115" x2="360" y2="80"/><line x1="400" y1="115" x2="400" y2="80"/><line x1="440" y1="115" x2="440" y2="80"/><line x1="480" y1="115" x2="480" y2="80"/>
                <line x1="320" y1="335" x2="320" y2="370"/><line x1="360" y1="335" x2="360" y2="370"/><line x1="400" y1="335" x2="400" y2="370"/><line x1="440" y1="335" x2="440" y2="370"/><line x1="480" y1="335" x2="480" y2="370"/>
                <line x1="280" y1="160" x2="245" y2="160"/><line x1="280" y1="200" x2="245" y2="200"/><line x1="280" y1="240" x2="245" y2="240"/><line x1="280" y1="280" x2="245" y2="280"/>
                <line x1="520" y1="160" x2="555" y2="160"/><line x1="520" y1="200" x2="555" y2="200"/><line x1="520" y1="240" x2="555" y2="240"/><line x1="520" y1="280" x2="555" y2="280"/>
            </g>
        """
    },
    "markets-fii-flows.svg": {
        "title": "FII Fund Flows",
        "category": "Institutional Flows",
        "bg_start": "#312e81", "bg_end": "#4338ca",
        "accent": "#a5b4fc",
        "icon": """
            <!-- Dual Directional Flows & Currency Globes -->
            <circle cx="270" cy="225" r="90" fill="#1e1b4b" stroke="#818cf8" stroke-width="6"/>
            <text x="270" y="240" font-family="system-ui, sans-serif" font-size="44" font-weight="bold" fill="#ffffff" text-anchor="middle">$</text>
            <circle cx="530" cy="225" r="90" fill="#1e1b4b" stroke="#34d399" stroke-width="6"/>
            <text x="530" y="240" font-family="system-ui, sans-serif" font-size="44" font-weight="bold" fill="#ffffff" text-anchor="middle">₹</text>
            <!-- Dynamic Arrow Waves -->
            <path d="M340,180 C400,140 430,140 460,180" fill="none" stroke="#34d399" stroke-width="12" stroke-linecap="round"/>
            <polygon points="455,160 480,185 445,195" fill="#34d399"/>
            <path d="M460,270 C400,310 370,310 340,270" fill="none" stroke="#f43f5e" stroke-width="12" stroke-linecap="round"/>
            <polygon points="345,290 320,265 355,255" fill="#f43f5e"/>
        """
    },
    "markets-fmcg-margins.svg": {
        "title": "FMCG Margin Dynamics",
        "category": "Corporate Earnings",
        "bg_start": "#7c2d12", "bg_end": "#ea580c",
        "accent": "#fdba74",
        "icon": """
            <!-- Shopping Cart & Inflation Bar Chart -->
            <g transform="translate(180, 120)">
                <path d="M40,40 L90,40 L130,160 L240,160 L270,80 L110,80" fill="none" stroke="#ffffff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="140" cy="195" r="20" fill="#ffffff"/>
                <circle cx="230" cy="195" r="20" fill="#ffffff"/>
            </g>
            <g transform="translate(460, 140)">
                <rect x="0" y="100" width="36" height="80" rx="6" fill="#fed7aa"/>
                <rect x="50" y="50" width="36" height="130" rx="6" fill="#fb923c"/>
                <rect x="100" y="10" width="36" height="170" rx="6" fill="#ea580c"/>
                <path d="M15,90 L65,40 L115,0" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
            </g>
        """
    },
    "crypto-btc-halving.svg": {
        "title": "Bitcoin Halving & ETFs",
        "category": "Digital Assets",
        "bg_start": "#78350f", "bg_end": "#d97706",
        "accent": "#fde68a",
        "icon": """
            <!-- Bitcoin Emblem & Institutional Columns -->
            <circle cx="400" cy="210" r="110" fill="#b45309" stroke="#fde68a" stroke-width="10"/>
            <text x="400" y="240" font-family="system-ui, sans-serif" font-size="95" font-weight="900" fill="#ffffff" text-anchor="middle">₿</text>
            <!-- Halving Slash & ETF Pillar -->
            <line x1="260" y1="70" x2="540" y2="350" stroke="#fef08a" stroke-width="12" stroke-linecap="round" opacity="0.85"/>
            <!-- 21M hard cap badge -->
            <rect x="320" y="340" width="160" height="44" rx="22" fill="#1e293b"/>
            <text x="400" y="369" font-family="monospace" font-size="20" font-weight="bold" fill="#fde68a" text-anchor="middle">21M RESERVE</text>
        """
    },
    "crypto-eth-l2.svg": {
        "title": "Ethereum L2 Gas",
        "category": "Blockchain Tech",
        "bg_start": "#1e1b4b", "bg_end": "#4f46e5",
        "accent": "#a5b4fc",
        "icon": """
            <!-- Ethereum Diamond & Layered Blocks -->
            <polygon points="400,90 470,210 400,250 330,210" fill="#818cf8" opacity="0.9"/>
            <polygon points="400,265 470,225 400,320 330,225" fill="#a5b4fc" opacity="0.75"/>
            <!-- L2 Rollup Base Layers -->
            <rect x="220" y="325" width="360" height="24" rx="8" fill="#c7d2fe"/>
            <rect x="250" y="358" width="300" height="20" rx="6" fill="#e0e7ff"/>
            <!-- Gas Meter -->
            <g transform="translate(520, 120)">
                <circle cx="50" cy="50" r="45" fill="#0f172a" stroke="#34d399" stroke-width="6"/>
                <path d="M50,50 L75,30" stroke="#34d399" stroke-width="6" stroke-linecap="round"/>
                <text x="50" y="80" font-family="sans-serif" font-size="14" font-weight="bold" fill="#34d399" text-anchor="middle">0.001¢</text>
            </g>
        """
    },
    "crypto-stablecoins.svg": {
        "title": "Trillion Dollar Settlement",
        "category": "Stablecoins",
        "bg_start": "#064e3b", "bg_end": "#059669",
        "accent": "#6ee7b7",
        "icon": """
            <!-- Stablecoin Tether/Circle Motif -->
            <circle cx="400" cy="225" r="120" fill="#047857" stroke="#a7f3d0" stroke-width="8"/>
            <circle cx="400" cy="225" r="80" fill="none" stroke="#ffffff" stroke-width="6"/>
            <text x="400" y="255" font-family="system-ui, sans-serif" font-size="80" font-weight="bold" fill="#ffffff" text-anchor="middle">₮</text>
            <!-- Settlement Globe Rings -->
            <ellipse cx="400" cy="225" rx="260" ry="110" fill="none" stroke="#6ee7b7" stroke-width="4" stroke-dasharray="8 8"/>
            <ellipse cx="400" cy="225" rx="220" ry="170" fill="none" stroke="#a7f3d0" stroke-width="3" opacity="0.5"/>
        """
    },
    "crypto-defi-yield.svg": {
        "title": "DeFi Real Yield",
        "category": "DeFi Protocols",
        "bg_start": "#581c87", "bg_end": "#9333ea",
        "accent": "#f0abfc",
        "icon": """
            <!-- Liquidity Pool & Growth Sprout -->
            <rect x="250" y="150" width="300" height="180" rx="24" fill="#3b0764" stroke="#c084fc" stroke-width="6"/>
            <!-- Stacking Tokens -->
            <ellipse cx="330" cy="260" rx="45" ry="16" fill="#a855f7"/>
            <ellipse cx="330" cy="245" rx="45" ry="16" fill="#c084fc"/>
            <ellipse cx="330" cy="230" rx="45" ry="16" fill="#e9d5ff"/>
            <ellipse cx="470" cy="240" rx="45" ry="16" fill="#34d399"/>
            <ellipse cx="470" cy="220" rx="45" ry="16" fill="#6ee7b7"/>
            <!-- Yield Percentage Badge -->
            <rect x="350" y="110" width="100" height="46" rx="12" fill="#10b981"/>
            <text x="400" y="142" font-family="system-ui, sans-serif" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle">REAL %</text>
        """
    },
    "crypto-regulations.svg": {
        "title": "Global Crypto Rules",
        "category": "Regulatory Policy",
        "bg_start": "#1e293b", "bg_end": "#475569",
        "accent": "#cbd5e1",
        "icon": """
            <!-- Scales of Justice & Blockchain Mesh -->
            <line x1="400" y1="110" x2="400" y2="340" stroke="#f8fafc" stroke-width="10" stroke-linecap="round"/>
            <line x1="260" y1="160" x2="540" y2="160" stroke="#f8fafc" stroke-width="8" stroke-linecap="round"/>
            <!-- Left Pan -->
            <polygon points="260,160 210,250 310,250" fill="none" stroke="#38bdf8" stroke-width="5"/>
            <circle cx="260" cy="240" r="22" fill="#38bdf8"/>
            <!-- Right Pan -->
            <polygon points="540,160 490,250 590,250" fill="none" stroke="#f59e0b" stroke-width="5"/>
            <polygon points="540,215 565,245 515,245" fill="#f59e0b"/>
            <!-- Base -->
            <rect x="330" y="330" width="140" height="24" rx="8" fill="#f8fafc"/>
        """
    },
    "personal-finance-mutual-funds.svg": {
        "title": "Direct vs Regular Mutual Funds",
        "category": "Wealth Building",
        "bg_start": "#065f46", "bg_end": "#047857",
        "accent": "#34d399",
        "icon": """
            <!-- Exponential Compounding Curves -->
            <path d="M180,330 Q400,320 620,130" fill="none" stroke="#34d399" stroke-width="12" stroke-linecap="round"/>
            <path d="M180,330 Q400,330 620,230" fill="none" stroke="#f87171" stroke-width="8" stroke-linecap="round" stroke-dasharray="10 10"/>
            <!-- Difference Gap Tag -->
            <g transform="translate(560, 160)">
                <rect x="0" y="0" width="140" height="50" rx="10" fill="#ffffff"/>
                <text x="70" y="32" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#047857" text-anchor="middle">+₹1.2 Cr</text>
            </g>
            <text x="260" y="170" font-family="system-ui, sans-serif" font-size="26" font-weight="bold" fill="#34d399">Direct Plan</text>
            <text x="260" y="270" font-family="system-ui, sans-serif" font-size="22" font-weight="600" fill="#fca5a5">Regular Plan (1% fee)</text>
        """
    },
    "personal-finance-budgeting.svg": {
        "title": "50/30/20 Rule",
        "category": "Budgeting",
        "bg_start": "#1e3a8a", "bg_end": "#2563eb",
        "accent": "#93c5fd",
        "icon": """
            <!-- Pie/Donut Chart breakdown -->
            <circle cx="400" cy="225" r="110" fill="none" stroke="#60a5fa" stroke-width="50" stroke-dasharray="345 345" stroke-dashoffset="0"/>
            <circle cx="400" cy="225" r="110" fill="none" stroke="#34d399" stroke-width="50" stroke-dasharray="138 552" stroke-dashoffset="-345"/>
            <circle cx="400" cy="225" r="110" fill="none" stroke="#f59e0b" stroke-width="50" stroke-dasharray="207 483" stroke-dashoffset="-483"/>
            <text x="400" y="235" font-family="system-ui, sans-serif" font-size="34" font-weight="bold" fill="#ffffff" text-anchor="middle">50/30/20</text>
        """
    },
    "personal-finance-insurance.svg": {
        "title": "Term Insurance Fine Print",
        "category": "Protection",
        "bg_start": "#831843", "bg_end": "#be185d",
        "accent": "#fbcfe8",
        "icon": """
            <!-- Protective Shield & Verification Magnifier -->
            <path d="M400,90 L510,140 L510,250 C510,320 400,370 400,370 C400,370 290,320 290,250 L290,140 Z" fill="#9d174d" stroke="#fbcfe8" stroke-width="8"/>
            <path d="M360,230 L390,260 L450,190" fill="none" stroke="#34d399" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- Document Fine Print Lines -->
            <line x1="340" y1="290" x2="460" y2="290" stroke="#fbcfe8" stroke-width="4" stroke-linecap="round"/>
            <line x1="360" y1="310" x2="440" y2="310" stroke="#fbcfe8" stroke-width="4" stroke-linecap="round"/>
        """
    },
    "personal-finance-taxation.svg": {
        "title": "Tax Regimes: NPS vs PPF",
        "category": "Tax Planning",
        "bg_start": "#374151", "bg_end": "#1f2937",
        "accent": "#fbbf24",
        "icon": """
            <!-- Calculator & Tax Shield -->
            <rect x="290" y="110" width="220" height="240" rx="16" fill="#111827" stroke="#fbbf24" stroke-width="6"/>
            <rect x="320" y="140" width="160" height="46" rx="8" fill="#374151"/>
            <text x="460" y="172" font-family="monospace" font-size="24" font-weight="bold" fill="#34d399" text-anchor="end">0 TAX</text>
            <!-- Keypad Buttons -->
            <circle cx="345" cy="220" r="14" fill="#4b5563"/><circle cx="400" cy="220" r="14" fill="#4b5563"/><circle cx="455" cy="220" r="14" fill="#fbbf24"/>
            <circle cx="345" cy="265" r="14" fill="#4b5563"/><circle cx="400" cy="265" r="14" fill="#4b5563"/><circle cx="455" cy="265" r="14" fill="#3b82f6"/>
            <circle cx="345" cy="310" r="14" fill="#4b5563"/><circle cx="400" cy="310" r="14" fill="#4b5563"/><circle cx="455" cy="310" r="14" fill="#10b981"/>
        """
    },
    "personal-finance-behavioral.svg": {
        "title": "Behavioral Finance & Drawdowns",
        "category": "Psychology",
        "bg_start": "#1e1b4b", "bg_end": "#312e81",
        "accent": "#c7d2fe",
        "icon": """
            <!-- Brain & Volatility Waves -->
            <circle cx="400" cy="220" r="100" fill="#3730a3" stroke="#818cf8" stroke-width="6"/>
            <path d="M350,210 Q400,160 450,210 T550,210" fill="none" stroke="#f43f5e" stroke-width="8" stroke-linecap="round"/>
            <path d="M250,240 Q350,290 400,230 T550,240" fill="none" stroke="#34d399" stroke-width="8" stroke-linecap="round"/>
            <circle cx="400" cy="220" r="16" fill="#fbbf24"/>
            <text x="400" y="360" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#c7d2fe" text-anchor="middle">STAY THE COURSE</text>
        """
    },
    "algo-mean-reversion.svg": {
        "title": "Mean Reversion Strategy",
        "category": "Statistical Arbitrage",
        "bg_start": "#0f172a", "bg_end": "#1e293b",
        "accent": "#38bdf8",
        "icon": """
            <!-- Bollinger / Z-score Bands & Oscillator -->
            <line x1="160" y1="225" x2="640" y2="225" stroke="#64748b" stroke-width="4" stroke-dasharray="6 6"/>
            <line x1="160" y1="140" x2="640" y2="140" stroke="#f43f5e" stroke-width="4"/>
            <line x1="160" y1="310" x2="640" y2="310" stroke="#34d399" stroke-width="4"/>
            <path d="M160,225 Q220,110 280,225 T400,330 T520,120 T640,225" fill="none" stroke="#38bdf8" stroke-width="10" stroke-linecap="round"/>
            <!-- Signal Points -->
            <circle cx="250" cy="140" r="12" fill="#f43f5e"/>
            <circle cx="430" cy="310" r="12" fill="#34d399"/>
            <text x="600" y="130" font-family="monospace" font-size="16" fill="#f87171">+2σ SELL</text>
            <text x="600" y="335" font-family="monospace" font-size="16" fill="#4ade80">-2σ BUY</text>
        """
    },
    "algo-vwap-orderflow.svg": {
        "title": "VWAP & Order Flow",
        "category": "Microstructure",
        "bg_start": "#18181b", "bg_end": "#27272a",
        "accent": "#fbbf24",
        "icon": """
            <!-- Candlestick Volume Profile Bars -->
            <g transform="translate(180, 100)">
                <rect x="0" y="40" width="120" height="24" rx="4" fill="#ef4444" opacity="0.8"/>
                <rect x="0" y="75" width="220" height="24" rx="4" fill="#3b82f6" opacity="0.9"/>
                <rect x="0" y="110" width="310" height="24" rx="4" fill="#fbbf24"/>
                <rect x="0" y="145" width="190" height="24" rx="4" fill="#3b82f6" opacity="0.9"/>
                <rect x="0" y="180" width="80" height="24" rx="4" fill="#10b981" opacity="0.8"/>
            </g>
            <path d="M220,280 L350,180 L480,240 L590,140" fill="none" stroke="#ffffff" stroke-width="8" stroke-linecap="round"/>
            <text x="500" y="270" font-family="monospace" font-size="22" font-weight="bold" fill="#fbbf24">POC / VWAP</text>
        """
    },
    "algo-backtest-pitfalls.svg": {
        "title": "Backtesting Pitfalls",
        "category": "Quant Strategy",
        "bg_start": "#450a0a", "bg_end": "#7f1d1d",
        "accent": "#fca5a5",
        "icon": """
            <!-- Warning Sign & Overfitting Trap -->
            <polygon points="400,100 540,330 260,330" fill="#991b1b" stroke="#fca5a5" stroke-width="8" stroke-linejoin="round"/>
            <line x1="400" y1="180" x2="400" y2="260" stroke="#ffffff" stroke-width="12" stroke-linecap="round"/>
            <circle cx="400" cy="295" r="7" fill="#ffffff"/>
            <text x="400" y="375" font-family="monospace" font-size="18" font-weight="bold" fill="#fecaca" text-anchor="middle">OVERFITTING BIAS</text>
        """
    },
    "algo-kelly-criterion.svg": {
        "title": "Kelly Criterion Position Sizing",
        "category": "Risk Management",
        "bg_start": "#042f2e", "bg_end": "#115e59",
        "accent": "#5eead4",
        "icon": """
            <!-- Mathematical Kelly Equation Formula & Scale -->
            <rect x="220" y="140" width="360" height="170" rx="16" fill="#134e4a" stroke="#5eead4" stroke-width="6"/>
            <text x="400" y="225" font-family="serif" font-size="52" font-style="italic" font-weight="bold" fill="#ffffff" text-anchor="middle">f* = (bp - q) / b</text>
            <text x="400" y="275" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" fill="#5eead4" text-anchor="middle">OPTIMAL POSITION SIZE</text>
        """
    },
    "algo-execution-engine.svg": {
        "title": "Low Latency Engine",
        "category": "Systems Architecture",
        "bg_start": "#022c22", "bg_end": "#064e3b",
        "accent": "#34d399",
        "icon": """
            <!-- High Speed Lightning & Packet Routing -->
            <polygon points="410,90 350,220 420,220 370,350 470,200 400,200" fill="#34d399" stroke="#ffffff" stroke-width="4"/>
            <!-- Data Stream Nodes -->
            <circle cx="240" cy="180" r="16" fill="#6ee7b7"/><circle cx="220" cy="270" r="12" fill="#6ee7b7"/>
            <circle cx="560" cy="180" r="16" fill="#6ee7b7"/><circle cx="580" cy="270" r="12" fill="#6ee7b7"/>
            <line x1="256" y1="180" x2="350" y2="210" stroke="#6ee7b7" stroke-width="4" stroke-dasharray="6 6"/>
            <line x1="430" y1="210" x2="544" y2="180" stroke="#6ee7b7" stroke-width="4" stroke-dasharray="6 6"/>
            <text x="400" y="380" font-family="monospace" font-size="16" font-weight="bold" fill="#6ee7b7" text-anchor="middle">&lt; 250μs TICK-TO-TRADE</text>
        """
    }
}

for filename, data in THUMBNAILS.items():
    filepath = os.path.join(r"C:\Users\T37\Desktop\T37\wealth\assets\thumbnails", filename)
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="grad_{filename[:6]}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{data['bg_start']}"/>
      <stop offset="100%" stop-color="{data['bg_end']}"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.06"/>
    </pattern>
  </defs>
  <rect width="800" height="450" fill="url(#grad_{filename[:6]})"/>
  <rect width="800" height="450" fill="url(#grid)"/>
  
  {data['icon']}
  
  <!-- Subtle Category Tag on graphic -->
  <g transform="translate(40, 40)">
    <rect x="0" y="0" width="160" height="32" rx="16" fill="#ffffff" opacity="0.18"/>
    <text x="80" y="21" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">{data['category'].upper()}</text>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())

print(f"Generated {len(THUMBNAILS)} SVG thumbnails successfully.")
