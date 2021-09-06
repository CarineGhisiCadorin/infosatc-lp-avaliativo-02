lista_filmes  = ["bob_esponja", "caçador_de_recompenças", "Jenifer"]
lista_jogos   = ["undertale", "minecraft", "cs"]
lista_livros  = ["diario_frank","Amelia","Dark"]
lista_esporte = ["xadrez","futebol", "futsal"]
print(lista_filmes)
print(lista_jogos)
print(lista_livros)
print(lista_esporte)

lista_filmes.append ("Cinderela") 
lista_filmes.append("A_branca_de_neve")  
lista_jogos.append("Valorant")  
lista_jogos.append("Transformice")  
lista_livros.append("Perdida_no_tempo")  
lista_livros.append("Onde_está_a_Segunda")  
lista_esporte.append("Volei")  
lista_esporte.append("Basquete")  

print(lista_filmes)
print(lista_jogos)
print(lista_livros)
print(lista_esporte) 

lista_completa =  lista_filmes + lista_jogos + lista_livros + lista_esporte
print(lista_completa)
print(lista_completa.index("Volei"))
lista_esporte.remove("Volei")
print(lista_esporte)
lista_diciplina = lista_completa.copy()