from app import app
from database import migrate_up


if __name__ == "__main__":
    migrate_up()
    app.run()