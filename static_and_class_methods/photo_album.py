import math


class PhotoAlbum:
    MAX_PAGES = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]  # matrix of photos

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / PhotoAlbum.MAX_PAGES))

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            number_photos = len(self.photos[i])

            if number_photos < PhotoAlbum.MAX_PAGES:
                self.photos[i].append(label)

                return f"{label} photo added successfully on page {i + 1} " \
                       f"slot {number_photos + 1}"

        else:
            return "No more free slots"

    def display(self):
        album = [11 * '-']

        for page in self.photos:
            album.append(' '.join(['[]' for _ in range(len(page))]))

            album.append(11 * '-')

        return '\n'.join(album)

