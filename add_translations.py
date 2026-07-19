import re

def update_script():
    with open('script.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    vi_insert = """
    // Nav & Footer
    megaForBusiness: 'Dành cho Doanh nghiệp',
    megaWhyJoin: 'Vì sao gia nhập Remeli',
    megaRegisterBusiness: 'Đăng ký doanh nghiệp',
    footerMerchantSection: 'Doanh nghiệp',
    footerWhyJoin: 'Vì sao gia nhập Remeli',
    footerRegisterBusiness: 'Đăng ký doanh nghiệp',

    // Vì sao gia nhập
    whyHeroEyebrow: 'Dành cho đối tác',
    whyHeroTitle: 'Mở rộng kinh doanh,<br/><span style="color: var(--yellow);">Giảm thiểu lãng phí</span>',
    whyHeroDesc: 'Đồng hành cùng Remeli để biến lượng thức ăn dư thừa cuối ngày thành nguồn doanh thu mới và thu hút thêm lượng lớn khách hàng tiềm năng.',
    whyHeroBtn: 'Đăng ký đối tác ngay',
    whyBenefitEyebrow: 'Lợi ích thiết thực',
    whyBenefitTitle: 'Vì sao gia nhập Remeli?',
    whyBen1Title: 'Giảm thiểu lãng phí',
    whyBen1Desc: 'Không còn nỗi đau phải bỏ đi những mẻ bánh ngon hay nồi canh tâm huyết. Remeli giúp bạn tối ưu hoá 100% nguyên liệu sản xuất mỗi ngày.',
    whyBen2Title: 'Thêm nguồn thu nhập',
    whyBen2Desc: 'Biến thức ăn thừa thành tiền. Những sản phẩm từng bị lãng quên giờ đây sẽ mang lại doanh thu gia tăng cho cửa hàng của bạn một cách dễ dàng.',
    whyBen3Title: 'Khách hàng tiềm năng',
    whyBen3Desc: 'Tiếp cận hàng ngàn người dùng trẻ tuổi, yêu môi trường qua app. Họ đến nhận món và hoàn toàn có thể trở thành khách hàng trung thành của quán.',
    whyOpEyebrow: 'Vận hành đơn giản',
    whyOpTitle: 'Chỉ với 3 bước mỗi ngày',
    whyStep1Title: 'Đóng gói & Cập nhật',
    whyStep1Desc: 'Vào cuối ca làm, bạn gom thức ăn dư vào túi mù (Surprise Bag) và lên app cập nhật số lượng có sẵn chỉ trong 5 giây.',
    whyStep2Title: 'Khách đặt qua App',
    whyStep2Desc: 'Người dùng trong khu vực sẽ nhận được thông báo, tiến hành thanh toán giữ chỗ trực tiếp trên ứng dụng Remeli.',
    whyStep3Title: 'Giao món tận tay',
    whyStep3Desc: 'Khách ghé tiệm theo khung giờ quy định, bạn chỉ cần quét mã QR xác nhận và giao túi thức ăn. Tiền sẽ tự động cộng vào ví!',
    whyMetric1: 'Phí khởi tạo ban đầu',
    whyMetric2: 'Doanh thu ước tính tăng thêm',
    whyMetric3Value: 'Hỗ trợ',
    whyMetric3: 'Marketing độc quyền 0đ',
    whyCtaTitle: 'Bắt đầu hành trình<br/>chống lãng phí cùng Remeli',
    whyCtaDesc: 'Tham gia hoàn toàn miễn phí. Hàng ngàn khách hàng đang chờ để "giải cứu" những món ngon của bạn mỗi ngày.',
    whyCtaBtn: 'Đăng ký cửa hàng ngay',

    // Đăng ký doanh nghiệp
    regHeroEyebrow: 'Đăng ký doanh nghiệp',
    regHeroTitle: 'Trở thành đối tác<br/><span style="color: var(--yellow);">cùng Remeli</span>',
    regHeroDesc: 'Hãy để lại thông tin, chúng tôi sẽ giúp bạn biến thức ăn cuối ngày thành nguồn doanh thu mới ngay hôm nay.',
    regFormTitle: 'Đăng ký cửa hàng',
    regFormDesc: 'Để lại thông tin, đội ngũ Remeli sẽ liên hệ hỗ trợ bạn thiết lập gian hàng chỉ trong vòng 24 giờ. Hoàn toàn miễn phí đăng ký!',
    regFormName: 'Tên cửa hàng *',
    regFormNamePlace: 'Nhập tên quán ăn, nhà hàng, tiệm bánh...',
    regFormPhone: 'Số điện thoại *',
    regFormPhonePlace: 'Nhập số điện thoại liên hệ...',
    regFormArea: 'Khu vực (Thành phố/Quận) *',
    regFormAreaPlace: 'Ví dụ: Quận 1, TP.HCM...',
    regFormSubmit: 'Gửi thông tin đăng ký',
"""
    
    en_insert = """
    // Nav & Footer
    megaForBusiness: 'For Business',
    megaWhyJoin: 'Why join Remeli',
    megaRegisterBusiness: 'Register business',
    footerMerchantSection: 'Business',
    footerWhyJoin: 'Why join Remeli',
    footerRegisterBusiness: 'Register business',

    // Vì sao gia nhập
    whyHeroEyebrow: 'For Partners',
    whyHeroTitle: 'Grow your business,<br/><span style="color: var(--yellow);">Reduce waste</span>',
    whyHeroDesc: 'Join Remeli to turn end-of-day surplus food into new revenue and attract potential customers.',
    whyHeroBtn: 'Register as a partner',
    whyBenefitEyebrow: 'Practical Benefits',
    whyBenefitTitle: 'Why join Remeli?',
    whyBen1Title: 'Reduce waste',
    whyBen1Desc: 'No more pain of throwing away good food. Remeli helps you optimize 100% of your daily ingredients.',
    whyBen2Title: 'Extra revenue',
    whyBen2Desc: 'Turn surplus food into cash. Forgotten products will now easily generate extra revenue for your store.',
    whyBen3Title: 'Potential customers',
    whyBen3Desc: 'Reach thousands of young, eco-conscious users. They pick up food and can easily become loyal customers.',
    whyOpEyebrow: 'Simple Operation',
    whyOpTitle: 'Just 3 steps a day',
    whyStep1Title: 'Pack & Update',
    whyStep1Desc: 'At the end of your shift, pack surplus food into Surprise Bags and update the quantity on the app in 5 seconds.',
    whyStep2Title: 'Order via App',
    whyStep2Desc: 'Nearby users get notified, reserve, and pay directly on the Remeli app.',
    whyStep3Title: 'Hand over',
    whyStep3Desc: 'Customers visit during the pickup window. Just scan the QR code and hand over the bag. Money goes straight to your wallet!',
    whyMetric1: 'Initial setup fee',
    whyMetric2: 'Estimated revenue increase',
    whyMetric3Value: 'Support',
    whyMetric3: 'Exclusive marketing 0đ',
    whyCtaTitle: 'Start your zero-waste journey<br/>with Remeli',
    whyCtaDesc: 'Join for free. Thousands of customers are waiting to "rescue" your good food every day.',
    whyCtaBtn: 'Register store now',

    // Đăng ký doanh nghiệp
    regHeroEyebrow: 'Register Business',
    regHeroTitle: 'Become a partner<br/><span style="color: var(--yellow);">with Remeli</span>',
    regHeroDesc: 'Leave your information, we will help you turn end-of-day food into new revenue today.',
    regFormTitle: 'Register Store',
    regFormDesc: 'Leave your details, Remeli team will contact you to set up your store within 24 hours. 100% free!',
    regFormName: 'Store Name *',
    regFormNamePlace: 'e.g., Cafe, Restaurant, Bakery...',
    regFormPhone: 'Phone Number *',
    regFormPhonePlace: 'Enter contact phone number...',
    regFormArea: 'Area (City/District) *',
    regFormAreaPlace: 'e.g., District 1, HCMC...',
    regFormSubmit: 'Submit Registration',
"""
    
    # Insert at end of vi
    content = content.replace("    roleOther: 'Khác',\n", "    roleOther: 'Khác',\n" + vi_insert)
    # Insert at end of en
    content = content.replace("    roleOther: 'Other',\n", "    roleOther: 'Other',\n" + en_insert)
    
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(content)

update_script()
