import pprint
from sumy.parsers.plaintext import PlaintextParser
from sumalgos import *

def updatescore(d, algo, scores):
	for i in range(len(scores)):
		d[algo][i] += scores[i]/5

def bestalgo(d):
	algo_scores = dict()

	for i in range(5):
		maxa = ""
		maxs = 0
		for key, scores in d.items():
			if scores[i] > maxs:
				maxa = key
				maxs = scores[i]
#		print(maxa, maxs)
		algo_scores[maxa] = algo_scores.get(maxa, 0) + 1

#	print(algo_scores)

	maxs = 0
	maxa = ""
	for key, val in algo_scores.items():
		if val > maxs:
			maxs = val
			maxa = key

	return maxa

if __name__ == '__main__':
	types = ['ent', 'sports', 'science']
	for t in types:
		catscore = dict()
		catscore['lsa'] = [0,0,0,0,0]
		catscore['klsum'] = [0,0,0,0,0]
		catscore['textrank'] = [0,0,0,0,0]
		catscore['lexrank'] = [0,0,0,0,0]
		catscore['luhn'] = [0,0,0,0,0]

		start = 1
		end = 6
		if t == 'science':
			start = 6
			end = 11
		
		for i in range(start,end):
#			print(t, i, ":")
			docfile = "corpus/" + t + str(i) + ".txt"
			docparser = PlaintextParser.from_file(docfile, Tokenizer("english"))
			sumfile = "corpus/" + t + str(i) + "sum.txt"
			sumparser =  PlaintextParser.from_file(sumfile, Tokenizer("english"))
			sumparsed_sen = sumparser.document.sentences

			lsa_results = lsa(docparser, sumparsed_sen)
			updatescore(catscore,'lsa',lsa_results)
			luhn_results = luhn(docparser, sumparsed_sen)
			updatescore(catscore,'luhn',luhn_results)
			klsum_results = klsum(docparser, sumparsed_sen)
			updatescore(catscore,'klsum',klsum_results)
			textrank_results = textrank(docparser, sumparsed_sen)
			updatescore(catscore,'textrank',textrank_results)
			lexrank_results = lexrank(docparser, sumparsed_sen)
			updatescore(catscore,'lexrank',lexrank_results)

#			print("Lsa:", lsa_results)
#			print("Klsum:", klsum_results)
#			print("TextRank:", textrank_results)
#			print("LexRank:", lexrank_results)
#			print("Luhn:", luhn_results)

		print(t)
		pprint.pprint(catscore, width=1)
		print("Best for ", t, ": ", bestalgo(catscore))
		
