from goodreadsclass import GoodreadsAPIClient

book=GoodreadsAPIClient()
book_url=str(input("Enter URL\n"))
bookdetails= book.get_book_details(book_url)
print(bookdetails)