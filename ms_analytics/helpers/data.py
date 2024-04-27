
import json
from typing import Any


def get_data() -> dict[str, Any]:
    with open("ms_analytics/data/data.json") as f:
        return json.load(f)
