import csv

asibf = []
asiba = []

inaf=[]
inaa=[]

chrisf=[]
chrisa=[]
with open('D:\Projects\harrypotterFanFiction\data\evaluation\\asibbewertung.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        asibf.append(int(row['fluency']))
        asiba.append(int(row['adequacy']))

with open('D:\Projects\harrypotterFanFiction\data\evaluation\\chrisbewertung.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        chrisf.append(int(row['fluency']))
        chrisa.append(int(row['adequacy']))

with open('D:\Projects\harrypotterFanFiction\data\evaluation\\inabewertung.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        inaf.append(int(row[' fluency']))
        inaa.append(int(row[' adequacy']))

print(af := sum(asibf)/len(asibf))
print(aa := sum(asiba)/len(asiba))

print(cf := sum(chrisf)/len(chrisf))
print(ca := sum(chrisa)/len(chrisa))

print(iaf :=sum(inaf)/len(inaf))
print(ia := sum(inaa)/len(inaa))

print("-------------------------------------------------------------------------")
print(gesaf := (af+cf+iaf)/3)
print(gesaa := (aa+ca+ia)/3)

def interAnnotatorAgreement(list1, list2):
    k = 0
    for i in range(0,len(list1)):
        if list1[i] == list2[i]:
            k = k + 1
    rel = k/len(list1)
    return ((rel - 0.2)/0.8)

print("##################################################################################")
print(avgiaaa := (interAnnotatorAgreement(chrisa, asiba) + interAnnotatorAgreement(inaa, asiba) + interAnnotatorAgreement(inaa, chrisa))/3)
print(avgiaaf := (interAnnotatorAgreement(chrisf, asibf) + interAnnotatorAgreement(inaf, asibf) + interAnnotatorAgreement(inaf, chrisf))/3)
print((avgiaaa + avgiaaf)/2)