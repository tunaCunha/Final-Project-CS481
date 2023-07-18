def getText():
    import speech_recognition as sr
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    #print(r)
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    #print(sr.Microphone)
    with sr.Microphone() as source:
        # adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        print("Ask a question...")
        # wait for speech for a maximum of 4 seconds
        # listen to speech for a maximum of 5 seconds
        audio_text = r.listen(source, timeout=4.0, phrase_time_limit=5.0)
        #query = ""
        print("Analyzing your question...")
        return str(r.recognize_google(audio_text))

        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        # try:
            # using google speech recognition
            # print("Text: " + r.recognize_google(audio_text))
        #
        # try:
        #     if r.recognize_google(audio_text) == None:
        #         print("Sorry, I did not get that.")
        #     #elif len(str(r.recognize_google(audio_text))) == 0:
        #         #print("Sorry, I did not get that.")
        #     else:
        #         return str(r.recognize_google(audio_text))
        # except:
        #     print("Nope.")

#print(getText())
