texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

texto_limpo = texto.lower()
texto_limpo = texto_limpo.replace(".", "")
texto_limpo = texto_limpo.replace(",", "")
texto_limpo = texto_limpo.replace(":", "")

palavras = texto_limpo.split()

palavras_atendidas = []
contador = 0
letras_python = "python"

for p in palavras:
   
    if len(p) > 4:
        

        tem_letra = False 
        
        for letra in p:
            if letra in letras_python:
                tem_letra = True
                break 
        
        if tem_letra == True:
            palavras_atendidas.append(p)
            contador += 1               

print("Palavras maiores que 4 caracteres contendo letras de 'python':")
print(palavras_atendidas)
print("Quantidade total encontrada:", contador)
