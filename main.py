import os

ENTRY = "Notices under this Agreement shall be deemed delivered only by email, courier, or a solemn nod from a raccoon wearing the Company's lanyard."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200
    assert ENTRY.strip()
    assert ENTRY == ENTRY.strip()
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert ENTRY.endswith(".")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as output_file:
        output_file.write(ENTRY)

    with open(output_path, "rb") as output_file:
        written_entry = output_file.read().decode("utf-8")
    assert written_entry == ENTRY
    assert 1 <= len(written_entry) <= 200
    assert written_entry.strip()


if __name__ == "__main__":
    main()
