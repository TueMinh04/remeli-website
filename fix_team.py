import re

with open('our-team.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('>Đội ngũ<', ' data-i18n="teamEyebrow2">Đội ngũ<')

with open('our-team.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("    teamFounders: 'Những nhà sáng lập',\n", "    teamFounders: 'Những nhà sáng lập',\n    teamEyebrow2: 'Đội ngũ',\n")
content = content.replace("    teamFounders: 'The Founders',\n", "    teamFounders: 'The Founders',\n    teamEyebrow2: 'The Team',\n")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)
