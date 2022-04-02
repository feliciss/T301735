import pywikibot
from pywikibot.exceptions import OtherPageSaveError


class PageOperator:

    def __init__(self, source, user):
        self.source = source
        self.user = user

    # get_user
    def get_user(self) -> pywikibot.User:
        # connect wikidata
        site = pywikibot.Site(self.source, self.source)
        repo = site.data_repository()
        # get user
        user = pywikibot.User(repo, self.user)
        # return user
        return user

    # get_user_content
    def get_content_of_the_user(self) -> str:
        # get user
        user = self.get_user()
        # get the content of the user page
        content = user.get()
        # return content
        return content

    # print_user_page: print the user content from source
    def print_content_of_the_user(self) -> None:
        # get the content of the user page
        content = self.get_content_of_the_user()
        # print the content
        print(content)

    def add_content_to_a_user(self, text) -> None:
        # get user
        user = self.get_user()
        # get the content of the user page
        content = self.get_content_of_the_user()
        # add text to the end of the content
        target = content.__add__(text)
        # put target content to a user if logged in
        try:
            user.put(target, summary='submit by script')
        except OtherPageSaveError:
            pywikibot.exception()


def main(*args: str) -> None:
    # set source
    source = 'wikidata'

    # set user
    user = 'Feliciss'

    # init operator
    page_operator = PageOperator(source, user)

    # print content of the user
    page_operator.print_content_of_the_user()
    # add content to a user
    page_operator.add_content_to_a_user(text='\n\nHello')


if __name__ == '__main__':
    main()
