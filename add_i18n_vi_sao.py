import re

with open('vi-sao-gia-nhap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Hero
content = content.replace('class="eyebrow eyebrow-yellow"', 'class="eyebrow eyebrow-yellow" data-i18n="whyHeroEyebrow"')
content = content.replace('Mở rộng kinh doanh,<br/><span style="color: var(--yellow);">Giảm thiểu lãng phí</span>', '<span data-i18n="whyHeroTitle">Mở rộng kinh doanh,<br/><span style="color: var(--yellow);">Giảm thiểu lãng phí</span></span>')
content = content.replace('Đồng hành cùng Remeli để biến lượng thức ăn dư thừa cuối ngày thành nguồn doanh thu mới và thu hút thêm lượng lớn khách hàng tiềm năng.', '<span data-i18n="whyHeroDesc">Đồng hành cùng Remeli để biến lượng thức ăn dư thừa cuối ngày thành nguồn doanh thu mới và thu hút thêm lượng lớn khách hàng tiềm năng.</span>')
content = content.replace('Đăng ký đối tác ngay', '<span data-i18n="whyHeroBtn">Đăng ký đối tác ngay</span>')

# Benefits
content = content.replace('Lợi ích thiết thực', '<span data-i18n="whyBenefitEyebrow">Lợi ích thiết thực</span>')
content = content.replace('Vì sao gia nhập Remeli?', '<span data-i18n="whyBenefitTitle">Vì sao gia nhập Remeli?</span>')

content = content.replace('>Giảm thiểu lãng phí<', ' data-i18n="whyBen1Title">Giảm thiểu lãng phí<')
content = content.replace('>Không còn nỗi đau phải bỏ đi những mẻ bánh ngon hay nồi canh tâm huyết. Remeli giúp bạn tối ưu hoá 100% nguyên liệu sản xuất mỗi ngày.<', ' data-i18n="whyBen1Desc">Không còn nỗi đau phải bỏ đi những mẻ bánh ngon hay nồi canh tâm huyết. Remeli giúp bạn tối ưu hoá 100% nguyên liệu sản xuất mỗi ngày.<')

content = content.replace('>Thêm nguồn thu nhập<', ' data-i18n="whyBen2Title">Thêm nguồn thu nhập<')
content = content.replace('>Biến thức ăn thừa thành tiền. Những sản phẩm từng bị lãng quên giờ đây sẽ mang lại doanh thu gia tăng cho cửa hàng của bạn một cách dễ dàng.<', ' data-i18n="whyBen2Desc">Biến thức ăn thừa thành tiền. Những sản phẩm từng bị lãng quên giờ đây sẽ mang lại doanh thu gia tăng cho cửa hàng của bạn một cách dễ dàng.<')

content = content.replace('>Khách hàng tiềm năng<', ' data-i18n="whyBen3Title">Khách hàng tiềm năng<')
content = content.replace('>Tiếp cận hàng ngàn người dùng trẻ tuổi, yêu môi trường qua app. Họ đến nhận món và hoàn toàn có thể trở thành khách hàng trung thành của quán.<', ' data-i18n="whyBen3Desc">Tiếp cận hàng ngàn người dùng trẻ tuổi, yêu môi trường qua app. Họ đến nhận món và hoàn toàn có thể trở thành khách hàng trung thành của quán.<')

# Operation
content = content.replace('>Vận hành đơn giản<', ' data-i18n="whyOpEyebrow">Vận hành đơn giản<')
content = content.replace('>Chỉ với 3 bước mỗi ngày<', ' data-i18n="whyOpTitle">Chỉ với 3 bước mỗi ngày<')

content = content.replace('>Đóng gói & Cập nhật<', ' data-i18n="whyStep1Title">Đóng gói & Cập nhật<')
content = content.replace('>Vào cuối ca làm, bạn gom thức ăn dư vào túi mù (Surprise Bag) và lên app cập nhật số lượng có sẵn chỉ trong 5 giây.<', ' data-i18n="whyStep1Desc">Vào cuối ca làm, bạn gom thức ăn dư vào túi mù (Surprise Bag) và lên app cập nhật số lượng có sẵn chỉ trong 5 giây.<')

content = content.replace('>Khách đặt qua App<', ' data-i18n="whyStep2Title">Khách đặt qua App<')
content = content.replace('>Người dùng trong khu vực sẽ nhận được thông báo, tiến hành thanh toán giữ chỗ trực tiếp trên ứng dụng Remeli.<', ' data-i18n="whyStep2Desc">Người dùng trong khu vực sẽ nhận được thông báo, tiến hành thanh toán giữ chỗ trực tiếp trên ứng dụng Remeli.<')

content = content.replace('>Giao món tận tay<', ' data-i18n="whyStep3Title">Giao món tận tay<')
content = content.replace('>Khách ghé tiệm theo khung giờ quy định, bạn chỉ cần quét mã QR xác nhận và giao túi thức ăn. Tiền sẽ tự động cộng vào ví!<', ' data-i18n="whyStep3Desc">Khách ghé tiệm theo khung giờ quy định, bạn chỉ cần quét mã QR xác nhận và giao túi thức ăn. Tiền sẽ tự động cộng vào ví!<')

# Metrics
content = content.replace('>Phí khởi tạo ban đầu<', ' data-i18n="whyMetric1">Phí khởi tạo ban đầu<')
content = content.replace('>Doanh thu ước tính tăng thêm<', ' data-i18n="whyMetric2">Doanh thu ước tính tăng thêm<')
content = content.replace('>Hỗ trợ<', ' data-i18n="whyMetric3Value">Hỗ trợ<')
content = content.replace('>Marketing độc quyền 0đ<', ' data-i18n="whyMetric3">Marketing độc quyền 0đ<')

# CTA
content = content.replace('Bắt đầu hành trình<br/>chống lãng phí cùng Remeli', '<span data-i18n="whyCtaTitle">Bắt đầu hành trình<br/>chống lãng phí cùng Remeli</span>')
content = content.replace('>Tham gia hoàn toàn miễn phí. Hàng ngàn khách hàng đang chờ để "giải cứu" những món ngon của bạn mỗi ngày.<', ' data-i18n="whyCtaDesc">Tham gia hoàn toàn miễn phí. Hàng ngàn khách hàng đang chờ để "giải cứu" những món ngon của bạn mỗi ngày.<')
content = content.replace('>Đăng ký cửa hàng ngay<', ' data-i18n="whyCtaBtn">Đăng ký cửa hàng ngay<')

with open('vi-sao-gia-nhap.html', 'w', encoding='utf-8') as f:
    f.write(content)


with open('dang-ki-doanh-nghiep.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('class="eyebrow eyebrow-yellow"', 'class="eyebrow eyebrow-yellow" data-i18n="regHeroEyebrow"')
content = content.replace('Trở thành đối tác<br/><span style="color: var(--yellow);">cùng Remeli</span>', '<span data-i18n="regHeroTitle">Trở thành đối tác<br/><span style="color: var(--yellow);">cùng Remeli</span></span>')
content = content.replace('Hãy để lại thông tin, chúng tôi sẽ giúp bạn biến thức ăn cuối ngày thành nguồn doanh thu mới ngay hôm nay.', '<span data-i18n="regHeroDesc">Hãy để lại thông tin, chúng tôi sẽ giúp bạn biến thức ăn cuối ngày thành nguồn doanh thu mới ngay hôm nay.</span>')
content = content.replace('Đăng ký cửa hàng</h2>', 'Đăng ký cửa hàng</h2>'.replace('Đăng ký cửa hàng', '<span data-i18n="regFormTitle">Đăng ký cửa hàng</span>'))
content = content.replace('>Để lại thông tin, đội ngũ Remeli sẽ liên hệ hỗ trợ bạn thiết lập gian hàng chỉ trong vòng 24 giờ. Hoàn toàn miễn phí đăng ký!<', ' data-i18n="regFormDesc">Để lại thông tin, đội ngũ Remeli sẽ liên hệ hỗ trợ bạn thiết lập gian hàng chỉ trong vòng 24 giờ. Hoàn toàn miễn phí đăng ký!<')
content = content.replace('>Tên cửa hàng *<', ' data-i18n="regFormName">Tên cửa hàng *<')
content = content.replace('placeholder="Nhập tên quán ăn, nhà hàng, tiệm bánh..."', 'placeholder="Nhập tên quán ăn, nhà hàng, tiệm bánh..." data-i18n-placeholder="regFormNamePlace"')
content = content.replace('>Số điện thoại *<', ' data-i18n="regFormPhone">Số điện thoại *<')
content = content.replace('placeholder="Nhập số điện thoại liên hệ..."', 'placeholder="Nhập số điện thoại liên hệ..." data-i18n-placeholder="regFormPhonePlace"')
content = content.replace('>Khu vực (Thành phố/Quận) *<', ' data-i18n="regFormArea">Khu vực (Thành phố/Quận) *<')
content = content.replace('placeholder="Ví dụ: Quận 1, TP.HCM..."', 'placeholder="Ví dụ: Quận 1, TP.HCM..." data-i18n-placeholder="regFormAreaPlace"')
content = content.replace('>Gửi thông tin đăng ký<', ' data-i18n="regFormSubmit">Gửi thông tin đăng ký<')

with open('dang-ki-doanh-nghiep.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating vi-sao-gia-nhap.html and dang-ki-doanh-nghiep.html")
