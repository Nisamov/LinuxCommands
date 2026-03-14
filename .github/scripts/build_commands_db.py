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
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # buscar categoría
        category_match = re.search(r'^\s*:category:\s*([^\n\r]+)', content, re.MULTILINE)
        if not category_match:
            print(f"Sin :category: -> {file_path}")
            return None

        category = category_match.group(1).strip()

        # localizar bloque metadata
        md_match = re.search(r'\[\s*\.metadata\s*\]', content)
        if not md_match:
            print(f"Sin [.metadata] -> {file_path}")
            return None

        md_pos = md_match.end()

        start_brace = content.find('{', md_pos)
        if start_brace == -1:
            print(f"Sin inicio JSON -> {file_path}")
            return None

        # encontrar cierre JSON
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
            print(f"JSON sin cierre -> {file_path}")
            return None

        raw_json = content[start_brace:end_brace + 1]
        clean_json = robust_json_clean(raw_json)

        try:
            data = json.loads(clean_json)
        except json.JSONDecodeError as e:
            print(f"Error JSON en {os.path.basename(file_path)}: {e}")
            return None

        # asegurar nombre
        data['name'] = data.get(
            'name',
            os.path.basename(file_path).replace('.adoc', '')
        )

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

        # ignorar directorios
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]

        # solo procesar carpetas de comandos
        if 'commands' not in root:
            continue

        for file in files:

            if not file.endswith('.adoc'):
                continue

            if file == 'index.adoc':
                continue

            full_path = os.path.join(root, file)

            cmd_data = extract_json_metadata(full_path)

            if cmd_data:
                database.append(cmd_data)
                print(f"Indexado: {cmd_data['name']}")

    # ordenar alfabéticamente
    database.sort(key=lambda x: x['name'])

    output_path = os.path.join(BASE_PATH, 'docs', 'commands.json')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as out:
        json.dump(database, out, ensure_ascii=False, indent=2)

    print(f"\nTerminado: {len(database)} comandos indexados.")


if __name__ == "__main__":
    build_database()