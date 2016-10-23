from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer 
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.evaluation import cosine_similarity
from sumy.models import TfDocumentModel


file = "doc1.txt"
parser = PlaintextParser.from_file(file, Tokenizer("english"))
print(parser.document)

print("\nLexRank:")
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 10)
for sen in summary:
	print(sen)

print("\nTextRank:")
summarizer = TextRankSummarizer()
summary = summarizer(parser.document, 10)
for sen in summary:
	print(sen)

print("\nLSA:")
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 10)
lsasum = ""
for sen in summary:
	print(sen)
	lsasum += str(sen)

print("\nLuhn:")
summarizer = LuhnSummarizer()
summary = summarizer(parser.document, 10)
for sen in summary:
	print(sen)

print("\nKL:")
summarizer = KLSummarizer()
summary = summarizer(parser.document, 10)
klsum = ""
for sen in summary:
	klsum += str(sen)


sum_text = """On the internet, I rarely engage in social/political/religious discussions. That’s not for a lack of opinion. 
There is clearly a hierarchy of importance of these issues. However, social media doesn’t always project it in that manner
The tendency of knee-jerk reactions on online platforms is staggering. People don’t realize that in today’s day and age, every word they put up on Facebook or Twitter has weight. Day in and day out, people’s words have the power to make or break someone
People have surprisingly limited attention spans these days. Therefore everything has a shelf life, even news items
These days, if you do decide to take up the debate through a logical discourse by educating yourself first, a process which would naturally take some time, you are considered to be out of step with the trend, for you have missed the ‘window of opportunity’ pertaining to the issue. Its almost as if taking time to put forward a measured, weighted and logical stance is an undesired quality.
Social media is integral in formulating public opinion and is an active stakeholder in reflecting societal expectations and perceptions.
Conflicting viewpoints aren’t dangerous. Unsubstantiated viewpoints are dangerous.
"""
lsasummodel = TfDocumentModel(lsasum, Tokenizer("english"))
summodel = TfDocumentModel(sum_text, Tokenizer("english"))

print(cosine_similarity(lsasummodel, summodel))
