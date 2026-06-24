#!/usr/bin/env python3
"""사이트맵 핑 — 검색엔진에 sitemap.xml 갱신을 알린다.

주의: 구글은 2023년 6월 sitemap ping(ping?sitemap=) 엔드포인트를 폐지했다.
구글은 Search Console 의 사이트맵 등록 또는 Indexing API 를 사용해야 한다.
이 스크립트는 아직 ping 을 지원하는 엔진에만 요청을 보내고,
구글에 대해서는 안내 메시지를 출력한다.

사용법:
    python tools/sitemap_ping.py
"""
import sys
import os
import urllib.request
import urllib.error
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL

SITEMAP = BASE_URL.rstrip("/") + "/sitemap.xml"


def ping(name: str, url: str) -> None:
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            print(f"  {name}: HTTP {resp.status}")
    except urllib.error.HTTPError as e:
        print(f"  {name}: HTTP {e.code}")
    except urllib.error.URLError as e:
        print(f"  {name}: 실패 — {e.reason}")


def main() -> None:
    enc = urllib.parse.quote(SITEMAP, safe="")
    print(f"sitemap: {SITEMAP}\n")
    # 빙은 IndexNow 권장이지만 sitemap ping 도 아직 동작
    ping("Bing", f"https://www.bing.com/ping?sitemap={enc}")
    print(
        "\n구글: sitemap ping 은 폐지되었습니다.\n"
        "  → Search Console > 색인 > Sitemaps 에서 sitemap.xml 을 한 번 등록하면\n"
        "    이후 구글이 자동으로 주기적 크롤링합니다.\n"
        "  → 즉시 색인이 필요하면 tools/google_indexing.py (Indexing API) 사용."
    )


if __name__ == "__main__":
    main()
