# 안산 정보 페이지 — 5개 (예약, 가이드, 정책 등)

from .pricing import get_pricing_section

def create_info_page(path, title, desc, h1, breadcrumb, body_content):
    """정보 페이지 생성 헬퍼 함수"""
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }

# ===== 5개 정보 페이지 =====

reservation = create_info_page(
    path="reservation/",
    title="예약 안내｜안산 출장마사지·홈타이 예약 방법",
    desc="안산 출장마사지·홈타이 예약 방법, 취소 정책, 서비스 시간을 확인하세요.",
    h1="예약 안내",
    breadcrumb=[("안산", "/"), ("예약 안내", "")],
    body_content="""
<section>
<h2>예약 방법</h2>
<p>바로 GO의 안산 출장마사지·홈타이 예약은 다음과 같이 진행됩니다:</p>
<ul>
<li><strong>전화 예약</strong>: <a href="tel:0508-202-4719">0508-202-4719</a> (24시간 상담)</li>
<li><strong>상담 시간</strong>: 연중무휴 24시간</li>
<li><strong>예약 확인</strong>: 전화 통화로 즉시 확인</li>
<li><strong>서비스 시간</strong>: 협의 후 결정</li>
</ul>
</section>

<section>
<h2>예약 시 필요한 정보</h2>
<p>예약 전화 시 다음 정보를 정확히 알려주세요:</p>
<ol>
<li><strong>서비스 지역</strong>: 구별, 동, 또는 역명 (예: 중앙동, 중앙역)</li>
<li><strong>정확한 주소</strong>
  <ul>
  <li>아파트 단지인 경우: 단지명, 동호수</li>
  <li>주택/오피스텔: 정확한 주소 및 건물명</li>
  <li>상업 시설: 빌딩명 또는 상점명</li>
  </ul>
</li>
<li><strong>예약 시간</strong>: 희망 서비스 시간대</li>
<li><strong>서비스 시간</strong>: 1시간, 2시간, 3시간 등</li>
<li><strong>연락처</strong>: 핸드폰 번호</li>
</ol>
</section>

<section>
<h2>서비스 요금 안내</h2>
<p>바로 GO의 안산 출장마사지·홈타이 요금은 서비스 시간에 따라 결정됩니다:</p>
<ul>
<li><strong>1시간</strong>: 70,000원~</li>
<li><strong>2시간</strong>: 140,000원~</li>
<li><strong>3시간</strong>: 210,000원~</li>
</ul>
<p>정확한 가격은 지역, 시간대, 서비스 내용에 따라 상이할 수 있습니다. <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요.</p>
</section>

<section>
<h2>취소 및 환불 정책</h2>
<p><strong>취소 정책</strong>은 다음과 같습니다:</p>
<ul>
<li><strong>예약 24시간 전 취소</strong>: 전액 환불</li>
<li><strong>예약 12시간 전 취소</strong>: 50% 환불</li>
<li><strong>예약 1시간 전 취소</strong>: 환불 불가</li>
<li><strong>당일 취소</strong>: 환불 불가</li>
<li><strong>무단 불출현</strong>: 환불 불가</li>
</ul>
<p>정확한 취소 정책은 예약 시 상담 내용을 따릅니다.</p>
</section>

<section>
<h2>접근성 안내</h2>
<p>서비스를 위해 다음 사항을 미리 알려주세요:</p>
<ul>
<li><strong>아파트 단지</strong>: 외부인 출입 가능 여부, 보안 게이트 여부</li>
<li><strong>엘리베이터</strong>: 위치 및 사용 가능 여부</li>
<li><strong>주차</strong>: 단지 내 주차 가능 여부, 주차 위치</li>
<li><strong>접근로</strong>: 계단 또는 엘리베이터 위치</li>
<li><strong>야간 출입</strong>: 야간 시간의 특별 출입 방법</li>
</ul>
</section>

<section>
<h2>결제 방법</h2>
<p>결제는 <strong>서비스 후 현장에서</strong> 진행됩니다:</p>
<ul>
<li><strong>현금 결제</strong>: 서비스 완료 후 현금 지급</li>
<li><strong>카드 결제</strong>: 현장 카드 결제 가능 (문의)</li>
<li><strong>계좌이체</strong>: 미리 계약 시 가능</li>
</ul>
</section>

<section>
<h2>안전 및 신뢰</h2>
<p>바로 GO는 <a href="/check/">이용 전 확인사항</a>을 꼭 읽으신 후 예약하시기를 권장합니다. 건전하고 안전한 서비스 이용을 위해 필요한 모든 정보를 담고 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<ul>
<li><strong>Q: 예약 직후 서비스가 가능한가요?</strong>
  <br>A: 상담 후 가능한 경우 즉시 서비스가 가능합니다. 자세한 사항은 전화 상담 시 확인하세요.</li>
<li><strong>Q: 특정 시간대에 예약할 수 없나요?</strong>
  <br>A: 대부분의 시간대 예약이 가능합니다. 야간이나 새벽 시간도 가능합니다.</li>
<li><strong>Q: 정기적인 예약은 가능한가요?</strong>
  <br>A: 정기 예약도 가능합니다. 상담 시 조율하시기 바랍니다.</li>
</ul>
</section>

<section>
<h2>예약 단계별 상세 안내</h2>
<p>처음 바로 GO를 이용하시는 분들을 위해 예약 과정을 단계별로 자세히 설명드립니다. 복잡한 절차 없이 전화 한 통이면 모든 예약이 완료되므로 부담 없이 이용하실 수 있습니다.</p>
<ol>
<li><strong>1단계 — 상담 전화</strong>: <a href="tel:0508-202-4719">0508-202-4719</a>로 전화하시면 전문 상담원이 친절하게 응대합니다. 처음이라 무엇을 말해야 할지 모르셔도 상담원이 차례대로 여쭤보니 편하게 답변만 하시면 됩니다.</li>
<li><strong>2단계 — 지역 확인</strong>: 현재 계신 지역을 말씀해 주세요. <a href="/sangnok-gu/">상록구</a> 또는 <a href="/danwon-gu/">단원구</a> 어느 곳이든 안산시 전역으로 방문이 가능합니다.</li>
<li><strong>3단계 — 시간 협의</strong>: 원하시는 방문 시간과 서비스 시간(1시간·2시간·3시간)을 정합니다. 가장 가까운 관리사의 도착 예상 시간도 함께 안내해 드립니다.</li>
<li><strong>4단계 — 예약 확정</strong>: 주소와 연락처를 한 번 더 확인한 뒤 예약을 확정합니다. 확정 후에는 관리사가 출발 시 다시 한 번 연락을 드립니다.</li>
<li><strong>5단계 — 방문 및 서비스</strong>: 약속된 시간에 관리사가 방문하여 사전에 안내된 서비스를 진행합니다.</li>
</ol>
<p>예약 전 서비스의 전체 흐름이 궁금하시면 <a href="/guide/">이용 가이드</a>를 먼저 읽어보시는 것을 권장합니다.</p>
</section>

<section>
<h2>예약 가능 시간과 운영 안내</h2>
<p>바로 GO는 <strong>연중무휴 24시간</strong> 예약 상담을 운영합니다. 직장인 고객님을 위해 늦은 저녁 시간대와 심야, 새벽 예약까지 폭넓게 지원하며, 주말과 공휴일에도 동일하게 서비스가 가능합니다. 다만 시간대와 지역에 따라 관리사 배정 상황이 달라질 수 있으므로, 원하는 시간이 정해져 있다면 미리 예약하시는 것이 좋습니다.</p>
<ul>
<li><strong>주간 예약</strong>: 오전부터 오후까지 비교적 빠른 배정이 가능합니다.</li>
<li><strong>야간·심야 예약</strong>: 퇴근 후 또는 늦은 밤에도 이용하실 수 있으며, 사전 예약 시 더 원활합니다.</li>
<li><strong>주말·공휴일</strong>: 수요가 많은 시간대이므로 여유 있게 예약하시기를 권장합니다.</li>
</ul>
<p>특히 <a href="/area/jungang-gojan/">중앙·고잔 생활권</a>이나 <a href="/area/ansan-station-wongok/">안산역·원곡 생활권</a>처럼 수요가 집중되는 지역은 주말 저녁 예약이 일찍 마감될 수 있으니 참고하시기 바랍니다.</p>
</section>

<section>
<h2>예약 변경 및 추가 이동비 안내</h2>
<p>일정 변경이 필요하신 경우 가능한 빠르게 연락 주시면 다른 시간대로 조정해 드립니다. 변경 요청은 빠를수록 원하는 시간으로 재배정될 가능성이 높습니다.</p>
<ul>
<li><strong>시간 변경</strong>: 예약 시간 이전에 연락 주시면 관리사 일정에 따라 조정해 드립니다.</li>
<li><strong>장소 변경</strong>: 방문 주소가 바뀌는 경우 거리에 따라 이동 조건이 달라질 수 있으므로 반드시 사전에 알려주세요.</li>
<li><strong>추가 이동비</strong>: 안산시 외곽 지역이나 접근이 어려운 위치는 거리·시간에 따라 소정의 추가 이동비가 발생할 수 있습니다. 정확한 금액은 예약 상담 시 투명하게 안내해 드립니다.</li>
</ul>
<p>방문 주소·출입 방법 등 사전에 점검해야 할 사항은 <a href="/check/">이용 전 확인사항</a>에 정리되어 있습니다.</p>
</section>

<section>
<h2>예약 자주 묻는 질문</h2>
<ul>
<li><strong>Q: 예약 없이 바로 방문이 가능한가요?</strong>
  <br>A: 원활한 서비스를 위해 사전 예약을 권장합니다. 다만 관리사 배정이 가능한 시간대라면 당일 즉시 예약도 가능하니 전화로 문의해 주세요.</li>
<li><strong>Q: 두 명 이상 동시에 받을 수 있나요?</strong>
  <br>A: 복수 인원 예약도 가능합니다. 인원 수에 맞춰 관리사를 배정해야 하므로 예약 시 미리 말씀해 주세요.</li>
<li><strong>Q: 예약 후 도착까지 얼마나 걸리나요?</strong>
  <br>A: 지역과 시간대에 따라 다르지만, <a href="/station/jungang-station/">중앙역</a>이나 <a href="/station/sangnoksu-station/">상록수역</a> 인근 등 중심 생활권은 비교적 빠른 도착이 가능합니다.</li>
<li><strong>Q: 결제는 어떻게 하나요?</strong>
  <br>A: 서비스 완료 후 현장에서 현금 또는 카드로 결제하실 수 있으며, 사전 계좌이체도 협의 가능합니다.</li>
</ul>
</section>

<section>
<h2>예약 연락처</h2>
<p><strong>바로 GO</strong></p>
<ul>
<li><strong>예약 전화</strong>: <a href="tel:0508-202-4719">0508-202-4719</a></li>
<li><strong>상담 시간</strong>: 연중무휴 24시간</li>
<li><strong>서비스 지역</strong>: 안산시 전지역</li>
</ul>
<p>예약 전 마지막으로 확인하고 싶은 점이 있으시면 <a href="/support/">고객센터</a>를 통해서도 도움을 받으실 수 있습니다.</p>
</section>
""" + get_pricing_section()
)

