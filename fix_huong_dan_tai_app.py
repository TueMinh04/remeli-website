import re

with open('huong-dan-tai-app.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('<span class="eyebrow eyebrow-yellow" style="margin: 0 auto 16px;">Tải ứng dụng</span>', '<span class="eyebrow eyebrow-yellow" style="margin: 0 auto 16px;" data-i18n="appDownloadApp">Tải ứng dụng</span>'),
    ('<span>Bắt đầu với</span><span>Remeli</span>', '<span data-i18n="appGetStarted">Bắt đầu với</span><span data-i18n="appRemeli">Remeli</span>'),
    ('<p style="margin: 24px auto; max-width: 800px; font-size: 1.05rem; opacity: 0.9;">Khám phá các phần ăn ngon cuối\n        ngày từ các nhà hàng xung quanh bạn.<br />Tải ứng dụng trên App Store hoặc Google Play ngay hôm nay!</p>', '<p style="margin: 24px auto; max-width: 800px; font-size: 1.05rem; opacity: 0.9;" data-i18n="appHeroDesc">Khám phá các phần ăn ngon cuối\n        ngày từ các nhà hàng xung quanh bạn.<br />Tải ứng dụng trên App Store hoặc Google Play ngay hôm nay!</p>'),
    ('<span class="eyebrow"\n        style="color: var(--green-800); background: var(--white); box-shadow: 0 8px 24px rgba(16, 60, 41, 0.06);">Trải\n        nghiệm mượt mà</span>', '<span class="eyebrow"\n        style="color: var(--green-800); background: var(--white); box-shadow: 0 8px 24px rgba(16, 60, 41, 0.06);" data-i18n="appSmooth">Trải\n        nghiệm mượt mà</span>'),
    ('<h2 style="color: var(--green-900); margin-top: 24px;">Dễ dàng sử dụng mỗi ngày</h2>', '<h2 style="color: var(--green-900); margin-top: 24px;" data-i18n="appEasyDaily">Dễ dàng sử dụng mỗi ngày</h2>'),
    ('<p style="color: var(--green-800); max-width: 600px; margin: 20px auto 0; font-size: 1.15rem; line-height: 1.6;">\n        Chỉ với vài thao tác cơ bản trên ứng dụng, bạn đã có thể tận hưởng món ngon với mức giá siêu hời.</p>', '<p style="color: var(--green-800); max-width: 600px; margin: 20px auto 0; font-size: 1.15rem; line-height: 1.6;" data-i18n="appEasyDesc">\n        Chỉ với vài thao tác cơ bản trên ứng dụng, bạn đã có thể tận hưởng món ngon với mức giá siêu hời.</p>'),
    ('<span class="eyebrow" style="color: var(--green-700); background: var(--green-100);">Bước 01</span>', '<span class="eyebrow" style="color: var(--green-700); background: var(--green-100);" data-i18n="appStep1">Bước 01</span>'),
    ('<h2 class="split-title" style="color: var(--text);"><span>Tìm & Chọn</span><span>món ăn</span></h2>', '<h2 class="split-title" style="color: var(--text);"><span data-i18n="appFindSelect">Tìm & Chọn</span><span data-i18n="appFood">món ăn</span></h2>'),
    ('<p class="balanced-two-line" style="color: var(--muted);">Mở ứng dụng, khám phá các cửa hàng xung quanh và chọn\n          gói món ăn bạn yêu thích với mức giá siêu hời.</p>', '<p class="balanced-two-line" style="color: var(--muted);" data-i18n="appStep1Desc2">Mở ứng dụng, khám phá các cửa hàng xung quanh và chọn\n          gói món ăn bạn yêu thích với mức giá siêu hời.</p>'),
    ('<span class="eyebrow" style="color: var(--green-700); background: var(--green-100);">Bước 02</span>', '<span class="eyebrow" style="color: var(--green-700); background: var(--green-100);" data-i18n="appStep2">Bước 02</span>'),
    ('<h2 class="split-title" style="color: var(--text);"><span>Đặt chỗ &</span><span>Thanh toán</span></h2>', '<h2 class="split-title" style="color: var(--text);"><span data-i18n="appReserve">Đặt chỗ &</span><span data-i18n="appPay">Thanh toán</span></h2>'),
    ('<p class="balanced-two-line" style="color: var(--muted);">Thanh toán và giữ chỗ trước qua ứng dụng để đảm bảo\n          phần ăn của bạn luôn sẵn sàng.</p>', '<p class="balanced-two-line" style="color: var(--muted);" data-i18n="appStep2Desc2">Thanh toán và giữ chỗ trước qua ứng dụng để đảm bảo\n          phần ăn của bạn luôn sẵn sàng.</p>'),
    ('<span class="eyebrow" style="color: var(--green-700); background: var(--green-100);">Bước 03</span>', '<span class="eyebrow" style="color: var(--green-700); background: var(--green-100);" data-i18n="appStep3">Bước 03</span>'),
    ('<h2 class="split-title" style="color: var(--text);"><span>Đến lấy</span><span>(Pick up)</span></h2>', '<h2 class="split-title" style="color: var(--text);"><span data-i18n="appArrive">Đến lấy</span><span data-i18n="appPickup">(Pick up)</span></h2>'),
    ('<p class="balanced-two-line" style="color: var(--muted);">Đến trực tiếp cửa hàng theo đúng khung giờ quy định để\n          nhận món ăn nóng hổi một cách dễ dàng.</p>', '<p class="balanced-two-line" style="color: var(--muted);" data-i18n="appStep3Desc2">Đến trực tiếp cửa hàng theo đúng khung giờ quy định để\n          nhận món ăn nóng hổi một cách dễ dàng.</p>'),
    ('>[Hình ảnh minh hoạ 1]<', ' data-i18n="appImg1">[Hình ảnh minh hoạ 1]<'),
    ('>[Hình ảnh minh hoạ 2]<', ' data-i18n="appImg2">[Hình ảnh minh hoạ 2]<'),
    ('>[Hình ảnh minh hoạ 3]<', ' data-i18n="appImg3">[Hình ảnh minh hoạ 3]<')
]

