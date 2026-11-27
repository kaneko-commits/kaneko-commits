ic1='<svg viewBox="0 0 60 40" fill="none" stroke="#3a5144" stroke-width="1.8"><rect x="4" y="6" width="24" height="28" rx="1"/><rect x="32" y="6" width="24" height="28" rx="1"/><path d="M9 28h14M12 28v-6h8v6" stroke="#c8643b"/><circle cx="44" cy="20" r="4" stroke="#c8643b"/><path d="M38 31c2-4 10-4 12 0" stroke="#c8643b"/><text x="16" y="15" font-size="6" fill="#3a5144" stroke="none" text-anchor="middle" font-family="Noto Sans JP" font-weight="700">書斎</text><text x="44" y="13" font-size="6" fill="#3a5144" stroke="none" text-anchor="middle" font-family="Noto Sans JP" font-weight="700">趣味</text></svg>'
ic2='<svg viewBox="0 0 60 40" fill="none" stroke="#c8643b" stroke-width="1.8"><rect x="4" y="6" width="52" height="28" rx="1"/><path d="M30 6v28" stroke-dasharray="2 2"/><rect x="9" y="17" width="16" height="11" rx="1.5"/><rect x="35" y="17" width="16" height="11" rx="1.5"/><path d="M9 20.5h5M35 20.5h5"/></svg>'
ic3='<svg viewBox="0 0 60 40" fill="none" stroke="#5d7d45" stroke-width="1.8"><path d="M4 18 18 8l14 10"/><path d="M7 16v18h22V16"/><path d="M29 29h17" stroke="#8a6a45" stroke-width="2.6"/><path d="M31 29v5M44 29v5" stroke="#8a6a45"/><path d="M51 34V23"/><circle cx="51" cy="18" r="5"/><path d="M57 34v-6"/><circle cx="57" cy="25" r="2.6"/></svg>'
K=1.38
def X(x): return round(12+(x-12)*K,2)
def W(w): return round(w*K,2)
def room(x,y,w,h,label,fill='#fff',stroke='#5a645c',fs=7,tc='#25312c'):
    return f'<rect x="{X(x)}" y="{y}" width="{W(w)}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width=".8"/><text x="{X(x)+W(w)/2}" y="{y+h/2+2.4}" font-size="{fs}" text-anchor="middle" fill="{tc}" font-family="Noto Sans JP" font-weight="700">{label}</text>'
def band(x,y,w,h,label,fill,stroke,tc,fs=6.5,dash=False):
    d=' stroke-dasharray="2 1.5"' if dash else ''
    return f'<rect x="{X(x)}" y="{y}" width="{W(w)}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width=".8"{d}/><text x="{X(x)+W(w)/2}" y="{y+h/2+2.2}" font-size="{fs}" text-anchor="middle" fill="{tc}" font-family="Noto Sans JP" font-weight="700">{label}</text>'
def plan(after):
    g='<svg viewBox="0 0 162 92">'
    g+='<text x="1" y="16" font-size="6" fill="#5a645c" font-family="Noto Sans JP" font-weight="700">2階</text>'
    if not after:
        g+=room(12,2,34,24,'子ども部屋')+room(46,2,34,24,'子ども部屋')+room(80,2,38,24,'主寝室')
    else:
        g+=room(12,2,34,24,'夫の書斎','#fbeee6','#c8643b')+room(46,2,34,24,'妻の趣味室','#fbeee6','#c8643b')+room(80,2,38,24,'寝室')
        g+=f'<path d="M{X(99)} 3v14" stroke="#c8643b" stroke-width=".9" stroke-dasharray="1.5 1.2"/><text x="{X(99)}" y="24" font-size="5" text-anchor="middle" fill="#c8643b" font-family="Noto Sans JP" font-weight="700">仕切れる</text>'
    g+='<text x="1" y="52" font-size="6" fill="#5a645c" font-family="Noto Sans JP" font-weight="700">1階</text>'
    if not after:
        g+=room(12,36,30,28,'和室')+room(42,36,50,28,'LDK')+room(92,36,26,28,'水まわり',fs=6.2)
        g+=band(12,70,106,18,'庭（あまり使っていない）','#eef2e8','#5d7d45','#5d7d45',dash=True)
    else:
        g+=room(12,36,80,28,'庭を眺める広いLDK','#fbeee6','#c8643b')+room(92,36,26,28,'水まわり',fs=6.2)
        g+=band(12,64,80,7,'ウッドデッキ','#d9c2a3','#8a6a45','#5a3d1f',fs=5.2)
        g+=band(12,73,106,15,'家庭菜園・お茶ができる庭','#eef2e8','#5d7d45','#5d7d45')
    return g+'</svg>'
