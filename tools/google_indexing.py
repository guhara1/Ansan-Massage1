#!/usr/bin/env python3
"""구글 Indexing API — URL 즉시 색인/갱신 통보.

구글은 IndexNow 에 참여하지 않으므로, 즉시 색인을 원하면 Indexing API 를 쓴다.
(공식적으로는 채용공고/라이브 영상용이지만 일반 페이지에도 널리 사용된다.)

사전 준비(최초 1회):
  1) Google Cloud Console 에서 프로젝트 생성 → "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드 → tools/google-sa.json 으로 저장
  3) Search Console 에서 해당 사이트 속성에 서비스 계정 이메일을
     "소유자(Owner)" 권한으로 추가
  4) 의존성 설치:
     pip install google-auth google-auth-httplib2 google-api-python-client

사용법:
    python tools/google_indexing.py            # sitemap.xml 의 모든 URL 통보
    python tools/google_indexing.py URL1 URL2  # 특정 URL만 통보

키 파일 경로는 환경변수 GOOGLE_SA_JSON 로 덮어쓸 수 있다.
"""
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

SA_JSON = os.environ.get("GOOGLE_SA_JSON", os.path.join(ROOT, "tools", "google-sa.json"))
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def read_sitemap_urls() -> list:
    sm = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(sm):
        print("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
        sys.exit(1)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text.strip() for loc in ET.parse(sm).findall(".//sm:loc", ns)]


def main() -> None:
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        print("의존성이 없습니다. 다음을 실행하세요:\n"
              "  pip install google-auth google-auth-httplib2 google-api-python-client")
        sys.exit(1)

    if not os.path.exists(SA_JSON):
        print(f"서비스 계정 키가 없습니다: {SA_JSON}\n"
              "  파일 상단의 '사전 준비'를 참고해 발급·배치하세요.")
        sys.exit(1)

    urls = sys.argv[1:] or read_sitemap_urls()
    creds = service_account.Credentials.from_service_account_file(SA_JSON, scopes=SCOPES)
    session = AuthorizedSession(creds)

    ok = 0
    for u in urls:
        body = {"url": u, "type": "URL_UPDATED"}
        r = session.post(ENDPOINT, json=body, timeout=30)
        status = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        if r.status_code == 200:
            ok += 1
        print(f"  [{status}] {u}")
        if r.status_code != 200:
            print("        ", r.text[:200])
    print(f"\n완료: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    main()
