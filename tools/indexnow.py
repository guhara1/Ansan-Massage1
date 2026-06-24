#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스 공용.

sitemap.xml 의 색인 허용 URL 전체를 IndexNow 엔드포인트로 한 번에 통보한다.
글을 새로 올리거나 수정한 뒤 실행하면 빙·네이버에 즉시 색인 요청이 전달된다.

사용법:
    python tools/indexnow.py            # sitemap.xml 의 모든 URL 통보
    python tools/indexnow.py --dry-run  # 실제 전송 없이 대상 URL만 출력
    python tools/indexnow.py URL1 URL2  # 특정 URL만 통보

키 파일(<KEY>.txt)이 사이트 루트에 배포되어 있어야 검증을 통과한다.
"""
import json
import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY

BASE = BASE_URL.rstrip("/")
HOST = BASE.split("://", 1)[-1]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"  # 빙·네이버·얀덱스에 자동 전파


def read_sitemap_urls() -> list:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sm = os.path.join(root, "sitemap.xml")
    if not os.path.exists(sm):
        print("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
        sys.exit(1)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(sm)
    return [loc.text.strip() for loc in tree.findall(".//sm:loc", ns)]


def submit(urls: list) -> None:
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow 응답: HTTP {resp.status}")
            print("  200/202 이면 정상 접수입니다.")
    except urllib.error.HTTPError as e:
        print(f"IndexNow 오류: HTTP {e.code} — {e.read().decode('utf-8', 'ignore')[:300]}")
    except urllib.error.URLError as e:
        print(f"네트워크 오류: {e.reason}")


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    urls = args if args else read_sitemap_urls()
    if not urls:
        print("통보할 URL이 없습니다.")
        return
    print(f"대상 {len(urls)}개 URL:")
    for u in urls:
        print("  -", u)
    print(f"키 파일: {KEY_LOCATION}")
    if dry:
        print("[dry-run] 실제 전송하지 않았습니다.")
        return
    submit(urls)


if __name__ == "__main__":
    main()
