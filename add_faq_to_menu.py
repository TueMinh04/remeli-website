import glob

old_str = '<a href="phan-hoi-khach-hang.html" data-i18n="megaCustomerFeedback">Phản hồi khách hàng</a>'
new_str = '<a href="phan-hoi-khach-hang.html" data-i18n="megaCustomerFeedback">Phản hồi khách hàng</a>\n            <a href="faq.html" data-i18n="navFaq">FAQ</a>'

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

print("Added FAQ to Mega Menu across all HTML files.")
