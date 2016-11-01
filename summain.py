from sumy.parsers.plaintext import PlaintextParser
from sumalgos import *

if __name__ == '__main__':
	types = ['sc','sp','po']
	for t in types:
		for i in range(1,6):
			docfile = t + "doc" + str(i) + ".txt"
			docparser = PlaintextParser.from_file(docfile, Tokenizer("english"))
			sumfile = t + "doc" + str(i) + "sum.txt"
			sumparser =  PlaintextParser.from_file(sumfile, Tokenizer("english"))
			sumparsed_sen = sumparser.document.sentences

			lsa_results = lsa(docparser, sumparsed_sen)
			luhn_results = luhn(docparser, sumparsed_sen)
			klsum_results = klsum(docparser, sumparsed_sen)
			textrank_results = textrank(docparser, sumparsed_sen)
			lexrank_results = lexrank(docparser, sumparsed_sen)

			print("Lsa:", lsa_results)
			print("Klsum:", klsum_results)
			print("TextRank:", textrank_results)
			print("LexRank:", lexrank_results)
			print("Luhn:", luhn_results)