check = create_info_page(
    path="check/",
    title="이용 전 확인사항｜안산 출장마사지·홈타이 안전 가이드",
    desc="출장마사지·홈타이 이용 전 반드시 확인해야 할 안전 사항을 안내합니다.",
    h1="이용 전 확인사항",
    breadcrumb=[("안산", "/"), ("이용 전 확인사항", "")],
    body_content="""
<section>
<h2>바로 GO 이용 시 안내</h2>
<p><strong>바로 GO</strong>는 안산시에서 건전하고 안전한 출장마사지·홈타이 서비스를 제공합니다. 불법적인 요청은 어떤 경우에도 응하지 않으며, 고객님의 안전과 신뢰를 최우선으로 생각합니다.</p>
</section>

<section>
<h2>건전한 서비스 원칙</h2>
<p>바로 GO는 다음과 같은 원칙으로 서비스를 제공합니다:</p>
<ol>
<li><strong>법적 준수</strong>: 모든 서비스는 관계 법령을 준수합니다</li>
<li><strong>안전성</strong>: 고객과 직원의 안전을 최우선으로</li>
<li><strong>위생 관리</strong>: 철저한 위생 기준 유지</li>
<li><strong>신뢰성</strong>: 약속된 시간과 장소에서 정확한 서비스 제공</li>
<li><strong>거절 권리</strong>: 불합리한 요청에 대한 정중한 거절</li>
</ol>
</section>

<section>
<h2>서비스 가능 범위</h2>
<p><strong>바로 GO에서 제공하는 서비스는 다음과 같습니다:</strong></p>
<ul>
<li>근육 이완 마사지</li>
<li>혈액 순환 개선 마사지</li>
<li>스트레스 해소 마사지</li>
<li>피로 회복 마사지</li>
<li>건강 관리 서비스</li>
</ul>
<p>모든 서비스는 건강과 웰니스를 목표로 하며, 의료 행위는 포함되지 않습니다.</p>
</section>

<section>
<h2>서비스 불가 사항</h2>
<p><strong>다음과 같은 경우는 서비스를 제공할 수 없습니다:</strong></p>
<ul>
<li>불법적인 요청</li>
<li>성적인 서비스 요청</li>
<li>약물 관련 요청</li>
<li>기타 법적 문제가 될 수 있는 행동</li>
</ul>
<p>이러한 요청 시 즉시 서비스를 중단하며, 경찰에 신고할 수 있습니다.</p>
</section>

<section>
<h2>위생 기준</h2>
<p><strong>바로 GO는 다음의 위생 기준을 유지합니다:</strong></p>
<ul>
<li>모든 직원은 정기적인 건강 검진 실시</li>
<li>사용 도구는 매번 소독 및 세정</li>
<li>손 세정 및 위생 관리 철저</li>
<li>마스크 착용 및 개인 위생 관리</li>
<li>고객 안전을 위한 위생 프로토콜 준수</li>
</ul>
</section>

<section>
<h2>개인정보 보호</h2>
<p><strong>바로 GO는 고객의 개인정보를 철저히 보호합니다:</strong></p>
<ul>
<li>예약 정보는 예약 목적으로만 사용</li>
<li>개인정보는 제3자와 공유하지 않음</li>
<li><a href="/support/privacy/">개인정보처리방침</a> 준수</li>
<li>고객 비밀 유지</li>
</ul>
</section>

<section>
<h2>문제 발생 시 처리</h2>
<p><strong>서비스 이용 중 문제가 발생한 경우:</strong></p>
<ol>
<li>즉시 서비스를 중단합니다</li>
<li>고객의 의견을 듣고 성실하게 처리합니다</li>
<li>필요한 경우 재서비스를 제공합니다</li>
<li>반복되는 문제는 <a href="/support/">고객센터</a>에 보고합니다</li>
</ol>
</section>

<section>
<h2>고객 책임</h2>
<p><strong>고객님께서 지켜주셔야 할 사항:</strong></p>
<ul>
<li>예약된 시간에 도착하여 대기</li>
<li>예약 정보의 정확한 제공</li>
<li>서비스 중 직원 존중</li>
<li>불가능한 요청 자제</li>
<li>계약된 요금 정확히 지불</li>
</ul>
</section>

<section>
<h2>방문 주소 및 건물 출입 확인</h2>
<p>출장 서비스의 특성상 <strong>정확한 주소 확인</strong>은 가장 중요한 사전 점검 항목입니다. 관리사가 헤매지 않고 약속된 시간에 정확히 도착할 수 있도록 다음 사항을 예약 시 미리 정리해 주세요.</p>
<ul>
<li><strong>상세 주소</strong>: 도로명 주소와 함께 아파트 단지명·동·호수, 또는 건물명과 층수를 알려주세요.</li>
<li><strong>출입 방법</strong>: 공동현관 비밀번호, 보안 게이트 통과 방법, 인터폰 호출 방식 등을 안내해 주시면 도착 즉시 입실이 가능합니다.</li>
<li><strong>주차 안내</strong>: 방문 차량 주차 가능 여부와 위치를 확인해 주세요. 주차가 어려운 경우 인근 공영주차장 정보를 알려주시면 좋습니다.</li>
<li><strong>야간 출입</strong>: 심야 시간에는 건물 출입문이 잠기는 경우가 있으니 별도 출입 방법을 미리 공유해 주세요.</li>
</ul>
<p><a href="/danwon-gu/gojan-dong/">고잔동</a>, <a href="/danwon-gu/jungang-dong/">중앙동</a> 등 대단지 아파트가 많은 지역은 단지 내부 동 위치까지 알려주시면 도착이 한결 수월합니다.</p>
</section>

<section>
<h2>본인 확인 및 예약자 일치</h2>
<p>안전한 서비스 제공을 위해 방문 시 예약자 본인 여부를 간단히 확인할 수 있습니다. 이는 예약 정보의 혼선을 막고 양측 모두를 보호하기 위한 절차이므로 협조해 주시기 바랍니다.</p>
<ul>
<li>예약 시 등록한 연락처와 실제 방문지가 일치하는지 확인합니다.</li>
<li>대리 예약의 경우 실제 서비스를 받는 분의 정보를 미리 알려주세요.</li>
<li>미성년자에게는 서비스를 제공하지 않습니다.</li>
</ul>
</section>

<section>
<h2>건강 상태 사전 고지 안내</h2>
<p>마사지는 신체에 직접 작용하는 관리이므로, <strong>건강상 주의가 필요한 상태</strong>는 예약 시 반드시 미리 알려주셔야 합니다. 사전 고지를 통해 관리사가 압력과 자세, 관리 부위를 안전하게 조절할 수 있습니다.</p>
<ul>
<li><strong>임신 중</strong>: 임신 여부와 개월 수를 알려주세요. 상태에 따라 관리가 제한될 수 있습니다.</li>
<li><strong>고혈압·심혈관 질환</strong>: 강한 자극을 피해야 하므로 사전 고지가 필요합니다.</li>
<li><strong>디스크·관절 질환</strong>: 통증 부위와 진단 내용을 알려주시면 해당 부위를 조심스럽게 다룹니다.</li>
<li><strong>골절·수술 회복 중</strong>: 회복 경과에 따라 관리 가능 여부가 달라집니다.</li>
<li><strong>피부 질환·상처</strong>: 감염 우려가 있는 부위는 관리에서 제외합니다.</li>
</ul>
<p>음주 후나 발열·몸살 등 컨디션이 좋지 않은 날에는 관리를 미루시는 것이 안전합니다. 자세한 준비 사항은 <a href="/guide/">이용 가이드</a>에서도 확인하실 수 있습니다.</p>
</section>

<section>
<h2>합법적 서비스 범위 재확인</h2>
<p>바로 GO는 <strong>건전한 웰니스 관리만을 제공</strong>하는 합법적 안내 서비스입니다. 근육 이완, 피로 회복, 혈액순환 개선 등 건강 목적의 관리에 한정되며, 그 외의 어떠한 불법적·부적절한 요청에도 응하지 않습니다. 이는 고객과 관리사 모두를 보호하기 위한 확고한 원칙입니다. 서비스 범위에 대한 오해가 없도록 예약 전에 이 점을 충분히 이해해 주시기 바랍니다.</p>
</section>

<section>
<h2>이용 전 확인사항 자주 묻는 질문</h2>
<ul>
<li><strong>Q: 주차 공간이 없으면 이용이 불가능한가요?</strong>
  <br>A: 그렇지 않습니다. 인근 공영주차장이나 대중교통을 이용해 방문할 수 있으니 예약 시 주차 사정을 알려만 주시면 됩니다.</li>
<li><strong>Q: 건강 상태를 꼭 미리 말해야 하나요?</strong>
  <br>A: 안전한 관리를 위해 반드시 필요합니다. 사전 고지가 없으면 적절한 압력 조절이 어려울 수 있습니다.</li>
<li><strong>Q: 예약자와 실제 이용자가 달라도 되나요?</strong>
  <br>A: 가능합니다. 다만 정확한 서비스를 위해 실제 이용자의 정보를 예약 시 알려주세요.</li>
</ul>
<p>추가로 궁금한 점은 <a href="/support/">고객센터</a>나 <a href="/reservation/">예약 안내</a> 페이지를 참고해 주세요.</p>
</section>

<section>
<h2>문의</h2>
<p>이용 전 확인사항에 대해 더 알고 싶으시면 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요.</p>
</section>
""" + get_pricing_section()
)

