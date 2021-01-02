def training():
	try:
		q = input('Posez une question:').lower()
		r = input('Donner la réponse:').lower()
		with open('data', 'a') as f:
			f.write(f'{q}&&{r}\n')
		return True
	except Exception as e:
		print(e)
		return False

training()