import uvicorn

from ms_analytics.config import load_metadata
from ms_analytics.config.constants.environment import PORT
from ms_analytics.server import app


def main(dev: bool = False) -> None:
    load_metadata(app)

    uvicorn.run(f"{__package__}.main:app", reload=dev, port=PORT)


if __name__ == "__main__":
    main()
