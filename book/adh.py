from pathlib import Path

def add_header_to_md_files(root_folder):
    root = Path(root_folder)

    for md_file in root.rglob("*.md"):
        filename = md_file.stem  # filename without extension
        header = f"({filename})=\n"

        try:
            content = md_file.read_text(encoding="utf-8")

            # Skip if header already exists
            if content.startswith(f"({filename})="):
                print(f"Skipped (already has header): {md_file}")
                continue

            new_content = header + content
            md_file.write_text(new_content, encoding="utf-8")

            print(f"Updated: {md_file}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")


if __name__ == "__main__":
    folder_path = input("Enter folder path: ").strip()
    add_header_to_md_files(folder_path)