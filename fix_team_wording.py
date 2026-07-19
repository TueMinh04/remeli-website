import re

# Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("megaOurTeam: 'Nhóm chúng tôi'", "megaOurTeam: 'Đội ngũ'")
content = content.replace("megaOurTeam: 'Nhóm chúng tôi',", "megaOurTeam: 'Đội ngũ',")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Update our-team.html
with open('our-team.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Nhóm\n          chúng tôi', 'Đội ngũ')
content = content.replace('Nhóm chúng tôi', 'Đội ngũ')
content = content.replace('Nhóm\n            chúng tôi', 'Đội ngũ')
content = re.sub(r'Nhóm\s+chúng\s+tôi', 'Đội ngũ', content)

with open('our-team.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done fixing wording.")
