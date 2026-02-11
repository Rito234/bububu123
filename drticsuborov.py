#fr = open("subory/data.txt", "r", encoding="utf-8")

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

#def is_cool(word):
 # for i in range(len(word)-1):
  #    if word[i] > word[i+1]:
   #       return False
  #return True

#words = 0
#words_no_e = 0
#words_e = 0
#for row in fr:
 #   row = row.strip() #oddrbal som enter
  #  words +=1
   # if 'e' in row:
    #    words_e +=1
    #else:
     #   words_no_e +=1
#print("Počet slov spolu:", words)
#print("Počet slov s písmenom e:", words_e) 
#print("Počet slov bez písmena e:", words_no_e)
#print(is_cool("aba"))

#domaca uloha kolko je slov bez samohlasiek
#def is_cool2(word):
#    vowels = "aeiouy"
#    for vowel in vowels:
#        if vowel in word:
#            return False
#    return True
fr = open("subory/meteo_stanice.txt", "r", encoding="utf-8")
fw = open("subory/moje_vystupy", "w", encoding="utf-8")
counter = 0
max_teplota = -1000
temperatures = []
for row in fr:
    processed_line = row.strip().split(" ")
    temperatures.append(float(processed_line[3].replace(",", ".")))
    print(processed_line)
    counter += 1
print(f"Počet meraní: {counter}")
fw.write(f"Počet meraní: {counter}")
fw.write("\n")
print(f"Teploty su: {temperatures}")
print(f"Najvysia teplota: {max(temperatures)}")
fw.write(f"Najvysia teplota: {max(temperatures)}\n")
fw.close()