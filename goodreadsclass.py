import xml.etree.ElementTree as ET
import requests
from requests.exceptions import ConnectionError

class InvalidGoodreadsURL(Exception):
    pass

class GoodreadsAPIClient:

    def get_book_details(self,book_url):
        self.book_url=book_url
        parameters = {
            "key": "djkgPqybaXbaxu1Q2420qA"
        }
        bookdetails = dict()
        try:
            response = requests.get(book_url, params=parameters)
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                for child in root[1]:
                    if child.tag == 'title':
                        bookdetails['title'] = child.text
                    if child.tag == 'average_rating':
                        bookdetails['average_rating'] = float(child.text)
                    if child.tag == 'ratings_count':
                        bookdetails['ratings_count'] = int(child.text)
                    if child.tag == 'num_pages':
                        bookdetails['num_pages'] = int(child.text)
                    if child.tag == 'image_url':
                        bookdetails['image_url'] = child.text
                    if child.tag == 'publication_year':
                        bookdetails['publication_year'] = child.text
                    if child.tag == 'authors':
                        authors = []
                        authorsfordictionary = str()
                        for eachauthor in child.iter('authors'):
                            for child1 in child.iter('name'):
                                authors.append(child1.text)
                        authorsfordictionary = ",".join(authors)
                        bookdetails['authors'] = authorsfordictionary
                return bookdetails
            else:
                return bookdetails
                raise InvalidGoodreadsURL
        except InvalidGoodreadsURL:
            print('Invalid URL')
            return bookdetails
        except ConnectionError:
            print("connection Error")
            return bookdetails
        except:
            print("An error occurred")
            return bookdetails


#book=GoodreadsAPIClient()
#book_url=str(input("Enter URL\n"))
#bookdetails= book.get_book_details(book_url)
#print(bookdetails)