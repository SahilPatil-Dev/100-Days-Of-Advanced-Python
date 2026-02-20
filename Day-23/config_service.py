from typing import Dict, Any
import copy


class ConfigService:
    def __init__(self, config: Dict[str, Any]) -> None:
        # Store internal config safely
        self._config = copy.deepcopy(config)

    def get_config(self) -> Dict[str, Any]:
        # Return defensive copy to prevent mutation
        return copy.deepcopy(self._config)


if __name__ == "__main__":
    initial_config = {
        "env": "production",
        "features": {
            "beta": True
        }
    }

    service = ConfigService(initial_config)

    config1 = service.get_config()
    config1["features"]["beta"] = False

    config2 = service.get_config()

    print("Config1:", config1)
    print("Config2:", config2)  # Remains unchanged
