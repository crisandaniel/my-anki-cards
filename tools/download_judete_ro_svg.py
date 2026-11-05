import os
import urllib.request

# Maparea județelor cu codul de înmatriculare și numele oficial de fișier din Wikimedia Commons
counties = {
    "ab": "Alba_in_Romania.svg",
    "ar": "Arad_in_Romania.svg",
    "ag": "Arges_in_Romania.svg",
    "bc": "Bacau_in_Romania.svg",
    "bh": "Bihor_in_Romania.svg",
    "bn": "Bistrita-Nasaud_in_Romania.svg",
    "bt": "Botosani_in_Romania.svg",
    "bv": "Brasov_in_Romania.svg",
    "br": "Braila_in_Romania.svg",
    "bz": "Buzau_in_Romania.svg",
    "cs": "Caras-Severin_in_Romania.svg",
    "cl": "Calarasi_in_Romania.svg",
    "cj": "Cluj_in_Romania.svg",
    "ct": "Constanta_in_Romania.svg",
    "cv": "Covasna_in_Romania.svg",
    "db": "Dambovita_in_Romania.svg",
    "dj": "Dolj_in_Romania.svg",
    "gl": "Galati_in_Romania.svg",
    "gr": "Giurgiu_in_Romania.svg",
    "gj": "Gorj_in_Romania.svg",
    "hr": "Harghita_in_Romania.svg",
    "hd": "Hunedoara_in_Romania.svg",
    "il": "Ialomita_in_Romania.svg",
    "is": "Iasi_in_Romania.svg",
    "if": "Ilfov_in_Romania.svg",
    "mm": "Maramures_in_Romania.svg",
    "mh": "Mehedinti_in_Romania.svg",
    "ms": "Mures_in_Romania.svg",
    "nt": "Neamt_in_Romania.svg",
    "ot": "Olt_in_Romania.svg",
    "ph": "Prahova_in_Romania.svg",
    "sm": "Satu_Mare_in_Romania.svg",
    "sj": "Salaj_in_Romania.svg",
    "sb": "Sibiu_in_Romania.svg",
    "sv": "Suceava_in_Romania.svg",
    "tr": "Teleorman_in_Romania.svg",
    "tm": "Timis_in_Romania.svg",
    "tl": "Tulcea_in_Romania.svg",
    "vs": "Vaslui_in_Romania.svg",
    "vl": "Valcea_in_Romania.svg",
    "vn": "Vrancea_in_Romania.svg",
    "b": "Bucharest_in_Romania.svg"
}

# Folderul unde se vor salva imaginile
output_dir = "anki_media"
os.makedirs(output_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("Începe descărcarea hărților pentru județele României...\n")

for code, filename in counties.items():
    # URL-ul de thumbnail de înaltă rezoluție (PNG) din Wikimedia Commons
    url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/archive/c/c8/{filename}/500px-{filename}.png"
    # Fallback către calea standard dacă arhivele diferă
    direct_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{filename}?width=500"
    
    local_filename = f"ro_{code}.png"
    file_path = os.path.join(output_dir, local_filename)
    
    try:
        req = urllib.request.Request(direct_url, headers=headers)
        with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"✅ Descărcat: {local_filename} (Județul {code.upper()})")
    except Exception as e:
        print(f"❌ Eroare la {code.upper()}: {e}")

print(f"\nGata! Toate imaginile au fost salvate în folderul '{output_dir}'.")