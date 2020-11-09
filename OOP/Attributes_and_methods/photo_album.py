class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        self.page = 0
        for num in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        try:
            if len(self.photos[self.page]) == 4:
                self.page += 1
        except:
            return 'No more free spots'
        if self.page >= self.pages:
            return 'No more free spots'
        self.photos[self.page].append(label)
        return f"{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}"

    def display(self):
        result = ""
        for page in self.photos:
            result += "-"*11 + "\n"
            for index in range(len(page)):
                if index == len(page) - 1:
                    result += "[]"
                else:
                    result += "[] "
            result += "\n"
        result += '-'*11 + '\n'
        return result

