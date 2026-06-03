from pathlib import Path


def main() -> None:
    root = Path.cwd()
    env_path = root / ".env"
    example_path = root / ".env.example"
    if not env_path.exists() and example_path.exists():
        env_path.write_text(example_path.read_text(encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    main()
