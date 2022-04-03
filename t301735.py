# Example bot for T301735 (https://phabricator.wikimedia.org/T301735) task
# (C) Feliciss, task completed on 03-April-2022

import pywikibot
from pywikibot import exception, ItemPage, Site, User
from pywikibot.site import DataSite
from pywikibot.exceptions import OtherPageSaveError


class T301735Bot:

    def __init__(self, source, user):
        self.source = source
        self.user = user

    # get_data_site: get and connect data site
    def get_data_site(self) -> DataSite:
        # connect site
        site = Site(self.source, self.source)
        repo = site.data_repository()
        return repo

    # get_user: get a user from a data site
    def get_user(self) -> User:
        # get data site
        data_site = self.get_data_site()
        # get user
        user = User(data_site, self.user)
        # return user
        return user

    # get_user_content: get the content from the user page
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

    # add_content_to_a_user: add content to the end of the user page
    def add_content_to_a_user(self, text, summary) -> None:
        # get user
        user = self.get_user()
        # get the content of the user page
        content = self.get_content_of_the_user()
        # add text to the end of the content
        target = content.__add__(text)
        # put target content to a user if logged in
        try:
            user.put(target, summary)
        except OtherPageSaveError:
            exception()

    # search_data_from_a_user: search keywords of data items on Wikidata from a user
    def search_data_from_a_user(self, wikidata_data_type) -> list:
        # get user
        user = self.get_user()

        # get wikidata pages from the user
        pages = user.linkedPages()

        # list of page titles
        page_titles = []

        # search title of the data type on wikidata
        for page in pages:
            title = page.title()
            if title.startswith(wikidata_data_type):
                # add title if it's not an empty title
                if len(title) > 1:
                    page_titles.append(title)

        return page_titles

    # print_property_value_from_a_page: now only supports printing author names on Wikidata items page
    def print_property_value_from_a_page(self, page_titles, property_key, linked_property_key, label_key,
                                         language_key) -> None:
        # get data site
        data_site = self.get_data_site()
        # code refers to https://www.wikidata.org/wiki/Wikidata:Creating_a_bot#Example_11:_Get_values_of_sub-properties
        # and https://github.com/mpeel/wikicode/blob/master/example.py
        for title in page_titles:
            item = ItemPage(data_site, title)
            if property_key in item.claims:
                for property in item.claims[property_key]:
                    target = property.getTarget()
                    title = target.title()
                    print(title)
            if linked_property_key in item.claims:
                for property in item.claims[linked_property_key]:
                    target = property.getTarget()
                    title = target.title()
                    item = ItemPage(data_site, title)
                    label = item.get()[label_key]
                    if language_key:
                        try:
                            language = label[language_key]
                            print(language)
                        except KeyError:
                            exception()
                    else:
                        print(label)


def main(*args: str) -> None:
    # set source
    source = input('Please enter your source from, example: wikidata, wikipedia: ')

    # set user
    user = input('Please enter your username from that source: ')

    # init T301735 bot
    bot = T301735Bot(source, user)

    # print content of the user
    bot.print_content_of_the_user()

    # set text
    text = input('\nPlease enter the text you want to add onto that user: ')

    # set submit summary
    summary = input('\nPlease leave the summary you would like to submit (default: submit by script): ') or 'submit by ' \
                                                                                                            'script '
    # # add content to a user
    bot.add_content_to_a_user(text, summary)

    # set data type on Wikidata
    wikidata_data_type = input('\nPlease enter a data type on Wikidata, example: Q, P (default: Q): ') or 'Q'

    # search data from a user
    page_titles = bot.search_data_from_a_user(wikidata_data_type)

    # print page titles
    print(page_titles)

    # set property, linked property, label and language as keys to find the values on page
    property_key, linked_property_key, label_key = [str(i) for i in (
            input('\nPlease enter property, linked property, label '
                  'and language (optional) as keys used on Wikidata, '
                  'example (default): P2093 P50 labels: ') or 'P2093 P50 labels').split()]

    # set optional language as key to find the values on page
    language_key = input('Please enter language (optional) as key used on Wikidata, example: en, de, fr: ')

    # print property value from a page
    bot.print_property_value_from_a_page(page_titles, property_key, linked_property_key, label_key,
                                                   language_key)


if __name__ == '__main__':
    main()
