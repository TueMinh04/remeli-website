import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# huong-dan-tai-app.html
app_replacements = [
    ('>Tải ứng dụng<', ' data-i18n="appDownloadApp">Tải ứng dụng<'),
    ('<span>Bắt đầu với</span><span>Remeli</span>', '<span data-i18n="appGetStarted">Bắt đầu với</span><span data-i18n="appRemeli">Remeli</span>'),
    ('>Khám phá các phần ăn ngon cuối\n        ngày từ các nhà hàng xung quanh bạn.<br />Tải ứng dụng trên App Store hoặc Google Play ngay hôm nay!<', ' data-i18n="appHeroDesc">Khám phá các phần ăn ngon cuối\n        ngày từ các nhà hàng xung quanh bạn.<br />Tải ứng dụng trên App Store hoặc Google Play ngay hôm nay!<'),
    ('>Trải\n        nghiệm mượt mà<', ' data-i18n="appSmooth">Trải\n        nghiệm mượt mà<'),
    ('<span>Chỉ 1 phút</span><span>để bắt đầu</span>', '<span data-i18n="appJustOneMin">Chỉ 1 phút</span><span data-i18n="appToStart">để bắt đầu</span>'),
    ('>Bạn không cần tạo tài khoản phức tạp. Đăng nhập bằng Apple, Google hoặc số điện thoại chỉ trong vài giây.<', ' data-i18n="appNoComplex">Bạn không cần tạo tài khoản phức tạp. Đăng nhập bằng Apple, Google hoặc số điện thoại chỉ trong vài giây.<'),
    ('>Tải ứng dụng<', ' data-i18n="appStep1Title">Tải ứng dụng<'),
    ('>Tìm Remeli trên kho ứng dụng App Store hoặc Google Play và cài đặt hoàn toàn miễn phí.<', ' data-i18n="appStep1Desc">Tìm Remeli trên kho ứng dụng App Store hoặc Google Play và cài đặt hoàn toàn miễn phí.<'),
    ('>Đăng nhập nhanh<', ' data-i18n="appStep2Title">Đăng nhập nhanh<'),
    ('>Sử dụng tài khoản Google, Apple hoặc số điện thoại để vào app ngay lập tức.<', ' data-i18n="appStep2Desc">Sử dụng tài khoản Google, Apple hoặc số điện thoại để vào app ngay lập tức.<'),
    ('>Khám phá<', ' data-i18n="appStep3Title">Khám phá<'),
    ('>Bật định vị để xem ngay các cửa hàng đang có phần ăn hấp dẫn xung quanh bạn.<', ' data-i18n="appStep3Desc">Bật định vị để xem ngay các cửa hàng đang có phần ăn hấp dẫn xung quanh bạn.<')
]
update_file('huong-dan-tai-app.html', app_replacements)

# lam-sao-de-pick-up.html
pickup_replacements = [
    ('>Hướng dẫn lấy món<', ' data-i18n="pickupGuide">Hướng dẫn lấy món<'),
    ('<span>Làm sao để</span><span>nhận món?</span>', '<span data-i18n="pickupHowTo">Làm sao để</span><span data-i18n="pickupReceive">nhận món?</span>'),
    ('>Đơn giản, nhanh chóng và thân thiện. Dưới đây là các bước để bạn lấy phần ăn đã đặt.<', ' data-i18n="pickupDesc">Đơn giản, nhanh chóng và thân thiện. Dưới đây là các bước để bạn lấy phần ăn đã đặt.<'),
    ('>Quy trình nhận món<', ' data-i18n="pickupProcess">Quy trình nhận món<'),
    ('<span>3 bước</span><span>tại cửa hàng</span>', '<span data-i18n="pickup3Steps">3 bước</span><span data-i18n="pickupAtStore">tại cửa hàng</span>'),
    ('>Tới đúng giờ<', ' data-i18n="pickupStep1Title">Tới đúng giờ<'),
    ('>Đến cửa hàng trong khung giờ nhận được thông báo trên ứng dụng.<', ' data-i18n="pickupStep1Desc">Đến cửa hàng trong khung giờ nhận được thông báo trên ứng dụng.<'),
    ('>Đưa mã cho nhân viên<', ' data-i18n="pickupStep2Title">Đưa mã cho nhân viên<'),
    ('>Mở app, đưa mã QR hoặc mã đơn hàng cho nhân viên cửa hàng xác nhận.<', ' data-i18n="pickupStep2Desc">Mở app, đưa mã QR hoặc mã đơn hàng cho nhân viên cửa hàng xác nhận.<'),
    ('>Nhận phần ăn<', ' data-i18n="pickupStep3Title">Nhận phần ăn<'),
    ('>Tận hưởng món ngon và tự hào vì bạn vừa giúp giảm lãng phí thực phẩm!<', ' data-i18n="pickupStep3Desc">Tận hưởng món ngon và tự hào vì bạn vừa giúp giảm lãng phí thực phẩm!<')
]
update_file('lam-sao-de-pick-up.html', pickup_replacements)