for old, new in replacements:
    content = content.replace(old, new)

with open('huong-dan-tai-app.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# I will append new strings for huong-dan-tai-app.html to script.js right after appRemeli in both vi and en objects
vi_new = """
    appEasyDaily: 'Dễ dàng sử dụng mỗi ngày',
    appEasyDesc: 'Chỉ với vài thao tác cơ bản trên ứng dụng, bạn đã có thể tận hưởng món ngon với mức giá siêu hời.',
    appStep1: 'Bước 01',
    appFindSelect: 'Tìm & Chọn',
    appFood: 'món ăn',
    appStep1Desc2: 'Mở ứng dụng, khám phá các cửa hàng xung quanh và chọn gói món ăn bạn yêu thích với mức giá siêu hời.',
    appStep2: 'Bước 02',
    appReserve: 'Đặt chỗ &',
    appPay: 'Thanh toán',
    appStep2Desc2: 'Thanh toán và giữ chỗ trước qua ứng dụng để đảm bảo phần ăn của bạn luôn sẵn sàng.',
    appStep3: 'Bước 03',
    appArrive: 'Đến lấy',
    appPickup: '(Pick up)',
    appStep3Desc2: 'Đến trực tiếp cửa hàng theo đúng khung giờ quy định để nhận món ăn nóng hổi một cách dễ dàng.',
    appImg1: '[Hình ảnh minh hoạ 1]',
    appImg2: '[Hình ảnh minh hoạ 2]',
    appImg3: '[Hình ảnh minh hoạ 3]',
"""

en_new = """
    appEasyDaily: 'Easy to use every day',
    appEasyDesc: 'With just a few basic steps on the app, you can enjoy delicious food at great prices.',
    appStep1: 'Step 01',
    appFindSelect: 'Find & Select',
    appFood: 'your food',
    appStep1Desc2: 'Open the app, discover nearby stores, and choose your favorite food at a discounted price.',
    appStep2: 'Step 02',
    appReserve: 'Reserve &',
    appPay: 'Pay',
    appStep2Desc2: 'Pay and reserve in advance through the app to ensure your meal is always ready.',
    appStep3: 'Step 03',
    appArrive: 'Arrive',
    appPickup: '(Pick up)',
    appStep3Desc2: 'Go directly to the store during the designated time window to pick up your hot food easily.',
    appImg1: '[Illustration 1]',
    appImg2: '[Illustration 2]',
    appImg3: '[Illustration 3]',
"""

js_content = js_content.replace("    appRemeli: 'Remeli',\n", "    appRemeli: 'Remeli',\n" + vi_new, 1)
js_content = js_content.replace("    appRemeli: 'Remeli',\n", "    appRemeli: 'Remeli',\n" + en_new)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
