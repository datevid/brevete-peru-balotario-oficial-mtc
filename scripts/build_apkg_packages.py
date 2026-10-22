#!/usr/bin/env python3
"""
Compilador oficial de paquetes Anki (.apkg) para Brevete.net.pe
Genera paquetes legítimos compatibles con Anki Desktop, AnkiDroid y AnkiMobile.
"""

import os
import json
import sqlite3
import zipfile
import hashlib
import time
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMP_FILE = os.path.join(ROOT_DIR, 'scripts', 'questions_dump.json')
PUBLIC_DIR = os.path.join(ROOT_DIR, 'public')
OUTPUT_DIR = os.path.join(PUBLIC_DIR, 'balotarios', 'anki')
CATALOG_TS_FILE = os.path.join(ROOT_DIR, 'data', 'ankiPackages.ts')

os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_ID = 17001002026

CARD_CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #1e293b;
  background-color: #f8fafc;
  padding: 16px;
  margin: 0 auto;
  max-width: 620px;
}
.nightMode .card {
  color: #f1f5f9;
  background-color: #0f172a;
}
.anki-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #64748b;
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 8px;
}
.nightMode .anki-header {
  color: #94a3b8;
  border-bottom-color: #334155;
}
.anki-badge-cat {
  background: #ede9fe;
  color: #6d28d9;
  padding: 3px 8px;
  border-radius: 6px;
}
.nightMode .anki-badge-cat {
  background: #4c1d95;
  color: #ddd6fe;
}
.anki-badge-topic {
  color: #2563eb;
}
.nightMode .anki-badge-topic {
  color: #60a5fa;
}
.anki-question-text {
  font-size: 17px;
  font-weight: 700;
  line-height: 1.4;
  color: #0f172a;
  margin: 14px 0;
}
.nightMode .anki-question-text {
  color: #f8fafc;
}
.anki-image-box {
  text-align: center;
  margin: 14px 0;
  background: #ffffff;
  padding: 12px;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
}
.nightMode .anki-image-box {
  background: #1e293b;
  border-color: #334155;
}
.anki-image-box img {
  max-height: 200px;
  max-width: 100%;
  height: auto;
  display: inline-block;
  border-radius: 8px;
}
.anki-options {
  margin: 14px 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.anki-opt {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 10px 12px;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  font-size: 14px;
}
.nightMode .anki-opt {
  background: #1e293b;
  border-color: #334155;
}
.anki-opt-letter {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  background: #f1f5f9;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  font-weight: 700;
  font-size: 12px;
  color: #475569;
  flex-shrink: 0;
}
.nightMode .anki-opt-letter {
  background: #334155;
  border-color: #475569;
  color: #e2e8f0;
}
.anki-opt-text {
  flex: 1;
}
.anki-hint {
  font-size: 12px;
  color: #64748b;
  text-align: center;
  margin-top: 14px;
  font-style: italic;
}
.nightMode .anki-hint {
  color: #94a3b8;
}
hr#answer {
  border: none;
  border-top: 2px dashed #94a3b8;
  margin: 20px 0;
}
.nightMode hr#answer {
  border-top-color: #475569;
}
.anki-answer-container {
  margin-top: 12px;
}
.anki-answer-banner {
  background: #ecfdf5;
  border: 2px solid #10b981;
  border-radius: 10px;
  padding: 14px 16px;
  margin-bottom: 12px;
}
.nightMode .anki-answer-banner {
  background: #064e3b;
  border-color: #059669;
}
.anki-answer-badge {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #047857;
  margin-bottom: 6px;
}
.nightMode .anki-answer-badge {
  color: #6ee7b7;
}
.anki-answer-title {
  font-size: 16px;
  font-weight: 700;
  color: #064e3b;
  line-height: 1.4;
}
.nightMode .anki-answer-title {
  color: #ecfdf5;
}
.anki-meta-box {
  background: #f1f5f9;
  border-left: 4px solid #3b82f6;
  border-radius: 0 8px 8px 0;
  padding: 10px 14px;
  margin-top: 10px;
  font-size: 13px;
  line-height: 1.45;
  color: #334155;
}
.nightMode .anki-meta-box {
  background: #1e293b;
  border-left-color: #60a5fa;
  color: #cbd5e1;
}
.anki-meta-box.legal {
  border-left-color: #8b5cf6;
}
.nightMode .anki-meta-box.legal {
  border-left-color: #a78bfa;
}
.anki-meta-title {
  font-weight: 700;
  margin-bottom: 2px;
  display: block;
}
.anki-brand {
  font-weight: 800;
  font-size: 11px;
  color: #2563eb;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.nightMode .anki-brand {
  color: #60a5fa;
}
.anki-footer-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  color: #64748b;
  margin-top: 14px;
  padding-top: 8px;
  border-top: 1px dashed #cbd5e1;
}
.nightMode .anki-footer-bar {
  color: #94a3b8;
  border-top-color: #334155;
}
.anki-brand-stamp {
  font-weight: 800;
  color: #7c3aed;
  font-size: 11px;
  letter-spacing: 0.02em;
}
.nightMode .anki-brand-stamp {
  color: #a78bfa;
}
.anki-credits-card {
  margin-top: 16px;
  padding: 10px 14px;
  background: #f1f5f9;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 11px;
  color: #475569;
  border: 1px solid #e2e8f0;
}
.nightMode .anki-credits-card {
  background: #1e293b;
  border-color: #334155;
  color: #94a3b8;
}
.nightMode .anki-credits-card b {
  color: #f1f5f9;
}
"""

FRONT_TEMPLATE = """
<div class="card">
  <div class="anki-header">
    <span class="anki-badge-cat">{{Categoria}}</span>
    <span class="anki-brand">Brevete.net.pe</span>
    <span class="anki-badge-topic">{{Materia}} • Pregunta {{Id}}</span>
  </div>
  
  <div class="anki-question-text">{{Pregunta}}</div>
  
  {{#Imagen}}
    <div class="anki-image-box">{{Imagen}}</div>
  {{/Imagen}}
  
  <div class="anki-options">
    {{Opciones}}
  </div>
  
  <div class="anki-footer-bar">
    <span>💡 Piensa tu respuesta antes de voltear</span>
    <span class="anki-brand-stamp">Brevete.net.pe</span>
  </div>
</div>
"""

BACK_TEMPLATE = """
{{FrontSide}}

<hr id="answer">

<div class="card anki-answer-container">
  <div class="anki-answer-banner">
    <div class="anki-answer-badge">✔ RESPUESTA OFICIAL MTC — OPCIÓN {{RespuestaLetra}}</div>
    <div class="anki-answer-title">{{RespuestaCorrecta}}</div>
  </div>
  
  {{#BaseLegal}}
  <div class="anki-meta-box legal">
    <span class="anki-meta-title">⚖ Base Legal:</span>
    <div>{{BaseLegal}}</div>
  </div>
  {{/BaseLegal}}
  
  {{#Explicacion}}
  <div class="anki-meta-box">
    <span class="anki-meta-title">💡 Explicación Técnica:</span>
    <div>{{Explicacion}}</div>
  </div>
  {{/Explicacion}}

  <div class="anki-credits-card">
    <div>🚗 Tarjetas Oficiales MTC 2026 por <b>Brevete.net.pe</b></div>
    <div>Simulador en vivo: <a href="https://www.brevete.net.pe" style="color: #2563eb; text-decoration: underline;">www.brevete.net.pe</a></div>
  </div>
</div>
"""

DECK_IDS = {
    'a1': 17002026001,
    'a2a': 17002026002,
    'a2b': 17002026003,
    'a3a': 17002026004,
    'a3b': 17002026005,
    'a3c': 17002026006,
    'b2a': 17002026007,
    'b2b': 17002026008,
    'b2c': 17002026009,
}

def create_deck(slug, data):
    meta = data['meta']
    questions = data['questions']
    deck_id = DECK_IDS.get(slug, 17002026099)
    deck_name = f"Brevete.net.pe — MTC {meta['code']} 2026 ({meta['denomination'].split('(')[0].strip()})"
    deck_desc = f"Mazo oficial de tarjetas de memoria Anki para la licencia Clase {meta['code']} de Perú (MTC 2026). Balotario oficial verificado y compilado por Brevete.net.pe (https://www.brevete.net.pe)."
    
    filename = f"brevete_mtc_{slug}_2026.apkg"
    output_apkg = os.path.join(OUTPUT_DIR, filename)
    
    # Directorio temporal de trabajo
    temp_dir = os.path.join(OUTPUT_DIR, f"_temp_{slug}")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir, exist_ok=True)
    
    db_path = os.path.join(temp_dir, "collection.anki2")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE col (
        id integer primary key,
        crt integer not null,
        mod integer not null,
        scm integer not null,
        ver integer not null,
        dty integer not null,
        usn integer not null,
        ls integer not null,
        conf text not null,
        models text not null,
        decks text not null,
        dconf text not null,
        tags text not null
    );
    """)
    cur.execute("""
    CREATE TABLE notes (
        id integer primary key,
        guid text not null,
        mid integer not null,
        mod integer not null,
        usn integer not null,
        tags text not null,
        flds text not null,
        sfld text not null,
        csum integer not null,
        flags integer not null,
        data text not null
    );
    """)
    cur.execute("""
    CREATE TABLE cards (
        id integer primary key,
        nid integer not null,
        did integer not null,
        ord integer not null,
        mod integer not null,
        usn integer not null,
        type integer not null,
        queue integer not null,
        due integer not null,
        ivl integer not null,
        factor integer not null,
        reps integer not null,
        lapses integer not null,
        left integer not null,
        odue integer not null,
        odid integer not null,
        flags integer not null,
        data text not null
    );
    """)
    cur.execute("""
    CREATE TABLE revlog (
        id integer primary key,
        cid integer not null,
        usn integer not null,
        ease integer not null,
        ivl integer not null,
        lastIvl integer not null,
        factor integer not null,
        time integer not null,
        type integer not null
    );
    """)
    
    now_ts = int(time.time())
    
    model_dict = {
        str(MODEL_ID): {
            "id": MODEL_ID,
            "name": "Brevete.net.pe — Modelo Oficial MTC 2026",
            "type": 0,
            "mod": now_ts,
            "usn": -1,
            "sortf": 0,
            "did": deck_id,
            "tmpls": [
                {
                    "name": "Tarjeta Oficial Brevete.net.pe",
                    "ord": 0,
                    "qfmt": FRONT_TEMPLATE,
                    "afmt": BACK_TEMPLATE,
                    "bqfmt": "",
                    "bafmt": "",
                    "did": None
                }
            ],
            "flds": [
                {"name": "Id", "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 14, "media": []},
                {"name": "Materia", "ord": 1, "sticky": False, "rtl": False, "font": "Arial", "size": 14, "media": []},
                {"name": "Pregunta", "ord": 2, "sticky": False, "rtl": False, "font": "Arial", "size": 18, "media": []},
                {"name": "Imagen", "ord": 3, "sticky": False, "rtl": False, "font": "Arial", "size": 14, "media": []},
                {"name": "Opciones", "ord": 4, "sticky": False, "rtl": False, "font": "Arial", "size": 14, "media": []},
                {"name": "RespuestaCorrecta", "ord": 5, "sticky": False, "rtl": False, "font": "Arial", "size": 16, "media": []},
                {"name": "RespuestaLetra", "ord": 6, "sticky": False, "rtl": False, "font": "Arial", "size": 14, "media": []},
                {"name": "BaseLegal", "ord": 7, "sticky": False, "rtl": False, "font": "Arial", "size": 12, "media": []},
                {"name": "Explicacion", "ord": 8, "sticky": False, "rtl": False, "font": "Arial", "size": 13, "media": []},
                {"name": "Categoria", "ord": 9, "sticky": False, "rtl": False, "font": "Arial", "size": 12, "media": []}
            ],
            "css": CARD_CSS,
            "tags": [],
            "req": [[0, "all", [0, 2]]]
        }
    }
    
    decks_dict = {
        "1": {
            "id": 1,
            "mod": now_ts,
            "name": "Default",
            "usn": 0,
            "lrnToday": [0, 0],
            "revToday": [0, 0],
            "newToday": [0, 0],
            "timeToday": [0, 0],
            "collapsed": False,
            "browserCollapsed": False,
            "desc": "",
            "dyn": 0,
            "conf": 1,
            "extendNew": 10,
            "extendRev": 50
        },
        str(deck_id): {
            "id": deck_id,
            "mod": now_ts,
            "name": deck_name,
            "usn": 0,
            "lrnToday": [0, 0],
            "revToday": [0, 0],
            "newToday": [0, 0],
            "timeToday": [0, 0],
            "collapsed": False,
            "browserCollapsed": False,
            "desc": deck_desc,
            "dyn": 0,
            "conf": 1,
            "extendNew": 10,
            "extendRev": 50
        }
    }
    
    dconf_dict = {
        "1": {
            "id": 1,
            "mod": 0,
            "name": "Default",
            "usn": 0,
            "maxTaken": 60,
            "autoplay": True,
            "timer": 0,
            "replayq": True,
            "new": {"delays": [1, 10], "ints": [1, 4, 7], "initialFactor": 2500, "separate": True, "order": 1, "perDay": 20},
            "lapse": {"delays": [10], "mult": 0, "minInt": 1, "leechFails": 8, "leechAction": 0},
            "rev": {"perDay": 200, "ease4": 1.3, "fuzz": 0.05, "minSpace": 1, "ivlFct": 1, "maxIvl": 36500}
        }
    }
    
    conf_dict = {
        "nextPos": 1,
        "estTimes": True,
        "activeDecks": [1],
        "sortType": "noteFld",
        "timeLim": 0,
        "sortBackwards": False,
        "addToCur": True,
        "curDeck": 1,
        "curModel": None,
        "collapseTime": 1200
    }
    
    cur.execute("""
    INSERT INTO col VALUES (
        1, ?, ?, ?, 11, 0, 0, 0, ?, ?, ?, ?, '{}'
    )
    """, (now_ts, now_ts, now_ts, json.dumps(conf_dict), json.dumps(model_dict), json.dumps(decks_dict), json.dumps(dconf_dict)))
    
    media_map = {}
    media_files_to_copy = {}
    media_counter = 0
    
    letters = ['A', 'B', 'C', 'D', 'E']
    
    for idx, q in enumerate(questions):
        note_id = (now_ts * 1000) + idx
        card_id = (now_ts * 1000) + 500000 + idx
        guid = hashlib.sha1(f"{slug}_{q['id']}_{q['questionText']}".encode('utf-8')).hexdigest()[:10]
        
        q_id = str(q['id'])
        materia = q['subjectType']
        pregunta = q['questionText']
        
        # Procesar imagen
        img_tag = ""
        if q.get('imageUrl'):
            orig_rel_path = q['imageUrl'].lstrip('/')
            full_img_path = os.path.join(PUBLIC_DIR, orig_rel_path)
            if os.path.exists(full_img_path):
                img_basename = os.path.basename(orig_rel_path)
                if img_basename not in media_files_to_copy:
                    media_files_to_copy[img_basename] = (str(media_counter), full_img_path)
                    media_map[str(media_counter)] = img_basename
                    media_counter += 1
                img_tag = f'<img src="{img_basename}">'
        
        # Opciones
        opts = q.get('options', [])
        correct_idx = q.get('correctAnswerIndex', 0)
        correct_letter = letters[correct_idx] if 0 <= correct_idx < len(letters) else 'A'
        correct_text = opts[correct_idx] if 0 <= correct_idx < len(opts) else ''
        
        opts_html_parts = []
        for o_idx, opt_text in enumerate(opts):
            l = letters[o_idx] if o_idx < len(letters) else '?'
            opts_html_parts.append(f'<div class="anki-opt"><span class="anki-opt-letter">{l}</span><span class="anki-opt-text">{opt_text}</span></div>')
        options_html = "".join(opts_html_parts)
        
        legal_basis = q.get('legalBasis') or ''
        explanation = q.get('explanation') or ''
        category_header = f"MTC Clase {meta['code']} 2026"
        
        fields_list = [
            q_id,
            materia,
            pregunta,
            img_tag,
            options_html,
            correct_text,
            correct_letter,
            legal_basis,
            explanation,
            category_header
        ]
        
        flds = "\x1f".join(fields_list)
        sfld = q_id
        csum = int(hashlib.sha1(q_id.encode('utf-8')).hexdigest()[:8], 16)
        tag_str = f" MTC_Peru Brevete_{meta['code']} 2026 {slug} "
        
        cur.execute("""
        INSERT INTO notes VALUES (?, ?, ?, ?, -1, ?, ?, ?, ?, 0, '')
        """, (note_id, guid, MODEL_ID, now_ts, tag_str, flds, sfld, csum))
        
        cur.execute("""
        INSERT INTO cards VALUES (?, ?, ?, 0, ?, -1, 0, 0, ?, 0, 0, 0, 0, 0, 0, 0, 0, '')
        """, (card_id, note_id, deck_id, now_ts, idx + 1))
    
    cur.execute("CREATE INDEX ix_notes_usn on notes (usn);")
    cur.execute("CREATE INDEX ix_cards_usn on cards (usn);")
    cur.execute("CREATE INDEX ix_cards_nid on cards (nid);")
    cur.execute("CREATE INDEX ix_cards_sched on cards (did, queue, due);")
    cur.execute("CREATE INDEX ix_revlog_usn on revlog (usn);")
    cur.execute("CREATE INDEX ix_revlog_cid on revlog (cid);")
    cur.execute("CREATE INDEX ix_notes_csum on notes (csum);")
    
    conn.commit()
    conn.close()
    
    # Escribir el archivo media JSON
    media_json_path = os.path.join(temp_dir, "media")
    with open(media_json_path, "w", encoding="utf-8") as f:
        json.dump(media_map, f)
    
    # Empaquetar todo en el ZIP .apkg
    with zipfile.ZipFile(output_apkg, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(db_path, "collection.anki2")
        z.write(media_json_path, "media")
        for basename, (num_key, full_path) in media_files_to_copy.items():
            z.write(full_path, num_key)
            
    # Limpiar temp_dir
    shutil.rmtree(temp_dir)
    
    # Verificar el .apkg resultante
    size_bytes = os.path.getsize(output_apkg)
    sha256 = hashlib.sha256()
    with open(output_apkg, 'rb') as f:
        while chunk := f.read(65536):
            sha256.update(chunk)
    hash_hex = sha256.hexdigest().upper()
    
    # Comprobar que se puede abrir y leer collection.anki2
    with zipfile.ZipFile(output_apkg, "r") as z:
        names = z.namelist()
        assert "collection.anki2" in names, "Falta collection.anki2"
        assert "media" in names, "Falta media"
        
    return {
        "slug": slug,
        "code": meta['code'],
        "deckName": deck_name,
        "filename": filename,
        "downloadUrl": f"/balotarios/anki/{filename}",
        "sizeBytes": size_bytes,
        "sizeFormatted": f"{size_bytes / 1024:.1f} KB" if size_bytes < 1048576 else f"{size_bytes / 1048576:.2f} MB",
        "sha256": hash_hex,
        "totalCards": len(questions),
        "totalImages": len(media_files_to_copy)
    }

import subprocess

def main():
    if not os.path.exists(DUMP_FILE):
        print("Extrayendo preguntas desde TypeScript...")
        export_script = os.path.join(ROOT_DIR, 'scripts', 'export-questions.cjs')
        subprocess.run(['node', export_script], check=True)

    print(f"Cargando preguntas desde {DUMP_FILE}...")
    with open(DUMP_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    results = {}
    print("Compilando paquetes Anki legítimos...")
    for slug, cat_data in data.items():
        res = create_deck(slug, cat_data)
        results[slug] = res
        print(f"✔ [{res['code']}] {res['filename']} ({res['totalCards']} tarjetas, {res['totalImages']} imágenes, {res['sizeFormatted']}) - SHA256: {res['sha256'][:16]}...")
        
    # Escribir catálogo TypeScript
    ts_content = f"""// Catálogo oficial de paquetes Anki (.apkg) verificados de Brevete.net.pe
// Generado automáticamente con integridad criptográfica SHA-256.

export interface AnkiPackageMeta {{
  slug: string;
  code: string;
  deckName: string;
  filename: string;
  downloadUrl: string;
  sizeBytes: number;
  sizeFormatted: string;
  sha256: string;
  totalCards: number;
  totalImages: number;
}}

export const ANKI_PACKAGES: Record<string, AnkiPackageMeta> = {json.dumps(results, indent=2)};

export function getAnkiPackage(slug: string): AnkiPackageMeta | undefined {{
  return ANKI_PACKAGES[slug.toLowerCase()];
}}
"""
    with open(CATALOG_TS_FILE, 'w', encoding='utf-8') as f:
        f.write(ts_content)
    print(f"Catálogo generado con éxito en: {CATALOG_TS_FILE}")

if __name__ == "__main__":
    main()