guide = create_info_page(
    path="guide/",
    title="홈타이 이용 가이드｜안산 출장마사지 서비스 설명",
    desc="홈타이 서비스의 개념, 종류, 이용 방법을 안내합니다.",
    h1="홈타이 이용 가이드",
    breadcrumb=[("안산", "/"), ("이용 가이드", "")],
    body_content="""
<section>
<h2>홈타이란?</h2>
<p><strong>홈타이</strong>는 고객의 집이나 숙소로 마사지사가 방문하여 제공하는 출장 마사지 서비스입니다. 바로 GO의 홈타이는 편안한 환경에서 전문적인 마사지를 받을 수 있는 웰니스 서비스입니다.</p>
</section>

<section>
<h2>홈타이의 장점</h2>
<ul>
<li><strong>편의성</strong>: 집에서 편하게 서비스 이용</li>
<li><strong>프라이버시</strong>: 개인 공간에서의 서비스로 프라이버시 보장</li>
<li><strong>시간 절약</strong>: 이동 시간 없음</li>
<li><strong>맞춤 서비스</strong>: 개인 맞춤형 마사지 제공</li>
<li><strong>편안한 환경</strong>: 자신이 편한 공간에서 치료</li>
</ul>
</section>

<section>
<h2>홈타이 서비스 종류</h2>
<p><strong>바로 GO에서 제공하는 주요 서비스:</strong></p>
<ul>
<li><strong>타이 마사지</strong>: 전통 태국식 마사지 기법</li>
<li><strong>스웨디시 마사지</strong>: 근육 이완과 혈액 순환 개선</li>
<li><strong>아로마테라피</strong>: 향기를 이용한 치료</li>
<li><strong>릴렉싱 마사지</strong>: 스트레스 해소 서비스</li>
<li><strong>풀바디 마사지</strong>: 전신 마사지</li>
</ul>
</section>

<section>
<h2>예약부터 서비스까지</h2>
<ol>
<li><strong>전화 예약</strong>: <a href="tel:0508-202-4719">0508-202-4719</a>로 상담</li>
<li><strong>정보 제공</strong>: 주소, 시간, 서비스 종류 안내</li>
<li><strong>예약 확인</strong>: 예약 시간 및 내용 재확인</li>
<li><strong>마사지사 방문</strong>: 약속된 시간에 도착</li>
<li><strong>서비스 제공</strong>: 전문가의 마사지 서비스</li>
<li><strong>결제</strong>: 서비스 완료 후 결제</li>
</ol>
</section>

<section>
<h2>최고의 경험을 위한 준비</h2>
<p><strong>홈타이 서비스를 받기 전에 준비하세요:</strong></p>
<ul>
<li>편안한 복장 준비</li>
<li>마사지 공간 정리 (침대 또는 매트)</li>
<li>따뜻한 물과 수건 준비</li>
<li>실내 온도 조절 (24~25도 권장)</li>
<li>휴대폰 무음 설정</li>
<li>마사지 받을 부위 확인</li>
</ul>
</section>

<section>
<h2>서비스 중 주의사항</h2>
<ul>
<li>시술자의 지시를 따르기</li>
<li>불편한 점 미리 알리기</li>
<li>과도한 알코올 섭취 자제</li>
<li>심한 질병이 있으면 미리 알리기</li>
<li>너무 강한 자극 요청 자제</li>
</ul>
</section>

<section>
<h2>마사지 후 관리</h2>
<p><strong>서비스 후 빠른 회복을 위해:</strong></p>
<ul>
<li>따뜻한 물로 가볍게 씻기</li>
<li>수분 섭취 충분히 하기</li>
<li>2시간 이상 찬바람 피하기</li>
<li>과도한 활동 자제</li>
<li>푹신한 베개 사용</li>
</ul>
</section>

<section>
<h2>자주 묻는 질문</h2>
<ul>
<li><strong>Q: 매주 정기적으로 받을 수 있나요?</strong>
  <br>A: 네, 정기 예약이 가능합니다.</li>
<li><strong>Q: 질병이 있어도 되나요?</strong>
  <br>A: 예약 시 미리 알려주세요. 전문가가 조언해 드릴 수 있습니다.</li>
<li><strong>Q: 남녀 선택이 가능한가요?</strong>
  <br>A: 예약 시 상담하시기 바랍니다.</li>
</ul>
</section>

<section>
<h2>홈타이 서비스 전체 흐름</h2>
<p>처음 홈타이를 이용하시는 분들이 가장 궁금해하시는 것은 "방문부터 마무리까지 실제로 어떻게 진행되는가"입니다. 바로 GO의 출장 관리는 다음과 같은 흐름으로 진행되어 누구나 편안하게 받을 수 있습니다.</p>
<ol>
<li><strong>방문 및 인사</strong>: 관리사가 약속 시간에 도착해 간단한 인사와 함께 오늘 받으실 관리 부위, 원하시는 강도를 확인합니다.</li>
<li><strong>준비와 자세 안내</strong>: 편안한 자세로 누우실 수 있도록 안내하며, 매트나 침대 위에서 관리를 시작합니다.</li>
<li><strong>본 관리 진행</strong>: 근육의 긴장을 풀어주는 순서로 어깨·등·허리·다리 등을 차례로 관리합니다.</li>
<li><strong>마무리 스트레칭</strong>: 뭉친 부위를 부드럽게 풀어주는 동작으로 마무리합니다.</li>
<li><strong>결제 및 정리</strong>: 관리 종료 후 현장에서 결제하고 다음 이용을 위한 간단한 안내를 받습니다.</li>
</ol>
<p>예약 절차가 궁금하시면 <a href="/reservation/">예약 안내</a>를, 방문 전 점검 사항은 <a href="/check/">이용 전 확인사항</a>을 함께 확인하시면 더욱 매끄럽게 이용하실 수 있습니다.</p>
</section>

<section>
<h2>방문 전 준비 체크리스트</h2>
<p>약간의 사전 준비만으로 관리의 만족도가 크게 달라집니다. 관리사가 도착하기 전 아래 항목을 미리 챙겨두시면 더 깊은 이완을 경험하실 수 있습니다.</p>
<ul>
<li><strong>공간 확보</strong>: 매트나 침대 주변에 사람이 누울 수 있는 여유 공간을 정리해 주세요.</li>
<li><strong>실내 온도</strong>: 24~26도 정도로 따뜻하게 유지하면 근육이 더 잘 이완됩니다.</li>
<li><strong>가벼운 샤워</strong>: 관리 전 가볍게 샤워하시면 한층 쾌적하게 받으실 수 있습니다.</li>
<li><strong>수분 보충</strong>: 따뜻한 물 한 잔을 미리 마셔두는 것이 좋습니다.</li>
<li><strong>방해 요소 차단</strong>: 휴대폰은 무음으로 설정해 온전히 휴식에 집중하세요.</li>
</ul>
</section>

<section>
<h2>관리 중 유의할 점</h2>
<p>관리를 받는 동안에는 몸의 힘을 빼고 호흡을 천천히 유지하는 것이 중요합니다. 긴장을 풀수록 근육 이완 효과가 커집니다.</p>
<ul>
<li>압력이 너무 약하거나 강하면 즉시 관리사에게 알려 조절을 요청하세요.</li>
<li>특정 부위에 통증이 느껴지면 참지 말고 바로 말씀해 주세요.</li>
<li>관리 중 졸음이 오는 것은 자연스러운 현상이니 편하게 휴식하셔도 됩니다.</li>
<li>대화는 편한 만큼만, 조용한 휴식을 원하시면 그렇게 말씀하셔도 됩니다.</li>
</ul>
</section>

<section>
<h2>관리 후 케어 방법</h2>
<p>관리가 끝난 뒤의 관리도 효과 유지에 중요합니다. 다음 사항을 지키시면 시원함과 개운함이 더 오래갑니다.</p>
<ul>
<li><strong>수분 섭취</strong>: 노폐물 배출을 돕기 위해 미지근한 물을 충분히 드세요.</li>
<li><strong>휴식</strong>: 관리 직후 격한 운동이나 무거운 식사는 피하고 충분히 쉬어주세요.</li>
<li><strong>보온</strong>: 찬바람을 피하고 몸을 따뜻하게 유지하세요.</li>
<li><strong>수면</strong>: 관리 후 숙면을 취하면 피로 회복 효과가 극대화됩니다.</li>
</ul>
</section>

<section>
<h2>자주 하는 실수와 이용 팁</h2>
<p>오랫동안 만족스럽게 홈타이를 이용하시는 분들의 공통점은 작은 습관에 있습니다. 반대로 처음 이용하시는 분들이 흔히 하는 실수도 미리 알아두면 도움이 됩니다.</p>
<ul>
<li><strong>실수 1 — 식사 직후 예약</strong>: 배가 부른 상태에서는 엎드린 자세가 불편할 수 있으니 식후 1시간 이상 지난 뒤가 좋습니다.</li>
<li><strong>실수 2 — 건강 상태 미고지</strong>: 통증 부위나 질환을 알리지 않으면 관리 강도 조절이 어렵습니다.</li>
<li><strong>실수 3 — 무리한 강도 요청</strong>: 무조건 강한 것이 좋은 것은 아니며, 본인에게 맞는 강도가 효과적입니다.</li>
<li><strong>이용 팁</strong>: 같은 관리사를 정기적으로 지정하면 몸 상태를 잘 파악해 더 맞춤화된 관리를 받을 수 있습니다.</li>
</ul>
<p><a href="/sangnok-gu/sa-dong/">사동</a>, <a href="/danwon-gu/wongok-dong/">원곡동</a> 등 안산 전 지역으로 방문하니, 거주지 인근에서 편하게 이용하실 수 있습니다.</p>
</section>

<section>
<h2>문의</h2>
<p>홈타이 서비스에 대해 더 알고 싶으시면 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요. 운영 전반에 대한 안내는 <a href="/support/">고객센터</a>에서도 도와드립니다.</p>
</section>
""" + get_pricing_section()
)

