from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.__init__photos(pages)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)


    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f'{label} photo added successfully on page {index + 1} slot {len(page)}.'
        return f'No more free slots'

    def display(self):
        page_separation = "-" * 11
        result = page_separation + "\n"
        for row in self.photos:
            result += ' '.join('[]' for _ in row) + "\n"
            result += page_separation + "\n"
        return result.strip()

    def __init__photos(self, pages):
        return [[] for row in range(pages)]




album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

