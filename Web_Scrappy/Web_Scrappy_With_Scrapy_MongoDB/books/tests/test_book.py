import unittest
from scrapy.http import HtmlResponse, Request
from books.spiders.book import BookSpider, BooksItem


class BookSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = BookSpider()
        self.example_html = """
        <html>
            <body>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-sm-8 col-md-9">
                            <section>
                                <div>
                                    <article class="product_pod">
                                        <h3><a href="book1.html" title="Book One">Book One</a></h3>
                                        <div class="product_price">
                                            <p class="price_color">£25.99</p>
                                        </div>
                                    </article>
                                    <article class="product_pod">
                                        <h3><a href="book2.html" title="Book Two">Book Two</a></h3>
                                        <div class="product_price">
                                            <p class="price_color">£15.49</p>
                                        </div>
                                    </article>
                                </div>
                                <ul class="pager">
                                    <li class="next">
                                        <a href="catalogue/page-2.html">next</a>
                                    </li>
                                </ul>
                            </section>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        """
        self.response = HtmlResponse(
            url='https://books.toscrape.com',
            body=self.example_html,
            encoding='utf-8'
        )

    def test_parse_scrapes_all_items(self):
        """Test if the spider scrapes books and pagination links."""
        # Collect the items produced by the generator in a list
        # so that it's possible to iterate over it more than once.
        results = list(self.spider.parse(self.response))

        # There should be two book items and one pagination request
        book_items = [item for item in results if isinstance(item, BooksItem)]
        pagination_requests = [
            item for item in results if isinstance(item, Request)
        ]
        self.assertEqual(len(book_items), 2)
        self.assertEqual(len(pagination_requests), 1)

    def test_parse_scrapes_correct_book_information(self):
        """Test if the spider scrapes the correct information for each book."""
        pass

    def test_parse_creates_pagination_request(self):
        """Test if the spider creates a pagination request correctly."""
        pass

if __name__ == "__main__":
    unittest.main()