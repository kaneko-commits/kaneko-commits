import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from takae_icons import ic1, ic3, plan
from takae_common import *

G = '#5d7d45'; W = '#c8643b'; FO = '#3a5144'; BR = '#8a6a45'
def svg(body, c):
    return f'<svg viewBox="0 0 60 40" fill="none" stroke="{c}" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round">{body}</svg>'
def t(x, y, s, c, fs=5.5):
    return f'<text x="{x}" y="{y}" font-size="{fs}" fill="{c}" stroke="none" text-anchor="middle" font-family="Noto Sans JP" font-weight="900">{s}</text>'
ic_doma = svg('<path d="M8 18 26 6l18 12"/><path d="M11 16v20h30V16"/><path d="M11 28h14v8"/><rect x="11" y="28" width="14" height="8" fill="#efe3d3" stroke="none"/><path d="M11 28h14v8"/>' + t(18, 34.5, '土間', BR, 4.8) + '<path d="M31 22h7v6h-7z"/><path d="M50 36V27"/><circle cx="50" cy="23" r="4"/>', W)
ic_hanare = svg('<path d="M4 20 17 9l13 11"/><path d="M7 18v18h20V18"/><path d="M38 26l8-6 8 6"/><path d="M40 25v11h12V25"/><path d="M44 36v-5h4v5"/><path d="M27 33h13" stroke-dasharray="1.5 2"/><path d="M2 36h56"/>', G)
ic_garage = svg('<path d="M6 16 30 6l24 10v20H6z"/><path d="M12 36V21h36v15"/><path d="M12 25h36M12 29h36"/><path d="M18 36v-4h10v4" stroke="' + FO + '"/><path d="M38 33l4-4M41 29l2-2" stroke="' + FO + '"/>', BR)
ic_guest = svg('<rect x="6" y="20" width="30" height="10" rx="2"/><path d="M6 30v4M36 30v4"/><rect x="9" y="16" width="9" height="5" rx="1.5"/><circle cx="47" cy="17" r="4"/><path d="M41 32c1-6 11-6 12 0"/><circle cx="55" cy="22" r="2.5"/><path d="M51.5 32c.5-4 6.5-4 7 0"/>', W)
ic_plus = ic1

ideas = [
    (ic3, '庭とつながる<br>ウッドデッキ', '朝ごはんも、夕涼みも、<br>デッキで。'),
    (ic_doma, '土間のある<br>暮らし', '庭仕事や趣味の道具も、<br>そのまま置ける土間に。'),
    (ic_hanare, '趣味の<br>はなれ・小屋', '敷地のゆとりを生かして、<br>庭に小さなはなれを。'),
    (ic_garage, 'ガレージ・<br>作業場', '車いじりやDIYを楽しむ、<br>自分だけの場所。'),
    (ic_plus, '子ども部屋を<br>それぞれの部屋に', '書斎、アトリエ、<br>音楽の部屋に。'),
    (ic_guest, '孫が泊まれる<br>部屋', '帰ってくる家族を、<br>ゆったり迎えられる。'),
]
cards = ''.join(f'      <div class="idea">{i}<b>{b}</b><p>{p}</p></div>\n' for i, b, p in ideas)

html = head('高江ニュータウンだからできるリフォーム', css('takae.css', 'takae_b.css')) + f'''
<!-- ================= 表面 ================= -->
<section class="page">
{top}

  <div class="hd">
    <p class="pre">敷地にゆとりがあり、家も比較的新しい。</p>
    <h1><small>高江ニュータウンだからできる。</small><em>こんなリフォーム</em>。</h1>
    <p class="lead">子どもたちが巣立ったいま、<em>夫婦ふたりだからこそ楽しめる暮らし</em>を。<br>この街の家だから、できることがあります。</p>
  </div>

  <div class="why">
    <div><span class="n">理由<b>1</b></span><p><b>敷地にゆとりがある</b>庭やデッキ、はなれ、ガレージまで。外の暮らしを、ぐっと広げられます。</p></div>
    <div><span class="n">理由<b>2</b></span><p><b>家が比較的新しい</b>新耐震以降の家が多く、直す工事より<em>楽しむ工事</em>にご予算を回しやすい。</p></div>
  </div>

  <div class="sec six">
    <h2><small>ふたりで楽しむ</small>たとえば、こんなリフォーム</h2>
    <div class="ideas">
{cards}    </div>
  </div>

{ctabox('ふたりで楽しむリフォーム、<em>ご相談はお電話一本で</em>。')}</section>

<!-- ================= 裏面 ================= -->
<section class="page">
{top}

  <div class="sec day">
    <h2><small>リフォームのあと</small>ふたりの一日は、こう変わる</h2>
    <ol>
      <li><span>朝</span><b>デッキで朝ごはん</b><p>庭を眺めて、<br>ふたりでコーヒー。</p></li>
      <li><span>昼</span><b>土間で庭仕事</b><p>道具も長靴も、<br>土間にそのまま。</p></li>
      <li><span>夕方</span><b>それぞれの部屋で</b><p>書斎とアトリエで、<br>自分の時間。</p></li>
      <li><span>週末</span><b>孫が泊まりに</b><p>広い居間と庭に、<br>みんなで。</p></li>
    </ol>
  </div>

  <div class="sec plan">
    <h2><small>たとえば、こんな間取りに</small>ふたりで楽しむ家へ</h2>
    <div class="pv">
      <figure><figcaption>いま</figcaption>{plan(False)}</figure>
      <div class="ar">▶</div>
      <figure class="af"><figcaption>リフォーム後</figcaption>{plan(True)}</figure>
    </div>
    <p class="note">※間取りは一例です。お住まいに合わせてご提案します。</p>
  </div>

  <div class="kijun">
    <div class="t">楽しむ前に<br>家の状態を</div>
    <p>新耐震（1981年〜）の家でも、<em>2000年より前に建てた木造住宅</em>は、2000年に強化された接合金物や壁の配置を、一度確かめておくと安心です。</p>
  </div>

  <div class="satei"><span class="free">無料</span>住み替えもお考えの方には、<b>この家の査定書</b>もおつくりします。</div>

{staffhtml('家を診て、<br>楽しむ間取りを描きます', 'デッキも小屋も、<br>この手でつくります')}{flow([('お電話', 'やりたいことを<br>お聞かせください'), ('ご自宅へ', '家と庭を一緒に<br>見て回ります'), ('ご提案', '間取りと費用を<br>ご説明します'), ('工事', 'ご納得いただけたら<br>着工します')])}
{ctabox('夫婦ふたりの、<em>これからの楽しみ</em>を一緒に描きましょう。')}</section>
</body></html>
'''
open(F + 'takae/flyer-takae-tanoshimu.html', 'w', encoding='utf-8').write(html)
print('written B')
