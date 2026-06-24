# 안산시 출장마사지 사이트 공통 설정

BASE_URL = "https://www.ansan-massage.example.com"

BRAND = "바로 GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시
NAV = [
    ("안산", "/", []),
    ("구별 안내", "/gyeonggi/ansan/", [
        ("상록구", "/gyeonggi/ansan/sangnok-gu/"),
        ("단원구", "/gyeonggi/ansan/danwon-gu/"),
    ]),
    ("지역별 안내", "/gyeonggi/ansan/areas/", [
        ("중앙동", "/gyeonggi/ansan/danwon-gu/jungang-dong/"),
        ("고잔동", "/gyeonggi/ansan/danwon-gu/gojan-dong/"),
        ("초지동", "/gyeonggi/ansan/danwon-gu/choji-dong/"),
        ("원곡동", "/gyeonggi/ansan/danwon-gu/wongok-dong/"),
        ("선부동", "/gyeonggi/ansan/danwon-gu/seonbu-dong/"),
        ("본오동", "/gyeonggi/ansan/sangnok-gu/bono-dong/"),
        ("사동", "/gyeonggi/ansan/sangnok-gu/sa-dong/"),
        ("월피동", "/gyeonggi/ansan/sangnok-gu/wolpi-dong/"),
    ]),
    ("역세권 안내", "/gyeonggi/ansan/station/", [
        ("상록수역", "/gyeonggi/ansan/station/sangnoksu-station/"),
        ("한대앞역", "/gyeonggi/ansan/station/hanyang-univ-at-ansan-station/"),
        ("중앙역", "/gyeonggi/ansan/station/jungang-station/"),
        ("고잔역", "/gyeonggi/ansan/station/gojan-station/"),
        ("초지역", "/gyeonggi/ansan/station/choji-station/"),
        ("안산역", "/gyeonggi/ansan/station/ansan-station/"),
        ("선부역", "/gyeonggi/ansan/station/seonbu-station/"),
        ("원곡역", "/gyeonggi/ansan/station/wongok-station/"),
        ("원시역", "/gyeonggi/ansan/station/wonsi-station/"),
    ]),
    ("생활권 안내", "/gyeonggi/ansan/area/", [
        ("중앙역·고잔", "/gyeonggi/ansan/area/jungang-gojan/"),
        ("초지역·초지동", "/gyeonggi/ansan/area/choji-dong/"),
        ("안산역·원곡동", "/gyeonggi/ansan/area/ansan-station-wongok/"),
        ("상록수·본오", "/gyeonggi/ansan/area/sangnoksu-bono/"),
        ("선부역·선부동", "/gyeonggi/ansan/area/seonbu-station/"),
    ]),
    ("예약 안내", "/gyeonggi/ansan/reservation/", []),
    ("이용 전 확인사항", "/gyeonggi/ansan/check/", []),
    ("고객센터", "/gyeonggi/ansan/support/", [
        ("개인정보처리방침", "/gyeonggi/ansan/support/privacy/"),
    ]),
]
