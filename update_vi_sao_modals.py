import re

# Read index.html to extract modals
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract from <div class="modal" id="merchantModal" to </iframe>
start_str = '<div class="modal" id="merchantModal" aria-hidden="true">'
end_str = '</iframe>'
start_idx = index_content.find(start_str)
end_idx = index_content.find(end_str, start_idx) + len(end_str)
modals_html = index_content[start_idx:end_idx]

# Read vi-sao-gia-nhap.html
with open('vi-sao-gia-nhap.html', 'r', encoding='utf-8') as f:
    vi_sao_content = f.read()

# 1. Remove the header button
btn_header_str = '<a href="#dang-ki" class="btn btn-yellow" style="font-size: 1.2rem; padding: 20px 48px; border-radius: 999px;"><span data-i18n="whyHeroBtn">Đăng ký đối tác ngay</span></a>'
# Let's use regex in case of slight whitespace variations
vi_sao_content = re.sub(r'<a href="#dang-ki".*?>\s*<span data-i18n="whyHeroBtn">.*?</span>\s*</a>', '', vi_sao_content, flags=re.DOTALL)

# 2. Change CTA button from <a> to <button data-open-modal>
cta_btn_old = '<a href="dang-ki-doanh-nghiep.html" class="btn btn-yellow" style="font-size: 1.3rem; padding: 24px 56px; border-radius: 999px; position: relative; z-index: 2;" data-i18n="whyCtaBtn">Đăng ký cửa hàng ngay</a>'
cta_btn_new = '<button type="button" class="btn btn-yellow" style="font-size: 1.3rem; padding: 24px 56px; border-radius: 999px; position: relative; z-index: 2; border: none; cursor: pointer; font-family: inherit; font-weight: 700;" data-open-modal="merchantModal" data-i18n="whyCtaBtn">Đăng ký cửa hàng ngay</button>'
vi_sao_content = vi_sao_content.replace(cta_btn_old, cta_btn_new)

# 3. Inject modals before </body>
# But ensure we don't inject multiple times
if start_str not in vi_sao_content:
    vi_sao_content = vi_sao_content.replace('</body>', modals_html + '\n</body>')

with open('vi-sao-gia-nhap.html', 'w', encoding='utf-8') as f:
    f.write(vi_sao_content)

print("Updated vi-sao-gia-nhap.html with modals and button changes.")
