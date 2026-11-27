"""判田で家を探しているアパート暮らしの方へ：高江ニュータウンの中古住宅をフルリノベーション
python3 flyer/takae-renov/src/build.py で flyer/takae-renov/flyer-takae-renov.html を生成"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'takae', 'src'))
import takae_common as C

FL = '/home/user/kaneko-commits/flyer/'
top = '''  <div class="top">
    <span class="to">判田で家を探している、アパート暮らしの皆さまへ</span>
    <div class="brand">樹の家こころ舎<small>新築もリフォームもする工務店</small></div>
  </div>'''


def room(x, y, w, h, label, fill='#fff', stroke='#5a645c', fs=7, tc='#25312c'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width=".8"/>'
            f'<text x="{x+w/2}" y="{y+h/2+2.4}" font-size="{fs}" text-anchor="middle" fill="{tc}" font-family="Noto Sans JP" font-weight="700">{label}</text>')


def plan(after):
    O, OS = '#fbeee6', '#c8643b'
    g = '<svg viewBox="0 0 162 92">'
    g += '<text x="1" y="16" font-size="6" fill="#5a645c" font-family="Noto Sans JP" font-weight="700">2階</text>'
    g += '<text x="1" y="52" font-size="6" fill="#5a645c" font-family="Noto Sans JP" font-weight="700">1階</text>'
    if not after:
        g += room(12, 2, 47, 24, '洋室') + room(59, 2, 47, 24, '洋室') + room(106, 2, 54, 24, '和室')
        g += room(12, 36, 41, 28, '和室') + room(53, 36, 50, 28, '台所・食堂', fs=6.4) + room(103, 36, 26, 28, '居間', fs=6.4) + room(129, 36, 31, 28, '水まわり', fs=6)
        g += ('<rect x="12" y="70" width="148" height="18" fill="#eef2e8" stroke="#5d7d45" stroke-width=".8" stroke-dasharray="2 1.5"/>'
              '<text x="86" y="81" font-size="6.5" text-anchor="middle" fill="#5d7d45" font-family="Noto Sans JP" font-weight="700">庭</text>')
    else:
        g += room(12, 2, 47, 24, '子ども部屋', O, OS) + room(59, 2, 47, 24, '子ども部屋', O, OS) + room(106, 2, 54, 24, '寝室＋収納', O, OS)
        g += room(12, 36, 91, 28, '家族が集まる広いLDK', O, OS) + room(103, 36, 26, 28, '家族の<tspan x="116" dy="7.5">収納</tspan>', O, OS, fs=5.6) + room(129, 36, 31, 28, '新しい<tspan x="144.5" dy="7.5">水まわり</tspan>', O, OS, fs=5.6)
        g += ('<rect x="12" y="64" width="91" height="7" fill="#d9c2a3" stroke="#8a6a45" stroke-width=".8"/>'
              '<text x="57.5" y="69.3" font-size="4.8" text-anchor="middle" fill="#5a3d1f" font-family="Noto Sans JP" font-weight="700">ウッドデッキ</text>'
              '<rect x="12" y="73" width="148" height="15" fill="#eef2e8" stroke="#5d7d45" stroke-width=".8"/>'
              '<text x="86" y="82.5" font-size="6.5" text-anchor="middle" fill="#5d7d45" font-family="Noto Sans JP" font-weight="700">子どもが遊べる庭・駐車スペース</text>')
    return g + '</svg>'


css = C.css_base + C.cta + C.staffcss + open(os.path.join(HERE, 'style.css'), encoding='utf-8').read()

bubbles = ['下の階に、足音が<br>響いていないか心配', '子どもの物が増えて、<br>部屋が手狭に',
           '駐車場が<br>足りない・遠い', '家賃を払い続けて<br>いいのかな']
bub = ''.join(f'<div class="bub">{b}</div>' for b in bubbles)

takae = [('1', '敷地にゆとりがある', '庭もデッキも、車も自転車も。<br>外の暮らしが、ぐんと広がります。'),
         ('2', '家が比較的新しい', '新耐震以降の家が多く、骨組みを<br>生かしやすい。予算を内装・断熱・<br>設備に回せます。'),
         ('3', 'まわりも一戸建て', '一戸建てが並ぶ住宅地。足音や<br>生活音を気にせず、のびのびと。'),
         ('4', '出会える家がある', '子どもが独立し、住み替える世帯も。<br>だから出会える家があります。')]
tk = ''.join(f'<div class="tk"><span class="n">{n}</span><div><b>{a}</b><p>{b}</p></div></div>' for n, a, b in takae)

ideas = ['家族が集まる<br>広いLDK', '庭につながる<br>ウッドデッキ', '帰ってすぐ片づく<br>土間収納',
         '家族みんなの<br>ファミリークローゼット', '断熱で、<br>夏も冬も快適に', '成長に合わせて<br>仕切れる子ども部屋']
idea = ''.join(f'<li>{i}</li>' for i in ideas)

flowhtml = C.flow([('ご相談', 'ローン診断と<br>ライフプランから'), ('物件探し', '高江ニュータウンの<br>家を一緒に探します'), ('無料の建物診断', '買う前に、家の<br>状態を確かめます'), ('設計・工事', 'お引き渡しまで<br>しっかりと')]).replace('お打ち合わせは、<em>すべてご自宅で</em>。', '家探しから、<em>住むまでずっと</em>。')
html = C.head('高江ニュータウン 中古住宅をフルリノベーション', css) + f'''
<!-- ================= 表面 ================= -->
<section class="page">
{top}

  <div class="hd">
    <p class="pre q">「やっぱり、判田に住みたい」</p>
    <h1>高江ニュータウンの家を、<br><em>まるごとリノベーション</em>。</h1>
    <p class="lead">新築だけが、マイホームじゃない。中古の一戸建てを買って、<br>家族に合わせてつくり直す。<em>判田で暮らす、もうひとつの選択肢</em>です。</p>
  </div>

  <div class="photo">
    <figure style="background-image:url('../reform-usuki/img/living.jpg');background-position:50% 60%"></figure>
    <figure style="background-image:url('../reform-usuki/img/kitchen.jpg');background-position:50% 55%"></figure>
    <p class="cap">樹の家こころ舎の施工例</p>
  </div>

  <div class="worries">
    <h2>アパート暮らしで、こんなこと気になりませんか？</h2>
    <div class="bubbles">{bub}</div>
  </div>

  <div class="sec front">
    <h2><small>判田で暮らすなら</small>高江ニュータウンだからこそ、<em>できること</em></h2>
    <div class="tks">{tk}</div>
  </div>


{C.ctabox('物件探し・<em>無料の建物診断</em>・ローンのご相談まで、お電話一本で。')}</section>

<!-- ================= 裏面 ================= -->
<section class="page">
{top}


  <div class="sec ideas6">
    <h2><small>骨組みを生かして、中はまるごと新しく</small>フルリノベで、こんな暮らしに</h2>
    <ul>{idea}</ul>
    <p class="note">土地から買って新築するのとは別の、<em>もうひとつの予算の組み方</em>です。</p>
  </div>

  <div class="sec support">
    <h2><small>家探しから、住むまで</small>まるごと、<em>お手伝いします</em></h2>
    <div class="sp">
      <div><span class="t">物件探し</span><b>家を、<br>一緒に探します</b><p>高江ニュータウンで、<br>リノベに向いた家を<br>一緒に探します。</p></div>
      <div><span class="t">建物診断</span><span class="free">無料</span><b>買う前に、<br>家を見ます</b><p>耐震診断士が、柱や<br>基礎、雨漏りの跡まで<br>確かめます。</p></div>
      <div><span class="t">お金のこと</span><b>ローン診断と<br>ライフプラン</b><p>購入費とリノベ費用を<br>合わせて、無理のない<br>返済計画を一緒に。</p></div>
    </div>
  </div>

{C.staffhtml('買う前に家を診て、<br>暮らしを描きます', '古い家も、<br>この手で新しく').replace('ご自宅に伺うのは、', 'ご一緒するのは、')}{flowhtml}
{C.ctabox('判田で、<em>庭のある一戸建て</em>を。まずはお電話ください。')}</section>
</body></html>
'''
open(FL + 'takae-renov/flyer-takae-renov.html', 'w', encoding='utf-8').write(html)
print('written')
