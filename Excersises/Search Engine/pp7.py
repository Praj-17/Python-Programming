#SEARCH ENGINE
def matchingWords(s1,s2):
    words1 = s1.split()
    words2 = s2.split()
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"MAtching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score +=1
    return score


# print(matchingWords("This is snake", "Python is good", "harry is a good boy", "Subscribe to code with harry"))
sentences = ["This is snake", "Python is good", "harry is a good boy", "Subscribe to code with harry"]
query = input("PLs input the query string\n")
scores = [matchingWords(query, sentence) for sentence in sentences]
# print(scores)
sortedsentscore = [sentscore for sentscore in sorted(zip(scores, sentences), reverse = True)]
# print(sortedsentscore)
print(f"{len(sortedsentscore)} results found")
for score , item in sortedsentscore:
    print(f"\"{item}\" With a score of \"{score}\"")