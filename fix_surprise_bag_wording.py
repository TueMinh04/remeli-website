# Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Vietnamese replacement
old_vi = "whyStep1Desc: 'Vào cuối ca làm, bạn gom thức ăn dư vào túi mù (Surprise Bag) và lên app cập nhật số lượng có sẵn chỉ trong 5 giây.',"
new_vi = "whyStep1Desc: 'Vào cuối ca làm, bạn chụp ảnh các phần ăn còn dư (hoặc gom vào Túi mù - Surprise Bag) và lên app cập nhật số lượng chỉ trong 5 giây.',"
content = content.replace(old_vi, new_vi)

# English replacement
old_en = "whyStep1Desc: 'At the end of your shift, pack surplus food into Surprise Bags and update the quantity on the app in 5 seconds.',"
new_en = "whyStep1Desc: 'At the end of your shift, simply snap a photo of surplus food (or create a Surprise Bag) and update the quantity on the app in 5 seconds.',"
content = content.replace(old_en, new_en)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Update vi-sao-gia-nhap.html
with open('vi-sao-gia-nhap.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_html = 'Vào cuối ca làm, bạn gom thức ăn dư vào túi mù (Surprise Bag) và lên app cập nhật số lượng có sẵn chỉ trong 5 giây.'
new_html = 'Vào cuối ca làm, bạn chụp ảnh các phần ăn còn dư (hoặc gom vào Túi mù - Surprise Bag) và lên app cập nhật số lượng chỉ trong 5 giây.'
content = content.replace(old_html, new_html)

with open('vi-sao-gia-nhap.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Surprise Bag wording.")