# about-remeli.html
about_replacements = [
    ('>Về chúng tôi<', ' data-i18n="aboutUs">Về chúng tôi<'),
    ('<span>Câu chuyện</span><span>Remeli</span>', '<span data-i18n="aboutStory">Câu chuyện</span><span data-i18n="aboutRemeli">Remeli</span>'),
    ('>Hành trình kết nối những bữa ăn ngon với sứ mệnh giảm thiểu lãng phí và bảo vệ môi trường Việt Nam.<', ' data-i18n="aboutHeroDesc">Hành trình kết nối những bữa ăn ngon với sứ mệnh giảm thiểu lãng phí và bảo vệ môi trường Việt Nam.<'),
    ('>Ý tưởng khởi nguồn<', ' data-i18n="aboutIdea">Ý tưởng khởi nguồn<'),
    ('>Cứu lấy thức ăn, bảo vệ Trái Đất<', ' data-i18n="aboutSaveFood">Cứu lấy thức ăn, bảo vệ Trái Đất<'),
    ('Tại Việt Nam, hàng tấn thức ăn hoàn toàn ngon lành bị lãng phí mỗi ngày chỉ vì chưa tìm được người dùng kịp thời. Remeli ra đời với một khát vọng đơn giản: tạo ra một nền tảng kết nối các cửa hàng thực phẩm với những người yêu ẩm thực, giúp <strong>cứu lấy những bữa ăn ngon</strong>, tiết kiệm chi phí, và quan trọng nhất là <strong>giảm thiểu lượng khí thải carbon</strong> gây hiệu ứng nhà kính từ rác thải thực phẩm.', '<span data-i18n="aboutVisionDesc">Tại Việt Nam, hàng tấn thức ăn hoàn toàn ngon lành bị lãng phí mỗi ngày chỉ vì chưa tìm được người dùng kịp thời. Remeli ra đời với một khát vọng đơn giản: tạo ra một nền tảng kết nối các cửa hàng thực phẩm với những người yêu ẩm thực, giúp <strong>cứu lấy những bữa ăn ngon</strong>, tiết kiệm chi phí, và quan trọng nhất là <strong>giảm thiểu lượng khí thải carbon</strong> gây hiệu ứng nhà kính từ rác thải thực phẩm.</span>'),
    ('<span>Vì sao Remeli</span><span>ra đời?</span>', '<span data-i18n="aboutWhyRemeli">Vì sao Remeli</span><span data-i18n="aboutBorn">ra đời?</span>'),
    ('>Bảo vệ Môi trường<', ' data-i18n="aboutProtectEnv">Bảo vệ Môi trường<'),
    ('>Mỗi phần ăn được cứu khỏi thùng rác đồng nghĩa với việc giảm thiểu lượng khí thải methane. Cùng nhau, chúng ta đang làm xanh lại bầu không khí của Việt Nam.<', ' data-i18n="aboutProtectEnvDesc">Mỗi phần ăn được cứu khỏi thùng rác đồng nghĩa với việc giảm thiểu lượng khí thải methane. Cùng nhau, chúng ta đang làm xanh lại bầu không khí của Việt Nam.<'),
    ('>Chống Lãng phí<', ' data-i18n="aboutFightWaste">Chống Lãng phí<'),
    ('>Chúng tôi tin rằng thức ăn ngon được tạo ra là để thưởng thức. Remeli giúp các nhà hàng tối ưu hoá nguồn nguyên liệu và không để phí phạm công sức đầu bếp.<', ' data-i18n="aboutFightWasteDesc">Chúng tôi tin rằng thức ăn ngon được tạo ra là để thưởng thức. Remeli giúp các nhà hàng tối ưu hoá nguồn nguyên liệu và không để phí phạm công sức đầu bếp.<'),
    ('>Tiết kiệm &amp; Gắn kết<', ' data-i18n="aboutSaveConnect">Tiết kiệm &amp; Gắn kết<'),
    ('>Tiết kiệm & Gắn kết<', ' data-i18n="aboutSaveConnect">Tiết kiệm & Gắn kết<'),
    ('>Người dùng được ăn ngon với mức giá ưu đãi, cửa hàng có thêm thu nhập, và cộng đồng xích lại gần nhau hơn trong một mục tiêu chung vô cùng ý nghĩa.<', ' data-i18n="aboutSaveConnectDesc">Người dùng được ăn ngon với mức giá ưu đãi, cửa hàng có thêm thu nhập, và cộng đồng xích lại gần nhau hơn trong một mục tiêu chung vô cùng ý nghĩa.<')
]
update_file('about-remeli.html', about_replacements)

