# 색인(인덱싱) 도구

검색엔진에 새 글/변경을 빠르게 알리는 스크립트 모음입니다.
모든 스크립트는 `content/site.py` 의 `BASE_URL`, `INDEXNOW_KEY` 설정을 자동으로 읽습니다.

## 빌드가 만들어 주는 색인 자산
`python build.py` 실행 시 사이트 루트에 자동 생성됩니다.

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | 색인 허용 페이지 목록 (lastmod 포함) |
| `rss.xml` | RSS 2.0 피드 (구독/일부 색인기 수집용) |
| `robots.txt` | 크롤러 허용 + 사이트맵 위치 |
| `<INDEXNOW_KEY>.txt` | IndexNow 소유확인 키 파일 |

## 1) IndexNow — 빙·네이버·얀덱스 즉시 통보 (권장)
```bash
python build.py            # 먼저 빌드(사이트맵 갱신)
python tools/indexnow.py            # sitemap.xml 의 모든 URL 통보
python tools/indexnow.py --dry-run  # 전송 없이 대상만 확인
python tools/indexnow.py https://ansan-massage1.pages.dev/  # 특정 URL만
```
- 키 파일(`<KEY>.txt`)이 **배포된 상태**여야 검증을 통과합니다. 배포 후 실행하세요.
- 빙에 통보하면 IndexNow 네트워크(네이버·얀덱스 등)로 자동 전파됩니다.

## 2) 사이트맵 핑
```bash
python tools/sitemap_ping.py
```
- 빙에 사이트맵 갱신을 핑합니다.
- 구글은 ping 엔드포인트를 폐지했으므로, Search Console 에 사이트맵을
  **한 번만 등록**하면 이후 자동 크롤링됩니다.

## 3) 구글 Indexing API — 구글 즉시 통보 (선택)
구글은 IndexNow 미참여이므로 즉시 색인을 원하면 이 API 를 사용합니다.
```bash
pip install google-auth google-auth-httplib2 google-api-python-client
python tools/google_indexing.py
```
사전 준비는 `tools/google_indexing.py` 파일 상단 주석을 참고하세요.
서비스 계정 키(`tools/google-sa.json`)는 `.gitignore` 로 제외되어 커밋되지 않습니다.

## 검색엔진 소유확인
- **네이버**: `content/site.py` 의 `NAVER_SITE_VERIFICATION` 값이 메인 페이지
  `<head>` 에 메타태그로 출력됩니다. 서치어드바이저에서 "확인"을 누르세요.
- **구글**: `GOOGLE_SITE_VERIFICATION` 에 서치콘솔 메타값을 넣고 빌드하면
  동일하게 메인 페이지에 출력됩니다.

## 글 올릴 때마다 권장 순서
```bash
# 1. 콘텐츠 수정 후 빌드
python build.py
# 2. 커밋·푸시 → Cloudflare Pages 배포 완료까지 대기
git add -A && git commit -m "..." && git push
# 3. 배포 확인 후 즉시 통보
python tools/indexnow.py            # 빙·네이버
python tools/google_indexing.py     # 구글(설정했다면)
```
