from bs4 import BeautifulSoup
import requests

class X_tractor:
    def __init__(self, BASE_URL):
        if not isinstance(BASE_URL, str):
            raise ValueError("BASE_URL should be a string")

        self.__private_currentPage = BeautifulSoup(requests.get(BASE_URL).text, 'html.parser')

        self.__private_BASE_URL = BASE_URL
        self.__private_allLinks = []
        self.__private_baseLinks = []
        self.__private_socialMediaAccounts = []
        self.__private_documentLinks = []
        self.__private_youtubeVideoLinks = []

    def convert_To_HTML_File(self, fileName):
        try :
            file = open(f"{fileName}.html", "x")
            file.write(requests.get(self.__private_BASE_URL).text)
            file.close()
            f"File saved successfully at location {fileName}"

            return True

        except FileExistsError:
            RED = "\033[91m"
            RESET = "\033[0m"
            print(RED+ f"A file already exists with the name {fileName}.html"+ RESET)

            return False

    def getCurrentPage(self):
        return self.__private_currentPage

    def getPrettyCurrentPage(self):
        return self.__private_currentPage.prettify()

    def extractLinks(self):
        try :
            for link in self.__private_currentPage.findAll('a'):
                link_url = link.get('href')

                self.__private_allLinks.append(link_url)

                if ("facebook" in link_url or
                        "twitter" in link_url or
                        "@gmail" in link_url or
                        f"@{self.__private_BASE_URL[8:len(self.__private_BASE_URL)]}" in link_url):

                    self.__private_socialMediaAccounts.append(link_url)

                elif "youtube.com" in link_url:
                    self.__private_youtubeVideoLinks.append(link_url)

                elif "docs" in link_url.replace(self.__private_BASE_URL, "").lower():
                    self.__private_documentLinks.append(link_url)

                else:
                    self.__private_baseLinks.append(link_url)
            return True

        except Exception as e:
            print(e)
            return False


    def get_allLinks(self):
        return self.__private_allLinks

    def get_baseLinks(self):
        return self.__private_baseLinks

    def get_socialMediaAccounts(self):
        return self.__private_socialMediaAccounts

    def get_documentLinks(self):
        return self.__private_documentLinks

    def get_youtubeVideoLinks(self):
        return self.__private_youtubeVideoLinks

