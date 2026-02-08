import os
import json
import re
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
IGNORE_DIRS = {'.git', '.github', 'docs', 'linux_fundamentals', 'host_web_server', 'templates', 'styles'}
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
            category_match = re.search(r':category:\s*([^\n\r]+)', content)
            if category_match:
                category = category_match.group(1).strip()
            else:
                parts = file_path.split(os.sep)
                category = parts[-3] if len(parts) > 2 else "general"
            metadata_match = re.search(r'\[\.metadata\]\s*(\{.*\})', content, re.DOTALL)
            if metadata_match:
                raw_json = metadata_match.group(1)
                clean_json = robust_json_clean(raw_json)
                try:
                    data = json.loads(clean_json)
                    data['name'] = os.path.basename(file_path).replace('.adoc', '')
                    data['category'] = category
                    rel_path = os.path.relpath(file_path, start=BASE_PATH)
                    data['source_path'] = rel_path.replace('\\', '/')
                    return data
                except json.JSONDecodeError as e:
                    print(f"Error JSON en {os.path.basename(file_path)}: {e}")
            return None
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
    output_path = os.path.join(BASE_PATH, 'docs', 'commands.json'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as out:
        json.dump(database, out, ensure_ascii=False, indent=2)
    print(f"\nTerminado: {len(database)} comandos indexados.")
if __name__ == "__main__":
    build_database()