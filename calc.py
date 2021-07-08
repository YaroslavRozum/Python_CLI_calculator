from src import factory


def main():
    try:
        app = factory()
        result = app()
        print(result)
    except ValueError:
        pass


if __name__ == '__main__':
    main()
