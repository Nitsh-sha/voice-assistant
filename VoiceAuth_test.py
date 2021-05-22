import VoiceAuth

def test_create_user():
    va = VoiceAuth.create_user()
    assert len(va) == 36