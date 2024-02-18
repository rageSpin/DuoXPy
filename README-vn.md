<picture><img align="left" src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/duo.svg" width="20%"/></picture>
<h1>DuoXPy - Dự án Sandy</h1>
<h3> ⚡️ Farm XP và giữ Streak cho Duolingo🔥</h3>
<h4>Dưới sự hỗ trợ của GitHub Actions 🐙 và Python 🐍</h5>

#

<p align="center">
  <a href="https://github.com/gorouflex/DuoXPy/">English 🇺🇸</a>
  •
  <a href="README-vn.md">Tiếng Việt 🇻🇳</a>
 <p align="center">
  <a href="#tính-năng">Tính năng</a>
  •
  <a href="#cách-sử-dụng">Cách sử dụng</a>
  •
  <a href="#config">Config</a>     
  •
  <a href="#xem-trước">Xem trước</a>
  •
  <a href="#trách-nhiệm">Trách nhiệm</a>  
</p>
<p align="center">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/gorouflex/DuoXPy?style=flat">
  <img src="https://img.shields.io/github/forks/gorouflex/DuoXPy?style=flat">
<p align="center">
  <img src="https://img.shields.io/github/stars/gorouflex/DuoXPy?style=flat">
  <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/gorouflex/DuoXPy?style=flat">
  <img src="https://img.shields.io/github/contributors/gorouflex/DuoXPy?style=flat">
</p>
<p align="center">
  <a href="https://github.com/gorouflex/DuoXPy/actions/workflows/codeql.yml"><img src="https://github.com/gorouflex/DuoXPy/actions/workflows/codeql.yml/badge.svg"></a>
  <a href="https://github.com/gorouflex/DuoXPy/actions/workflows/cl.yml"><img src="https://github.com/gorouflex/DuoXPy/actions/workflows/cl.yml/badge.svg"></a>
</p>
<p align="center">
  <a href="https://github.com/gorouflex/DuoXPy/actions/workflows/daily.yml"><img src="https://github.com/gorouflex/DuoXPy/actions/workflows/daily.yml/badge.svg"></a>
  <a href="https://github.com/gorouflex/DuoXPy/actions/workflows/manual.yml"><img src="https://github.com/gorouflex/DuoXPy/actions/workflows/manual.yml/badge.svg"></a> (*)
</p>

#

### ⚠️ Dự án này vẫn đang ở giai đoạn đầu và có thể không hoạt động như mong đợi đối với một số tài khoản, hãy thử hoàn thành ít nhất 9 bài học và chạy lại sau 2-3 ngày ⚠️, <a href="https://github.com/gorouflex/DuoXPy/blob/main/README-vn.md#cách-để-fix-error-500---no-skillid-found-in-xpgains">fix lỗi ở đây</a>   

### Thuộc chuỗi dự án Sandy

