mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
prva_vojska = mat[0]
vtora_vojska = mat[1]
treta_vojska = mat[2]
cetvrta_vojska = mat[3]
petta_vojska = mat[4]




mat1 = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]

mat1.sort()
prva_vojska1 = mat1[0]
vtora_vojska2 = mat1[1]
treta_vojska3 = mat1[2]
cetvrta_vojska4 = mat1[3]
petta_vojska5 = mat1[4]





def SoberiVojnici(lista):
    rezultat = 0
    for x in lista:
        rezultat = rezultat + x
    return rezultat


print(f"Brojot na vojnici vo sekoja vojska e \n prva vojska: {SoberiVojnici(prva_vojska)} \n vtora vojska: {SoberiVojnici(vtora_vojska)} \n treta vojska: {SoberiVojnici(vtora_vojska)} \n cetvrta vojska: {SoberiVojnici(cetvrta_vojska)} \n petta vojska: {SoberiVojnici(petta_vojska)} ")

print(f"Podredeni po broj na vojnici se: \n prva vojska: {SoberiVojnici(prva_vojska1)} \n vtora vojska {SoberiVojnici(vtora_vojska2)} \ntreta vojska {SoberiVojnici(treta_vojska3)} \ncetvrta vojska  {SoberiVojnici(cetvrta_vojska4)}\n petta vojska: {SoberiVojnici(petta_vojska5) } ")
