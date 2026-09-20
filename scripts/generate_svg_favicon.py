import base64
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_PATH = os.path.join(ROOT, "assets", "logo.png")

with open(LOGO_PATH, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">
  <circle cx="64" cy="64" r="62" fill="#ffffff" stroke="#d1d5db" stroke-width="4"/>
  <image href="data:image/png;base64,{b64}" x="8" y="32" width="112" height="64" preserveAspectRatio="xMidYMid meet"/>
</svg>'''

fav_svg_path = os.path.join(ROOT, "assets", "favicons", "favicon.svg")
root_svg_path = os.path.join(ROOT, "favicon.svg")

with open(fav_svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)
with open(root_svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Generated vector circular SVG favicons successfully!")
