from voiceit2 import VoiceIt2

# Your api key and token
api_key = "key_55b2a004b4634bddb007563df070f6ca"
api_token = "tok_2e2b55e8d47149d2a202d60530a40ff1"

# A pharse in your language
# Your voice will get registered on this phrase
PHRASE = 'never forget tomorrow is a new day'

# Only language supported on free tier of VoiceIt2 is no-speech-to-text
LANGUAGE = "no-STT"


# Register a user on voiceit2
def create_user():

    my_voiceit = VoiceIt2(api_key,api_token)
    
    # voiceit2 create_user API 
    # More info - https://api.voiceit.io/#create-a-user

    res = my_voiceit.create_user()
    
    # returns a response object like 
    # {
    #     "message": "Created user with userId : usr_feb6d1fcd80448628db8ec6a7ddb6322",
    #     "status": 201,
    #     "timeTaken": "0.055s",
    #     "createdAt": 1487026658000,
    #     "userId": "usr_feb6d1fcd80448628db8ec6a7ddb6322",
    #     "responseCode":"SUCC"
    # }
    
    print(res)
    
    if res["responseCode"] == "SUCC":
        return res['userId']
    else:
        return None


# Register atleast 3 times against a phrase for accurate results
def register_voices(uid, audio):

    my_voiceit = VoiceIt2(api_key,api_token)
    
    # voiceit2 create_voice_enrollment API 
    # More info - https://api.voiceit.io/#create-voice-enrollment
    
    res = my_voiceit.create_voice_enrollment(uid, LANGUAGE, PHRASE, audio)

    # returns a response object like 
    # {
    #     "message": "Successfully enrolled voice for user with userId : usr_49c98304252549239775e2b52a84006a",
    #     "contentLanguage": "en-US",
    #     "id": 57,
    #     "status": 201,
    #     "text": "never forget tomorrow is a new day",
    #     "textConfidence": 100.00,
    #     "createdAt": 1487026658000,
    #     "timeTaken": "7.718s",
    #     "responseCode" : "SUCC"
    # }
    
    print(res)
    
    if res["responseCode"] == "SUCC":
        return True
    else:
        return False


# Verify a user's voice
def verify(uid, audio):
    
    my_voiceit = VoiceIt2(api_key,api_token)
    
    # voiceit2 voice_verification API    
    # https://api.voiceit.io/#verify-a-user-s-voice

    res = my_voiceit.voice_verification(uid, LANGUAGE, PHRASE, audio)

    # {
    #     "message": "Successfully verified voice for user with userId : usr_feb6d1fcd80448628db8ec6a7ddb6322",
    #     "status": 200,
    #     "confidence": 94.0,
    #     "text": "never forget tomorrow is a new day",
    #     "textConfidence": 100,
    #     "timeTaken": "6.055s",
    #     "responseCode":"SUCC"
    # }

    print(res)
    
    if res["responseCode"] == "SUCC":
        return True
    else:
        return False