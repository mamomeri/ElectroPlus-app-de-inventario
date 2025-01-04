from components.application_facade import ApplicationFacade
from utils.config import DATABASE_PATH

def main():
    facade = ApplicationFacade(DATABASE_PATH)
    facade.run()

if __name__ == "__main__":
    main()
