import re

# Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("whyHeroDesc: 'Đồng hành cùng Remeli để biến lượng thức ăn dư thừa cuối ngày thành nguồn doanh thu mới và thu hút thêm lượng lớn khách hàng tiềm năng.',", "whyHeroDesc: 'Đồng hành cùng Remeli để biến lượng thức ăn dư thừa cuối ngày<br/>thành nguồn doanh thu mới và thu hút thêm lượng lớn khách hàng tiềm năng.',")

content = content.replace("whyHeroDesc: 'Join Remeli to turn end-of-day surplus food into new revenue and attract potential customers.',", "whyHeroDesc: 'Join Remeli to turn end-of-day surplus food<br/>into new revenue and attract potential customers.',")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Update vi-sao-gia-nhap.html
with open('vi-sao-gia-nhap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Increase max-width to allow the full sentence to stretch out before wrapping, then add <br/>
content = content.replace('max-width: 700px;', 'max-width: 900px;')
content = content.replace('dư thừa cuối ngày thành nguồn', 'dư thừa cuối ngày<br/>thành nguồn')

with open('vi-sao-gia-nhap.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed to 2 lines.")
