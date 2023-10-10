import pandas as pd

#Uso basico de PANDAS
#1. fuente de datos (Lista)

ciudades=['Jerusalen','Telabit','Kiev','itagui','pitalito']

#2.Procesar y convertir una lista en Dataframe

dataframeciudades=pd.DataFrame({'Ciudad':ciudades})

print(dataframeciudades)

######
#1. Fuente de datos una list de diccionarios(Coleccion)
estudiantes=[
    {'id':1,'nombre':'Juan Discotecas', 'promedio':0.0},
    {'id':1,'nombre':'Santi el Bicho', 'promedio':0.5},
    {'id':1,'nombre':'Santi diomedez', 'promedio':2.0},
    {'id':1,'nombre':'susana no vivi', 'promedio':1.8},
    {'id':1,'nombre':'Manuela todo si', 'promedio':5.0},
]
#2. convertir los datos de ebtrada enun dataframe 

dataframeEstudiantes=pd.DataFrame(estudiantes)

print(dataframeEstudiantes)