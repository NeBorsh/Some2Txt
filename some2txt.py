import os
import argparse

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"File read error: {e}"

def main():
    parser = argparse.ArgumentParser(description='Combines files with specified extensions from the given folders into one file.')
    parser.add_argument('--dirs', nargs='+', default=['src'], help='Folders to process (default: src)')
    parser.add_argument('--extensions', nargs='+', default=['.cpp', '.h'], help='File extensions (default: .cpp .h)')
    parser.add_argument('--output', default='output.txt', help='Output file name (default: output.txt)')
    args = parser.parse_args()

    files = []
    for source_dir in args.dirs:
        if not os.path.isdir(source_dir):
            print(f"Folder {source_dir} does not exist!")
            continue
        for file in os.listdir(source_dir):
            if any(file.endswith(ext) for ext in args.extensions):
                files.append((source_dir, file))

    files.sort(key=lambda x: (x[1].lower().replace('.cpp', '').replace('.h', ''), x[1].endswith('.h')))

    with open(args.output, 'w', encoding='utf-8') as out:
        for source_dir, filename in files:
            filepath = os.path.join(source_dir, filename)
            code = read_file(filepath)
            out.write(f"{source_dir}/{filename}:\n")
            out.write(f"{code}\n\n")

    print(f"Files successfully combined into {args.output}")

if __name__ == "__main__":
    main()
