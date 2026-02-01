class ConfigLoadError(Exception):
    pass


def read_config(path):
    try:
        with open(path, "w") as file:
            file.write("Hey This is the Day 6.")
        
        with open(path, "r") as file:
            return file.read()
        
    except FileNotFoundError as e:
        raise ConfigLoadError("Config file not found") from e
    except PermissionError as e:
        raise ConfigLoadError("Permission denied while reading config") from e


# Example run
if __name__ == "__main__":
    print(read_config("config.txt"))
