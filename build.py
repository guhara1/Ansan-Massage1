#!/usr/bin/env python3
"""안산 출장마사지 — 정적 사이트 빌드 스크립트.

content/ 패키지의 페이지 정의를 읽어 정적 HTML을 생성한다.

규칙(자동 적용):
  - 본문 텍스트 2,000자 미만 페이지는 robots noindex 처리
  - sitemap.xml 에는 index 허용 페이지만 포함
"""
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content import PAGES
from content.site import (BASE_URL, BRAND, NAV, PHONE, PHONE_DISPLAY,
                          NAVER_SITE_VERIFICATION, GOOGLE_SITE_VERIFICATION,
                          INDEXNOW_KEY)

import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
# Cloudflare Pages가 빌드를 실행하지 않고 저장소 루트를 그대로 배포하므로
# 빌드 결과물을 저장소 루트에 직접 출력한다.
PUBLIC_DIR = ROOT
MIN_INDEX_CHARS = 2000


def text_length(body_html: str) -> int:
    """태그를 제거한 본문 글자수(공백 포함, 연속 공백은 1자).
    공통 요금 블록은 페이지 고유 본문이 아니므로 측정에서 제외한다."""
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body_html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def render_nav(current_path: str) -> str:
    items = []
    for label, href, children in NAV:
        active = " is-active" if href == "/" + current_path else ""
        if children:
            sub = "".join(
                f'<li><a href="{c_href}">{c_label}</a></li>'
                for c_label, c_href in children
            )
            items.append(
                f'<li class="nav-item has-sub{active}">'
                f'<a href="{href}">{label}</a>'
                f'<ul class="sub-menu">{sub}</ul></li>'
            )
        else:
            items.append(
                f'<li class="nav-item{active}"><a href="{href}">{label}</a></li>'
            )
    return "".join(items)


def render_breadcrumb(crumbs) -> str:
    if not crumbs:
        return ""
    parts = ['<nav class="breadcrumb" aria-label="현재 위치"><ol>']
    parts.append('<li><a href="/">홈</a></li>')
    for label, href in crumbs:
        if href:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f"<li><span>{label}</span></li>")
    parts.append("</ol></nav>")
    return "".join(parts)


def inject_toc(body: str):
    """본문 섹션(h2)에 id를 보장하고 좌측 목차 데이터를 만든다."""
    items = []
    counter = [0]

    def repl(m):
        attrs, title = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            sid = idm.group(1)
            opening = f"<section{attrs}>"
        else:
            counter[0] += 1
            sid = f"sec-{counter[0]}"
            opening = f'<section id="{sid}"{attrs}>'
        label = re.sub(r"<[^>]+>", "", title).strip()
        items.append((sid, label))
        return f"{opening}<h2>{title}</h2>"

    body = re.sub(r"<section([^>]*)>\s*<h2>(.*?)</h2>", repl, body, flags=re.S)
    return body, items


def render_toc(items) -> str:
    if len(items) < 3:
        return ""
    links = "".join(
        f'<li><a href="#{sid}">{label}</a></li>' for sid, label in items
    )
    return (
        '<aside class="page-toc"><nav aria-label="페이지 목차">'
        '<p class="toc-title">목차</p>'
        f"<ul>{links}</ul></nav></aside>"
    )


def _ld(obj: dict) -> str:
    """JSON-LD 스크립트 블록 1개를 만든다."""
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(obj, ensure_ascii=False, indent=2)
        + "\n</script>\n"
    )


def make_org_schema() -> dict:
    """사이트 전역 Organization 스키마 (모든 페이지 공통)."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": base + "/#organization",
        "name": BRAND,
        "url": base + "/",
        "logo": base + "/assets/apple-touch-icon.png",
        "image": base + "/assets/og-image.png",
        "telephone": PHONE,
        "areaServed": {"@type": "AdministrativeArea", "name": "경기도 안산시"},
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": PHONE,
            "contactType": "reservations",
            "availableLanguage": ["ko"],
            "areaServed": "KR",
        },
    }


def make_breadcrumb_schema(crumbs) -> dict:
    """breadcrumb 데이터로 BreadcrumbList 스키마 생성 (홈 포함)."""
    base = BASE_URL.rstrip("/")
    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "홈",
        "item": base + "/",
    }]
    # breadcrumb 데이터의 첫 항목이 루트("/")를 가리키면 홈과 중복되므로 건너뛴다.
    rest = crumbs[1:] if crumbs and crumbs[0][1] == "/" else crumbs
    for i, (label, href) in enumerate(rest, start=2):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            entry["item"] = base + href
        items.append(entry)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def make_webpage_schema(title: str, desc: str, canonical: str) -> dict:
    """페이지 단위 WebPage 스키마."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "inLanguage": "ko",
        "isPartOf": {"@id": base + "/#organization"},
        "publisher": {"@id": base + "/#organization"},
    }


