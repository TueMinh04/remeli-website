import os
import glob
import re

replacement = """        <h3 data-i18n="footerExplore">Khám phá</h3>
        <a href="index.html#home" data-i18n="navHome">Trang chủ</a>
        <a href="index.html#how-it-works" data-i18n="navHow">Cách hoạt động</a>
        <a href="index.html#impact" data-i18n="navImpact">Tác động</a>
        <a href="index.html#community" data-i18n="navCommunity">Cộng đồng</a>
        <a href="faq.html" data-i18n="navFaq">FAQ</a>
        
        <h4 style="margin-top: 20px; margin-bottom: 8px; color: var(--green-900); font-weight: 700; font-size: 1rem;">Doanh nghiệp</h4>
        <a href="vi-sao-gia-nhap.html">Vì sao gia nhập Remeli</a>
        <a href="dang-ki-doanh-nghiep.html">Đăng ký gian hàng</a>"""

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace everything from <h3 data-i18n="footerExplore">Khám phá</h3>
    # to the </div> right before <div>\s*<h3 data-i18n="footerLegal">Pháp lý</h3>
    pattern = re.compile(r'<h3 data-i18n="footerExplore">Khám phá</h3>.*?</div>\s*<div>\s*<h3 data-i18n="footerLegal">Pháp lý</h3>', re.DOTALL)
    
    new_content = pattern.sub(replacement + '\n      </div>\n      <div>\n        <h3 data-i18n="footerLegal">Pháp lý</h3>', content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Fixed footer in {f}")
    else:
        print(f"Could not fix footer in {f}")
