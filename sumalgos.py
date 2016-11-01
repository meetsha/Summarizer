from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer 
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumeval import *

def summarize(doc, summarizer):
	summary = summarizer(doc.document, '10%')
	return summary

def lsa(doc, refsum):
	summarizer = LsaSummarizer()
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)

def lexrank(doc, refsum):
	summarizer = LexRankSummarizer()
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)

def textrank(doc, refsum):
	summarizer = TextRankSummarizer()
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)

def luhn(doc, refsum):
	summarizer = LuhnSummarizer()
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)

def klsum(doc, refsum):
	summarizer = KLSummarizer()
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)

if __name__ == '__main__':
	
	file = "doc1.txt"
	parser = PlaintextParser.from_file(file, Tokenizer("english"))

	rfile = "doc1sum.txt"
	refparser = PlaintextParser.from_file(rfile, Tokenizer("english"))
	refparser = refparser.document.sentences

	print(lsa(parser,refparser))

	