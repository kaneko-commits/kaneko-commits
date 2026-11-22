"""完成見学会チラシのQRからリンクするイベントページ（マンション版・アパート版）を生成する。

    python3 build.py   ->  mansion.html（分譲マンションにお住まいの子育て世帯向け）
                           apartment.html（アパートにお住まいの子育て世帯向け）

アイコン・間取り図・暮らしのポイントは ../flyer/build.py と共通です。
黄色い点線の【要確認】は、公開前に埋める箇所です（納品メモ参照）。
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).parent
_spec = importlib.util.spec_from_file_location('flyer_build', HERE.parent / 'flyer' / 'build.py')
fb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fb)

PRODUCT = 'essence atelier'  # 商品名（チラシと合わせる）
TEL = '0972-83-5918'


def ph(text):
    """公開前に埋める箇所（黄色い点線）"""
    return f'<span class="ph">{text}</span>'


# ---------------------------------------------------------------- 版ごとの文言
VARIANTS = {
    'mansion': dict(
        file='mansion.html',
        title='マンションからの住み替え｜S様邸 注文住宅 完成見学会｜樹の家こころ舎',
        desc='大分駅近く・金池小校区。庭と駐車場3台のある注文住宅の完成見学会。マンションからの住み替えのご相談もどうぞ。ご予約制・無料・お子さま連れ歓迎。',
        h1='「走らないで！」って、<br><em>本当は言いたくない。</em>',
        lead_big='下の階を気にせず、<br class="sp">家でも庭でも思いきり。',
        lead='駅近に、庭と駐車場のある注文住宅を。<br class="sp">マンションからの住み替えという選択肢。',
        q='マンションの<br class="sp">「ちょっと不便」、<br class="sp">ありませんか？',
        icons=[('kid', '子どもの足音が<br>気になる'), ('box', '収納が足りず<br>一部屋が物置に'), ('tower', '機械式駐車場の<br>出庫待ち'),
               ('door', '駐車場から<br>玄関が遠い'), ('bbq', '七輪やBBQが<br>できない')],
        scene_h='人生で何時間、<br class="sp"><em>車が下りてくるのを</em><br class="sp">待つんだろう。',
        scene_sub='機械式駐車場の出庫待ちは、<b>年間約36時間</b>。※1回3分・1日2回で試算',
        now_label='いまのマンション',
        scenes=[
            ('子ども', '「走らないで！」と、今日も言ってしまう', '吹抜けのリビングに響く足音を、笑って聞いていられる'),
            ('駐車場', '寝た子を抱いて、機械式の出庫待ち', '玄関の前に3台分。抱っこのまま数歩で家の中へ'),
            ('収納', '開かずの一部屋に、段ボールが積み上がる', 'ベビーカーもBBQ道具も外部収納へ。部屋は家族のために'),
            ('週末', 'BBQは車で遠くの公園まで。片付けでへとへと', '南の小さな庭で七輪。焼ける間に、子どもは水遊び'),
            ('お金', '機械式の更新で、修繕積立金が上がる不安', '管理費・駐車場代はゼロ。修繕は自分たちのペースで計画'),
        ],
        now_cost='いまのローン＋管理費・修繕積立金＋駐車場代',
        new_cost_note='売却額を頭金に',
        event='住み替え相談会',
        consult_h='見学のついでに、<br class="sp"><em>住み替えの順番</em>まで<br class="sp">整理できます。',
        consult=[
            ('いまのマンション、いくらで売れる？', '売却の考え方と、査定の受け方をご説明します。売却はお客様がお選びの不動産会社で行っていただきます。'),
            ('売るのが先？ 建てるのが先？', '「売り先行」「建て先行」それぞれの流れと、仮住まいが要るかどうかを一緒に確認します。'),
            ('二重ローンにならない？', 'ローン残債と売却の見込みから、無理のない資金計画を試算します。'),
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
        topics=['住み替えの順番・売却の考え方', 'ローン残債・二重ローンの不安', '月々の支払いの比較', '土地探し（金池小校区など）', '見学だけしたい'],
        note='※マンションの売却は、お客様がお選びの不動産会社で行っていただきます。※出庫待ち時間は1回3分・1日2回で試算した目安です。',
    ),
    'apartment': dict(
        file='apartment.html',
        title='アパートから家づくり｜S様邸 注文住宅 完成見学会｜樹の家こころ舎',
        desc='大分駅近く・金池小校区。庭と駐車場3台のある注文住宅の完成見学会。「いまの家賃で建つ？」もご相談ください。ご予約制・無料・お子さま連れ歓迎。',
        h1='駅チカがいい。<br><em>でも、マンションは嫌。</em>',
        lead_big='大分駅近く、<br class="sp">マンション以外の選択肢があったんだ。',
        lead='庭と駐車場のある、街なかの注文住宅。<br class="sp">家賃を払い続ける暮らしから、卒業しませんか。',
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
        now_cost='いまの家賃＋駐車場代',
        new_cost_note='頭金なし',
        event='家づくり相談会',
        consult_h='見学のついでに、<br class="sp"><em>「いまの家賃で建つ？」</em>を<br class="sp">確かめられます。',
        consult=[
            ('いまの家賃と、月々いくら違う？', 'いまの家賃・駐車場代と、S様邸のような家の月々の支払いを並べて比べます。'),
            ('頭金がなくても大丈夫？', '頭金なしで組む場合も含めて、収入から無理のない予算を試算します。'),
            ('何から始めればいい？', '土地探し・資金計画・プランづくりの順番と、S様が実際にかかった期間をご説明します。'),
        ],
        gift1=('家づくり資金シミュレーション', 'いまの家賃・収入から、無理のない予算を試算'),
        faq=[
            ('まだ家を建てるか決めていません。参加してもいいですか？', 'もちろん大丈夫です。「何から始めればいいかわからない」段階のご相談がいちばん多いです。'),
            ('頭金がなくても家は建てられますか？', '頭金なしで家づくりをされる方もいらっしゃいます。見学会の「家づくり資金シミュレーション」で、お客様の場合を試算します。'),
            ('土地を持っていなくても大丈夫ですか？', '大丈夫です。S様も土地探しから始めました。気になる土地があれば「建つかどうか」ラフプランでお見せします。'),
            ('子ども連れで行っても大丈夫ですか？', 'お子さま連れ歓迎です。実際に走り回って、足音を気にしなくていい暮らしを体感してください。'),
            ('しつこい営業はありませんか？', '無理な売り込みはいたしません。見学だけで帰られても大丈夫です。'),
        ],
        current_options=['賃貸アパート・マンション', '社宅・官舎', '分譲マンション（持ち家）', 'その他'],
        current_default=0,
        topics=['いまの家賃で建つか知りたい', '頭金・住宅ローンのこと', '土地探し（金池小校区など）', '家づくりの進め方', '見学だけしたい'],
        note='「頭金がない」「何から始めればいいかわからない」段階からのご相談で大丈夫です。',
    ),
}

# ---------------------------------------------------------------- CSS
CSS = """
:root{--ink:#25312c;--muted:#5d675f;--forest:#3a5144;--deep:#283a30;--sage:#7d9583;--ivory:#faf9f5;--cream:#f2f0e8;--line:#d6d8cf;--warm:#c8643b;--warm-d:#a94f2b;--sun:#f3d27a;--mint:#eef3ee}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--ivory);color:var(--ink);font-family:'Noto Sans JP',sans-serif;font-size:16px;line-height:1.8;padding-bottom:72px}
img,svg{max-width:100%;display:block}
a{color:inherit}
em{font-style:normal}
.serif{font-family:'Noto Serif JP',serif}
.ph{background:#fff5b8;outline:1.5px dashed #d4a800;padding:0 .3em;border-radius:3px;color:var(--ink)}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
.narrow{max-width:760px}
br.sp{display:inline}
@media(min-width:720px){br.sp{display:none}}

/* header */
.hd{position:sticky;top:0;z-index:20;background:#faf9f5ee;backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;height:56px}
.logo{text-decoration:none;line-height:1.2}
.logo small{display:block;font-size:10px;color:var(--muted);letter-spacing:.04em}
.logo b{font-family:'Noto Serif JP',serif;font-size:18px;letter-spacing:.12em;color:var(--forest)}
.hd .btn{padding:8px 16px;font-size:14px}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.5em;background:var(--warm);color:#fff;text-decoration:none;font-weight:700;border-radius:999px;padding:14px 28px;border:0;cursor:pointer;font-size:16px;font-family:inherit;transition:background .2s}
.btn:hover{background:var(--warm-d)}
.btn.ghost{background:transparent;border:1.5px solid currentColor;color:var(--forest)}
.btn.ghost:hover{background:var(--mint)}
.btn.lg{font-size:18px;padding:18px 36px}

/* hero */
.hero{position:relative;color:#fff;min-height:min(92vh,760px);display:flex;align-items:flex-end;overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:60% 50%}
.hero:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,#1c2a2299 0%,#1c2a2233 35%,#1c2a2200 50%,#1c2a22cc 85%)}
.hero .wrap{position:relative;z-index:1;width:100%;padding-top:40px;padding-bottom:36px;display:flex;flex-direction:column;min-height:inherit}
.hero .to{align-self:flex-start;background:var(--warm);font-size:13px;font-weight:700;padding:4px 12px;letter-spacing:.06em}
.hero h1{font-family:'Noto Serif JP',serif;font-weight:700;font-size:clamp(26px,7.8vw,68px);line-height:1.4;margin-top:16px;letter-spacing:.02em;white-space:nowrap;text-shadow:0 2px 16px #0006}
.hero h1 em{color:var(--sun)}
.hero .lead{margin-top:auto;padding-top:120px}
.hero .lead b{display:block;font-family:'Noto Serif JP',serif;font-size:clamp(20px,4.6vw,30px);line-height:1.5;text-shadow:0 2px 10px #0008}
.hero .lead span{display:block;font-size:15px;margin-top:8px;text-shadow:0 1px 6px #000a}
.hero .cg{position:absolute;top:12px;right:12px;font-size:11px;background:#0006;padding:2px 8px;z-index:1}

/* event card */
.card{position:relative;z-index:2;margin-top:-20px;background:#fff;border:1.5px solid var(--forest);border-radius:12px;box-shadow:0 6px 24px #0002;overflow:hidden}
.card .top{display:flex;flex-wrap:wrap}
.card .tag{background:var(--forest);color:#fff;font-weight:900;padding:14px 20px;display:flex;flex-direction:column;justify-content:center;line-height:1.4;letter-spacing:.08em;font-size:14px}
.card .tag b{color:var(--sun);font-size:20px}
.card .nm{flex:1;min-width:240px;padding:14px 20px}
.card .nm b{font-family:'Noto Serif JP',serif;font-size:24px;letter-spacing:.12em;color:var(--forest)}
.card .nm>span{display:block;font-size:13px;color:var(--muted);font-weight:700;line-height:1.6}
.card .price{padding:14px 20px;text-align:center;border-left:1px solid var(--line);display:flex;flex-direction:column;justify-content:center}
.card .price small{font-size:12px;color:var(--muted);font-weight:700}
.card .price b{font-family:Georgia,serif;font-weight:400;font-size:34px;line-height:1.1;color:var(--warm)}
.card .price b small{font-family:'Noto Sans JP';font-size:14px;color:var(--warm);font-weight:700}
.card dl{display:grid;grid-template-columns:auto 1fr;border-top:1px solid var(--line)}
.card dt,.card dd{padding:10px 20px;border-bottom:1px solid var(--line);font-size:15px}
.card dt{font-weight:700;color:var(--forest);background:var(--mint);white-space:nowrap}
.card dd small{display:block;font-size:12px;color:var(--muted)}
.card .act{padding:18px 20px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:center;background:var(--cream)}
.card .act p{width:100%;text-align:center;font-size:13px;color:var(--muted)}
@media(max-width:620px){.card .price{border-left:0;border-top:1px solid var(--line);width:100%;flex-direction:row;align-items:baseline;gap:12px;justify-content:center}.card .tag{width:100%;flex-direction:row;gap:10px;align-items:baseline;padding:10px 20px}}

/* section */
section.s{padding:72px 0}
section.s.alt{background:var(--cream)}
.h2{font-family:'Noto Serif JP',serif;font-weight:700;font-size:clamp(24px,5.4vw,34px);line-height:1.5;letter-spacing:.04em;text-align:center}
.h2 em{color:var(--warm)}
.sub{text-align:center;color:var(--muted);font-weight:700;margin-top:10px;font-size:15px}
.sub b{color:var(--warm)}
.eyebrow{display:block;text-align:center;font-size:12px;letter-spacing:.24em;color:var(--sage);font-weight:700;margin-bottom:8px}

/* icons */
.icons{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:24px 16px;margin-top:40px}
.ic{text-align:center}
.ic .c{position:relative;width:104px;height:104px;margin:0 auto;border-radius:50%;background:#fff;border:1px solid var(--line);display:flex;align-items:center;justify-content:center}
.ic .c:after{content:'×';position:absolute;top:-2px;right:-2px;width:30px;height:30px;border-radius:50%;background:var(--warm);color:#fff;font-weight:900;display:flex;align-items:center;justify-content:center;font-size:18px;line-height:1}
.ic svg{width:56px;height:56px;fill:none;stroke:var(--forest);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.ic p{margin-top:12px;font-weight:700;font-size:15px;line-height:1.5}
.answer{margin-top:44px;text-align:center;font-family:'Noto Serif JP',serif;font-weight:700;font-size:clamp(19px,4.4vw,24px);color:var(--forest);line-height:1.6}
.answer em{color:var(--warm)}

/* scenes */
.scenes{margin-top:36px;display:grid;gap:12px}
.scene{display:grid;grid-template-columns:88px 1fr 32px 1.2fr;background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden}
.scene>*{padding:16px;display:flex;align-items:center}
.scene .lb{font-weight:900;color:var(--forest);justify-content:center;background:var(--mint)}
.scene .now{color:var(--muted);font-size:15px}
.scene .ar{color:var(--warm);font-weight:900;justify-content:center;padding:0}
.scene .fut{background:var(--forest);color:#fff;font-weight:700}
.scene small{display:none}
.scene-hd{display:grid;grid-template-columns:88px 1fr 32px 1.2fr;font-size:13px;font-weight:700;text-align:center}
.scene-hd span:nth-child(2){color:var(--muted)}
.scene-hd span:nth-child(4){color:var(--forest)}
@media(max-width:720px){
 .scene-hd{display:none}
 .scene{grid-template-columns:1fr}
 .scene>*{padding:12px 16px}
 .scene .lb{justify-content:flex-start;padding:8px 16px}
 .scene .ar{display:none}
 .scene small{display:block;font-size:11px;font-weight:700;letter-spacing:.08em;margin-right:12px;white-space:nowrap;opacity:.75}
 .scene .now,.scene .fut{align-items:baseline}
}

/* money */
.money{margin-top:28px;display:grid;grid-template-columns:1fr 40px 1fr;border-radius:12px;overflow:hidden}
.money>div{padding:20px;display:flex;flex-direction:column;justify-content:center}
.money .m-now{background:#e7e7e2;color:var(--muted)}
.money .m-new{background:var(--forest);color:#fff}
.money .m-ar{background:linear-gradient(90deg,#e7e7e2 50%,var(--forest) 50%);color:var(--warm);font-weight:900;align-items:center;padding:0}
.money span{font-size:14px;line-height:1.5}
.money b{font-size:26px;margin-top:6px;white-space:nowrap}
.money .m-new b{color:var(--sun)}
.money-note{font-size:12px;color:var(--muted);margin-top:8px;text-align:center}
@media(max-width:620px){.money{grid-template-columns:1fr}.money .m-ar{background:linear-gradient(180deg,#e7e7e2 50%,var(--forest) 50%);height:32px}.money .m-ar:before{content:'▼'}.money .m-ar span{display:none}}

/* house */
.spec{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:10px;overflow:hidden;margin-top:32px}
.spec div{background:#fff;padding:14px;text-align:center}
.spec small{display:block;font-size:12px;color:var(--muted);font-weight:700}
.spec b{font-size:20px;color:var(--forest)}
.plans{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:20px;margin-top:28px;align-items:end}
.plans figure{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px}
.plans figcaption{font-weight:700;color:var(--forest);font-size:14px;margin-bottom:8px}
.plans figcaption small{font-weight:500;color:var(--muted);margin-left:6px}
.plans svg{width:100%;height:auto;font-family:'Noto Sans JP',sans-serif}
.plan-note{font-size:12px;color:var(--muted);margin-top:8px;text-align:right}
@media(max-width:820px){.plans{grid-template-columns:1fr}}
.pts{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:28px;counter-reset:p}
.pts li{background:#fff;border-radius:10px;padding:16px 18px 16px 60px;position:relative;border:1px solid var(--line);counter-increment:p}
.pts li:before{content:counter(p);position:absolute;left:16px;top:16px;width:30px;height:30px;border-radius:50%;background:var(--warm);color:#fff;font-weight:900;display:flex;align-items:center;justify-content:center;font-size:15px}
.pts b{display:block;font-size:17px}
.pts span{display:block;color:var(--muted);font-size:14px;line-height:1.7;margin-top:2px}

/* product */
.plan-lead{margin-top:20px;color:var(--muted);font-size:15px}
.plan-lead b{color:var(--forest)}
.ptbl{margin-top:24px;border:1.5px solid var(--warm);border-radius:12px;overflow:hidden;background:#fff}
.ptbl .pl{background:var(--warm);color:#fff;padding:12px 18px;font-weight:700;display:flex;justify-content:space-between;flex-wrap:wrap;gap:4px 12px;align-items:baseline}
.ptbl .pl small{font-size:13px;opacity:.9}
.ptbl .row{display:grid;grid-template-columns:repeat(4,1fr)}
.ptbl .pt{text-align:center;padding:16px 6px;border-left:1px solid var(--line);position:relative;line-height:1.3}
.ptbl .pt:first-child{border-left:0}
.ptbl .pt span{display:block;font-size:14px;font-weight:700;color:var(--muted)}
.ptbl .pt b{display:block;font-family:Georgia,serif;font-weight:400;font-size:clamp(20px,4.6vw,30px);margin:4px 0}
.ptbl .pt b small{font-family:'Noto Sans JP';font-size:13px;font-weight:700}
.ptbl .pt em{font-size:11px;color:var(--muted)}
.ptbl .pt.cur{background:#fbeee6}
.ptbl .pt.cur b{color:var(--warm)}
.ptbl .pt i{position:absolute;top:0;left:0;font-style:normal;font-size:11px;font-weight:900;background:var(--warm);color:#fff;padding:0 8px}
.ptbl .pn{font-size:12px;color:var(--muted);padding:10px 18px;border-top:1px solid var(--line)}
@media(max-width:520px){.ptbl .row{grid-template-columns:repeat(2,1fr)}.ptbl .pt:nth-child(3){border-left:0}.ptbl .pt:nth-child(n+3){border-top:1px solid var(--line)}}
.total{margin-top:16px;background:#fff;border-radius:10px;padding:14px 18px;border:1px solid var(--line);font-size:15px}
.total b{display:inline-block;background:var(--forest);color:#fff;font-size:13px;padding:2px 10px;border-radius:4px;margin-right:8px}
.total em{font-weight:900;color:var(--warm)}

/* timeline */
.tl{list-style:none;margin-top:36px;position:relative;display:grid;grid-template-columns:repeat(6,1fr);text-align:center}
.tl:before{content:'';position:absolute;left:8%;right:8%;top:38px;height:3px;background:var(--sage)}
.tl li{position:relative;display:flex;flex-direction:column;align-items:center;padding:0 4px}
.tl time{font-family:Georgia,serif;font-weight:700;color:var(--forest);font-size:15px;height:26px}
.tl li i{display:block;width:20px;height:20px;border-radius:50%;background:var(--forest);border:4px solid var(--ivory);margin:2px 0 8px;position:relative;z-index:1;box-sizing:content-box}
.tl li.now i{background:var(--warm)}
.tl li.now b{color:var(--warm)}
.tl b{font-size:15px;line-height:1.4}
.tl span{font-size:12px;color:var(--muted);line-height:1.5;margin-top:2px}
@media(max-width:720px){
 .tl{grid-template-columns:1fr;text-align:left;gap:0;padding-left:8px}
 .tl:before{left:21px;right:auto;top:12px;bottom:12px;width:3px;height:auto}
 .tl li{display:grid;grid-template-columns:28px 92px 1fr;align-items:start;column-gap:8px;padding:0 0 18px}
 .tl li i{grid-column:1;grid-row:1/3;margin:4px 0 0}
 .tl time{grid-column:2;grid-row:1/3;height:auto;padding-top:2px;white-space:nowrap;justify-self:start}
 .tl b{grid-column:3}.tl span{grid-column:3;margin-top:0}
}

/* consult / gift */
.consult{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:32px}
.consult div{background:#fff;border-radius:12px;padding:20px;border-top:4px solid var(--sage)}
.consult b{display:block;font-size:17px;color:var(--forest)}
.consult b:before{content:'Q. ';color:var(--warm)}
.consult p{font-size:14px;color:var(--muted);margin-top:6px}
.gifts{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:24px}
.gifts div{background:var(--deep);color:#dfe7de;border-radius:12px;padding:20px;font-size:14px}
.gifts small{display:inline-block;background:var(--warm);color:#fff;font-weight:700;font-size:12px;padding:1px 10px;border-radius:999px}
.gifts b{display:block;color:var(--sun);font-size:18px;margin:6px 0 2px;line-height:1.5}

/* faq */
.faq{margin-top:32px;display:grid;gap:10px}
.faq details{background:#fff;border:1px solid var(--line);border-radius:10px}
.faq summary{list-style:none;cursor:pointer;padding:16px 48px 16px 52px;font-weight:700;position:relative;line-height:1.6}
.faq summary::-webkit-details-marker{display:none}
.faq summary:before{content:'Q';position:absolute;left:18px;top:15px;font-family:Georgia,serif;color:var(--warm);font-size:20px;line-height:1.3}
.faq summary:after{content:'＋';position:absolute;right:18px;top:16px;color:var(--sage)}
.faq details[open] summary:after{content:'−'}
.faq details p{padding:0 20px 18px 52px;color:var(--muted);font-size:15px}

/* reserve */
.reserve{background:var(--deep);color:#fff;padding:72px 0}
.reserve .h2{color:#fff}
.reserve .sub{color:#cfdccf}
.reserve .story{font-family:'Noto Serif JP',serif;color:var(--sun);text-align:center;font-weight:700;margin-top:16px;line-height:1.7}
.reserve .notice{font-size:13px;color:#cfdccf;text-align:center;margin-top:10px}
form{background:#fff;color:var(--ink);border-radius:14px;padding:28px 22px;margin-top:32px}
.f{margin-bottom:22px}
.f>label,.f>p{display:block;font-weight:700;margin-bottom:8px;font-size:15px}
.req,.opt{display:inline-block;font-size:11px;font-weight:700;padding:0 8px;border-radius:3px;margin-left:8px;vertical-align:2px}
.req{background:var(--warm);color:#fff}
.opt{background:var(--line);color:var(--muted)}
input[type=text],input[type=tel],input[type=email],select,textarea{width:100%;font:inherit;font-size:16px;padding:12px 14px;border:1.5px solid var(--line);border-radius:8px;background:var(--ivory);color:var(--ink)}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--forest);background:#fff}
textarea{min-height:96px;resize:vertical}
.choices{display:grid;gap:8px}
.choices.two{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
.choices label{display:flex;align-items:center;gap:10px;border:1.5px solid var(--line);border-radius:8px;padding:11px 14px;cursor:pointer;font-size:15px;background:var(--ivory)}
.choices label:has(input:checked){border-color:var(--forest);background:var(--mint);font-weight:700}
.choices input{accent-color:var(--forest);width:18px;height:18px;flex:none}
.people{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.people label{font-size:14px;color:var(--muted);font-weight:700}
.privacy{font-size:13px;color:var(--muted);background:var(--cream);border-radius:8px;padding:12px 14px;margin-bottom:18px}
form .btn{width:100%}
.form-msg{display:none;text-align:center;padding:24px 0}
.form-msg b{display:block;font-size:20px;color:var(--forest);font-family:'Noto Serif JP',serif}
.tel{margin-top:32px;text-align:center;border-top:1px solid #ffffff2a;padding-top:28px}
.tel p{font-size:14px;color:#cfdccf}
.tel a{display:inline-block;font-family:Georgia,serif;font-size:clamp(32px,8vw,44px);letter-spacing:.04em;text-decoration:none;color:#fff;line-height:1.3}
.tel small{display:block;font-size:13px;color:#cfdccf}

/* footer */
footer{background:#1f2d25;color:#b9c6ba;font-size:13px;padding:32px 0 24px;line-height:1.8}
footer .brand{font-family:'Noto Serif JP',serif;font-size:20px;letter-spacing:.12em;color:#fff}
footer .notes{margin-top:14px;font-size:12px}

/* sticky bar (mobile) */
.bar{position:fixed;left:0;right:0;bottom:0;z-index:30;display:grid;grid-template-columns:1fr 1.6fr;gap:8px;padding:8px 12px calc(8px + env(safe-area-inset-bottom));background:#faf9f5f2;backdrop-filter:blur(6px);border-top:1px solid var(--line);transition:transform .25s}
.bar a{border-radius:10px;padding:12px 4px;font-size:15px}
.bar .btn.ghost{border-width:1.5px}
.bar.hide{transform:translateY(110%)}
@media(min-width:900px){.bar{display:none}body{padding-bottom:0}}
"""


# ---------------------------------------------------------------- HTML
def build(key, v):
    icons = ''.join(
        f'<div class="ic"><div class="c"><svg viewBox="0 0 48 48" aria-hidden="true">{fb.ICON[k]}</svg></div><p>{lbl}</p></div>'
        for k, lbl in v['icons'])
    scenes = ''.join(
        f'<div class="scene"><div class="lb">{a}</div><div class="now"><small>いま</small>{b}</div>'
        f'<div class="ar">▶</div><div class="fut"><small>S様邸</small>{c}</div></div>'
        for a, b, c in v['scenes'])
    pts = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in fb.PLAN_POINTS)
    consult = ''.join(f'<div><b>{a}</b><p>{b}</p></div>' for a, b in v['consult'])
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in v['faq'])
    current = ''.join(
        f'<label><input type="radio" name="current" value="{o}"{" checked" if i == v["current_default"] else ""}>{o}</label>'
        for i, o in enumerate(v['current_options']))
    topics = ''.join(f'<label><input type="checkbox" name="topics" value="{t}">{t}</label>' for t in v['topics'])
    g1t, g1d = v['gift1']
    other = 'apartment.html' if key == 'mansion' else 'mansion.html'

    return f'''<!doctype html>
<html lang="ja"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{v['title']}</title>
<meta name="description" content="{v['desc']}">
<meta property="og:type" content="website"><meta property="og:title" content="{v['title']}">
<meta property="og:description" content="{v['desc']}"><meta property="og:image" content="img/ogp.jpg">
<meta name="theme-color" content="#283a30">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Noto+Serif+JP:wght@500;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head><body>
<!-- 版：{key}（{v['now_label']}にお住まいの子育て世帯向け） -->
<header class="hd"><div class="wrap">
  <a class="logo" href="#top"><small>設計事務所がつくった工務店</small><b>樹の家こころ舎</b></a>
  <a class="btn" href="#reserve">見学会を予約</a>
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
</div>

<div class="wrap narrow">
  <div class="card">
    <div class="top">
      <div class="tag">注文住宅<b>完成見学会</b></div>
      <div class="nm"><b>S様邸</b><span>金池小・上野ヶ丘中校区／大分駅から{ph('○分')}<br>土地を読み解き一から設計する、こころ舎の「{PRODUCT}」</span></div>
      <div class="price"><small>この家は</small><b>4,000<small>万円台</small></b></div>
    </div>
    <dl>
      <dt>日時</dt><dd>{ph('【要確認】○月○日（土）・○日（日）')}<br>10:00〜17:00<small>各回{ph('○')}組限定・見学は約{ph('○分')}</small></dd>
      <dt>会場</dt><dd>大分市・金池小校区<small>個人のお住まいのため、詳しい場所はご予約時にご案内します</small></dd>
      <dt>参加費</dt><dd>無料（ご予約制）<small>ご夫婦・お子さま連れ歓迎／無理な売り込みはいたしません</small></dd>
    </dl>
    <div class="act">
      <a class="btn lg" href="#reserve">Webで予約する（1分）</a>
      <a class="btn ghost" href="tel:{TEL.replace('-', '')}">電話で予約</a>
      <p>※販売物件ではありません。施主様のご厚意で公開する注文住宅です。</p>
    </div>
  </div>
</div>

<section class="s">
  <div class="wrap">
    <h2 class="h2">{v['q']}</h2>
    <div class="icons">{icons}</div>
    <p class="answer">そのお悩み、<br class="sp"><em>駅近の注文住宅</em>なら<br class="sp">解決できるかもしれません。</p>
  </div>
</section>

<section class="s alt">
  <div class="wrap">
    <span class="eyebrow">BEFORE / AFTER</span>
    <h2 class="h2">{v['scene_h']}</h2>
    <p class="sub">{v['scene_sub']}</p>
    <div class="scenes">
      <div class="scene-hd"><span></span><span>{v['now_label']}</span><span></span><span>S様邸での光景</span></div>
      {scenes}
    </div>
    <div class="money">
      <div class="m-now"><span>{v['now_cost']}</span><b>月 {ph('○○.○')}万円</b></div>
      <div class="m-ar"><span>▶</span></div>
      <div class="m-new"><span>S様邸なら（{v['new_cost_note']}・{ph('35年・○%')}）</span><b>月 {ph('○○.○')}万円〜</b></div>
    </div>
    <p class="money-note">※月々の金額は目安です。金利・返済期間・お客様の条件により変わります。</p>
  </div>
</section>

<section class="s">
  <div class="wrap">
    <span class="eyebrow">THE HOUSE</span>
    <h2 class="h2">S様邸の、ある一日。</h2>
    <p class="sub">「庭は少しでいい。駐車場は3台欲しい。金池小校区で家を建てたい。」</p>
    <div class="spec">
      <div><small>土地</small><b>約44坪</b></div>
      <div><small>延床</small><b>約25坪</b></div>
      <div><small>駐車場</small><b>3台</b></div>
      <div><small>LDK</small><b>18帖＋吹抜け</b></div>
      <div><small>家族</small><b>4人</b></div>
      <div><small>性能</small><b style="font-size:15px">{ph('【要確認】耐震・断熱等級')}</b></div>
    </div>
    <div class="plans">
      <figure><figcaption>配置図<small>土地 約44坪（144.74㎡）</small></figcaption>{fb.PLAN_SITE}</figure>
      <figure><figcaption>1階<small>番号は下のポイント</small></figcaption>{fb.PLAN_1F}</figure>
      <figure><figcaption>2階</figcaption>{fb.PLAN_2F}</figure>
    </div>
    <p class="plan-note">※概略図です。延床 約25坪（83.63㎡）。車・植栽はイメージ</p>
    <ul class="pts">{pts}</ul>
  </div>
</section>

<section class="s alt">
  <div class="wrap">
    <span class="eyebrow">{PRODUCT.upper()}</span>
    <h2 class="h2">土地を読み解き、<br class="sp">一から設計する<em>「{PRODUCT}」</em>。</h2>
    <p class="plan-lead"><b>{PRODUCT}</b>（エッセンス アトリエ）は規格住宅ではありません。ご要望を伺い、土地・周辺環境・風・光・眺望まで読み解いて一から設計。<b>設計事務所がつくった工務店</b>が施工まで一貫。<b>クセのない間取り</b>だから、<b>売るときも、貸すときも価値が残りやすい</b>。</p>
    <div class="ptbl">
      <div class="pl">{PRODUCT}は広さごとの定額制<small>建物本体価格（税込）</small></div>
      <div class="row">
        <div class="pt cur"><i>S様邸</i><span>25.5坪</span><b>2,475<small>万円</small></b><em>税抜2,250万円</em></div>
        <div class="pt"><span>27坪</span><b>2,585<small>万円</small></b><em>税抜2,350万円</em></div>
        <div class="pt"><span>28.5坪</span><b>2,695<small>万円</small></b><em>税抜2,450万円</em></div>
        <div class="pt"><span>30坪</span><b>2,860<small>万円</small></b><em>税抜2,600万円</em></div>
      </div>
      <div class="pn">※付帯工事・外構・諸費用は別途　※価格は{ph('【要確認】○年○月')}時点</div>
    </div>
    <p class="total"><b>S様邸の総額例</b>土地{ph('○○○○万')}＋建物2,475万＋付帯工事・外構・諸費用{ph('○○○万')}＝<em>{ph('4,○○○万円')}</em></p>
  </div>
</section>

<section class="s">
  <div class="wrap">
    <span class="eyebrow">STORY</span>
    <h2 class="h2">S様の家づくり</h2>
    <p class="sub">はじめてのご相談から、お引渡しまで<b>約1年2ヶ月</b>。<br class="sp">走り回れる毎日は、もうすぐそこに。</p>
    <ol class="tl">
      <li><time>2025.10末</time><i></i><b>はじめてのご相談</b><span>「金池小校区で建てたい」</span></li>
      <li><time>{ph('○月')}</time><i></i><b>土地が決まる</b><span>駐車3台が叶う44坪</span></li>
      <li><time>{ph('○月')}</time><i></i><b>プランご提案</b><span>土地を読み解き一から設計</span></li>
      <li><time>{ph('○月')}</time><i></i><b>着工</b><span>設計から施工まで一貫</span></li>
      <li class="now"><time>2026.11</time><i></i><b>完成見学会</b><span>いま、ここ</span></li>
      <li><time>2026.12</time><i></i><b>お引渡し</b><span>新しい暮らしへ</span></li>
    </ol>
  </div>
</section>

<section class="s alt">
  <div class="wrap">
    <span class="eyebrow">CONSULTATION</span>
    <h2 class="h2">{v['consult_h']}</h2>
    <p class="sub">完成見学会 ＆ {v['event']}。ご希望の方だけ、見学のあとにご相談いただけます。</p>
    <div class="consult">{consult}</div>
    <div class="gifts">
      <div><small>ご予約特典 1</small><b>{g1t}</b>{g1d}</div>
      <div><small>ご予約特典 2</small><b>「建つかどうか」ラフプラン</b>気になる土地に建つ間取りをお見せします</div>
    </div>
  </div>
</section>

<section class="s">
  <div class="wrap narrow">
    <span class="eyebrow">FAQ</span>
    <h2 class="h2">よくあるご質問</h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="reserve" id="reserve">
  <div class="wrap narrow">
    <span class="eyebrow" style="color:var(--sun)">RESERVATION</span>
    <h2 class="h2">S様邸 完成見学会 ＆ {v['event']}<br>ご予約フォーム</h2>
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
      <a href="tel:{TEL.replace('-', '')}">{TEL}</a>
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
  <a class="btn ghost" href="tel:{TEL.replace('-', '')}">電話する</a>
  <a class="btn" href="#reserve">Webで予約</a>
</nav>

<script>
// チラシのQRなど、流入元をフォームに残す（例：?from=flyer）
(function(){{
  var p=new URLSearchParams(location.search);
  document.getElementById('source').value=p.get('from')||p.get('utm_source')||'';
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
