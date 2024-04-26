import uvicorn
from dotenv import load_dotenv

from src.config import load_metadata
from src.server import app


def main(dev: bool = False) -> None:
    load_dotenv()
    load_metadata(app)

    uvicorn.run(f"{__package__}.main:app", reload=dev)


if __name__ == "__main__":
    main()
