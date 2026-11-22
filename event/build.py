"""完成見学会チラシのQRからリンクするイベントページ（マンション版・アパート版）を生成する。

    python3 build.py   ->  mansion.html（分譲マンションにお住まいの子育て世帯向け）
                           apartment.html（アパートにお住まいの子育て世帯向け）

アイコン・暮らしのポイントは ../flyer/build.py と共通です。
黄色い点線の【要確認】は、公開前に埋める箇所です（納品メモ参照）。
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).parent
_spec = importlib.util.spec_from_file_location('flyer_build', HERE.parent / 'flyer' / 'build.py')
fb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fb)

PRODUCT = 'atelier'  # 商品名
EXAMPLE_LAND = 2000  # 価格例に使う土地の金額（万円）
TEL = '0972-83-5918'


def ph(text):
    """公開前に埋める箇所（黄色い点線）"""
    return f'<span class="ph">{text}</span>'


# ---------------------------------------------------------------- 版ごとの文言
VARIANTS = {
    'mansion': dict(
        file='mansion.html',
        title='マンションからの住み替え｜S様邸 注文住宅 完成見学会｜樹の家こころ舎',
        desc='ご希望の土地に、注文住宅を定額制で。金池小校区・庭と駐車場3台のS様邸 完成見学会。マンションからの住み替えのご相談もどうぞ。ご予約制・無料・お子さま連れ歓迎。',
        h1='「走らないで！」って、<br><em>本当は言いたくない。</em>',
        lead_big='下の階を気にせず、<br class="sp">家でも庭でも思いきり。',
        lead='ご希望の土地に、庭と駐車場のある注文住宅を定額制で。<br class="sp">マンションからの住み替えという選択肢。',
        q='マンションの<br class="sp">「ちょっと不便」、<br class="sp">ありませんか？',
        icons=[('kid', '子どもの足音が<br>気になる'), ('box', '収納が足りず<br>一部屋が物置に'), ('tower', '機械式駐車場の<br>出庫待ち'),
               ('door', '駐車場から<br>玄関が遠い'), ('bbq', '七輪やBBQが<br>できない')],
        scene_h='人生で何時間、<br class="sp"><em>車が下りてくるのを</em><br class="sp">待つんだろう。',
        scene_sub='機械式駐車場の出庫待ちは、<b>年間約36時間</b>。<br><small>※1回3分・1日2回で試算</small>',
        now_label='いまのマンション',
        scenes=[
            ('子ども', '「走らないで！」と、今日も言ってしまう', '吹抜けのリビングに響く足音を、笑って聞いていられる'),
            ('駐車場', '寝た子を抱いて、機械式の出庫待ち', '玄関の前に3台分。抱っこのまま数歩で家の中へ'),
            ('収納', '開かずの一部屋に、段ボールが積み上がる', 'ベビーカーもBBQ道具も外部収納へ。部屋は家族のために'),
            ('週末', 'BBQは車で遠くの公園まで。片付けでへとへと', '南の小さな庭で七輪。焼ける間に、子どもは水遊び'),
            ('お金', '機械式の更新で、修繕積立金が上がる不安', '管理費・駐車場代はゼロ。修繕は自分たちのペースで計画'),
        ],
        down_hint='マンションの売却額を頭金に充てる場合は、その見込み額を入れてください。',
        event='住み替え相談会',
        consult_h='見学のついでに、<br class="sp"><em>住み替えの順番</em>まで<br class="sp">整理できます。',
        consult=[
            ('いまのマンション、いくらで売れる？', '売却の考え方と、査定の受け方をご説明します。売却はお客様がお選びの不動産会社で行っていただきます。'),
            ('売るのが先？ 建てるのが先？', '「売り先行」「建て先行」それぞれの流れと、仮住まいが要るかどうかを一緒に確認します。'),
            ('二重ローンにならない？', 'ローン残債と売却の見込みから、無理のない資金計画を試算します。'),
            ('共働きの住宅ローンは、どう組む？', 'ペアローン・収入合算など、ご夫婦の働き方やライフプランに合わせた組み方を比較します。'),
        ],
        gift1=('住み替え資金シミュレーション', 'ローン残債・売る順番・二重ローンの不安まで整理'),
        faq=[
            ('マンションを売るかどうか、まだ決めていません。参加してもいいですか？', 'もちろん大丈夫です。「戸建てにしたら暮らしがどう変わるか」を実際の家で確かめるだけでも、ぜひお越しください。'),
            ('マンションの売却もお願いできますか？', '売却は、お客様がお選びの不動産会社で行っていただきます。売る順番や資金計画は、こころ舎で一緒に整理します。'),
            ('ローンが残っていても、住み替えはできますか？', '売却額と残債の関係によって方法が変わります。見学会の「住み替え資金シミュレーション」で、お客様の場合を試算します。'),
            ('子ども連れで行っても大丈夫ですか？', 'お子さま連れ歓迎です。実際に走り回って、足音を気にしなくていい暮らしを体感してください。'),
            ('しつこい営業はありませんか？', '無理な売り込みはいたしません。見学だけで帰られても大丈夫です。'),
        ],
        current_options=['分譲マンション（持ち家）', '賃貸マンション・アパート', 'その他'],
        current_default=0,
        topics=['住み替えの順番・売却の考え方', 'ローン残債・二重ローンの不安', '共働きの住宅ローン（ペアローン・収入合算）', '月々の支払いの比較', '土地探し（金池小校区など）', '見学だけしたい'],
        note='※マンションの売却は、お客様がお選びの不動産会社で行っていただきます。※出庫待ち時間は1回3分・1日2回で試算した目安です。',
    ),
    'apartment': dict(
        file='apartment.html',
        title='アパートから家づくり｜S様邸 注文住宅 完成見学会｜樹の家こころ舎',
        desc='ご希望の土地に、注文住宅を定額制で。金池小校区・庭と駐車場3台のS様邸 完成見学会。資金計画のご相談もどうぞ。ご予約制・無料・お子さま連れ歓迎。',
        h1='駅チカがいい。<br><em>でも、マンションは嫌。</em>',
        lead_big='希望の土地に、<br class="sp">注文住宅という選択肢があったんだ。',
        lead='駅の近くでも、子育てしやすいエリアでも。建物は定額制。<br class="sp">子どもが小さいいまも、その先も、住みやすい家を。',
        q='「走らないで」って、<br class="sp">本当は言いたくない。',
        icons=[('kid', '子どもの足音が<br>気になる'), ('box', '収納が足りず<br>一部屋が物置に'), ('yen', '家賃を払っても<br>何も残らない'),
               ('far', '駐車場が<br>家から離れている'), ('wall', '壁が薄くて<br>お隣の音が気になる')],
        scene_h='アパートの毎日は、<br class="sp"><em>こう変わります。</em>',
        scene_sub='引っ越したあとの、ある一日を想像してみてください。',
        now_label='いまのアパート',
        scenes=[
            ('子ども', '「走らないで！」と、今日も言ってしまう', '吹抜けのリビングに響く足音を、笑って聞いていられる'),
            ('駐車場', '雨の日、離れた月極から子どもを抱えて歩く', '玄関の前に3台分。抱っこのまま数歩で家の中へ'),
            ('収納', '押し入れはいっぱい。一部屋が物置に', 'ベビーカーもBBQ道具も外部収納へ。部屋は家族のために'),
            ('週末', 'BBQは車で遠くの公園まで。片付けでへとへと', '南の小さな庭で七輪。焼ける間に、子どもは水遊び'),
            ('お金', '家賃を払っても、手元に何も残らない', '毎月の支払いが、土地と家という資産に変わっていく'),
        ],
        down_hint='頭金なしで考える場合は、0のままで大丈夫です。',
        event='家づくり相談会',
        consult_h='見学のついでに、<br class="sp"><em>無理のない資金計画</em>まで<br class="sp">確かめられます。',
        consult=[
            ('いくらまでなら、無理なく借りられる？', 'ご夫婦の収入やこれからのライフプランから、無理のない借入額と月々の返済額を試算します。'),
            ('頭金がなくても大丈夫？', '頭金なしで組む場合も含めて、収入から無理のない予算を試算します。'),
            ('何から始めればいい？', '土地探し・資金計画・プランづくりの順番と、S様が実際にかかった期間をご説明します。'),
            ('共働きの住宅ローンは、どう組む？', 'ペアローン・収入合算など、ご夫婦の働き方やライフプランに合わせた組み方を比較します。'),
        ],
        gift1=('家づくり資金シミュレーション', 'ご夫婦の収入・ライフプランから、無理のない予算と返済計画を試算'),
        faq=[
            ('まだ家を建てるか決めていません。参加してもいいですか？', 'もちろん大丈夫です。「何から始めればいいかわからない」段階のご相談がいちばん多いです。'),
            ('頭金がなくても家は建てられますか？', '頭金なしで家づくりをされる方もいらっしゃいます。見学会の「家づくり資金シミュレーション」で、お客様の場合を試算します。'),
            ('土地を持っていなくても大丈夫ですか？', '大丈夫です。S様も土地探しから始めました。気になる土地があれば「建つかどうか」ラフプランでお見せします。'),
            ('子ども連れで行っても大丈夫ですか？', 'お子さま連れ歓迎です。実際に走り回って、足音を気にしなくていい暮らしを体感してください。'),
            ('しつこい営業はありませんか？', '無理な売り込みはいたしません。見学だけで帰られても大丈夫です。'),
        ],
        current_options=['賃貸アパート・マンション', '社宅・官舎', '分譲マンション（持ち家）', 'その他'],
        current_default=0,
        topics=['無理のない借入額・月々の返済額', '頭金・住宅ローンのこと', '共働きの住宅ローン（ペアローン・収入合算）', '土地探し（金池小校区など）', '家づくりの進め方', '見学だけしたい'],
        note='「頭金がない」「何から始めればいいかわからない」段階からのご相談で大丈夫です。',
    ),
}

# ---------------------------------------------------------------- CSS
CSS = """
:root{--ink:#1f2a25;--muted:#5f6a63;--soft:#8a948d;--forest:#2f4438;--deep:#1f2f27;--deeper:#17231d;--sage:#8a9a8c;--paper:#fbfaf7;--ivory:#f5f2ea;--line:#dcd6c8;--line2:#e9e4d8;--accent:#a8714a;--accent-d:#8c5b38;--gold:#cdb37e;--mint:#eef1ec}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--paper);color:var(--ink);font-family:'Noto Sans JP',sans-serif;font-weight:400;font-size:15.5px;line-height:2;letter-spacing:.03em;padding-bottom:68px;-webkit-font-smoothing:antialiased}
img,svg{max-width:100%;display:block}
a{color:inherit}
em{font-style:normal}
b{font-weight:500}
.ph{background:#fff5b8;outline:1.5px dashed #d4a800;padding:0 .3em;border-radius:2px;color:var(--ink)!important;letter-spacing:0;text-shadow:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
.narrow{max-width:780px}
br.sp{display:inline}
@media(min-width:720px){br.sp{display:none}}
.en{font-family:'Cormorant Garamond',serif;font-weight:500;letter-spacing:.14em}

/* header */
.hd{position:sticky;top:0;z-index:20;background:#fbfaf7f0;backdrop-filter:blur(8px);border-bottom:1px solid var(--line2)}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;height:60px}
.logo{text-decoration:none;line-height:1.3}
.logo small{display:block;font-size:10px;color:var(--soft);letter-spacing:.08em}
.logo b{font-family:'Noto Serif JP',serif;font-weight:500;font-size:18px;letter-spacing:.2em;color:var(--forest)}
.hd .btn{padding:9px 18px;font-size:13px}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.8em;background:var(--forest);color:#fff;text-decoration:none;font-weight:500;letter-spacing:.12em;border-radius:2px;padding:15px 30px;border:1px solid var(--forest);cursor:pointer;font-size:15px;font-family:inherit;transition:background .25s,color .25s}
.btn:after{content:'';width:18px;height:1px;background:currentColor;transition:width .25s}
.btn:hover{background:var(--deep)}
.btn:hover:after{width:26px}
.btn.ghost{background:transparent;color:var(--forest)}
.btn.ghost:hover{background:var(--mint)}
.btn.light{background:var(--gold);border-color:var(--gold);color:var(--deeper)}
.btn.light:hover{background:#d9c290}
.btn.lg{font-size:16px;padding:18px 40px}
.btn.plain:after{display:none}

/* hero */
.hero{position:relative;color:#fff;min-height:min(94vh,800px);display:flex;align-items:flex-end;overflow:hidden;background:var(--deeper)}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:60% 50%}
.hero:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,#121b16c7 0%,#121b1680 30%,#121b1600 55%,#121b16d9 90%)}
.hero .wrap{position:relative;z-index:1;width:100%;padding-top:48px;padding-bottom:56px;display:flex;flex-direction:column;min-height:inherit}
.hero .to{align-self:flex-start;font-size:12px;letter-spacing:.16em;padding-bottom:8px;border-bottom:1px solid #ffffff80}
.hero h1{font-family:'Noto Serif JP',serif;font-weight:500;font-size:clamp(25px,7.4vw,64px);line-height:1.55;margin-top:22px;letter-spacing:.06em;white-space:nowrap;text-shadow:0 2px 20px #0009,0 0 2px #0006}
.hero h1 em{color:var(--gold)}
.hero .lead{margin-top:auto;padding-top:120px;max-width:820px}
.hero .lead b{display:block;font-family:'Noto Serif JP',serif;font-weight:500;font-size:clamp(18px,4.2vw,26px);line-height:1.7;letter-spacing:.06em;text-shadow:0 2px 12px #0008}
.hero .lead span{display:block;font-size:14px;margin-top:12px;color:#ffffffde;text-shadow:0 1px 8px #000a}
.hero .cg{position:absolute;top:14px;right:16px;font-size:10px;letter-spacing:.1em;color:#ffffffb3;z-index:1}
.hero .scroll{position:absolute;right:24px;bottom:0;z-index:1;writing-mode:vertical-rl;font-size:11px;letter-spacing:.3em;color:#ffffffb3;padding-bottom:64px}
.hero .scroll:after{content:'';position:absolute;bottom:0;left:50%;width:1px;height:52px;background:#ffffff80}
@media(max-width:720px){.hero .scroll{display:none}}

/* event card */
.card{position:relative;z-index:2;margin-top:-28px;background:#fff;border:1px solid var(--line);box-shadow:0 20px 50px -24px #1f2f2740}
.card .top{display:grid;grid-template-columns:1fr auto;align-items:end;gap:8px 24px;padding:28px 28px 22px;border-bottom:1px solid var(--line2)}
.card .lbl{grid-column:1/3;display:flex;align-items:center;gap:12px;font-size:12px;letter-spacing:.2em;color:var(--accent)}
.card .lbl:after{content:'';flex:1;height:1px;background:var(--line2)}
.card .nm b{display:block;font-family:'Noto Serif JP',serif;font-weight:500;font-size:28px;letter-spacing:.16em;color:var(--forest);line-height:1.5}
.card .nm>span{display:block;font-size:13px;color:var(--muted);line-height:1.8}
.card .price{text-align:right;line-height:1.2}
.card .price small{display:block;font-size:11px;letter-spacing:.14em;color:var(--soft)}
.card .price b{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:44px;color:var(--ink);letter-spacing:.02em}
.card .price b small{display:inline;font-family:'Noto Serif JP',serif;font-size:14px;color:var(--ink);letter-spacing:.06em}
.card dl{display:grid;grid-template-columns:7em 1fr;padding:6px 28px}
.card dt,.card dd{padding:14px 0;border-bottom:1px solid var(--line2);font-size:15px}
.card dl>*:nth-last-child(-n+2){border-bottom:0}
.card dt{font-size:12px;letter-spacing:.2em;color:var(--soft);padding-top:17px}
.card dd small{display:block;font-size:12.5px;color:var(--muted);line-height:1.8}
.card .act{padding:24px 28px 26px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:center;background:var(--ivory)}
.card .act p{width:100%;text-align:center;font-size:12px;color:var(--soft)}
@media(max-width:620px){.card .top{grid-template-columns:1fr;padding:24px 22px 18px}.card .lbl{grid-column:1}.card .price{text-align:left}.card dl{padding:4px 22px;grid-template-columns:5.5em 1fr}.card .act{padding:22px}.card .act .btn{width:100%}}

/* section */
section.s{padding:104px 0}
section.s.alt{background:var(--ivory)}
.head{text-align:center;margin-bottom:56px}
.eyebrow{display:flex;align-items:center;justify-content:center;gap:14px;font-family:'Cormorant Garamond',serif;font-weight:500;font-size:15px;letter-spacing:.24em;color:var(--accent);margin-bottom:18px;text-transform:uppercase}
.eyebrow:before,.eyebrow:after{content:'';width:28px;height:1px;background:currentColor;opacity:.6}
.h2{font-family:'Noto Serif JP',serif;font-weight:500;font-size:clamp(22px,5vw,32px);line-height:1.75;letter-spacing:.08em}
.h2 em{color:var(--accent)}
.sub{color:var(--muted);margin-top:18px;font-size:14.5px}
.sub b{color:var(--accent);font-weight:500}
@media(max-width:720px){section.s{padding:80px 0}.head{margin-bottom:40px}}

/* concerns */
.icons{display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.ic{text-align:center;padding:36px 12px 30px;border-left:1px solid var(--line2)}
.ic:first-child{border-left:0}
.ic .n{font-family:'Cormorant Garamond',serif;font-size:14px;letter-spacing:.14em;color:var(--soft)}
.ic svg{width:46px;height:46px;margin:14px auto 16px;fill:none;stroke:var(--forest);stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.ic p{font-size:14px;line-height:1.8}
@media(max-width:820px){.icons{grid-template-columns:1fr}.ic{display:grid;grid-template-columns:36px 44px 1fr;align-items:center;gap:14px;text-align:left;padding:18px 4px;border-left:0;border-top:1px solid var(--line2)}.ic:first-child{border-top:0}.ic svg{width:38px;height:38px;margin:0}.ic p br{display:none}}
.answer{margin-top:56px;text-align:center;font-family:'Noto Serif JP',serif;font-weight:500;font-size:clamp(17px,4vw,22px);color:var(--forest);line-height:1.9;letter-spacing:.06em}
.answer em{color:var(--accent)}

/* scenes */
.scene-hd,.scene{display:grid;grid-template-columns:7em 1fr 48px 1.15fr;align-items:stretch}
.scene-hd{font-size:12px;letter-spacing:.2em;padding-bottom:12px;border-bottom:1px solid var(--ink)}
.scene-hd span:nth-child(2){color:var(--soft)}
.scene-hd span:nth-child(4){color:var(--forest)}
.scene{border-bottom:1px solid var(--line)}
.scene>*{padding:22px 0;display:flex;align-items:center}
.scene .lb{font-family:'Noto Serif JP',serif;font-weight:500;color:var(--forest);letter-spacing:.14em}
.scene .now{color:var(--soft);font-size:14.5px;padding-right:12px}
.scene .ar{justify-content:center}
.scene .ar:before{content:'';width:24px;height:1px;background:var(--accent);box-shadow:none}
.scene .ar:after{content:'';width:6px;height:6px;border-top:1px solid var(--accent);border-right:1px solid var(--accent);transform:rotate(45deg);margin-left:-6px}
.scene .fut{color:var(--ink);font-weight:500}
.scene small{display:none}
@media(max-width:720px){
 .scene-hd{display:none}
 .scene{grid-template-columns:1fr;padding:22px 0}
 .scene>*{padding:0}
 .scene .lb{font-size:14px;margin-bottom:8px}
 .scene .ar{display:none}
 .scene .now,.scene .fut{align-items:baseline;line-height:1.8}
 .scene .fut{margin-top:6px}
 .scene small{display:inline-block;flex:none;width:5.4em;white-space:nowrap;font-size:11px;letter-spacing:.12em;color:var(--soft);font-weight:400}
 .scene .fut small{color:var(--accent)}
}

/* house */
.spec{display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid var(--ink);border-bottom:1px solid var(--line)}
.spec div{padding:22px 10px;text-align:center;border-left:1px solid var(--line2)}
.spec div:first-child{border-left:0}
.spec small{display:block;font-size:11px;letter-spacing:.2em;color:var(--soft)}
.spec b{font-family:'Noto Serif JP',serif;font-weight:500;font-size:19px;color:var(--forest);letter-spacing:.06em}
@media(max-width:720px){.spec{grid-template-columns:repeat(2,1fr)}.spec div{border-top:1px solid var(--line2)}.spec div:nth-child(-n+2){border-top:0}.spec div:nth-child(odd){border-left:0}.spec div:last-child{grid-column:1/3;border-left:0}}
.spec-note{font-size:13px;color:var(--muted);text-align:center;margin-top:14px}
.pts{list-style:none;display:grid;grid-template-columns:repeat(3,1fr);gap:0 48px;margin-top:64px}
.pts li{padding:28px 0;border-top:1px solid var(--line)}
.pts .n{font-family:'Cormorant Garamond',serif;font-size:30px;line-height:1;color:var(--accent);letter-spacing:.04em}
.pts b{display:block;font-family:'Noto Serif JP',serif;font-weight:500;font-size:17px;margin-top:14px;letter-spacing:.06em}
.pts span{display:block;color:var(--muted);font-size:14px;line-height:1.9;margin-top:6px}
@media(max-width:820px){.pts{grid-template-columns:1fr;margin-top:40px}.pts li{display:grid;grid-template-columns:52px 1fr;column-gap:8px;padding:22px 0}.pts .n{grid-row:1/3;font-size:26px}.pts b{margin-top:0}}

/* product */
.plan-lead{color:var(--muted);font-size:15px;line-height:2.1}
.plan-lead b{color:var(--ink)}
.ptbl{margin-top:48px;border-top:1px solid var(--ink);border-bottom:1px solid var(--line)}
.ptbl .pl{padding:16px 4px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:4px 12px;align-items:baseline;border-bottom:1px solid var(--line2)}
.ptbl .pl span{font-family:'Noto Serif JP',serif;font-weight:500;letter-spacing:.08em}
.ptbl .pl small{font-size:12px;color:var(--soft);letter-spacing:.1em}
.ptbl .row{display:grid;grid-template-columns:repeat(4,1fr)}
.ptbl .pt{text-align:center;padding:34px 6px 22px;border-left:1px solid var(--line2);position:relative;line-height:1.4}
.ptbl .pt:first-child{border-left:0}
.ptbl .pt span{display:block;font-size:13px;letter-spacing:.14em;color:var(--muted)}
.ptbl .pt b{display:block;font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(28px,5.6vw,40px);margin:6px 0 2px;letter-spacing:.02em}
.ptbl .pt b small{font-family:'Noto Serif JP',serif;font-size:13px;letter-spacing:.06em}
.ptbl .pt em{font-size:11px;color:var(--soft)}
.ptbl .pt.cur{background:#fff}
.ptbl .pt.cur b{color:var(--accent)}
.ptbl .pt i{position:absolute;top:10px;left:50%;transform:translateX(-50%);font-style:normal;font-size:10px;letter-spacing:.2em;color:var(--accent);white-space:nowrap}
.ptbl .pn{font-size:12px;color:var(--soft);padding:12px 4px;border-top:1px solid var(--line2)}
@media(max-width:520px){.ptbl .row{grid-template-columns:repeat(2,1fr)}.ptbl .pt:nth-child(3){border-left:0}.ptbl .pt:nth-child(n+3){border-top:1px solid var(--line2)}}
.concept{margin-bottom:8px}
.concept .quote{font-family:'Noto Serif JP',serif;font-weight:500;font-size:clamp(17px,4vw,21px);line-height:2;letter-spacing:.08em;text-align:center;color:var(--forest)}
.concept .quote em{color:var(--accent)}
.concept p.body{margin-top:28px;color:var(--muted);font-size:15px;line-height:2.1}
.concept p.body b{color:var(--ink)}
.life3{list-style:none;display:grid;grid-template-columns:repeat(3,1fr);margin:56px 0 0;border-top:1px solid var(--ink);border-bottom:1px solid var(--line);position:relative}
.life3 li{padding:28px 22px 26px;border-left:1px solid var(--line2);position:relative}
.life3 li:first-child{border-left:0}
.life3 .t{font-family:'Cormorant Garamond',serif;font-size:13px;letter-spacing:.22em;color:var(--accent);text-transform:uppercase}
.life3 b{display:block;font-family:'Noto Serif JP',serif;font-weight:500;font-size:17px;letter-spacing:.06em;margin-top:6px}
.life3 span{display:block;font-size:13.5px;color:var(--muted);line-height:1.9;margin-top:8px}
.life3 svg{width:100%;max-width:150px;height:auto;margin:16px 0 4px}
.life3-note{font-size:12.5px;color:var(--soft);margin-top:12px;text-align:center}
@media(max-width:720px){.life3{grid-template-columns:1fr}.life3 li{border-left:0;border-top:1px solid var(--line2);display:grid;grid-template-columns:96px 1fr;column-gap:18px;padding:22px 0}.life3 li:first-child{border-top:0}.life3 svg{grid-row:1/4;grid-column:1;margin:4px 0 0}.life3 .t,.life3 b,.life3 span{grid-column:2}}
.pr-h{margin-top:88px;text-align:center}
.pr-h .h3{font-family:'Noto Serif JP',serif;font-weight:500;font-size:clamp(19px,4.4vw,25px);line-height:1.8;letter-spacing:.08em}
.pr-h .h3 em{color:var(--accent)}
.pr-h p{color:var(--muted);font-size:14.5px;margin-top:14px}
.ex{margin-top:28px;background:#fff;border:1px solid var(--line);padding:28px 28px 22px;text-align:center}
.ex-h{font-family:'Noto Serif JP',serif;font-weight:500;font-size:18px;letter-spacing:.08em}
.ex-h span{display:inline-block;font-size:12px;letter-spacing:.2em;color:var(--accent);border:1px solid var(--accent);padding:0 10px;margin-right:12px;vertical-align:3px;line-height:1.9}
.ex-h b{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:30px;color:var(--accent);margin:0 2px}
.ex-s{font-size:13px;color:var(--muted);margin-top:4px}
.ex .row{display:grid;grid-template-columns:repeat(4,1fr);margin-top:14px;border-top:1px solid var(--line2);border-bottom:1px solid var(--line2)}
.ex .pt{padding:16px 4px;border-left:1px solid var(--line2);line-height:1.4}
.ex .pt:first-child{border-left:0}
.ex .pt span{display:block;font-size:12.5px;color:var(--muted);letter-spacing:.1em}
.ex .pt b{display:block;font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(26px,5vw,34px);margin-top:4px}
.ex .pt b small{font-family:'Noto Serif JP',serif;font-size:12px}
.ex-n{font-size:12.5px;color:var(--soft);margin-top:14px;line-height:1.9}
@media(max-width:520px){.ex{padding:24px 16px 18px}.ex .row{grid-template-columns:repeat(2,1fr)}.ex .pt:nth-child(3){border-left:0}.ex .pt:nth-child(n+3){border-top:1px solid var(--line2)}}
.loanbox{margin-top:28px;background:var(--deep);color:#d5ddd6;text-align:center;padding:40px 28px;position:relative;font-size:14px;line-height:2}
.loanbox:before{content:'';position:absolute;inset:8px;border:1px solid #cdb37e40;pointer-events:none}
.loanbox .en{font-size:13px;color:var(--gold);letter-spacing:.24em;text-transform:uppercase}
.loanbox .lb-h{font-family:'Noto Serif JP',serif;font-weight:500;font-size:clamp(18px,4.2vw,22px);color:#fff;letter-spacing:.08em;margin:8px 0 10px;line-height:1.7}
.loanbox .btn{margin-top:20px;position:relative}
.total{margin-top:20px;font-size:14px;line-height:2;color:var(--muted)}
.total b{display:inline-block;font-size:11px;letter-spacing:.2em;color:var(--forest);border:1px solid var(--forest);padding:0 10px;margin-right:10px;line-height:1.9}
.total em{font-weight:500;color:var(--ink)}

/* timeline */
.tl{list-style:none;position:relative;display:grid;grid-template-columns:repeat(6,1fr);text-align:center}
.tl:before{content:'';position:absolute;left:8%;right:8%;top:41px;height:1px;background:var(--sage)}
.tl li{position:relative;display:flex;flex-direction:column;align-items:center;padding:0 6px}
.tl time{font-family:'Cormorant Garamond',serif;font-weight:500;color:var(--forest);font-size:18px;height:30px;letter-spacing:.06em}
.tl li i{display:block;width:9px;height:9px;border-radius:50%;background:var(--forest);outline:6px solid var(--paper);margin:3px 0 14px;position:relative;z-index:1}
.tl li.now i{background:var(--accent);width:13px;height:13px;margin:1px 0 12px}
.tl li.now b{color:var(--accent)}
.tl b{font-size:14.5px;line-height:1.6;font-weight:500}
.tl span{font-size:12px;color:var(--muted);line-height:1.7;margin-top:4px}
@media(max-width:720px){
 .tl{grid-template-columns:1fr;text-align:left;padding-left:4px}
 .tl:before{left:8px;right:auto;top:14px;bottom:14px;width:1px;height:auto}
 .tl li{display:grid;grid-template-columns:22px 96px 1fr;align-items:start;column-gap:6px;padding:0 0 22px}
 .tl li i{grid-column:1;grid-row:1/3;margin:10px 0 0}
 .tl li.now i{margin:8px 0 0 -2px}
 .tl time{grid-column:2;grid-row:1/3;height:auto;white-space:nowrap;justify-self:start;line-height:1.6}
 .tl b{grid-column:3}.tl span{grid-column:3;margin-top:0}
}

/* consult / gift */
.consult{display:grid;grid-template-columns:repeat(2,1fr);gap:0 48px}
.consult div{padding:26px 0;border-top:1px solid var(--line)}
.consult b{display:flex;gap:12px;font-family:'Noto Serif JP',serif;font-weight:500;font-size:17px;color:var(--forest);letter-spacing:.05em;line-height:1.7}
.consult b:before{content:'Q';font-family:'Cormorant Garamond',serif;font-size:22px;color:var(--accent);line-height:1.3}
.consult p{font-size:14px;color:var(--muted);margin-top:8px;padding-left:26px}
@media(max-width:720px){.consult{grid-template-columns:1fr}}
.gifts{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:48px}
.gifts div{background:var(--deep);color:#d5ddd6;padding:30px 30px 28px;font-size:14px;position:relative}
.gifts div:before{content:'';position:absolute;inset:8px;border:1px solid #cdb37e40;pointer-events:none}
.gifts small{font-family:'Cormorant Garamond',serif;font-size:13px;letter-spacing:.22em;color:var(--gold)}
.gifts b{display:block;font-family:'Noto Serif JP',serif;font-weight:500;color:#fff;font-size:18px;margin:8px 0 4px;line-height:1.6;letter-spacing:.06em}
@media(max-width:720px){.gifts{grid-template-columns:1fr}}

/* faq */
.faq{border-top:1px solid var(--ink)}
.faq details{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;padding:22px 44px 22px 40px;font-weight:500;position:relative;line-height:1.8}
.faq summary::-webkit-details-marker{display:none}
.faq summary:before{content:'Q';position:absolute;left:6px;top:19px;font-family:'Cormorant Garamond',serif;color:var(--accent);font-size:22px}
.faq summary:after{content:'';position:absolute;right:12px;top:32px;width:9px;height:9px;border-right:1px solid var(--sage);border-bottom:1px solid var(--sage);transform:rotate(45deg);transition:transform .25s}
.faq details[open] summary:after{transform:rotate(-135deg);top:36px}
.faq details p{padding:0 20px 24px 40px;color:var(--muted);font-size:14.5px}

/* reserve */
.reserve{background:var(--deep);color:#fff;padding:104px 0}
.reserve .eyebrow{color:var(--gold)}
.reserve .h2{color:#fff}
.reserve .story{font-family:'Noto Serif JP',serif;color:var(--gold);text-align:center;margin-top:22px;line-height:2;letter-spacing:.06em;font-size:15px}
.reserve .notice{font-size:13px;color:#c3cdc5;text-align:center;margin-top:10px}
form{background:var(--paper);color:var(--ink);padding:40px 36px;margin-top:48px}
@media(max-width:620px){form{padding:30px 20px}.reserve{padding:80px 0}}
.f{margin-bottom:28px}
.f>label,.f>p{display:block;font-weight:500;margin-bottom:10px;font-size:14.5px;letter-spacing:.06em}
.req,.opt{display:inline-block;font-size:10.5px;font-weight:400;letter-spacing:.1em;padding:0 8px;margin-left:10px;vertical-align:1px;line-height:1.8}
.req{border:1px solid var(--accent);color:var(--accent)}
.opt{border:1px solid var(--line);color:var(--soft)}
input[type=text],input[type=tel],input[type=email],select,textarea{width:100%;font:inherit;font-size:16px;letter-spacing:.03em;padding:13px 14px;border:1px solid var(--line);border-radius:0;background:#fff;color:var(--ink);-webkit-appearance:none;appearance:none}
select{background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6' fill='none' stroke='%238a948d'/%3E%3C/svg%3E") no-repeat right 14px center}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--forest);box-shadow:0 0 0 3px #2f443814}
input::placeholder,textarea::placeholder{color:#a9b0aa}
textarea{min-height:110px;resize:vertical}
.choices{display:grid;gap:8px}
.choices.two{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
.choices label{display:flex;align-items:center;gap:12px;border:1px solid var(--line);padding:12px 14px;cursor:pointer;font-size:14.5px;background:#fff;transition:border-color .2s,background .2s}
.choices label:has(input:checked){border-color:var(--forest);background:var(--mint)}
.choices input{accent-color:var(--forest);width:17px;height:17px;flex:none}
.people{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.people label{font-size:12.5px;color:var(--muted);letter-spacing:.1em}
.people select{margin-top:4px}
.privacy{font-size:12.5px;color:var(--muted);border-top:1px solid var(--line2);padding-top:18px;margin-bottom:22px}
form .btn{width:100%}
.form-msg{display:none;text-align:center;padding:40px 0;color:#d5ddd6}
.form-msg b{display:block;font-size:20px;color:#fff;font-family:'Noto Serif JP',serif;font-weight:500;letter-spacing:.08em;margin-bottom:10px}
.tel{margin-top:56px;text-align:center;border-top:1px solid #ffffff22;padding-top:44px}
.tel p{font-size:12px;letter-spacing:.2em;color:#c3cdc5}
.tel a{display:inline-block;font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(36px,9vw,50px);letter-spacing:.08em;text-decoration:none;color:#fff;line-height:1.4}
.tel small{display:block;font-size:12.5px;color:#c3cdc5}

/* footer */
footer{background:var(--deeper);color:#a9b5ac;font-size:12.5px;padding:48px 0 32px;line-height:2}
footer .brand{font-family:'Noto Serif JP',serif;font-weight:500;font-size:20px;letter-spacing:.22em;color:#fff;margin:2px 0 10px}
footer .notes{margin-top:20px;padding-top:20px;border-top:1px solid #ffffff1a;font-size:11.5px;color:#8e9a91}

/* sticky bar (mobile) */
.bar{position:fixed;left:0;right:0;bottom:0;z-index:30;display:grid;grid-template-columns:1fr 1.6fr;gap:8px;padding:8px 12px calc(8px + env(safe-area-inset-bottom));background:#fbfaf7f2;backdrop-filter:blur(8px);border-top:1px solid var(--line2);transition:transform .3s}
.bar a{padding:12px 4px;font-size:14px}
.bar.hide{transform:translateY(110%)}
@media(min-width:900px){.bar{display:none}body{padding-bottom:0}}

/* fade-in */
.rv{opacity:0;transform:translateY(16px);transition:opacity .9s ease,transform .9s ease}
.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}html{scroll-behavior:auto}}
"""


# ---------------------------------------------------------------- HTML
def head(en, h2, sub=''):
    return (f'<div class="head rv"><span class="eyebrow">{en}</span><h2 class="h2">{h2}</h2>'
            + (f'<p class="sub">{sub}</p>' if sub else '') + '</div>')


def build(key, v):
    icons = ''.join(
        f'<div class="ic"><span class="n">{i:02d}</span><svg viewBox="0 0 48 48" aria-hidden="true">{fb.ICON[k]}</svg><p>{lbl}</p></div>'
        for i, (k, lbl) in enumerate(v['icons'], 1))
    scenes = ''.join(
        f'<div class="scene"><div class="lb">{a}</div><div class="now"><small>いま</small>{b}</div>'
        f'<div class="ar"></div><div class="fut"><small>これから</small>{c}</div></div>'
        for a, b, c in v['scenes'])
    pts = ''.join(f'<li class="rv"><span class="n">{i:02d}</span><b>{a}</b><span>{b}</span></li>'
                  for i, (a, b) in enumerate(fb.PLAN_POINTS, 1))
    consult = ''.join(f'<div><b>{a}</b><p>{b}</p></div>' for a, b in v['consult'])
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in v['faq'])
    current = ''.join(
        f'<label><input type="radio" name="current" value="{o}"{" checked" if i == v["current_default"] else ""}>{o}</label>'
        for i, o in enumerate(v['current_options']))
    topics = ''.join(f'<label><input type="checkbox" name="topics" value="{t}">{t}</label>' for t in v['topics'])
    g1t, g1d = v['gift1']
    tel = TEL.replace('-', '')

    return f'''<!doctype html>
<html lang="ja"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{v['title']}</title>
<meta name="description" content="{v['desc']}">
<meta property="og:type" content="website"><meta property="og:title" content="{v['title']}">
<meta property="og:description" content="{v['desc']}"><meta property="og:image" content="img/ogp.jpg">
<meta name="theme-color" content="#1f2f27">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500&family=Noto+Sans+JP:wght@400;500&family=Noto+Serif+JP:wght@500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head><body>
<!-- 版：{key}（{v['now_label']}にお住まいの子育て世帯向け） -->
<header class="hd"><div class="wrap">
  <a class="logo" href="#top"><small>設計事務所がつくった工務店</small><b>樹の家こころ舎</b></a>
  <a class="btn plain" href="#reserve">見学会を予約</a>
</div></header>

<main id="top">
<div class="hero">
  <img src="img/exterior.jpg" alt="S様邸の外観イメージ。白い塗り壁の2階建てと、大きな掃き出し窓" fetchpriority="high">
  <span class="cg">※イメージCG</span>
  <div class="wrap">
    <span class="to">大分駅付近に職場があるご夫婦が建てた家</span>
    <h1>{v['h1']}</h1>
    <p class="lead"><b>{v['lead_big']}</b><span>{v['lead']}</span></p>
  </div>
  <span class="scroll en">SCROLL</span>
</div>

<div class="wrap narrow">
  <div class="card">
    <div class="top">
      <span class="lbl en">OPEN HOUSE ─ 注文住宅 完成見学会</span>
      <div class="nm"><b>S様邸</b><span>金池小・上野ヶ丘中校区／大分駅から{ph('○分')}<br>土地を読み解き一から設計する、こころ舎の「{PRODUCT}」</span></div>
      <div class="price"><small>建物は定額制（税込）</small><b>2,475<small>万円〜</small></b></div>
    </div>
    <dl>
      <dt>日時</dt><dd>{ph('【要確認】○月○日（土）・○日（日）')}<br>10:00〜17:00<small>各回{ph('○')}組限定・見学は約{ph('○分')}</small></dd>
      <dt>会場</dt><dd>大分市・金池小校区<small>個人のお住まいのため、詳しい場所はご予約時にご案内します</small></dd>
      <dt>参加費</dt><dd>無料（ご予約制）<small>ご夫婦・お子さま連れ歓迎／無理な売り込みはいたしません</small></dd>
    </dl>
    <div class="act">
      <a class="btn lg" href="#reserve">Webで予約する</a>
      <a class="btn ghost lg plain" href="tel:{tel}">電話で予約</a>
      <p>※販売物件ではありません。施主様のご厚意で公開する注文住宅です。</p>
    </div>
  </div>
</div>

<section class="s">
  <div class="wrap">
    {head('Concerns', v['q'])}
    <div class="icons rv">{icons}</div>
    <p class="answer rv">そのお悩み、<br class="sp"><em>ご希望の土地に建てる注文住宅</em>なら<br class="sp">解決できるかもしれません。</p>
  </div>
</section>

<section class="s alt">
  <div class="wrap">
    {head('Before / After', v['scene_h'], v['scene_sub'])}
    <div class="rv">
      <div class="scene-hd"><span></span><span>{v['now_label']}</span><span></span><span>S様邸での光景</span></div>
      {scenes}
    </div>
  </div>
</section>

<section class="s">
  <div class="wrap">
    {head('The House', 'S様邸の、ある一日。', '「庭は少しでいい。駐車場は3台欲しい。<br class="sp">金池小校区で家を建てたい。」')}
    <div class="spec rv">
      <div><small>土地</small><b>約44坪</b></div>
      <div><small>延床</small><b>約25坪</b></div>
      <div><small>駐車場</small><b>3台</b></div>
      <div><small>家族</small><b>4人</b></div>
      <div><small>性能</small><b style="font-size:14px">{ph('【要確認】耐震・断熱等級')}</b></div>
    </div>
    <ul class="pts">{pts}</ul>
  </div>
</section>

<section class="s alt">
  <div class="wrap narrow">
    {head(PRODUCT, f'設計し、建て続けてきた<br class="sp">私たちの答え。<br><em>「{PRODUCT}」</em>')}
    <div class="concept rv">
      <p class="quote">子どもが小さいいまも、<br class="sp">育ちざかりのころも、<br>夫婦ふたりに戻ってからも。<br><em>どの時期にも、住みやすい家</em>を。</p>
      <p class="body"><b>{PRODUCT}</b>（アトリエ）は、注文住宅の設計と施工を重ねてきた樹の家こころ舎が、その経験からたどり着いた答えです。子どもが小さい「いま」だけに合わせて間取りを決めると、数年後には使いにくい家になってしまう。だから{PRODUCT}は、家族の成長やはたらき方の変化を受け止められる<b>間取りの骨格</b>から考えます。<br>規格住宅ではありません。ご要望を伺い、土地・周辺環境・風・光・眺望まで読み解いて一から設計し、<b>設計事務所がつくった工務店</b>が施工まで一貫して手がけます。クセのない間取りだから、<b>売るときも、貸すときも価値が残りやすい</b>のも特長です。</p>
    </div>
    <ol class="life3 rv">
      <li><svg viewBox="0 0 150 80" aria-hidden="true"><rect x="2" y="2" width="146" height="76" fill="#fbfaf7" stroke="#2f4438" stroke-width="2"/><circle cx="55" cy="44" r="7" fill="none" stroke="#a8714a" stroke-width="1.6"/><circle cx="85" cy="48" r="6" fill="none" stroke="#a8714a" stroke-width="1.6"/></svg><span class="t">Now</span><b>きょうだいで広々と</b><span>子どもが小さいうちは、ひと続きの広い部屋で一緒に。</span></li>
      <li><svg viewBox="0 0 150 80" aria-hidden="true"><rect x="2" y="2" width="146" height="76" fill="#fbfaf7" stroke="#2f4438" stroke-width="2"/><line x1="75" y1="2" x2="75" y2="78" stroke="#a8714a" stroke-width="2" stroke-dasharray="5 4"/><circle cx="38" cy="42" r="8" fill="none" stroke="#a8714a" stroke-width="1.6"/><circle cx="112" cy="42" r="8" fill="none" stroke="#a8714a" stroke-width="1.6"/></svg><span class="t">Growing</span><b>成長したら、ふた部屋に</b><span>思春期には、間仕切りでそれぞれの個室へ。</span></li>
      <li><svg viewBox="0 0 150 80" aria-hidden="true"><rect x="2" y="2" width="146" height="76" fill="#fbfaf7" stroke="#2f4438" stroke-width="2"/><rect x="18" y="20" width="44" height="24" fill="none" stroke="#a8714a" stroke-width="1.6"/><line x1="96" y1="22" x2="132" y2="22" stroke="#a8714a" stroke-width="1.6"/><line x1="96" y1="34" x2="132" y2="34" stroke="#a8714a" stroke-width="1.6"/><line x1="96" y1="46" x2="132" y2="46" stroke="#a8714a" stroke-width="1.6"/></svg><span class="t">Later</span><b>夫婦ふたりの時間へ</b><span>子どもが巣立ったあとは、書斎や趣味の部屋として。</span></li>
    </ol>
    <p class="life3-note rv">子ども部屋を例にした、考え方のイメージです。S様邸の子供室7.5帖も、将来2部屋に分けられるつくりです。</p>

    <div class="pr-h rv">
      <span class="eyebrow">Price</span>
      <p class="h3"><em>ご希望の土地に</em>、<br class="sp">注文住宅を定額制で。</p>
      <p>建物は、広さごとの定額制。<br class="sp">土地の価格がわかれば、<br class="sp">総額の目安がすぐに見えてきます。</p>
    </div>
    <div class="ptbl rv">
      <div class="pl"><span>建物本体価格（定額制）</span><small>税込</small></div>
      <div class="row"><div class="pt cur"><i>S様邸</i><span>25.5坪</span><b>2,475<small>万円</small></b><em>税抜2,250万円</em></div><div class="pt"><span>27坪</span><b>2,585<small>万円</small></b><em>税抜2,350万円</em></div><div class="pt"><span>28.5坪</span><b>2,695<small>万円</small></b><em>税抜2,450万円</em></div><div class="pt"><span>30坪</span><b>2,860<small>万円</small></b><em>税抜2,600万円</em></div></div>
      <div class="pn">※付帯工事・外構・諸費用は別途　※価格は{ph('【要確認】○年○月')}時点</div>
    </div>
    <div class="ex rv">
      <p class="ex-h"><span>例えば</span>土地 <b>{EXAMPLE_LAND:,}</b>万円 の場合</p>
      <p class="ex-s">土地 {EXAMPLE_LAND:,}万円 ＋ 建物 ＝</p>
      <div class="row"><div class="pt"><span>25.5坪なら</span><b>{EXAMPLE_LAND+2475:,}<small>万円</small></b></div><div class="pt"><span>27坪なら</span><b>{EXAMPLE_LAND+2585:,}<small>万円</small></b></div><div class="pt"><span>28.5坪なら</span><b>{EXAMPLE_LAND+2695:,}<small>万円</small></b></div><div class="pt"><span>30坪なら</span><b>{EXAMPLE_LAND+2860:,}<small>万円</small></b></div></div>
      <p class="ex-n">ご希望のエリアの土地価格に置き換えて、考えてみてください。<br>※金額は計算例です。付帯工事・外構・諸費用は別途かかります（土地の条件によって変わります）。</p>
    </div>
    <div class="loanbox rv">
      <span class="en">Loan Simulation</span>
      <p class="lb-h">住宅ローンの<br class="sp">シミュレーションは、<br class="sp">見学会で。</p>
      <p>頭金・返済期間・金利タイプ、ペアローンや収入合算まで。<br>ご夫婦の収入とライフプランに合わせて、月々の返済額を一緒に試算します。</p>
      <a class="btn light" href="#reserve">見学会を予約する</a>
    </div>
  </div>
</section>

<section class="s">
  <div class="wrap">
    {head('Story', 'S様の家づくり', 'はじめてのご相談から、<br class="sp">お引渡しまで<b>約1年2ヶ月</b>。<br class="sp">走り回れる毎日は、もうすぐそこに。')}
    <ol class="tl rv">
      <li><time>2025.10</time><i></i><b>はじめてのご相談</b><span>「金池小校区で建てたい」</span></li>
      <li><time>{ph('○月')}</time><i></i><b>土地が決まる</b><span>駐車3台が叶う44坪</span></li>
      <li><time>{ph('○月')}</time><i></i><b>プランのご提案</b><span>土地を読み解き一から設計</span></li>
      <li><time>{ph('○月')}</time><i></i><b>着工</b><span>設計から施工まで一貫</span></li>
      <li class="now"><time>2026.11</time><i></i><b>完成見学会</b><span>いま、ここ</span></li>
      <li><time>2026.12</time><i></i><b>お引渡し</b><span>新しい暮らしへ</span></li>
    </ol>
  </div>
</section>

<section class="s alt">
  <div class="wrap">
    {head('Consultation', v['consult_h'], f'完成見学会 ＆ {v["event"]}。<br class="sp">ご希望の方だけ、<br class="sp">見学のあとにご相談いただけます。')}
    <div class="consult rv">{consult}</div>
    <div class="gifts rv">
      <div><small>PRIVILEGE 01</small><b>{g1t}</b>{g1d}</div>
      <div><small>PRIVILEGE 02</small><b>「建つかどうか」ラフプラン</b>気になる土地に建つプランをお見せします</div>
    </div>
  </div>
</section>

<section class="s">
  <div class="wrap narrow">
    {head('Q &amp; A', 'よくあるご質問')}
    <div class="faq rv">{faq}</div>
  </div>
</section>

<section class="reserve" id="reserve">
  <div class="wrap narrow">
    <span class="eyebrow">Reservation</span>
    <h2 class="h2" style="text-align:center">S様邸 完成見学会<br class="sp"> ＆ {v['event']}<br>ご予約</h2>
    <p class="story">「庭は少しでいい。駐車場は3台欲しい。金池小校区で家を建てたい。」<br>その想いに応えた、44坪・4人家族の家。</p>
    <p class="notice">ご予約制・無料／各回{ph('○')}組限定／会場はご予約時にご案内します</p>

    <!-- 【要確認】予約の送信先（フォームサービスのURL等）を action に設定する。未設定の間は送信せず完了表示のみ -->
    <form id="form" action="" method="post" novalidate>
      <input type="hidden" name="variant" value="{key}">
      <input type="hidden" name="source" id="source" value="">
            <div class="f"><p>ご希望の日時<span class="req">必須</span></p>
        <div class="choices two">
          <label><input type="radio" name="date" value="day1-am" required>{ph('○/○（土）')} 午前</label>
          <label><input type="radio" name="date" value="day1-pm">{ph('○/○（土）')} 午後</label>
          <label><input type="radio" name="date" value="day2-am">{ph('○/○（日）')} 午前</label>
          <label><input type="radio" name="date" value="day2-pm">{ph('○/○（日）')} 午後</label>
        </div>
      </div>
      <div class="f"><label for="name">お名前<span class="req">必須</span></label><input type="text" id="name" name="name" autocomplete="name" placeholder="例）大分 花子" required></div>
      <div class="f"><label for="tel">電話番号<span class="req">必須</span></label><input type="tel" id="tel" name="tel" autocomplete="tel" inputmode="tel" placeholder="例）090-1234-5678" required></div>
      <div class="f"><label for="email">メールアドレス<span class="opt">任意</span></label><input type="email" id="email" name="email" autocomplete="email" placeholder="予約確認をお送りします"></div>
      <div class="f"><p>ご参加人数<span class="opt">任意</span></p>
        <div class="people">
          <label>大人<select name="adults"><option>1名</option><option selected>2名</option><option>3名以上</option></select></label>
          <label>お子さま<select name="kids"><option>0名</option><option selected>1名</option><option>2名</option><option>3名以上</option></select></label>
        </div>
      </div>
      <div class="f"><p>いまのお住まい<span class="opt">任意</span></p><div class="choices">{current}</div></div>
      <div class="f"><p>ご相談したいこと<span class="opt">任意・複数可</span></p><div class="choices">{topics}</div></div>
      <div class="f"><label for="memo">ご質問・ご要望<span class="opt">任意</span></label><textarea id="memo" name="memo" placeholder="例）ベビーカーで伺います／気になる土地があります"></textarea></div>
      <p class="privacy">ご入力いただいた情報は、見学会のご案内とご相談のためにのみ使用します。{ph('【要確認】プライバシーポリシーへのリンク')}</p>
      <button class="btn lg" type="submit">この内容で予約する</button>
    </form>
    <div class="form-msg" id="done"><b>ご予約ありがとうございます。</b>担当者より、会場のご案内をお電話またはメールでお送りします。</div>

    <div class="tel">
      <p>お電話でのご予約</p>
      <a href="tel:{tel}">{TEL}</a>
      <small>受付 {ph('【要確認】9:00〜18:00')}</small>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <small>設計事務所がつくった工務店</small>
    <div class="brand">樹の家こころ舎</div>
    <p>株式会社 樹の家こころ舎　{ph('【要確認】住所・建設業許可番号')}<br>TEL {TEL}</p>
    <p class="notes">※販売物件ではありません。施主様のご厚意で公開する注文住宅です。<br>※掲載画像はイメージCGです。※価格は税込表示。付帯工事・外構・諸費用は別途です。{ph('【要確認】価格の内訳')}<br>{v['note']}</p>
  </div>
</footer>

<nav class="bar" id="bar" aria-label="予約">
  <a class="btn ghost plain" href="tel:{tel}">電話する</a>
  <a class="btn" href="#reserve">Webで予約</a>
</nav>

<script>
// チラシのQRなど、流入元をフォームに残す（例：?from=flyer）
(function(){{
  var p=new URLSearchParams(location.search);
  document.getElementById('source').value=p.get('from')||p.get('utm_source')||'';
}})();
// スクロールに合わせて、ゆっくり表示する
(function(){{
  var els=document.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in')}});return;}}
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}})}},{{rootMargin:'0px 0px -8% 0px'}});
  els.forEach(function(e){{io.observe(e)}});
}})();
// 予約フォームが見えている間は、下部の予約バーを隠す
(function(){{
  var bar=document.getElementById('bar'),r=document.getElementById('reserve');
  if(!('IntersectionObserver' in window))return;
  new IntersectionObserver(function(e){{bar.classList.toggle('hide',e[0].isIntersecting)}}).observe(r);
}})();
// 入力チェック。送信先（action）が未設定の間は送信せず、完了表示だけ確認できる
(function(){{
  var f=document.getElementById('form');
  f.addEventListener('submit',function(ev){{
    if(!f.checkValidity()){{ev.preventDefault();f.reportValidity();return;}}
    if(!f.getAttribute('action')){{ev.preventDefault();f.style.display='none';document.getElementById('done').style.display='block';
      document.getElementById('done').scrollIntoView({{behavior:'smooth',block:'center'}});}}
  }});
}})();
</script>
</body></html>
'''


SINGLE = {'mansion': '見学会ページ_マンション版.html', 'apartment': '見学会ページ_アパート版.html'}


def single_file(html):
    """写真を埋め込み、HTMLファイル1つで開ける版にする（確認・共有用）"""
    import base64
    import io
    from PIL import Image
    buf = io.BytesIO()
    Image.open(HERE / 'img' / 'exterior.jpg').resize((1280, 853)).save(buf, 'JPEG', quality=78, optimize=True, progressive=True)
    data = base64.b64encode(buf.getvalue()).decode()
    html = html.replace('src="img/exterior.jpg"', f'src="data:image/jpeg;base64,{data}"')
    html = html.replace('<meta property="og:image" content="img/ogp.jpg">', '')
    for k, name in SINGLE.items():
        html = html.replace(f'href="{VARIANTS[k]["file"]}"', f'href="{name}"')
    return html


if __name__ == '__main__':
    (HERE / 'single').mkdir(exist_ok=True)
    for key, v in VARIANTS.items():
        html = build(key, v)
        (HERE / v['file']).write_text(html, encoding='utf-8')
        (HERE / 'single' / SINGLE[key]).write_text(single_file(html), encoding='utf-8')
        print('wrote', v['file'], '/ single/' + SINGLE[key])
