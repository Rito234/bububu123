fr = open("subory/data.txt", "r", encoding="utf-8")

#Prvý spôsob čítania súboru
#for row in fr:
#   print(row)

#Druhý spôsob čítania súboru
#jozo = fr.readlines()
#print(jozo)

#Tretí spôsob čítania súboru
#first_line = fr.readline()
#print(first_line)
#for row in fr:
#    print(row)

def is_cool(word):
  for i in range(len(word)-1):
      if word[i] > word[i+1]:
          return False
  return True

words = 0
words_no_e = 0
words_e = 0
for row in fr:
    row = row.strip() #oddrbal som enter
    words +=1
    if 'e' in row:
        words_e +=1
    else:
        words_no_e +=1
print("Počet slov spolu:", words)
print("Počet slov s písmenom e:", words_e) 
print("Počet slov bez písmena e:", words_no_e)
print(is_cool("aba"))

#domaca uloha kolko je slov bez samohlasiek
def is_cool2(word):
    vowels = "aeiouy"
    for vowel in vowels:
        if vowel in word:
            return False
    return True