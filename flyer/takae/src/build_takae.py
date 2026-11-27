import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from takae_icons import plan
from takae_common import *

ic_move = '<svg viewBox="0 0 60 40" fill="none" stroke="#55628c" stroke-width="1.8" stroke-linejoin="round"><rect x="18" y="4" width="24" height="32" rx="1"/><path d="M23 10h4M33 10h4M23 16h4M33 16h4M23 22h4M33 22h4"/><path d="M27 36v-7h6v7"/><path d="M4 36h52"/><path d="M48 36v-9M44 27h8" stroke-width="1.4"/><text x="9" y="30" font-size="5.5" fill="#55628c" stroke="none" text-anchor="middle" font-family="Noto Sans JP" font-weight="900">駅</text><rect x="4" y="24" width="10" height="9" rx="1.5" stroke-width="1.2"/></svg>'
ic_stay = '<svg viewBox="0 0 60 40" fill="none" stroke="#5d7d45" stroke-width="1.8" stroke-linejoin="round"><path d="M6 19 21 8l15 11"/><path d="M9 17v19h24V17"/><path d="M18 36v-8h6v8"/><path d="M33 31h14" stroke="#8a6a45" stroke-width="2.6"/><path d="M35 31v5M45 31v5" stroke="#8a6a45"/><path d="M52 36V25"/><circle cx="52" cy="20" r="5"/><path d="M4 36h54"/></svg>'
doc = '<svg viewBox="0 0 40 48" fill="none" stroke="#55628c" stroke-width="1.6"><path d="M6 3h20l8 8v34H6z" fill="#fff"/><path d="M26 3v8h8"/><text x="20" y="18" font-size="6.5" fill="#55628c" stroke="none" text-anchor="middle" font-family="Noto Sans JP" font-weight="900">査定書</text><path d="M11 25h18M11 31h18M11 37h12" stroke-width="1.3"/></svg>'

html = head('高江ニュータウン 住み替えか、この家か', css('takae.css', 'takae_a.css')) + f'''
<!-- ================= 表面 ================= -->
<section class="page">
{top}

  <div class="hd">
    <p class="pre">子どもたちが巣立った、高江ニュータウンの家。</p>
    <h1><span class="m">住み替える</span>か、<br><span class="s">この家で暮らす</span>か。</h1>
    <p class="lead">どちらも、これからのふたりにとって良い選択です。<br>樹の家こころ舎は、<em>どちらを選んでも、決めるための材料</em>をおつくりします。</p>
  </div>

  <div class="duo">
    <div class="opt mv">
      <p class="k">住み替えるなら</p>
      {ic_move}
      <p class="big"><span class="free">無料</span>この家の査定書</p>
      <ul><li>この家の、今の価値がわかる</li><li>住み替え先の予算が立てやすい</li><li>売るか住むか、数字で比べられる</li><li>急がず、比べてから決められる</li></ul>
    </div>
    <div class="vs">それとも</div>
    <div class="opt st">
      <p class="k">この家で暮らすなら</p>
      {ic_stay}
      <p class="big">ふたりのリフォーム提案</p>
      <ul><li>子ども部屋を、それぞれの部屋に</li><li>寝室は、近くて別々に</li><li>庭とつながるリビングに</li><li>間取りと費用を、具体的に</li></ul>
    </div>
  </div>

  <div class="both">
    <p><b>まだ決めなくて、大丈夫です。</b>査定書とリフォームの提案、<em>両方をそろえて</em>、ご夫婦でゆっくり比べてください。</p>
  </div>

  <div class="kijun">
    <div class="t">売るときも<br>住むときも</div>
    <p>まずは家の状態を知ることから。新耐震（1981年〜）の家でも、<em>2000年より前に建てた木造住宅</em>は、2000年に強化された接合金物や壁の配置を一度確かめておくと安心です。</p>
  </div>

{ctabox('住み替えも、この家も。<em>どちらのご相談も</em>、お電話一本で。')}</section>

<!-- ================= 裏面 ================= -->
<section class="page">
{top}

  <div class="sec cmp">
    <h2><small>どちらが正解かは、ご夫婦それぞれ</small>住み替える？ この家で暮らす？</h2>
    <table>
      <colgroup><col style="width:33mm"><col><col></colgroup>
      <thead><tr><th class="x">比べること</th><th class="a">駅近くのマンションへ住み替え</th><th class="b">この家をリフォーム</th></tr></thead>
      <tbody>
        <tr><th>暮らしの便利さ</th><td>駅・買い物・病院が近い</td><td>車が中心。静かで落ち着いた環境</td></tr>
        <tr><th>広さと庭</th><td>コンパクトで、掃除や管理が楽</td><td>今の広さと庭を、そのまま生かせる</td></tr>
        <tr><th>費用</th><td>購入費・引越し代、管理費・修繕積立金</td><td>工事費。範囲はご予算に合わせて</td></tr>
        <tr><th>荷物と思い出</th><td>広さに合わせて整理し、身軽に</td><td>必要な分だけ整理すればよい</td></tr>
        <tr><th>ご近所</th><td>新しい街で、新しいつながりを</td><td>今のつながりのまま</td></tr>
      </tbody>
    </table>
  </div>

  <div class="sec pair">
    <h2><small>どちらを選んでも</small>樹の家こころ舎が、<em>ここまで</em>おつくりします</h2>
    <div class="pp">
      <div class="pc mv">
        <p class="k">住み替えるなら<b><span class="free">無料</span>査定書</b></p>
        <div class="in">{doc}<ul><li>この家の査定価格と、その根拠</li><li>住み替え先を探すときの予算の目安に</li><li>ご自宅を見て、おつくりします</li><li>ご相談だけでも大丈夫です</li></ul></div>
      </div>
      <div class="pc st">
        <p class="k">この家で暮らすなら<b>リフォームの提案</b></p>
        <div class="in pl">{plan(True)}<ul><li>子ども部屋2つを、書斎と趣味室に</li><li>和室とLDKをつなげ、庭を眺める居間に</li></ul></div>
      </div>
    </div>
    <p class="note">※間取りは一例です。お住まいに合わせてご提案します。</p>
  </div>

{staffhtml('家を診て、<br>間取りを描きます', 'ウッドデッキも、<br>この手でつくります')}{flow([('お電話', '迷っていることを<br>お聞かせください'), ('ご自宅へ', '家と庭を一緒に<br>見て回ります'), ('お渡し', '査定書や<br>リフォームの提案を'), ('ご決断', 'ご夫婦で、ゆっくり<br>決めてください')])}
{ctabox('これからの暮らし方を、<em>ご夫婦で一緒に</em>考えましょう。')}</section>
</body></html>
'''
open(F + 'takae/flyer-takae.html', 'w', encoding='utf-8').write(html)
print('written A')