- [Sandy](https://github.com/gorouflex/Sandy/) ( Official Documents and Information Repository for Project Sandy )
- [HoneygainPot](https://github.com/gorouflex/HoneygainPot/) ( 🐝 Automatically claim your Honeygain lucky pot every day 🍯 )
- [DuoXPy](https://github.com/gorouflex/DuoXPy/) ( ⚡️ XP farm and Streak keeper for Duolingo 🔥 )


> [!IMPORTANT]
> **Vui lòng đọc hết tất cả** tài liệu và văn bản hướng dẫn trong repo này trước khi làm!
>
> Đừng quên cho repo của mình 1 star nhé ⭐ 
> - Luôn cập nhật repo của các bạn theo repo gốc này để nhận được những bản cập nhật và vá lỗi mới nhất, và tôi GorouFlex sẽ không hỗ trợ nếu phát hiện repo của bạn đã lỗi thời và không được cập nhật theo repo chính.
> - **Vui lòng không** nhập thông tin tài khoản của bạn ( như token ) vào 2 file workflow ( `daily.yml` và `manual.yml`)  vì nó sẽ không hoạt động mà sẽ gây ra lỗi và còn có thể bị lộ thông tin cho người khác xem
> - (*) Không được fork repo nếu bạn thấy cả 1 trong 2 ( không bao gồm cả CodeQL và CL ) trạng thái của GitHub Actions đều chuyển sang đỏ, hãy chờ cho đến khi 1 trong 2 hoặc cả 2 chuyển sang màu xanh thì có thể fork
> - `Daily lessons` sẽ luôn luôn tự động chạy vào lúc 14:00 giờ ( UTC + 0 ) tức là 9:00 tối theo giờ UTC +7, nếu muốn chỉnh thì tham khảo tại [đây](https://github.com/gorouflex/DuoXPy/blob/main/README-vn.md#làm-thế-nào-để-chỉnh-lại-thời-gian-tự-động-chạy-mỗi-ngày)
> <img src="https://i.imgur.com/htGeFlY.jpg">
  
# Tính năng

- Farm XP ⚡️
- Giữ streak của bạn mỗi ngày với GitHub Actions 🔥

# Cách sử dụng

  1. Đến web [Duolingo](https://www.duolingo.com) và đăng nhập tài khoản Duolingo của bạn vào
  2. Sau khi đã đăng nhập mở công cụ cho lập trình viên của trình duyệt bằng cách ấn nút `F12` ( hoặc `Fn+F12` trên laptop )
  3. Ấn vào tab `Console` và dán đoạn mã này vào console
```
document.cookie
  .split(';')
  .find(cookie => cookie.includes('jwt_token'))
  .split('=')[1]
```
  4. Bạn sẽ thấy token sẽ được hiện lên trên console hãy bỏ `'` trước vào sau token đó ( vd: 'abcde1234` -> abcde1234 ) rồi copy cho các bước tiếp theo
  5. [Fork repo này 🍴](https://github.com/gorouflex/DuoXPy/fork)
  6. Đến repo mà bạn đã fork🍴
  7. Vào `Settings > Secrets and Variables > Actions`, và ấn nút `New Repository secret`
  8. Đặt tên thành `JWT_TOKEN` rồi dán Token mà bạn đã làm ở bước 3 
  9. Trở lại repo của bạn đã fork 🍴, vào Actions trên thanh công cụ repo rồi ấn `I understand my workflows, go ahead and enable them`
     
> [!IMPORTANT]
> Nếu muốn farm xp thì hãy đến workflows tên [`Manual lessons trigger`](https://github.com/gorouflex/DuoXPy/actions/workflows/manual.yml) ( ở trên tab Actions của repo ) rồi nhập số bài học cần farm ( 1 bài học = 20xp ) , và thường thường nếu nhập quá nhiều bài học ( như >1000 ) hoặc là Duolingo chưa phản hồi kịp thì bạn có thể nhận báo cáo lỗi của script nên hãy suy nghĩ kỹ số bài học cần farm nhé!
>
> Nếu bạn nhận được lỗi `No skillId found in xpGains` thì hãy làm ít nhất là 
1 bài học để có thể chạy lại bình thường nhé!

<p align="center">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/get_token.png">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/GitSettings.png">
</p>

# Config

- Thông thường bạn có tìm thấy thư mục config ở cùng nơi mà file `main.py` ở. Nhưng 1 số trường hợp đặc biệc thì bạn cần phải tự tìm file config thông quan cửa sổ thông tin khi chạy của file `main.py`
- Bạn có đổi thông tin token và số lượng bài học ở file config

## Cách để fix `Error 500 - No SkillID found in xpGains`?

- Không nên cho bậc học mới nhất của bạn trống ( level 0 ) mà hãy nâng lên level 1 như ở dưới bằng cách hoàn thành 1 bài học hoặc 1 vài bài học (áp dụng cho từng khóa học như tiếng Anh, tiếng Tây Ban Nha, tiếng Nhật, v.v...)

<p align="center">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/wrong.png">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/correct.png">
</p>

## Làm thế nào để chỉnh lại thời gian tự động chạy mỗi ngày?

> [!IMPORTANT]
File tự động chạy mỗi ngày ở ( mặc định là 14:00 UTC ± 0, và vui lòng **không** nhập email tài khoản và mật khẩu của bạn vào vì nó sẽ không hoạt động dẫn đến lỗi và còn có thể bị lộ thông tim cho người bên ngoài ): `.github/workflows/daily.yml`

- GitHub sử dụng giờ UTC quốc tế ( UTC ± 0 ) để đặt lịch trình chạy GitHub Actions, nên chúng ta phải đổi sang múi giờ của mình

- Ví dụ: Nếu tôi muốn đặt lịch để cho GitHub Actions chạy vào lúc 9:00 tối ( múi giờ UTC + 7 ) thì tôi phải chuyển thành là 2 giờ chiều theo múi giờ UTC ± 0, vì 2+7 là 9!
Lưu ý là phải sử dụng định dạng 24 giờ để đặt lịch: 

```
name: Daily claim
on:
  schedule:
    - cron: '0 14 * * *' # <- Use UTC Time +0 , change your time here ( 14 is hour , 0 is minutes) and use 24-hour format
```

- Nên nếu tôi muốn đặt vào lúc 5h sáng theo giờ UTC +7 thì tôi phải đặt thành 10h tối theo giờ UTC +0, và phải sử dụng định dạng 24 giờ:

```
name: Daily claim
on:
  schedule:
    - cron: '0 22 * * *' # <- Use UTC Time +0 , change your time here ( 14 is hour , 0 is minutes) and use 24-hour format
```

> [!NOTE]
> GitHub Actions có thể bị delay hơn so với giờ dự kiến đã đặt khoảng từ 3p đến 15p vì do nhu cầu chạy đang cao nên đừng lo lắng vì sao nó không chạy đúng giờ nhé!⏱️

# Xem trước

<p align="left">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/preview.png">
</p>

# Trách nhiệm

> [!WARNING]
> Dự án này được bảo hộ dưới giấy phép [MIT License](https://mit-license.org/)
> 
> Thông tin chi tiết ,vui lòng xem [file LICENSE](/LICENSE)
> - Script/Bot này **KHÔNG** có liên kết hay được xác nhận bởi Duolingo
> - **Tôi** **không có trách nhiệm** cho bất kỳ hậu quả mà có thể phát sinh trong quá trình dùng Script/Bot này
> - Script này sẽ không giúp bạn hoàn thành nhiệm vụ hằng ngày/nhiệm vụ bạn bè, nó chỉ giúp bạn nhận xp để lên rank trong Duolingo
> - Script này sẽ không làm những bài học/chuyện của bạn, chỉ làm phần luyện tập nên sẽ không ảnh hưởng đến tiến độ học của bạn
> - Bạn có thể bị **ban** từ Duolingo nếu quá lạm dụng script, nên hãy sử dụng cẩn thận!

## [![Repography logo](https://images.repography.com/logo.svg)](https://repography.com) / Recent activity [![Time period](https://images.repography.com/44739709/gorouflex/DuoXPy/recent-activity/WJ80z3pywpSIlPEOjRoSCvu-K9h5u0NtXJN_qAaLnRA/tero5srSFgivBt4WNpHw1eF_blCjOl895bVS_SEw2HU_badge.svg)](https://repography.com)
[![Timeline graph](https://images.repography.com/44739709/gorouflex/DuoXPy/recent-activity/WJ80z3pywpSIlPEOjRoSCvu-K9h5u0NtXJN_qAaLnRA/tero5srSFgivBt4WNpHw1eF_blCjOl895bVS_SEw2HU_timeline.svg)](https://github.com/gorouflex/DuoXPy/commits)
[![Issue status graph](https://images.repography.com/44739709/gorouflex/DuoXPy/recent-activity/WJ80z3pywpSIlPEOjRoSCvu-K9h5u0NtXJN_qAaLnRA/tero5srSFgivBt4WNpHw1eF_blCjOl895bVS_SEw2HU_issues.svg)](https://github.com/gorouflex/DuoXPy/issues)
[![Pull request status graph](https://images.repography.com/44739709/gorouflex/DuoXPy/recent-activity/WJ80z3pywpSIlPEOjRoSCvu-K9h5u0NtXJN_qAaLnRA/tero5srSFgivBt4WNpHw1eF_blCjOl895bVS_SEw2HU_prs.svg)](https://github.com/gorouflex/DuoXPy/pulls)
[![Trending topics](https://images.repography.com/44739709/gorouflex/DuoXPy/recent-activity/WJ80z3pywpSIlPEOjRoSCvu-K9h5u0NtXJN_qAaLnRA/tero5srSFgivBt4WNpHw1eF_blCjOl895bVS_SEw2HU_words.svg)](https://github.com/gorouflex/DuoXPy/commits)
[![Top contributors](https://images.repography.com/44739709/gorouflex/DuoXPy/recent-activity/WJ80z3pywpSIlPEOjRoSCvu-K9h5u0NtXJN_qAaLnRA/tero5srSFgivBt4WNpHw1eF_blCjOl895bVS_SEw2HU_users.svg)](https://github.com/gorouflex/DuoXPy/graphs/contributors)
[![Activity map](https://images.repography.com/44739709/gorouflex/DuoXPy/recent-activity/WJ80z3pywpSIlPEOjRoSCvu-K9h5u0NtXJN_qAaLnRA/tero5srSFgivBt4WNpHw1eF_blCjOl895bVS_SEw2HU_map.svg)](https://github.com/gorouflex/DuoXPy/commits)

### Đặt biệt cảm ơn 💖
- [rfoal](https://github.com/rfoel/) x [duolingo](https://github.com/rfoel/duolingo) cho mã nguồn mở ban đầu và ý tưởng
- [ESSTX](https://github.com/ESSTX) cho các sửa lỗi liên quan đến xpGains [PR #1](https://github.com/gorouflex/DuoXPy/pull/1), [PR #2](https://github.com/gorouflex/DuoXPy/pull/2)
