import requests
import zipfile
import io

proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

fmt = "fb2"
resp = requests.get(f"http://flibustahezeous3.onion/b/181956/{fmt}", proxies=proxies, stream=True)

total = int(resp.headers['content-length'])
bytes_per_percent = total // 100

with io.BytesIO() as downloaded_data:
    downloaded = 0

    for c in resp.iter_content(bytes_per_percent):
        downloaded_data.write(c)
        downloaded += len(c)
        percent = int(downloaded / total * 100)
        print(f"{downloaded}/{total} ({percent}%)")

    if zipfile.is_zipfile(downloaded_data):
        print("Unzipping")
        zip_file = zipfile.ZipFile(downloaded_data)
        filename = zip_file.filelist[0].filename
        book_file = zip_file.open(filename)
    else:
        book_file = downloaded_data

    print("Writing file")
    with book_file:
        with open(f"out.{fmt}", "wb") as out_file:
            try:
                book_file.seek(0)
            except io.UnsupportedOperation as _:
                pass
            out_file.write(book_file.read())