privacy = create_info_page(
    path="support/privacy/",
    title="개인정보처리방침｜안산 출장마사지 개인정보 보호",
    desc="바로 GO의 개인정보 수집, 이용, 보호 정책을 안내합니다.",
    h1="개인정보처리방침",
    breadcrumb=[("안산", "/"), ("고객센터", "/support/"), ("개인정보처리방침", "")],
    body_content="""
<section>
<h2>개인정보처리방침 개요</h2>
<p><strong>바로 GO</strong>는 고객의 개인정보를 소중히 여기며, 개인정보 보호법을 준수하여 고객의 개인정보를 안전하게 관리합니다.</p>
</section>

<section>
<h2>수집하는 개인정보</h2>
<p><strong>예약 시 수집하는 정보:</strong></p>
<ul>
<li>이름</li>
<li>전화번호</li>
<li>서비스 주소</li>
<li>예약 시간</li>
<li>서비스 요청사항</li>
</ul>
<p><strong>선택적 정보:</strong></p>
<ul>
<li>이메일 주소</li>
<li>특별 건강 상태 정보</li>
</ul>
</section>

<section>
<h2>개인정보 이용 목적</h2>
<p>수집된 개인정보는 다음 목적으로만 사용됩니다:</p>
<ul>
<li>예약 확인 및 서비스 제공</li>
<li>고객 연락 및 상담</li>
<li>서비스 개선</li>
<li>법적 요구사항 충족</li>
<li>분쟁 해결</li>
</ul>
</section>

<section>
<h2>개인정보 보관 기간</h2>
<ul>
<li><strong>기본 보관</strong>: 서비스 제공 종료 후 1년</li>
<li><strong>법적 보관</strong>: 관계 법령 요구 시 해당 기간</li>
<li><strong>고객 요청</strong>: 삭제 요청 시 즉시 삭제</li>
</ul>
</section>

<section>
<h2>개인정보 보안</h2>
<p><strong>바로 GO는 다음과 같이 개인정보를 보호합니다:</strong></p>
<ul>
<li>암호화 통신</li>
<li>접근 제한</li>
<li>정기적인 보안 감시</li>
<li>직원 교육 및 서명</li>
<li>물리적 보안 조치</li>
</ul>
</section>

<section>
<h2>개인정보 제3자 공유</h2>
<p><strong>바로 GO는 다음과 같은 경우를 제외하고 개인정보를 제3자와 공유하지 않습니다:</strong></p>
<ul>
<li>고객의 명시적인 동의</li>
<li>법적 요구 (경찰, 검찰, 법원)</li>
<li>서비스 제공을 위한 필수적인 경우</li>
</ul>
</section>

<section>
<h2>고객의 권리</h2>
<p><strong>고객님은 다음의 권리가 있습니다:</strong></p>
<ul>
<li><strong>열람권</strong>: 자신의 개인정보 열람 요청</li>
<li><strong>정정권</strong>: 잘못된 정보 수정 요청</li>
<li><strong>삭제권</strong>: 개인정보 삭제 요청</li>
<li><strong>처리 정지권</strong>: 개인정보 처리 중단 요청</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a>로 요청하실 수 있습니다.</p>
</section>

<section>
<h2>쿠키와 추적 기술</h2>
<p>바로 GO 웹사이트는 사용자 경험 개선을 위해 쿠키를 사용할 수 있습니다. 쿠키는 언제든 브라우저 설정에서 비활성화할 수 있습니다.</p>
</section>

<section>
<h2>정책 변경</h2>
<p>이 개인정보처리방침은 예고 없이 변경될 수 있습니다. 변경 시 웹사이트를 통해 공지합니다.</p>
</section>

<section>
<h2>문의</h2>
<p><strong>개인정보에 대한 문의:</strong></p>
<ul>
<li><strong>전화</strong>: <a href="tel:0508-202-4719">0508-202-4719</a></li>
<li><strong>상담 시간</strong>: 연중무휴 24시간</li>
<li><strong>텔레그램</strong>: <a href="https://t.me/googleseolab">@googleseolab</a></li>
</ul>
</section>

<section>
<h2>개인정보 수집 항목 상세</h2>
<p><strong>바로 GO</strong>는 서비스 제공에 꼭 필요한 최소한의 정보만을 수집하는 것을 원칙으로 합니다. 수집되는 항목은 수집 시점과 목적에 따라 아래와 같이 구분됩니다.</p>
<ul>
<li><strong>필수 항목</strong>: 이름, 연락처(전화번호), 방문 주소, 예약 일시. 이는 출장 서비스를 위한 최소 필수 정보입니다.</li>
<li><strong>선택 항목</strong>: 이메일, 건강 상태 관련 요청사항. 더 안전한 관리를 위해 자발적으로 제공하실 수 있으며, 제공하지 않아도 기본 서비스 이용에는 제한이 없습니다.</li>
<li><strong>자동 수집 항목</strong>: 웹사이트 이용 시 접속 기록, 쿠키 등이 자동으로 생성·수집될 수 있습니다.</li>
</ul>
<p>수집되는 정보의 활용과 예약 절차의 관계는 <a href="/reservation/">예약 안내</a>에서도 함께 확인하실 수 있습니다.</p>
</section>

<section>
<h2>수집 및 이용 목적 세부 안내</h2>
<p>수집된 개인정보는 사전에 고지하고 동의받은 범위 내에서만 이용되며, 그 목적이 달성된 후에는 지체 없이 파기됩니다. 주요 이용 목적은 다음과 같습니다.</p>
<ul>
<li><strong>예약 접수 및 확인</strong>: 예약 내용 확인, 일정 조율, 관리사 배정 안내</li>
<li><strong>서비스 제공</strong>: 방문 위치 안내, 서비스 진행 및 결제 처리</li>
<li><strong>고객 응대</strong>: 문의·상담·불만 처리 및 결과 회신</li>
<li><strong>안전 관리</strong>: 건강 상태 고지에 따른 안전한 관리 제공</li>
<li><strong>법령 준수</strong>: 관계 법령에 따른 의무 이행 및 분쟁 대응</li>
</ul>
</section>

<section>
<h2>개인정보 보유 및 이용 기간</h2>
<p>원칙적으로 개인정보는 수집·이용 목적이 달성되면 지체 없이 파기합니다. 다만 관계 법령에 따라 일정 기간 보존이 필요한 경우에는 해당 기간 동안 안전하게 분리 보관합니다.</p>
<ul>
<li><strong>예약·서비스 정보</strong>: 서비스 종료 후 1년 이내 파기</li>
<li><strong>소비자 불만 또는 분쟁 처리 기록</strong>: 관련 법령에 따른 보존 기간 준수</li>
<li><strong>대금 결제 및 재화 공급 기록</strong>: 전자상거래 관련 법령이 정한 기간 동안 보관</li>
<li><strong>고객 삭제 요청</strong>: 법령상 보존 의무가 없는 경우 요청 즉시 파기</li>
</ul>
</section>

<section>
<h2>개인정보 파기 절차 및 방법</h2>
<p>보유 기간이 경과하거나 처리 목적이 달성된 개인정보는 다음 절차와 방법에 따라 복구·재생이 불가능하도록 안전하게 파기합니다.</p>
<ul>
<li><strong>파기 절차</strong>: 목적 달성 후 별도 보관소로 이전되어 내부 방침 및 관련 법령에 따라 일정 기간 저장된 뒤 파기됩니다.</li>
<li><strong>전자적 파일</strong>: 복원이 불가능한 기술적 방법을 사용하여 영구 삭제합니다.</li>
<li><strong>출력물 등</strong>: 종이 문서는 분쇄하거나 소각하여 파기합니다.</li>
</ul>
</section>

<section>
<h2>이용자 권리 행사 방법</h2>
<p>고객님은 본인의 개인정보에 대해 열람, 정정, 삭제, 처리 정지를 언제든지 요구할 수 있습니다. 권리 행사는 <a href="tel:0508-202-4719">0508-202-4719</a> 전화 또는 <a href="/support/">고객센터</a>를 통해 접수할 수 있으며, 바로 GO는 지체 없이 필요한 조치를 취합니다. 또한 만 14세 미만 아동의 개인정보는 수집하지 않으며, 법정대리인의 권리 행사도 동일하게 보장합니다.</p>
</section>

<section>
<h2>정책 동의</h2>
<p>서비스 예약 및 이용으로 본 개인정보처리방침에 동의하는 것으로 간주됩니다. 본 방침과 관련하여 추가 안내가 필요하시면 <a href="/check/">이용 전 확인사항</a> 페이지의 개인정보 보호 항목도 함께 참고하시기 바랍니다. 바로 GO는 고객의 신뢰를 가장 중요한 가치로 삼아, 수집한 모든 개인정보를 관계 법령과 본 방침에 따라 책임감 있게 관리할 것을 약속드립니다. 개인정보 처리와 관련한 어떠한 의문이나 우려도 언제든 편하게 문의해 주시기 바랍니다.</p>
</section>
""" + get_pricing_section()
)