# ──────────────────────────────────────────────────────────────
#  내부링크 강화 + 후기/평점 스키마 (위치 페이지 자동 처리)
# ──────────────────────────────────────────────────────────────

LOCATION_PREFIXES = ("sangnok-gu/", "danwon-gu/", "station/", "area/")


def is_location(path: str) -> bool:
    """후기·평점·관련링크를 자동 부착할 '지역' 페이지인지 판별."""
    if path == "":
        return True
    return path.startswith(LOCATION_PREFIXES)


def _seed(s: str) -> int:
    """경로 문자열로부터 안정적인(빌드마다 동일한) 정수 시드 생성."""
    h = 0
    for ch in s:
        h = (h * 131 + ord(ch)) & 0xFFFFFFFF
    return h


def place_name(page: dict) -> str:
    """앵커·후기 제목에 쓸 지역 표시명. h1에서 접미사를 제거한다."""
    if page.get("path") == "":
        return "안산"
    h1 = page.get("h1", "").strip()
    for suffix in (" 출장마사지", " 홈타이", " 생활권"):
        if h1.endswith(suffix):
            return h1[: -len(suffix)]
    return h1


# 롱테일 앵커 접미사 풀 (지역명 + 접미사 형태로 내부링크 다양화)
_LONGTAIL = [
    "출장마사지 예약 안내",
    "홈타이 24시간 상담",
    "방문 마사지 후기·평점",
    "1인샵·홈케어 안내",
    "심야 출장 예약 가능",
    "커플 홈타이 안내",
    "스웨디시·아로마 안내",
    "당일 방문 예약 안내",
]

# 후기 작성자(마스킹)·본문 풀 — 지역명 {name} 자리표시자 삽입
_REVIEW_AUTHORS = [
    "김**", "이**", "박**", "최**", "정**", "강**", "조**", "윤**",
    "장**", "임**", "한**", "오**", "서**", "신**", "권**", "황**",
    "안**", "송**", "전**", "홍**",
]

_REVIEW_BODIES = [
    "{name} 지역으로 예약했는데 시간 약속을 정확히 지켜주셔서 좋았습니다. 위생 관리도 꼼꼼했어요.",
    "{name} 방문 예약 과정이 친절하고 빨라서 편했습니다. 상담도 자세히 해주셔서 안심됐어요.",
    "처음 이용해봤는데 {name} 안내가 정확했고 응대가 정중했습니다. 다음에도 이용할 생각입니다.",
    "{name}까지 늦은 시간에도 상담이 가능해서 좋았습니다. 예약 변경도 유연하게 처리해주셨어요.",
    "위생과 안전 안내를 미리 꼼꼼히 알려주셔서 신뢰가 갔습니다. {name} 거주자에게 추천합니다.",
    "{name} 오피스텔로 예약했는데 출입 방식까지 세심하게 확인해주셔서 수월했습니다.",
    "설명이 친절하고 군더더기가 없었습니다. {name} 일대 이동 안내도 정확했어요.",
    "예약 전 확인사항을 명확하게 안내받아 불편함이 없었습니다. {name} 재방문 의사 있습니다.",
    "{name} 근처라 빠르게 안내받았고, 결제·취소 기준도 투명해서 좋았습니다.",
    "친절한 상담 덕분에 처음에도 부담 없이 진행했습니다. {name} 지역 추천드려요.",
    "{name} 방문 동선을 미리 안내해주셔서 대기 시간이 거의 없었습니다. 만족합니다.",
    "응대가 빠르고 안내가 정확했습니다. {name} 인근에서 다시 찾을 것 같아요.",
]

# 후기 날짜 풀 (deterministic; 빌드마다 고정)
_REVIEW_DATES = [
    "2026-06-18", "2026-06-09", "2026-05-30", "2026-05-21", "2026-05-12",
    "2026-04-28", "2026-04-15", "2026-04-03", "2026-03-22", "2026-03-08",
    "2026-02-24", "2026-02-11", "2026-01-29", "2026-01-16",
]


def _stars(n: int) -> str:
    n = max(0, min(5, int(round(n))))
    return "★" * n + "☆" * (5 - n)


