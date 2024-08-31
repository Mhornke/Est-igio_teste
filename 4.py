import csv

with open('faturamento.csv', mode='w') as arq:
    escritor = csv.writer(arq)
    escritor.writerow(['ESTADO','FATURAMENTO'])   
    escritor.writerow(['SP',67.83643])   
    escritor.writerow(['RJ',36.67866])   
    escritor.writerow(['MG',29.22988])   
    escritor.writerow(['ES',27.16558])   
    escritor.writerow(['OUTROS',19.84853])  
    
with open('faturamento.csv', mode='r') as arq:
    leitor = csv.DictReader(arq)
    
    total = 0
    valores =[]
    
    for valor in leitor:
        faturaTotal = float(valor['FATURAMENTO'])       
        total += faturaTotal 
        valores.append(valor)
                  
    for estado in valores:
        faturamento = float(estado['FATURAMENTO'])
        porcentual = ((faturamento/total)*100)
        
        print(f"Estado: {estado['ESTADO']} {porcentual:.2F}%")
        
        
        
    
      
    
      