import re

texto = 'Python es genial'

resultado = re.match("Python", texto) #Match solo sirve para inicio de texto
resultado2 = re.search("genial", texto) #Con search solo la muestra una vez
resultado3 = re.findall("genial", texto) #Busca todo

texto = "Tengo 12 manzanas, 5 peras y 10 mangos"
resultado_texto = re.findall(r"\d+", texto) #\d+ Buscar caracter especifico


texto2 = "gato geto gito goto guto gaato"
resultado_texto2 = re.findall(r"g.to", texto2) #\. buscar un punto literalmente. 
#^ Evaluar si inicia con una palabra
#.$ Evaluar si termina con esa palabra

texto3 = "ac abc abbc abbbc abbbbc"
resultado_texto3 = re.findall(r"ab+c", texto3) #El "+" es que encuentra 1 o más ocurrencias que coincida con empezar con a, terminar en c y que tenga b en la mitad
texto4 = "ac abc abbc abbbc abbbbc"
resultado_texto4 = re.findall(r"ab*c", texto3) #El "*" es que encuentra lo que tenga a y c al final sin importar lo que haya al final. 
#Está o no está.

correo = "juan@gmail.com"
resultadoCorreo = re.findall(r".?@", correo)

correo2 = "oikjhgcx dfg@gmail.com"
resultadoCorreo2 = re.findall(r".+@", correo2) #Se pueden poner limite de caracteres con
                                               # ^.{3}@ o rangos con  ^.{5, 10}@

texto5 = "gato geto gito goto guto g6to"
resultado_texto5 = re.findall(r"g[aeiou]to", texto5) #Para encontrar un rango de letras [a-z]
                                                     #[^aeiou] el "^" es la negación, todo lo que no sea aeiou

texto6 = "Tengo un perro, un gato y un pez"
resultado_texto6 = re.findall(r"perro|gato", texto6) #  | esta linea es un or(|)

texto7 = "El precio es $100.00 (cien dolares)"
resultado_texto7 = re.findall(r"\$\d+\.\d+", texto7)

texto8 = "Java TypeScript CoffeeScript Python"
resultado_texto8 = re.findall(r"(Java|Type|Coffee)script", texto7)

correo3 = 'daniellopeztaba@gmail.com'
resultadoCorreo3 = re.findall(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", correo3)


if len(resultadoCorreo2)>0:
    print("Correo Valido")
else: 
    print("Correo Invalido")




print(resultado)
print(resultado2)
print(resultado3)
print(resultado_texto)
print(resultado_texto2)
print(resultado_texto3)
print(resultado_texto4)
print(resultado_texto5)
print(resultado_texto6)
print(resultado_texto7)
print(resultadoCorreo)
print(len(resultadoCorreo), correo)
print(resultadoCorreo3)



