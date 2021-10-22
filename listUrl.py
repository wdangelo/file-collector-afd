from models import Url


def list():
    urls = Url.select()

    return urls


if __name__ == '__main__':
    url = list()
    for items in url:
        print(items.url)