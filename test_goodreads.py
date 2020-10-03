import unittest
from goodreadsclass import GoodreadsAPIClient

class GoodreadsTestCase(unittest.TestCase):
    def test_validinput1(self):
        book1=GoodreadsAPIClient()
        testvalue=book1.get_book_details("https://www.goodreads.com/book/show/12067.Good_Omens")
        knownvalue={'title': 'Good Omens: The Nice and Accurate Prophecies of Agnes Nutter, Witch',
                    'image_url': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1392528568l/12067._SY160_.jpg',
                    'publication_year': '2006', 'average_rating': 4.24, 'num_pages': 491, 'ratings_count': 470437, 'authors': 'Terry Pratchett,Neil Gaiman'}
        self.assertEqual(knownvalue,testvalue)

    def test_validinput2(self):
        book2 = GoodreadsAPIClient()
        testvalue = book2.get_book_details("https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire")
        knownvalue = {'title': 'A Song of Ice and Fire (A Song of Ice and Fire, #1-5)',
                      'image_url': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1339340118l/12177850._SX98_.jpg',
                      'publication_year': '2011', 'average_rating': 4.57, 'num_pages': 5216, 'ratings_count': 27712, 'authors': 'George R.R. Martin'}
        self.assertEqual(knownvalue['title'], testvalue['title'])

    def test_invalidinput1(self):
        book1 = GoodreadsAPIClient()
        testvalue = book1.get_book_details("https://www.gooreads.com/book/show/12067.Good_Omens")
        knownvalue = {}
        self.assertEqual(knownvalue, testvalue)

    def test_invalidinput2(self):
        book2 = GoodreadsAPIClient()
        testvalue = book2.get_book_details("https://www.gooreads.com/book/show/.Good_Omens")
        knownvalue = {}
        self.assertEqual(knownvalue, testvalue)

if __name__ == '__main__':
    unittest.main()