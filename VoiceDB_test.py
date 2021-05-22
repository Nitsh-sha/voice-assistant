import VoiceDB

def test_insert_get():
    vdb = VoiceDB.VoiceDB
    vdb.insertUser("natasha", '123')
    assert vdb.getUser("natasha") == '123'