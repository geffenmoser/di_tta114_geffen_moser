class Page:
    def __init__(self, items, page_number):
        self.items = items
        self.page_number = page_number

class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)
        self.currentPage = 1
        self.pages = self._create_pages()

    def _create_pages(self):
        pages = []
        for i in range(self.totalPages):
            start = i * self.pageSize
            end = start + self.pageSize
            page_items = self.items[start:end]
            pages.append(Page(page_items, i + 1))
        return pages

    def getVisibleItems(self):
        return self.pages[self.currentPage - 1].items

    def prevPage(self):
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())

p.nextPage()
print(p.getVisibleItems())

p.lastPage()
print(p.getVisibleItems())
