import gtts
from playsound import playsound

tts = gtts.gTTS("Your order number 3 4 5 9 has been delivered on your doorstep. Go get it RIGHT NOW! Integer", slow=False)
tts.save("hello.mp3")
playsound("hello.mp3")

#texte = "Bonjour à tous, aujourd'hui on fait de la synthèse vocale!"
texte = "C'est fou ce qu'on peut faire en Python avec la bonne librairie!"

tts = gtts.gTTS(texte, lang="fr", slow=False, tld='ca')
tts.save("coucou.mp3")
playsound("coucou.mp3")