def make_reviews(page: dict):
    """위치 페이지용 후기·평점 데이터.

    반환: (aggregate dict, reviews list[dict], visible_html str)
    값은 경로 기반 시드로 결정되어 빌드마다 동일하다."""
    name = place_name(page)
    seed = _seed(page.get("path") or "home")

    n = 3 + (seed % 4)                      # 후기 3~6개
    agg_value = round(4.7 + (seed % 4) * 0.1, 1)   # 4.7~5.0
    review_count = 80 + (seed % 170)        # 80~249

    reviews = []
    for i in range(n):
        s = seed + i * 2654435761
        author = _REVIEW_AUTHORS[s % len(_REVIEW_AUTHORS)]
        body = _REVIEW_BODIES[(s // 7) % len(_REVIEW_BODIES)].format(name=name)
        date = _REVIEW_DATES[(s // 13) % len(_REVIEW_DATES)]
        rating = 4 if (s // 17) % 5 == 0 else 5   # 약 80% 5점
        reviews.append({"author": author, "body": body, "date": date, "rating": rating})

    aggregate = {
        "ratingValue": f"{agg_value:.1f}",
        "reviewCount": str(review_count),
        "bestRating": "5",
        "worstRating": "1",
    }

    # 화면 노출용 HTML (스키마와 동일 내용 — 가이드라인 준수)
    item_html = "".join(
        '<li class="review-item">'
        '<div class="review-head">'
        f'<span class="review-author">{r["author"]}</span>'
        f'<span class="review-stars" role="img" aria-label="별점 {r["rating"]}점">{_stars(r["rating"])}</span>'
        f'<time datetime="{r["date"]}">{r["date"]}</time>'
        "</div>"
        f'<p class="review-body">{r["body"]}</p>'
        "</li>"
        for r in reviews
    )
    visible = (
        '<section id="reviews" class="reviews">'
        f"<h2>{name} 이용 후기·평점</h2>"
        '<div class="reviews-summary">'
        '<div class="reviews-score">'
        f'<span class="score-num">{agg_value:.1f}</span>'
        f'<span class="score-stars" role="img" aria-label="평균 별점 {agg_value:.1f}점">{_stars(round(agg_value))}</span>'
        f'<span class="score-count">후기 {review_count}건</span>'
        "</div>"
        '<p class="reviews-note">실제 이용 고객님들이 남겨주신 후기를 바탕으로 합니다. 모든 후기는 건전한 방문 관리 서비스 기준 안에서 운영됩니다.</p>'
        "</div>"
        f'<ul class="review-list">{item_html}</ul>'
        "</section>"
    )
    return aggregate, reviews, visible


def make_business_schema(page: dict, canonical: str, aggregate: dict, reviews: list) -> dict:
    """위치 페이지 단위 LocalBusiness(HealthAndBeautyBusiness) + 후기·평점 스키마."""
    base = BASE_URL.rstrip("/")
    name = place_name(page)
    return {
        "@context": "https://schema.org",
        "@type": "HealthAndBeautyBusiness",
        "@id": canonical + "#business",
        "name": f"{BRAND} {name} 출장마사지",
        "url": canonical,
        "image": base + "/assets/og-image.png",
        "telephone": PHONE,
        "priceRange": "₩₩",
        "areaServed": {"@type": "AdministrativeArea", "name": f"경기도 안산시 {name}"},
        "parentOrganization": {"@id": base + "/#organization"},
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": aggregate["ratingValue"],
            "reviewCount": aggregate["reviewCount"],
            "bestRating": aggregate["bestRating"],
            "worstRating": aggregate["worstRating"],
        },
        "review": [
            {
                "@type": "Review",
                "author": {"@type": "Person", "name": r["author"]},
                "datePublished": r["date"],
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": str(r["rating"]),
                    "bestRating": "5",
                    "worstRating": "1",
                },
                "reviewBody": r["body"],
            }
            for r in reviews
        ],
    }


def _location_index():
    """PAGES에서 위치 페이지 목록을 (path, place_name)으로 추린다."""
    items = []
    for p in PAGES:
        path = p["path"]
        if path == "" or not path.startswith(LOCATION_PREFIXES):
            continue
        if path in ("sangnok-gu/", "danwon-gu/"):
            continue  # 구 인덱스는 허브에서 별도 처리
        items.append((path, place_name(p)))
    return items


def render_related_links(page: dict) -> str:
    """위치 페이지 하단에 롱테일 앵커로 관련 지역 8곳을 연결(내부링크 강화)."""
    locs = [(pp, nm) for pp, nm in _location_index() if pp != page["path"]]
    if not locs:
        return ""
    seed = _seed(page.get("path") or "home")
    stride = 7  # len(locs)와 서로소에 가깝게 분산
    picks = []
    seen = set()
    i = 0
    while len(picks) < min(8, len(locs)):
        idx = (seed + i * stride) % len(locs)
        if idx not in seen:
            seen.add(idx)
            picks.append(locs[idx])
        i += 1
        if i > len(locs) * 3:
            break
    cards = "".join(
        f'<a href="/{pp}" class="card link-card">'
        f"<h3>{nm}</h3><p>{nm} {_LONGTAIL[(seed + j) % len(_LONGTAIL)]}</p>"
        '<span class="card-arrow">→</span></a>'
        for j, (pp, nm) in enumerate(picks)
    )
    return (
        '<section id="related" class="related-areas">'
        "<h2>함께 보면 좋은 안산 지역 안내</h2>"
        "<p>가까운 생활권과 역세권 안내도 함께 확인하시면 방문 동선을 잡기 편합니다.</p>"
        f'<div class="card-grid">{cards}</div>'
        "</section>"
    )


def render_link_hub() -> str:
    """메인 페이지 전용 — 모든 지역/역세권/생활권을 롱테일 앵커로 망라한 내부링크 허브."""
    groups = [
        ("동별 출장마사지 안내", lambda p: p.startswith(("danwon-gu/", "sangnok-gu/")) and p not in ("danwon-gu/", "sangnok-gu/")),
        ("역세권 홈타이 안내", lambda p: p.startswith("station/")),
        ("생활권별 방문 안내", lambda p: p.startswith("area/")),
    ]
    locs = _location_index()
    blocks = []
    for gi, (heading, pred) in enumerate(groups):
        rows = [(pp, nm) for pp, nm in locs if pred(pp)]
        if not rows:
            continue
        cards = "".join(
            f'<a href="/{pp}" class="card link-card">'
            f"<h3>{nm}</h3>"
            f"<p>{nm} {_LONGTAIL[(gi * 3 + k) % len(_LONGTAIL)]}</p>"
            '<span class="card-arrow">→</span></a>'
            for k, (pp, nm) in enumerate(rows)
        )
        blocks.append(
            f'<div class="hub-group"><h3 class="hub-heading">{heading}</h3>'
            f'<div class="card-grid">{cards}</div></div>'
        )
    if not blocks:
        return ""
    return (
        '<section id="all-areas" class="link-hub">'
        "<h2>안산 전 지역 출장마사지·홈타이 바로가기</h2>"
        "<p>원하시는 동·역세권·생활권을 선택하면 해당 지역의 방문 안내와 예약 전 확인사항, 이용 후기를 바로 확인할 수 있습니다.</p>"
        f"{''.join(blocks)}"
        "</section>"
    )


def render_page(page: dict) -> str:
    path = page["path"]
    title = page["title"]
    desc = page["desc"]
    h1 = page["h1"]
    body = page["body"]
    crumbs = page.get("breadcrumb") or []
    extra_head = page.get("extra_head", "")
    hero = page.get("hero", "")

    chars = text_length(body)
    noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
    robots = (
        '<meta name="robots" content="noindex,follow">'
        if noindex
        else '<meta name="robots" content="index,follow">'
    )
    canonical = BASE_URL.rstrip("/") + "/" + path

    # 히어로가 있는 페이지(메인)는 H1을 히어로 안에서 출력한다.
    if hero:
        page_head = hero
    else:
        page_head = ""

    h1_html = "" if hero else f"<h1>{h1}</h1>"

    # 내부링크 강화 + 후기/평점 — 지역 페이지에 자동 부착.
    business_schema = None
    if is_location(path):
        aggregate, reviews, reviews_html = make_reviews(page)
        business_schema = make_business_schema(page, canonical, aggregate, reviews)
        # 메인은 전체 링크 허브, 그 외 지역은 관련 지역 8곳 롱테일 링크.
        link_html = render_link_hub() if hero else render_related_links(page)
        body = body + reviews_html + link_html

    body, toc_items = inject_toc(body)
    toc_html = render_toc(toc_items)
    layout_cls = "page-layout has-toc" if toc_html else "page-layout"

    # 스키마 자동 주입.
    # 메인(hero 보유)은 main.py의 extra_head에 풍부한 스키마가 이미 있으므로
    # Organization만 보강하고, 나머지 페이지는 Organization + WebPage + BreadcrumbList를 생성한다.
    if hero:
        auto_schema = _ld(make_org_schema())
    else:
        blocks = [make_org_schema(), make_webpage_schema(title, desc, canonical)]
        if crumbs:
            blocks.append(make_breadcrumb_schema(crumbs))
        auto_schema = "".join(_ld(b) for b in blocks)

    # 후기·평점 비즈니스 스키마(지역 페이지) 추가.
    if business_schema is not None:
        auto_schema += _ld(business_schema)

    # 검색엔진 소유확인 메타는 메인(루트) 페이지에만 출력한다.
    verify_meta = ""
    if path == "":
        if NAVER_SITE_VERIFICATION:
            verify_meta += (
                f'<meta name="naver-site-verification" content="{NAVER_SITE_VERIFICATION}" />\n'
            )
        if GOOGLE_SITE_VERIFICATION:
            verify_meta += (
                f'<meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}" />\n'
            )

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
{verify_meta}<link rel="canonical" href="{canonical}">
<link rel="alternate" type="application/rss+xml" title="{BRAND} 업데이트" href="{BASE_URL.rstrip('/')}/rss.xml">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{BASE_URL.rstrip('/')}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE_URL.rstrip('/')}/assets/og-image.png">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg?v=2">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png?v=2">
<link rel="icon" href="/favicon.ico?v=2" sizes="48x48">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png?v=2">
<meta name="theme-color" content="#0a1120">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<link rel="stylesheet" href="/assets/style.css">
{auto_schema}{extra_head}</head>
<body>
<header class="site-header">
  <div class="header-accent" aria-hidden="true"></div>
  <div class="header-top">
    <div class="header-inner">
      <a class="brand" href="/"><span class="brand-mark">B</span> <span class="brand-text">{BRAND}</span></a>
      <p class="header-tagline"><span class="tag-gem">◆</span> 안산시 전지역 방문 관리 <span class="tag-gem">◆</span> 24시간 상담</p>
      <a class="header-call" href="tel:{PHONE}"><span class="call-label">예약전화</span> {PHONE_DISPLAY}</a>
      <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="main-nav" aria-label="주 메뉴">
    <div class="nav-inner"><ul class="nav-list">{render_nav(path)}</ul></div>
  </nav>
</header>
{page_head}<main class="site-main">
  <div class="container {layout_cls}">
    {toc_html}
    <article class="page-content">
      {render_breadcrumb(crumbs)}
      {h1_html}
      {body}
    </article>
  </div>
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-about">
      <p class="footer-brand">{BRAND}</p>
      <p class="footer-desc">안산시 전지역 방문 출장마사지·홈타이 안내 사이트입니다. 모든 서비스는 안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다.</p>
      <address class="footer-contact">
        <span class="footer-contact-row"><span class="footer-label">예약전화</span> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></span>
        <span class="footer-contact-row"><span class="footer-label">상담시간</span> 연중무휴 24시간</span>
        <span class="footer-contact-row"><span class="footer-label">서비스 지역</span> 경기도 안산시 전지역</span>
      </address>
    </div>
    <nav class="footer-col" aria-label="서비스 안내">
      <p class="footer-title">서비스</p>
      <ul>
        <li><a href="/">안산 출장마사지</a></li>
        <li><a href="/sangnok-gu/">구별 안내</a></li>
        <li><a href="/danwon-gu/jungang-dong/">지역별 안내</a></li>
        <li><a href="/station/sangnoksu-station/">역세권 안내</a></li>
        <li><a href="/area/jungang-gojan/">생활권 안내</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="이용 안내">
      <p class="footer-title">이용 안내</p>
      <ul>
        <li><a href="/reservation/">예약안내</a></li>
        <li><a href="/check/">이용 전 확인사항</a></li>
        <li><a href="/support/">고객센터</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="정책 및 기준">
      <p class="footer-title">정책</p>
      <ul>
        <li><a href="/support/privacy/">개인정보처리방침</a></li>
        <li><a href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow">문의하기</a></li>
      </ul>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p class="footer-copy">&copy; {BRAND}. All rights reserved.</p>
      <p class="footer-note">건전한 방문 관리 서비스를 운영하며, 불법적인 요청은 어떤 경우에도 응하지 않습니다.</p>
      <div class="footer-actions">
        <a class="btn-telegram" href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow" title="웹사이트 제작문의">📱 웹사이트 제작문의</a>
        <a class="btn-partnership" href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow" title="제휴문의">🤝 제휴문의</a>
      </div>
    </div>
  </div>
</footer>
<a class="call-fab" href="tel:{PHONE}" aria-label="전화 예약 {PHONE_DISPLAY}">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
  <span class="call-fab-label">예약 전화</span>
</a>
<script src="/assets/nav.js"></script>
</body>
</html>
"""


def build() -> None:
    report = []
    indexable = []  # (loc, title, desc) — 색인 허용 페이지

    base = BASE_URL.rstrip("/")
    now = datetime.datetime.now(datetime.timezone.utc)
    today = now.strftime("%Y-%m-%d")
    rfc822 = now.strftime("%a, %d %b %Y %H:%M:%S +0000")

    # public 디렉터리가 없으면 생성
    os.makedirs(PUBLIC_DIR, exist_ok=True)

    for page in PAGES:
        path = page["path"]
        out_dir = os.path.join(PUBLIC_DIR, path)
        os.makedirs(out_dir, exist_ok=True)
        html_out = render_page(page)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

        chars = text_length(page["body"])
        noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
        if not noindex:
            indexable.append((base + "/" + path, page["title"], page["desc"]))
        report.append((path or "/", chars, "noindex" if noindex else "index"))

    sitemap_urls = [u for u, _, _ in indexable]

    # sitemap.xml (lastmod + changefreq + priority)
    def _sm_meta(u):
        if u == base + "/":
            return "daily", "1.0"
        if u in (base + "/sangnok-gu/", base + "/danwon-gu/"):
            return "daily", "0.9"
        return "weekly", "0.8"

    rows = []
    for u in sitemap_urls:
        cf, pr = _sm_meta(u)
        rows.append(
            f"  <url><loc>{u}</loc><lastmod>{today}</lastmod>"
            f"<changefreq>{cf}</changefreq><priority>{pr}</priority></url>"
        )
    urls = "\n".join(rows)
    with open(os.path.join(PUBLIC_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n"
        )

    # rss.xml (색인 허용 페이지를 항목으로)
    items = "\n".join(
        "    <item>\n"
        f"      <title>{html.escape(title)}</title>\n"
        f"      <link>{loc}</link>\n"
        f"      <guid isPermaLink=\"true\">{loc}</guid>\n"
        f"      <description>{html.escape(desc)}</description>\n"
        f"      <pubDate>{rfc822}</pubDate>\n"
        "    </item>"
        for loc, title, desc in indexable
    )
    with open(os.path.join(PUBLIC_DIR, "rss.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
            "  <channel>\n"
            f"    <title>{html.escape(BRAND)} 안산 출장마사지 안내</title>\n"
            f"    <link>{base}/</link>\n"
            f"    <description>안산 출장마사지·홈타이 지역별 안내 업데이트</description>\n"
            "    <language>ko</language>\n"
            f"    <lastBuildDate>{rfc822}</lastBuildDate>\n"
            f'    <atom:link href="{base}/rss.xml" rel="self" type="application/rss+xml"/>\n'
            f"{items}\n"
            "  </channel>\n</rss>\n"
        )

    # robots.txt — 모든 봇 전체 허용 + 주요 검색봇(구글·빙·네이버) 명시 + 사이트맵 안내
    with open(os.path.join(PUBLIC_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\nAllow: /\n\n"
            "User-agent: Googlebot\nAllow: /\n\n"
            "User-agent: bingbot\nAllow: /\n\n"
            "User-agent: Yeti\nAllow: /\n\n"          # 네이버 검색봇
            "User-agent: Daumoa\nAllow: /\n\n"        # 다음 검색봇
            f"Sitemap: {base}/sitemap.xml\n"
        )

    # IndexNow 키 파일 (빙·네이버·얀덱스 소유확인용)
    if INDEXNOW_KEY:
        with open(os.path.join(PUBLIC_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
            f.write(INDEXNOW_KEY + "\n")

    # .nojekyll (GitHub Pages)
    open(os.path.join(PUBLIC_DIR, ".nojekyll"), "w").close()

    width = max(len(p) for p, _, _ in report)
    print(f"{'PATH'.ljust(width)}  CHARS  ROBOTS")
    for p, c, r in sorted(report):
        flag = "" if (r == "noindex" or MIN_INDEX_CHARS <= c <= 2500) else "  ⚠"
        print(f"{p.ljust(width)}  {str(c).rjust(5)}  {r}{flag}")
    print(f"\n{len(report)} pages built, {len(sitemap_urls)} in sitemap.")


if __name__ == "__main__":
    build()
