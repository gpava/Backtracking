def suma_subconjuntos(suma, conj, subconj=[], suma_subconj=0):
	if suma_subconj == suma:
		print(subconj)
	else:
		for i in range(len(conj)):
			suma_subconjuntos(suma, conj[i + 1:], subconj + [conj[i]], suma_subconj + conj[i])

suma_subconjuntos(11, [1, 2, 3, 5, 8])