from gtts import gTTS

texto = input("Digite um texto para ser convertido em voz: ")

tts = gTTS(text=texto, lang='pt-br', slow=False)
tts.save("voz.mp3")
