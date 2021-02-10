"""
"""
def getTelegraph():
    import requests, bs4, html5lib


    URL = "https://www.telegraphindia.com/science-tech"
    res = requests.get(URL)

    soup = bs4.BeautifulSoup(res.content, "html5lib")    

    def title():
        title_storage = []
        title = soup.find_all('a', attrs={'class':"muted-link ellipsis_data_2"})
        for i in title:
            title_storage.append(i.text.strip())
        return title_storage

    
    def content():
        content_storage = []
        content = soup.find_all('div', attrs={'class':"uk-text-69 noto-regular pt-1 searchCard_desr"})
        for i in content:
            content_storage.append(i.text.replace('\n', " ").replace('\t', " ").replace("  ", ' '))   
        return content_storage

    title_list = title()
    content_list = content()
    for t in title_list:
        print("Title - ", t)
    for c in content_list:
        print("Contents - ", c)

getTelegraph()