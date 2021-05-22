import SecureConnection

def test_insert_get_message():
    SecureConnection.addMessage("Natasha", "7252189336", "Hey there!!")
    res = SecureConnection.getMessage()
    assert res[0]["content"] == "Hey there!!" and res[0]["number"] == "7252189336"

def test_insert_get_email():
    SecureConnection.addEmail("Natasha", "Annie", "First Email", "Hey there!!")
    res = SecureConnection.getEmail()
    assert res[0]["content"] == "Hey there!!" and res[0]["subject"] == "First Email"

def test_insert_get_note_true():
    SecureConnection.addNote("First Note", "Call Natasha", True)
    SecureConnection.addNote("Second Note", "Call Natasha again", False)
    res = SecureConnection.getNote(True)
    assert res[0]["title"] == "First Note" and res[0]["content"] == "Call Natasha"
    

def test_insert_get_note_false():
    SecureConnection.addNote("Second Note", "Call Natasha again", False)
    SecureConnection.addNote("First Note", "Call Natasha", True)
    res = SecureConnection.getNote(False)
    assert res[0]["title"] == "Second Note" and res[0]["content"] == "Call Natasha again"

def test_insert_get_weather():
    SecureConnection.addWeather("Barcelona", "Clouds", 89.5, "scattered clouds")
    res = SecureConnection.getWeather()
    assert res[0]["location"] == "Barcelona"
