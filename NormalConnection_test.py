import NormalConnection

def test_insert_get_wiki():
    NormalConnection.addWikiHistory("Farmers","We are farmers")
    res = NormalConnection.getWikiHisotry()
    assert res[0]["keyword"] == "Farmers" and res[0]["description"] == "We are farmers"

def test_insert_get_search():
    NormalConnection.addSearchHistory("Farmers","We are farmers")
    res = NormalConnection.getSearchHisotry()
    assert res[0]["keyword"] == "Farmers" and res[0]["description"] == "We are farmers"

def test_insert_get_web():
    NormalConnection.addWebHistory("www.dummy-developers.com")
    NormalConnection.addWebHistory("www.dummy-developers.in")
    res = NormalConnection.getWebHisotry()
    assert res[1]["keyword"] == "www.dummy-developers.com" and res[0]["keyword"] == "www.dummy-developers.in"
    
def test_insert_get_news():
    NormalConnection.addNewsHistory("Champions League")
    NormalConnection.addNewsHistory("IPL")
    res = NormalConnection.getNewsHisotry()
    assert res[1]["keyword"] == "Champions League" and res[0]["keyword"] == "IPL"
 
def test_insert_get_youtube():
    NormalConnection.addYoutubeHistory("video1")
    NormalConnection.addYoutubeHistory("video1")
    NormalConnection.addYoutubeHistory("video1")
    NormalConnection.addYoutubeHistory("video1")
    res = NormalConnection.getYoutubeFav()
    assert res[0]["keyword"] == "video1" and res[0]["count"] > 3
