import re
import os

base_dir = "/Users/minhvuong/Downloads/remeli-website-1 copy"
faq_file = os.path.join(base_dir, "faq.html")

with open(faq_file, "r") as f:
    content = f.read()

# Split into header, body, footer
header_match = re.search(r'(<header.*?</header>)', content, re.DOTALL)
header = header_match.group(1)

# Modify header to remove class="active" from main nav
header = header.replace('class="active"', '')

footer_match = re.search(r'(<footer.*</footer>.*?</body>)', content, re.DOTALL)
footer = footer_match.group(1)

pages = [
    ("cua-hang.html", "Cửa hàng", "Dành cho chủ cửa hàng"),
    ("huong-dan-tai-app.html", "Hướng dẫn tải App", "App"),
    ("lam-sao-de-pick-up.html", "Làm sao để pick up", "App"),
    ("about-remeli.html", "About Remeli", "About us"),
    ("our-team.html", "Our team", "About us"),
    ("tac-dong.html", "Tác động", "Community"),
    ("phan-hoi-khach-hang.html", "Phản hồi khách hàng", "Community")
]

for filename, title, eyebrow in pages:
    page_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Remeli giúp bạn tìm món ngon còn lại trong ngày từ cửa hàng địa phương tại Việt Nam, đặt trước dễ dàng và nhận tại cửa hàng." />
  <title>Remeli | {title}</title>
  <link rel="icon" type="image/png" href="assets/favicon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css" />
</head>
<body class="faq-page">
  <svg style="display: none;">
    <defs>
      <linearGradient id="googlePlayGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00a1ff" />
        <stop offset="30%" stop-color="#00e765" />
        <stop offset="70%" stop-color="#ffb300" />
        <stop offset="100%" stop-color="#ff3a44" />
      </linearGradient>
    </defs>
  </svg>

  {header}

  <section class="faq-section" id="content">
    <div class="faq-header reveal">
      <span class="eyebrow eyebrow-yellow">{eyebrow}</span>
      <h2>{title}</h2>
    </div>

    <div class="faq-list reveal" style="text-align: center; padding: 60px 0; background: var(--white); border-radius: 18px; border: 1px solid var(--line); box-shadow: 0 14px 42px rgba(16, 60, 41, 0.06);">
      <p style="color: var(--muted); font-size: 1.1rem; margin: 0;">Nội dung đang được cập nhật. Vui lòng quay lại sau!</p>
    </div>
  </section>

  {footer}
</html>
"""
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "w") as f:
        f.write(page_content)

print("Pages created successfully.")
