import behave


@behave.given('a user on "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@behave.when('they type "{text}" in the search bar and push "Enter"')
def step_impl(context, text):
    element = context.browser.find_element_by_name('q')
    element.send_keys(text)
    element.submit()


@behave.when('they type "{text}" in the search bar and push "Enter" (on wiki)')
def step_impl(context, text):
    search = context.browser.find_element_by_xpath("//input[@id='searchInput']")
    search.send_keys(text)
    search.submit()


@behave.then('they will see the page "{url}"')
def step_impl(context, url):
    x_path = "//a[@href='%s']" % url
    assert context.browser.find_element_by_xpath(x_path) is not None


@behave.then('they will see the article "{text}"')
def step_impl(context, text):
    url = 'https://en.wikipedia.org/wiki/%s' % text
    assert context.browser.current_url == url


@behave.then('they will see language "{language}" in the list')
def step_impl(context, language):
    assert context.browser.find_element_by_xpath("//*[@title='NUnit – Russian']").text == language
