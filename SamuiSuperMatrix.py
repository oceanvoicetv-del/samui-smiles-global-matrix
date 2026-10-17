import os
import json

base_dir = r"C:\GrowthEngine\SamuiSmiles_Core"
dist_dir = os.path.join(base_dir, "dist")
os.makedirs(dist_dir, exist_ok=True)

districts = [
    "Chaweng Noi", "Bophut", "Fisherman's Village", "Maenam", 
    "Plai Laem", "Choeng Mon", "Bangrak", "Lamai", 
    "Taling Ngam", "Lipa Noi", "Nathon", "Hua Thanon"
]

assets = [
    "Luxury Freehold Villas", 
    "Commercial Leasehold Hotels", 
    "Foreign Quota Condominiums", 
    "Prime Land for Development", 
    "High-Yield Turnkey Properties"
]

languages = {
    "en-US": {"lang": "English", "cta": "WhatsApp Nataliia (+66 82 640 2220)"},
    "ru-RU": {"lang": "Russian", "cta": "Написать Наталии в WhatsApp"},
    "de-DE": {"lang": "German", "cta": "WhatsApp mit Nataliia starten"},
    "fr-FR": {"lang": "French", "cta": "Contacter Nataliia sur WhatsApp"},
    "zh-CN": {"lang": "Mandarin Chinese", "cta": "通过 WhatsApp 联系 Nataliia"}
}

page_template = """<!DOCTYPE html>
<html lang="{code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{asset} in {district}, Koh Samui | Samui Smiles Co. Ltd.</title>
    <meta name="description" content="Explore {asset} in {district}, Koh Samui with Samui Smiles Co. Ltd. (DBD Reg. 0815566002814). Direct landowner network, secure legal structuring, and private appointments via WhatsApp.">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased">
    <header class="bg-slate-900 text-white py-6 px-8 shadow-md">
        <div class="max-w-4xl mx-auto flex justify-between items-center">
            <span class="font-bold text-xl tracking-wide">Samui Smiles Co., Ltd.</span>
            <span class="text-xs text-amber-400 uppercase tracking-widest font-semibold">DBD Verified #0815566002814</span>
        </div>
    </header>
    <main class="max-w-4xl mx-auto px-6 py-12">
        <article class="bg-white p-8 md:p-12 rounded-2xl shadow-sm border border-slate-200 space-y-6">
            <h1 class="text-3xl md:text-4xl font-extrabold text-slate-900">{asset} in {district}, Koh Samui</h1>
            <p class="text-lg text-slate-600 leading-relaxed">
                Looking for verified {asset_lower} in the prime micro-region of <strong>{district}</strong>, Koh Samui? Samui Smiles Co. Ltd. connects international investors directly with local landowners, bypassing inflated intermediary costs.
            </p>
            <h2 class="text-xl font-bold text-slate-900 pt-4">Direct Landowner Advantage & Legal Framework</h2>
            <p class="text-slate-600 leading-relaxed">
                Operating under strict Thai legal guidelines, our team—directed by Nataliia Marienko and Otilio J. Nunez—facilitates complete due diligence, secure Chanote title transfers, 30-year registered leaseholds, and foreign quota compliance. Our Maenam head office (7/101 Moo 1) operates strictly by private appointment to protect client confidentiality.
            </p>
            <div class="pt-6">
                <a href="https://wa.me/66826402220?text=Inquiry%20regarding%20{asset}%20in%20{district}" target="_blank" class="inline-block bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-4 px-8 rounded-xl shadow-lg transition-transform hover:-translate-y-0.5">
                    {cta_text}
                </a>
            </div>
        </article>
    </main>
    <footer class="text-center py-8 text-xs text-slate-500 border-t border-slate-200 mt-12">
        <p>&copy; 2026 Samui Smiles Co. Ltd. | Head Office: 7/101 Moo 1, Maenam, Koh Samui, Surat Thani 84330 / 84320 Thailand.</p>
    </footer>
</body>
</html>
"""

print("[Growth Engine] Compiling Samui Smiles Super Matrix...")
count = 0
for district in districts:
    for asset in assets:
        for code, meta in languages.items():
            clean_dist = district.lower().replace(" ", "_").replace("'", "")
            clean_asset = asset.lower().replace(" ", "_")
            filename = f"samui_{clean_dist}_{clean_asset}_{code}.html"
            filepath = os.path.join(dist_dir, filename)
            
            rendered = page_template.format(
                code=code,
                district=district,
                asset=asset,
                asset_lower=asset.lower(),
                cta_text=meta["cta"]
            )
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(rendered.strip())
            count += 1

print(f"SUCCESS_COUNT:{count}")
