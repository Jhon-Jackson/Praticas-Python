class book:
    def __init__(self, title, pages):
        self.title = title
        self. pages = pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages !"

    def __len__(self):
        return self.pages


book1 = book("python basics", 300)
print(book1)
print(len(book1))
