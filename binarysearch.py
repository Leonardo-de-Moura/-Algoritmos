def binary_search(lista, item):
	baixo= 0
	alto= len(lista)-1
	while baixo <= alto:
		meio= (baixo + alto) / 2
		meio= int(meio)
		chute= lista[meio]
		if chute == item:
			return meio
		if chute > meio:
			alto = meio-1
		if chute < meio:
				alto = meio+1
	return None
lista=[1,2,3,9,89,6,7,8,5,0]
binary_search(lista,5)
