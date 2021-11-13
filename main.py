from deep_translator import GoogleTranslator
Itxt = input("entrer le texte a traduire : ")
lng = input("entrer la langue a utiliser pour traduire le texte : ")
Rtxt = GoogleTranslator(source='auto', target=lng).translate(Itxt)
print(Rtxt)