# our-team.html
team_replacements = [
    ('>Đội ngũ Remeli<', ' data-i18n="teamEyebrow">Đội ngũ Remeli<'),
    ('<span>Những người</span><span>đứng sau Remeli</span>', '<span data-i18n="teamPeople">Những người</span><span data-i18n="teamBehind">đứng sau Remeli</span>'),
    ('>Một nhóm những người trẻ đam mê công nghệ, ẩm thực và môi trường, chung tay vì một Việt Nam xanh hơn.<', ' data-i18n="teamDesc">Một nhóm những người trẻ đam mê công nghệ, ẩm thực và môi trường, chung tay vì một Việt Nam xanh hơn.<'),
    ('>Tầm nhìn chung<', ' data-i18n="teamVision">Tầm nhìn chung<'),
    ('<span>Chúng tôi không chỉ</span><span>làm một ứng dụng</span>', '<span data-i18n="teamNotJustApp">Chúng tôi không chỉ</span><span data-i18n="teamMakingApp">làm một ứng dụng</span>'),
    ('>Chúng tôi đang xây dựng một cộng đồng những người quan tâm đến bữa ăn của mình và môi trường xung quanh. Mục tiêu là biến việc "cứu" thức ăn trở thành một thói quen hàng ngày của mọi người.<', ' data-i18n="teamVisionDesc">Chúng tôi đang xây dựng một cộng đồng những người quan tâm đến bữa ăn của mình và môi trường xung quanh. Mục tiêu là biến việc "cứu" thức ăn trở thành một thói quen hàng ngày của mọi người.<'),
    ('>Người Việt<', ' data-i18n="teamVietnamese">Người Việt<'),
    ('>Kiến tạo<', ' data-i18n="teamCreate">Kiến tạo<'),
    ('>Chúng tôi là tập hợp những con\n        người Việt Nam trẻ tuổi, đầy đam mê, cùng chung một khát vọng giải quyết bài toán chống lãng phí thực phẩm tại\n        quê hương mình.<', ' data-i18n="teamVietnameseDesc">Chúng tôi là tập hợp những con\n        người Việt Nam trẻ tuổi, đầy đam mê, cùng chung một khát vọng giải quyết bài toán chống lãng phí thực phẩm tại\n        quê hương mình.<'),
    ('>Những nhà sáng lập<', ' data-i18n="teamFounders">Những nhà sáng lập<')
]
update_file('our-team.html', team_replacements)

