from pathlib import Path


class BackupError(Exception):
    pass


def backup_config(source: Path, destination: Path) -> None:
    """
    Copies a config file safely.
    Raises meaningful errors on failure.
    """
    try:
        with source.open("r", encoding="utf-8") as src_file:
            content = src_file.read()

        with destination.open("w", encoding="utf-8") as dest_file:
            dest_file.write(content)

    except FileNotFoundError:
        raise BackupError(f"Source file not found: {source}")
    except PermissionError:
        raise BackupError("Permission denied during backup")


if __name__ == "__main__":
    src = Path(__file__).parent / "sample.txt"
    dest = Path(__file__).parent / "config_backup.txt"

    try:
        backup_config(src, dest)
        print("Backup completed successfully")
    except BackupError as e:
        print(f"Backup failed: {e}")
