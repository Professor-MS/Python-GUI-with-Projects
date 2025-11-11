from ucimlrepo import fetch_ucirepo 
  
print("Hello")  
# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
print("Hello")  
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
print("Hello")  
y = heart_disease.data.targets 
  
# metadata 
print(heart_disease.metadata) 
print("Hello")  
  
# variable information 
print(heart_disease.variables) 
print("Hello")  
