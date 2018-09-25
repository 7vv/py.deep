# LDA 모델링 패키지
import gensim
from gensim import corpora, models 

# 한국어 처리
from konlpy.tag import Twitter
twitter = Twitter()

import operator

documents = []

# 중복 토큰 필터
filterDocuments = []

for i in documents:

    # 문장 토큰화
    tokens = twitter.pos(i, norm=True, stem=True)
    
    # 명사만 추출하지 않고 진행시 거리가 먼 분류가 노출됨
    stem_tokens = [split[0] for split in tokens if split[1] == "Noun"]
       
    filterDocuments.append(stem_tokens)
        

# Dictionary 생성
dictinory = corpora.Dictionary(filterDocuments)

# 토큰으로 생성된 사전 중첩처리
corpus = [dictinory.doc2bow(text) for text in filterDocuments]

# LDA 모델 생성
analysisComplateList = []

for i in range(1, 50):
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 6, id2word = dictinory, passes = 20)
    
    ldaResults = ldamodel.print_topics(num_topics = 3, num_words = 1)    

    for result in ldaResults:         
        analysisComplateList.append(tuple(result[1].split("*")))

    print(i, " job working..")

sortldaResults = sorted(analysisComplateList, key=operator.itemgetter(0), reverse=True)

results = set()

for result in sortldaResults:
    results.add(result[1])    
    if len(results) == 3: break

print(sortldaResults)
print(results)

