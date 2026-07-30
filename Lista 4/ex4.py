texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

texto_limpo = texto.lower()
texto_limpo = texto_limpo.replace(".", "")
texto_limpo = texto_limpo.replace(",", "")
texto_limpo = texto_limpo.replace(":", "")

palavras = texto_limpo.split()

palavras_filtradas = []
letras_python = "python"

for p in palavras:
    primeira_letra = p[0]
    ultima_letra = p[-1]
    
    if primeira_letra in letras_python or ultima_letra in letras_python:
        palavras_filtradas.append(p)

print("Palavras que começam ou terminam com letras de 'python':")
print(palavras_filtradas)
