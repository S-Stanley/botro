def ask(message: str):
	q = input(message).lower()
	return q

def response(data: list, q: str):
	for item in data:
		x = item.split('&&')
		if x[0] == q:
			return x[1]
	return ('Je n\'ai pas compris la question')

def main():
	with open('data', 'r') as f:
		data = f.readlines()
	q = ask('Salut, je suis botro, quoi de neuf ?')
	while True:
		r = response(data, q)
		print(r)
		q = ask('')

main()