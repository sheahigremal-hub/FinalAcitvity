class BookPages:
	def __init__(self, page_count):
		self.page_count = page_count

	def __str__(self):
		return f"{self.page_count} pages"

	def __add__(self, other):
		if not isinstance(other, BookPages):
			return NotImplemented
		return BookPages(self.page_count + other.page_count)


first_book = BookPages(120)
second_book = BookPages(85)

print(first_book)
combined_book = first_book + second_book
print(combined_book)
