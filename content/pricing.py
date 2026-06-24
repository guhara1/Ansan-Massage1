# 가격 테이블 컴포넌트

def get_pricing_section():
    """모든 페이지에 공통으로 추가할 가격 섹션 HTML"""
    return """<section id="pricing">
  <h2>안산 출장마사지 가격 안내</h2>
  <p>전문 마사지 서비스의 표준 가격 기준입니다. 추가 이동비는 지역별로 상이하며, 예약 시 확인하세요.</p>
  <div class="pricing-table">
    <div class="pricing-card">
      <div class="pricing-duration">60분</div>
      <div class="pricing-amount">90,000<span>원</span></div>
      <div class="pricing-description">기본 마사지 서비스</div>
    </div>
    <div class="pricing-card pricing-featured">
      <div class="pricing-badge">추천</div>
      <div class="pricing-duration">90분</div>
      <div class="pricing-amount">150,000<span>원</span></div>
      <div class="pricing-description">가장 인기 있는 코스</div>
    </div>
    <div class="pricing-card">
      <div class="pricing-duration">120분</div>
      <div class="pricing-amount">180,000<span>원</span></div>
      <div class="pricing-description">풀 마사지 서비스</div>
    </div>
  </div>
  <p class="pricing-note">* 추가 이동비는 지역별 기본 이동권 범위를 초과할 시 발생합니다. 예약 전에 정확한 지역 확인 후 상담해주세요.</p>
</section>"""
