import uvicorn

from ms_analytics.config.constants.environment import PORT


def main(dev: bool = False) -> None:
    uvicorn.run(f"{__package__}.server:app", host="0.0.0.0", reload=dev, port=PORT)


if __name__ == "__main__":
    main()
