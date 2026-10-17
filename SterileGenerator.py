import os
import json
import urllib.request
import re

dist_dir = r"C:\GrowthEngine\SamuiSmiles_Core\dist"
areas = ["Chaweng Noi", "Bophut", "Fisherman's Village", "Maenam", "Plai Laem", "Choeng Mon", "Bangrak", "Lamai", "Taling Ngam", "Lipa Noi", "Nathon", "Hua Thanon"]
asset_types = ["Luxury Freehold Villas", "Commercial Leasehold Hotels", "Foreign Quota Condominiums", "Prime Land for Development", "High-Yield Turnkey Properties"]
languages = {"en-US": "English", "ru-RU": "Russian", "de-DE": "German", "fr-FR": "French", "zh-CN": "Mandarin Chinese"}

html_template = """<!DOCTYPE html>
<html lang="{lang_code}" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_text} | Samui Smiles Co. Ltd.</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary-gold: #D4AF37; --luxury-navy: #0f172a; --cream: #faf8f5; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--cream); color: #334155; }}
        .font-display {{ font-family: 'Playfair Display', serif; }}
        .hero-gradient {{ background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); }}
    </style>
</head>
<body class="antialiased">
    <header class="bg-white/95 backdrop-blur shadow-sm sticky top-0 z-50 border-b border-amber-200">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <span class="font-display font-bold text-2xl text-slate-900 tracking-tight">SamuiSmiles</span>
            <a href="#contact" class="bg-emerald-600 hover:bg-emerald-700 text-white font-medium px-6 py-2.5 rounded-full transition shadow-sm">Contact Now</a>
        </nav>
    </header>

    <main>
        <section class="py-20 text-white hero-gradient text-center px-6">
            <h1 class="font-display text-3xl md:text-5xl font-bold max-w-4xl mx-auto leading-tight">{title_text}</h1>
            <p class="mt-6 text-xl text-amber-400 font-semibold">Direct Landowner Network & Legal Facilitation</p>
        </section>

        <section class="py-16 container mx-auto px-6 max-w-3xl">
            <div class="bg-white p-8 md:p-12 rounded-2xl shadow-sm border border-slate-100">
                <div class="prose max-w-none text-slate-700 text-base leading-relaxed space-y-4">
                    {body_html}
                </div>
            </div>
        </section>

        <section id="contact" class="py-16 text-center bg-slate-900 text-white">
            <div class="container mx-auto px-6 max-w-xl">
                <h2 class="font-display text-3xl font-bold mb-4">Secure This Asset</h2>
                <a href="https://wa.me/66826402220?text=Inquiry%20regarding%20{asset_type}%20in%20{area_name}" target="_blank" class="inline-flex items-center gap-2 bg-emerald-500 hover:bg-emerald-600 text-white font-semibold py-4 px-8 rounded-xl shadow-lg transition-transform hover:-translate-y-0.5">
                    📱 WhatsApp Nataliia
                </a>
            </div>
        </section>
    </main>
</body>
</html>
"""

def sterilize_output(raw_text):
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
    clean_lines = []
    noise_regex = r"(?i)^(here is|here are|certainly|sure|below is|this is|optimized|persuasive|outputting|i have generated).*"
    
    for line in lines:
        if re.match(noise_regex, line): continue
        if line.lower() in ["listing:", "article:", "investment details:"]: continue
        
        # Strip all raw markdown asterisks and hashes
        clean_line = re.sub(r"^\*+|\*+$|^#+\s*|\*\*", "", line).strip()
        if clean_line:
            clean_lines.append(f"<p>{clean_line}</p>")
            
    return "\n".join(clean_lines)

print("[Growth Engine] Initializing Sterile Programmatic Generation...")

for area in areas:
    for asset in asset_types:
        for code, lang in languages.items():
            clean_area = area.replace(' ', '_').replace("'", "")
            clean_asset = asset.replace(' ', '_')
            file_name = f"Invest_{clean_area}_{clean_asset}_{code}.html"
            file_path = os.path.join(dist_dir, file_name)
            
            if os.path.exists(file_path): continue
            print(f"Generating Sterile Asset: {area} | {asset} | {lang}")
            
            prompt = f"""You are a sterile data-generation API. Output exactly three paragraphs in {lang} analyzing {asset} in {area}, Koh Samui. Mention Samui Smiles Co. Ltd. direct landowner network and Thai legal facilitation. DO NOT include any conversational preamble, greetings, or meta-commentary. Output ONLY the analysis."""
            
            req = urllib.request.Request("http://localhost:11434/api/generate", data=json.dumps({"model": "llama3", "prompt": prompt, "stream": False}).encode('utf-8'), headers={'Content-Type': 'application/json'})
            try:
                with urllib.request.urlopen(req) as response:
                    result = json.loads(response.read().decode('utf-8'))
                    body_html = sterilize_output(result['response'])
                    
                    rendered = html_template.format(
                        lang_code=code, title_text=f"{asset} in {area}, Koh Samui",
                        area_name=area, asset_type=asset, body_html=body_html
                    )
                    with open(file_path, "w", encoding="utf-8") as f: f.write(rendered)
            except Exception as e:
                print(f"Error on {file_name}: {e}")

print("[Growth Engine] Sterile matrix generation complete.")