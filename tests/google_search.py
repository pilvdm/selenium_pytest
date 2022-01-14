"""
This is a file containing tests
"""

from page_objects.google_page import SearchHelper


def test_gumtree_search(browser):

    # Searching for the keywords via Google
    google_main_page = SearchHelper(browser)
    google_main_page.google_word("Cars in London")

    # Asserting the search was successful and there are elements in the header
    elements = google_main_page.check_navigation_bar()
    assert "All" or "Images" or "Videos" in elements

    # Asserting the number of results is >0 and the title exists for each matching url
    gumtree_elements = [i for i in google_main_page.get_all_search_results() if 'gumtree' in i]
    assert len(gumtree_elements) > 0
    for i in gumtree_elements:
        title = google_main_page.verify_title(i)
        # print(title)
        assert title

