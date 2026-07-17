import os
import glob

# The old string
old_str = '<a href="doanh-nghiep.html" data-i18n="navMerchant">Doanh nghiệp</a>'

# The new string
new_str = '''<div class="nav-item-with-dropdown">
        <a href="doanh-nghiep.html" data-i18n="navMerchant">Doanh nghiệp</a>
        <div class="mega-menu">
          <div class="mega-menu-column">
            <h4>Dành cho Doanh nghiệp</h4>
            <a href="doanh-nghiep.html#vi-sao-gia-nhap">Vì sao gia nhập Remeli</a>
            <a href="doanh-nghiep.html#dang-ki">Đăng ký doanh nghiệp</a>
          </div>
        </div>
      </div>'''

# Find all html files
files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")