# tac-dong.html
impact_replacements = [
    ('>Tác động của Remeli<', ' data-i18n="impactOfRemeli">Tác động của Remeli<'),
    ('<span>Lựa chọn nhỏ</span><span>Thay đổi lớn</span>', '<span data-i18n="impactSmallChoice">Lựa chọn nhỏ</span><span data-i18n="impactBigChange">Thay đổi lớn</span>'),
    ('>Hành động tuy nhỏ bé của bạn đang từng bước tạo ra những tác động khổng lồ, góp phần bảo vệ hành tinh xanh của chúng ta.<', ' data-i18n="impactHeroDesc">Hành động tuy nhỏ bé của bạn đang từng bước tạo ra những tác động khổng lồ, góp phần bảo vệ hành tinh xanh của chúng ta.<'),
    ('>Phần ăn được giải cứu<', ' data-i18n="impactMealsSaved">Phần ăn được giải cứu<'),
    ('>Hàng chục ngàn bữa ăn ngon miệng đã đến tay người dùng kịp thời thay vì kết thúc tại bãi rác.<', ' data-i18n="impactMealsSavedDesc">Hàng chục ngàn bữa ăn ngon miệng đã đến tay người dùng kịp thời thay vì kết thúc tại bãi rác.<'),
    ('>CO₂e được ngăn chặn<', ' data-i18n="impactCO2">CO₂e được ngăn chặn<'),
    ('>Lượng khí thải carbon tương đương (CO₂e) khổng lồ được cắt giảm từ việc ngăn chặn rác thải.<', ' data-i18n="impactCO2Desc">Lượng khí thải carbon tương đương (CO₂e) khổng lồ được cắt giảm từ việc ngăn chặn rác thải.<'),
    ('>kg thức ăn được cứu<', ' data-i18n="impactKgSaved">kg thức ăn được cứu<'),
    ('>15.2 Tấn (tương đương 15,200 kg) nguyên liệu tươi ngon đã không bị lãng phí vô ích.<', ' data-i18n="impactKgSavedDesc">15.2 Tấn (tương đương 15,200 kg) nguyên liệu tươi ngon đã không bị lãng phí vô ích.<'),
    ('>Tầm nhìn bền vững<', ' data-i18n="impactVision">Tầm nhìn bền vững<'),
    ('<span>Mỗi phần ăn được cứu</span><span>là một bước tiến vì Trái Đất</span>', '<span data-i18n="impactEveryMeal">Mỗi phần ăn được cứu</span><span data-i18n="impactStepForEarth">là một bước tiến vì Trái Đất</span>'),
    ('>Lãng phí thực phẩm không chỉ là bài toán về kinh tế mà còn là gánh nặng khổng lồ đối với môi trường. Khi thức ăn bị vứt bỏ, toàn bộ năng lượng và nguồn tài nguyên nước dùng để gieo trồng, thu hoạch, vận chuyển và đóng gói cũng đều biến mất. Bằng việc đồng hành cùng Remeli, bạn đang góp phần vào một chuỗi cung ứng thực phẩm tuần hoàn, nơi mọi giá trị đều được trân trọng và Trái Đất được giảm tải áp lực.<', ' data-i18n="impactVisionDesc">Lãng phí thực phẩm không chỉ là bài toán về kinh tế mà còn là gánh nặng khổng lồ đối với môi trường. Khi thức ăn bị vứt bỏ, toàn bộ năng lượng và nguồn tài nguyên nước dùng để gieo trồng, thu hoạch, vận chuyển và đóng gói cũng đều biến mất. Bằng việc đồng hành cùng Remeli, bạn đang góp phần vào một chuỗi cung ứng thực phẩm tuần hoàn, nơi mọi giá trị đều được trân trọng và Trái Đất được giảm tải áp lực.<'),
    ('>Tác động Môi trường<', ' data-i18n="impactEnvTitle">Tác động Môi trường<'),
    ('<span>Giảm thiểu</span><span>Khí nhà kính</span>', '<span data-i18n="impactReduce">Giảm thiểu</span><span data-i18n="impactGreenhouse">Khí nhà kính</span>'),
    ('>Thực phẩm khi bị chôn lấp sẽ sinh ra lượng lớn khí methane - loại khí gây hiệu ứng nhà kính mạnh gấp 25 lần so với CO₂. Bằng việc cứu lấy thức ăn, chúng ta trực tiếp ngăn chặn sự nóng lên toàn cầu và bảo vệ bầu không khí trong lành cho thế hệ tương lai.<', ' data-i18n="impactEnvDesc">Thực phẩm khi bị chôn lấp sẽ sinh ra lượng lớn khí methane - loại khí gây hiệu ứng nhà kính mạnh gấp 25 lần so với CO₂. Bằng việc cứu lấy thức ăn, chúng ta trực tiếp ngăn chặn sự nóng lên toàn cầu và bảo vệ bầu không khí trong lành cho thế hệ tương lai.<'),
    ('>Tác động Kinh tế<', ' data-i18n="impactEconTitle">Tác động Kinh tế<'),
    ('<span>Tối ưu hoá</span><span>Nguồn lực</span>', '<span data-i18n="impactOptimize">Tối ưu hoá</span><span data-i18n="impactResources">Nguồn lực</span>'),
    ('>Mọi nguyên liệu, nhân công và năng lượng để sản xuất ra một món ăn đều đáng giá. Remeli giúp các doanh nghiệp và nhà hàng thu hồi được chi phí sản xuất, đồng thời mang đến cho người tiêu dùng những bữa ăn chất lượng với mức giá vô cùng hợp lý.<', ' data-i18n="impactEconDesc">Mọi nguyên liệu, nhân công và năng lượng để sản xuất ra một món ăn đều đáng giá. Remeli giúp các doanh nghiệp và nhà hàng thu hồi được chi phí sản xuất, đồng thời mang đến cho người tiêu dùng những bữa ăn chất lượng với mức giá vô cùng hợp lý.<'),
    ('>Tác động Xã hội<', ' data-i18n="impactSocialTitle">Tác động Xã hội<'),
    ('<span>Gắn kết</span><span>Cộng đồng</span>', '<span data-i18n="impactConnect">Gắn kết</span><span data-i18n="impactCommunity">Cộng đồng</span>'),
    ('>Không chỉ dừng lại ở việc mua bán, Remeli đang xây dựng một cộng đồng những người tiêu dùng có ý thức trách nhiệm cao. Chúng ta kết nối với nhau, với cửa hàng địa phương bằng một thông điệp tích cực: Sống xanh, tiêu dùng thông minh và trân trọng thức ăn.<', ' data-i18n="impactSocialDesc">Không chỉ dừng lại ở việc mua bán, Remeli đang xây dựng một cộng đồng những người tiêu dùng có ý thức trách nhiệm cao. Chúng ta kết nối với nhau, với cửa hàng địa phương bằng một thông điệp tích cực: Sống xanh, tiêu dùng thông minh và trân trọng thức ăn.<'),
    ('>Trở thành một phần<', ' data-i18n="impactBePart">Trở thành một phần<'),
    ('>của giải pháp<', ' data-i18n="impactOfSolution">của giải pháp<'),
    ('>Tải Remeli ngay hôm nay để bắt đầu hành trình giải cứu thức ăn và bảo vệ môi trường cùng hàng chục ngàn người Việt Nam khác.<', ' data-i18n="impactCtaDesc">Tải Remeli ngay hôm nay để bắt đầu hành trình giải cứu thức ăn và bảo vệ môi trường cùng hàng chục ngàn người Việt Nam khác.<'),
    ('>Tải Ứng Dụng Ngay<', ' data-i18n="impactCtaBtn">Tải Ứng Dụng Ngay<')
]
update_file('tac-dong.html', impact_replacements)

