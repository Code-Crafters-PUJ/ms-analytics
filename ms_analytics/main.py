import uvicorn
from dotenv import load_dotenv

from ms_analytics.config import load_metadata
from ms_analytics.server import app


def main(dev: bool = False) -> None:
    load_dotenv()
    load_metadata(app)

    uvicorn.run(f"{__package__}.main:app", reload=dev)


if __name__ == "__main__":
    main()
