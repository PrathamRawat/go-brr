from financescraper import scraper


def get_scraper_session():
    return scraper.FinanceScraper()


def get_current_price(ticker: str):
    return get_scraper_session().get_data(ticker).price