support = create_info_page(
    path="support/",
    title="고객센터｜안산 출장마사지 문의 및 지원",
    desc="바로 GO 고객센터 연락처, 문의 방법, 피드백을 안내합니다.",
    h1="고객센터",
    breadcrumb=[("안산", "/"), ("고객센터", "")],
    body_content="""
<section>
<h2>고객센터 안내</h2>
<p><strong>바로 GO</strong>는 24시간 고객 상담을 제공합니다. 예약, 서비스, 기술적 문제 등 모든 사항에 대해 도움을 드릴 준비가 되어 있습니다.</p>
</section>

<section>
<h2>연락처</h2>
<ul>
<li><strong>회사명</strong>: 바로 GO</li>
<li><strong>예약 및 상담 전화</strong>: <a href="tel:0508-202-4719">0508-202-4719</a></li>
<li><strong>상담 시간</strong>: 연중무휴 24시간 운영</li>
<li><strong>서비스 지역</strong>: 경기도 안산시 전지역</li>
</ul>
</section>

<section>
<h2>기타 연락 방법</h2>
<ul>
<li><strong>텔레그램</strong>: <a href="https://t.me/googleseolab">@googleseolab</a></li>
<li><strong>웹사이트</strong>: ansan-massage1.netlify.app</li>
</ul>
</section>

<section>
<h2>문의 사항 안내</h2>
<p>고객센터로 다음 사항들을 문의할 수 있습니다:</p>
<ul>
<li><strong>예약</strong>: <a href="/reservation/">예약 안내</a> 참조</li>
<li><strong>취소</strong>: 예약된 서비스 취소</li>
<li><strong>변경</strong>: 예약 시간 또는 내용 변경</li>
<li><strong>불만사항</strong>: 서비스 이용 중 문제</li>
<li><strong>기술 지원</strong>: 웹사이트 이용 문제</li>
<li><strong>제휴 및 협력</strong>: 비즈니스 제안</li>
<li><strong>기타</strong>: 모든 관련 문의</li>
</ul>
</section>

<section>
<h2>불만 처리 절차</h2>
<ol>
<li><strong>접수</strong>: 전화 또는 온라인으로 불만 접수</li>
<li><strong>조사</strong>: 상황 파악 및 원인 분석</li>
<li><strong>응답</strong>: 24시간 내 초기 응답</li>
<li><strong>해결</strong>: 적절한 조치 및 해결</li>
<li><strong>확인</strong>: 고객 만족도 확인</li>
</ol>
</section>

<section>
<h2>서비스 개선 피드백</h2>
<p>바로 GO는 고객의 의견을 소중히 여깁니다. 서비스 개선을 위한 모든 제안과 피드백을 환영합니다:</p>
<ul>
<li>좋았던 점 공유</li>
<li>개선할 사항 제안</li>
<li>새로운 서비스 아이디어</li>
<li>기타 건설적인 의견</li>
</ul>
</section>

<section>
<h2>자주 묻는 질문</h2>
<ul>
<li><strong>Q: 긴급 상황 발생 시 어떻게 하나요?</strong>
  <br>A: 즉시 전화로 연락 주세요. 긴급 상황은 우선 처리됩니다.</li>
<li><strong>Q: 야간에 연락할 수 있나요?</strong>
  <br>A: 네, 24시간 상담이 가능합니다.</li>
<li><strong>Q: 회사 정보를 알고 싶어요.</strong>
  <br>A: 전화로 상세한 정보를 제공합니다.</li>
</ul>
</section>

<section>
<h2>다른 지원</h2>
<p><strong>기타 도움이 필요한 사항:</strong></p>
<ul>
<li><a href="/check/">이용 전 확인사항</a> — 안전 가이드</li>
<li><a href="/guide/">홈타이 이용 가이드</a> — 서비스 설명</li>
<li><a href="/support/privacy/">개인정보처리방침</a> — 개인정보 보호</li>
<li><a href="/">메인 페이지</a> — 전체 정보</li>
</ul>
</section>

<section>
<h2>웹사이트 제작 문의</h2>
<p>이 웹사이트 제작에 관심이 있으시면 <a href="https://t.me/googleseolab">텔레그램</a>으로 문의하시기 바랍니다.</p>
</section>

<section>
<h2>문의 방법 안내</h2>
<p>바로 GO 고객센터는 고객님이 가장 편한 방식으로 연락하실 수 있도록 여러 채널을 운영합니다. 어떤 채널을 이용하셔도 동일하게 신속하고 친절한 응대를 받으실 수 있습니다.</p>
<ul>
<li><strong>전화 문의</strong>: <a href="tel:0508-202-4719">0508-202-4719</a> — 가장 빠른 응대가 가능한 방법으로, 예약·변경·긴급 문의에 모두 적합합니다.</li>
<li><strong>텔레그램 문의</strong>: <a href="https://t.me/googleseolab">@googleseolab</a> — 간단한 문의나 기록을 남기고 싶을 때 편리합니다.</li>
<li><strong>예약 관련 문의</strong>: 예약 절차가 궁금하시면 <a href="/reservation/">예약 안내</a> 페이지에서 먼저 확인하실 수 있습니다.</li>
</ul>
</section>

<section>
<h2>응대 시간 및 처리 기준</h2>
<p>고객센터는 <strong>연중무휴 24시간</strong> 상담을 운영합니다. 다만 문의 유형에 따라 처리에 소요되는 시간이 다를 수 있어 아래 기준을 안내해 드립니다.</p>
<ul>
<li><strong>예약·변경·취소</strong>: 전화 즉시 처리됩니다.</li>
<li><strong>일반 문의</strong>: 접수 후 가능한 빠르게 답변드립니다.</li>
<li><strong>불만·환불 검토</strong>: 사실 확인이 필요한 경우 24시간 이내 초기 응답 후 순차 처리됩니다.</li>
</ul>
</section>

<section>
<h2>환불 처리 절차</h2>
<p>환불은 예약 시 안내된 취소·환불 정책에 따라 진행됩니다. 절차를 투명하게 안내하여 고객님이 안심하고 이용하실 수 있도록 합니다.</p>
<ol>
<li><strong>환불 요청 접수</strong>: 전화 또는 텔레그램으로 환불 사유와 함께 요청을 접수합니다.</li>
<li><strong>사실 확인</strong>: 예약 내용, 취소 시점, 서비스 진행 여부 등을 확인합니다.</li>
<li><strong>환불 기준 적용</strong>: 취소 시점에 따른 환불 규정을 적용합니다. 상세 기준은 <a href="/reservation/">예약 안내</a>의 취소·환불 정책을 참고하세요.</li>
<li><strong>환불 처리</strong>: 확인이 완료되면 결제 수단에 맞춰 환불을 진행합니다.</li>
</ol>
</section>

<section>
<h2>분실물 처리 안내</h2>
<p>관리 과정에서 물품이 분실되거나 잊고 두신 소지품이 있는 경우 즉시 고객센터로 연락 주시기 바랍니다. 분실물은 확인 후 신속하게 안내해 드리며, 보관이 필요한 경우 일정 기간 안전하게 보관합니다. 정확한 확인을 위해 분실 추정 일시와 장소, 물품의 특징을 함께 알려주시면 처리가 빠릅니다. 시간이 지날수록 확인이 어려워질 수 있으므로 가능한 빠르게 연락 주시는 것을 권장합니다.</p>
</section>

<section>
<h2>이용 채널 및 추가 안내</h2>
<p>바로 GO 고객센터는 단순한 문의 응대를 넘어 고객님이 서비스를 안심하고 이용하실 수 있도록 전반적인 안내를 제공합니다. 처음 이용하시는 분이라면 아래 페이지들을 함께 살펴보시면 도움이 됩니다.</p>
<ul>
<li><a href="/guide/">이용 가이드</a>에서 홈타이 서비스의 전체 흐름과 준비 사항을 확인할 수 있습니다.</li>
<li><a href="/check/">이용 전 확인사항</a>에서 방문 주소·건강 상태 고지 등 사전 점검 항목을 안내합니다.</li>
<li>거주 지역에 따른 이용 정보는 <a href="/sangnok-gu/bono-dong/">본오동</a>, <a href="/danwon-gu/choji-dong/">초지동</a> 등 지역 페이지에서 확인하실 수 있습니다.</li>
<li>개인정보 처리와 관련한 사항은 <a href="/support/privacy/">개인정보처리방침</a>을 참고해 주세요.</li>
</ul>
<p>이처럼 바로 GO는 예약 전후의 모든 단계에서 고객님이 궁금해하실 만한 정보를 투명하게 안내하여, 신뢰할 수 있는 서비스 경험을 제공하기 위해 노력하고 있습니다.</p>
</section>

<section>
<h2>제휴 및 협력</h2>
<p><strong>바로 GO와의 제휴 및 협력을 원하시면:</strong></p>
<p><a href="https://t.me/googleseolab">Telegram: @googleseolab</a></p>
<p>또는 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락 주세요. 서비스 이용 전 확인이 필요한 사항은 <a href="/check/">이용 전 확인사항</a>에서도 자세히 안내하고 있습니다.</p>
</section>
""" + get_pricing_section()
)

# PAGES 리스트에 모든 정보 페이지 집계
PAGES = [
    reservation,
    check,
    guide,
    privacy,
    support,
]
