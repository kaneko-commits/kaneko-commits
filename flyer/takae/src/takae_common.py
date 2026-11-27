import os
D = os.path.dirname(os.path.abspath(__file__))
F = '/home/user/kaneko-commits/flyer/'
src = open(F + 'handadai/flyer-handadai.html', encoding='utf-8').read()
css_base = src[src.index('@page'):src.index('/* ===== 表面 ===== */')]
cta = src[src.index('.cta{'):src.index('/* ===== 裏面 ===== */')]
staffcss = src[src.index('.staff{'):src.index('/* 相談会 */')]
tel = src[src.index('<div class="tel">'):src.index('<p class="hours">')]
_staff = src[src.index('  <div class="staff">'):src.index('  <div class="flow">')]


def staffhtml(kudo, himeno):
    return (_staff.replace('家を診て、<br>3つの方法を描きます', kudo)
                  .replace('残したい柱も、<br>この手で生かします', himeno))


co = ('<p class="hours">受付時間 9:00〜18:00（水曜定休）　「チラシを見た」とお伝えください</p>\n'
      '    <p class="co">設計事務所がつくった工務店　株式会社 樹の家こころ舎　〒870-1132 大分県大分市大字光吉566番地1</p>')
top = '''  <div class="top">
    <span class="to">高江ニュータウンにお住まいの皆さまへ</span>
    <div class="brand">樹の家こころ舎<small>新築もリフォームもする工務店</small></div>
  </div>'''


def css(*extra):
    return css_base + cta + staffcss + ''.join(open(os.path.join(D, e), encoding='utf-8').read() for e in extra)


def head(title, cssstr):
    return f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<title>{title}｜樹の家こころ舎</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@500;700;900&family=Noto+Serif+JP:wght@600;700;900&family=Zen+Maru+Gothic:wght@700&display=swap" rel="stylesheet">
<style>
{cssstr}</style></head>
<body>
'''


def flow(steps):
    lis = ''.join(f'      <li><b>{b}</b><span>{s}</span></li>\n' for b, s in steps)
    return f'''  <div class="flow">
    <h4>お打ち合わせは、<em>すべてご自宅で</em>。</h4>
    <ol>
{lis}    </ol>
  </div>
'''


def ctabox(msg, extra=''):
    return f'''  <div class="cta">
    <p class="msg">{msg}</p>{extra}
    {tel}{co}
  </div>
'''