# phan-hoi-khach-hang.html
feedback_replacements = [
    ('>Cộng đồng Remeli<', ' data-i18n="fbCommunity">Cộng đồng Remeli<'),
    ('<span>Tiếng nói từ</span><span>Cộng đồng</span>', '<span data-i18n="fbVoice">Tiếng nói từ</span><span data-i18n="fbComm">Cộng đồng</span>'),
    ('>Khám phá những trải nghiệm chân thực nhất từ hàng ngàn khách hàng và đối tác đã đồng hành cùng Remeli trên hành trình chống lãng phí.<', ' data-i18n="fbDesc">Khám phá những trải nghiệm chân thực nhất từ hàng ngàn khách hàng và đối tác đã đồng hành cùng Remeli trên hành trình chống lãng phí.<'),
    ('>Cảm nhận thực tế<', ' data-i18n="fbRealExp">Cảm nhận thực tế<'),
    ('>Bí kíp ăn ngon, giá hời!<', ' data-i18n="fbTitle1">Bí kíp ăn ngon, giá hời!<'),
    ('>"App siêu tiện lợi luôn! Mình hay canh giờ tối để đặt túi mù từ tiệm bánh yêu thích. Vừa được ăn ngon, vừa tiết kiệm được kha khá tiền, cảm giác bóc quà bất ngờ lắm!"<', ' data-i18n="fbText1">"App siêu tiện lợi luôn! Mình hay canh giờ tối để đặt túi mù từ tiệm bánh yêu thích. Vừa được ăn ngon, vừa tiết kiệm được kha khá tiền, cảm giác bóc quà bất ngờ lắm!"<'),
    ('>Người dùng • TP. HCM<', ' data-i18n="fbRole1">Người dùng • TP. HCM<'),
    ('>Cứu cánh cuối tháng<', ' data-i18n="fbTitle2">Cứu cánh cuối tháng<'),
    ('>"Là sinh viên nên Remeli cứu rỗi ví tiền của mình rất nhiều. Thức ăn vẫn còn rất nóng hổi và chất lượng, hy vọng app mở rộng thêm nhiều cửa hàng gần trường mình hơn."<', ' data-i18n="fbText2">"Là sinh viên nên Remeli cứu rỗi ví tiền của mình rất nhiều. Thức ăn vẫn còn rất nóng hổi và chất lượng, hy vọng app mở rộng thêm nhiều cửa hàng gần trường mình hơn."<'),
    ('>Sinh viên • Hà Nội<', ' data-i18n="fbRole2">Sinh viên • Hà Nội<'),
    ('>Giải pháp chống lãng phí<', ' data-i18n="fbTitle3">Giải pháp chống lãng phí<'),
    ('>"Từ ngày đăng ký bán phần ăn cuối ngày trên Remeli, quán tôi không còn phải bỏ mứa đồ ăn nữa. Doanh thu tăng nhẹ nhưng vui nhất là không lãng phí công sức nấu nướng."<', ' data-i18n="fbText3">"Từ ngày đăng ký bán phần ăn cuối ngày trên Remeli, quán tôi không còn phải bỏ mứa đồ ăn nữa. Doanh thu tăng nhẹ nhưng vui nhất là không lãng phí công sức nấu nướng."<'),
    ('>Đối tác • Quận 3<', ' data-i18n="fbRole3">Đối tác • Quận 3<'),
    ('>Hành động nhỏ, ý nghĩa lớn<', ' data-i18n="fbTitle4">Hành động nhỏ, ý nghĩa lớn<'),
    ('>"Thật tuyệt vời khi được chung tay bảo vệ môi trường mỗi ngày chỉ bằng những bữa ăn ngon. Thiết kế app cực kỳ dễ thương và dễ sử dụng!"<', ' data-i18n="fbText4">"Thật tuyệt vời khi được chung tay bảo vệ môi trường mỗi ngày chỉ bằng những bữa ăn ngon. Thiết kế app cực kỳ dễ thương và dễ sử dụng!"<'),
    ('>Người dùng • Đà Nẵng<', ' data-i18n="fbRole4">Người dùng • Đà Nẵng<'),
    ('>Tiện lợi, mượt mà<', ' data-i18n="fbTitle5">Tiện lợi, mượt mà<'),
    ('>"Tính năng pick-up của app hoạt động cực kỳ mượt mà. Mình tan làm ghé ngang cửa hàng, chỉ cần đưa mã quét là nhận đồ ngay, không phải chờ đợi phút nào."<', ' data-i18n="fbText5">"Tính năng pick-up của app hoạt động cực kỳ mượt mà. Mình tan làm ghé ngang cửa hàng, chỉ cần đưa mã quét là nhận đồ ngay, không phải chờ đợi phút nào."<'),
    ('>Nhân viên văn phòng • TP.HCM<', ' data-i18n="fbRole5">Nhân viên văn phòng • TP.HCM<'),
    ('>Niềm vui người thợ bánh<', ' data-i18n="fbTitle6">Niềm vui người thợ bánh<'),
    ('>"Không còn đau đầu vì bánh tồn kho mỗi tối, tôi cảm thấy rất biết ơn đội ngũ Remeli đã tạo ra một nền tảng thực sự ý nghĩa cho xã hội."<', ' data-i18n="fbText6">"Không còn đau đầu vì bánh tồn kho mỗi tối, tôi cảm thấy rất biết ơn đội ngũ Remeli đã tạo ra một nền tảng thực sự ý nghĩa cho xã hội."<'),
    ('>Chủ tiệm bánh • Hà Nội<', ' data-i18n="fbRole6">Chủ tiệm bánh • Hà Nội<')
]
update_file('phan-hoi-khach-hang.html', feedback_replacements)

# Also wait, team names / roles
team2 = [
    ('>Trưởng phòng Vận hành<', ' data-i18n="teamOps">Trưởng phòng Vận hành<'),
    ('>Giám đốc Kỹ thuật<', ' data-i18n="teamTech">Giám đốc Kỹ thuật<'),
    ('>Giám đốc Marketing<', ' data-i18n="teamMkt">Giám đốc Marketing<')
]
update_file('our-team.html', team2)

