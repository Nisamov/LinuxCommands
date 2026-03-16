#!/usr/bin/env python3
import sys
import re
import html
import unicodedata
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from deep_translator import GoogleTranslator

LANG_MAP = {
    'en': 'en', 'de': 'de', 'es': 'es', 'ru': 'ru',
    'zh': 'zh-CN', 'ko': 'ko', 'ja': 'ja', 'pt': 'pt'
}

# Patrones que no deben traducirse (directivas de AsciiDoc)
SKIP_PATTERNS = [
    re.compile(r'^include::'), re.compile(r'^:[\w-]+:'),
    re.compile(r'^\[source'), re.compile(r'^\[\.metadata\]'),
    re.compile(r'^//'), re.compile(r'^image::'), re.compile(r'^video::'),
    re.compile(r'^\[cols=') # Ignorar configuración de columnas de tablas
]

def translate_text(translator, text, target_lang):
    # No traducir si es vacío, un solo carácter, o solo números/bits (común en tus tablas)
    clean_text = text.strip()
    if not clean_text or len(clean_text) <= 1 or re.match(r'^[01\s\-\.\d]+$', clean_text):
        return text
    
    text = unicodedata.normalize('NFC', text)
    try:
        chunk = html.escape(text) if target_lang not in ['zh-CN', 'ko', 'ja'] else text
        translated = translator.translate(chunk)
        return html.unescape(translated) if translated else text
    except Exception:
        return text

def process_line(line, translator, target_lang, state):
    stripped = line.strip()
    
    # --- BLOQUES DE CÓDIGO ---
    if re.match(r'^----\s*$', stripped):
        state['in_code'] = not state['in_code']
        return line

    if state['in_code']:
        # Traducir comentarios (# o //) dentro del código
        comment_match = re.match(r'^(\s*(?:#|//)\s*)(.*)', line)
        if comment_match:
            prefix, content = comment_match.groups()
            return prefix + translate_text(translator, content, target_lang)
        return line

    # --- TABLAS ---
    if re.match(r'^\|===', stripped):
        state['in_table'] = not state['in_table']
        return line

    if state['in_table'] and stripped.startswith('|'):
        # Separar celdas manteniendo el primer pipe vacío si existe
        # Ejemplo: "|Celda1|Celda2" -> ['', 'Celda1', 'Celda2']
        cells = line.split('|')
        translated_cells = []
        
        for i, cell in enumerate(cells):
            if i == 0 and not cell.strip(): # El espacio antes del primer pipe
                translated_cells.append('')
            else:
                translated_cells.append(translate_text(translator, cell, target_lang))
        
        return "|".join(translated_cells)

    # --- SALTOS DE DIRECTIVAS ---
    if any(p.match(stripped) for p in SKIP_PATTERNS):
        return line

    # --- TÍTULOS Y LISTAS ---
    header_match = re.match(r'^(=+)\s+(.+)', stripped)
    if header_match:
        dots, title = header_match.groups()
        return f"{dots} {translate_text(translator, title, target_lang)}"

    list_match = re.match(r'^(\s*[\*\-\.\d]+\s+)(.+)', line)
    if list_match:
        prefix, content = list_match.groups()
        return prefix + translate_text(translator, content, target_lang)

    # --- PÁRRAFO NORMAL ---
    if stripped:
        return translate_text(translator, line, target_lang)
    
    return line

def translate_file(src_path, dst_path, target_lang):
    if target_lang == 'es':
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.write_text(src_path.read_text(encoding="utf-8"), encoding="utf-8")
        return

    translator = GoogleTranslator(source="auto", target=LANG_MAP.get(target_lang, target_lang))
    try:
        content = src_path.read_text(encoding="utf-8")
        lines = content.splitlines()
        state = {'in_code': False, 'in_table': False}
        translated_lines = [process_line(l, translator, target_lang, state) for l in lines]
        
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.write_text("\n".join(translated_lines), encoding="utf-8")
        print(f"✓ {target_lang.upper()}: {src_path.name}")
    except Exception as e:
        print(f"Error en {src_path.name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python translate_adoc.py <SRC_DIR> <DST_DIR> <LANG>")
        sys.exit(1)
    
    src_root, dst_root, lang = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    files = list(src_root.rglob("*.adoc"))
    with ThreadPoolExecutor(max_workers=4) as executor:
        for f in files:
            executor.submit(translate_file, f, dst_root / f.relative_to(src_root), lang)