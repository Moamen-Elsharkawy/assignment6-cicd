import logging
import os

logging.basicConfig(
    filename="training.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
)
logger = logging.getLogger(__name__)


def train():
    logger.info("Training started.")
    print("Starting training run...")

    epochs = 3
    for epoch in range(1, epochs + 1):
        loss = round(1.0 / epoch, 4)
        logger.info("Epoch %d/%d — loss: %s", epoch, epochs, loss)
        print(f"  Epoch {epoch}/{epochs} — loss: {loss}")

    logger.info("Training completed successfully.")
    print("Training complete.")


if __name__ == "__main__":
    train()