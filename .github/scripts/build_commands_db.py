import os
import json
import re
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
IGNORE_DIRS = {'.git', '.github', 'docs'}
def robust_json_clean(json_str):
    json_str = re.sub(r'//.*', '', json_str)
    json_str = " ".join(json_str.splitlines())
    json_str = re.sub(r',\s*([\]}])', r'\1', json_str)
    json_str = re.sub(r'\s+', ' ', json_str)
    return json_str.strip()
def extract_json_metadata(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

            # exigir línea :category:
            category_match = re.search(r':category:\s*([^\n\r]+)', content)
            if not category_match:
                return None
            category = category_match.group(1).strip()

            # localizar la sección [.metadata] y extraer el JSON buscando la llave de cierre emparejada
            md_pos = content.find('[.metadata]')
            if md_pos == -1:
                return None
            start_brace = content.find('{', md_pos)
            if start_brace == -1:
                return None

            # buscar la llave de cierre correspondiente contando llaves
            i = start_brace
            depth = 0
            end_brace = None
            while i < len(content):
                ch = content[i]
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        end_brace = i
                        break
                i += 1

            if end_brace is None:
                print(f"Error JSON en {os.path.basename(file_path)}: llave de cierre no encontrada")
                return None

            raw_json = content[start_brace:end_brace+1]
            clean_json = robust_json_clean(raw_json)
            try:
                data = json.loads(clean_json)
            except json.JSONDecodeError as e:
                print(f"Error JSON en {os.path.basename(file_path)}: {e}")
                return None

            # asegurar campos esenciales y mantener estructura esperada
            data['name'] = data.get('name', os.path.basename(file_path).replace('.adoc', ''))
            data['category'] = category
            rel_path = os.path.relpath(file_path, start=BASE_PATH)
            data['source_path'] = rel_path.replace('\\', '/')
            return data
    except Exception as e:
        print(f"Error crítico en {file_path}: {e}")
        return None
def build_database():
    database = []
    print(f"Iniciando escaneo desde raíz: {BASE_PATH}")
    for root, dirs, files in os.walk(BASE_PATH):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
        for file in files:
            if file.endswith('.adoc') and file != 'index.adoc':
                full_path = os.path.join(root, file)
                cmd_data = extract_json_metadata(full_path)
                if cmd_data:
                    database.append(cmd_data)
                    print(f"Indexado: {cmd_data['name']}")
    output_path = os.path.join(BASE_PATH, 'docs', 'commands.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as out:
        json.dump(database, out, ensure_ascii=False, indent=2)
    print(f"\nTerminado: {len(database)} comandos indexados.")
if __name__ == "__main__":
    build_database()