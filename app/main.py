"""
Package summary.
"""

import logging


def main() -> None:
    """
    Run the app.
    """
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )
    logger = logging.getLogger(__name__)
    logger.info("Hello, World!")


if __name__ == "__main__":
    main()
