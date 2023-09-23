from notion import get_pages, create_page, upload_page
from webcrawler import get_video, get_book
from urllib.parse import urlparse


def main():
    # READ URLS FROM FILE
    with open('urls.txt', 'r') as f:
        urls = f.read().splitlines()

    # GET ALL PAGES FROM NOTION
    pages = get_pages()
    pages = [page['properties']['URL']['url'] for page in pages]

    # CREATE PAGES IF NOT EXIST
    for url in urls:
        if url not in pages:
            if urlparse(url).netloc == 'youtu.be' or urlparse(url).netloc == 'youtube.com':
                data = get_video(url)
            elif urlparse(url).netloc == 'annas-archive.org':
                data = get_book(url)

            # SEND NEW PAGE TO NOTION
            store = create_page(data)
            upload_page(store)


if __name__ == '__main__':
    main()
