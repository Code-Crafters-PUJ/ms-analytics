import os

from dotenv import load_dotenv

load_dotenv()


def get_environment_variable[T](key: str, default: T | None = None) -> T | str:
    value = os.environ.get(key)

    if value is not None:
        if default is not None:
            return type(default)(value)
        else:
            return value

    if default is not None:
        return default
    raise KeyError(f"Environment variable {key} not set")


PORT: int = int(get_environment_variable("PORT", 8000))

JWT_SECRET: str = get_environment_variable("JWT_SECRET")
