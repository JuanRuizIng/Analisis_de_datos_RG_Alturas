import pandas as pd

df_base_v1 = pd.read_excel("BASE DATOS RG ALTURAS.xlsx", sheet_name ="GENERAL")
df_cer_b = pd.read_excel("CARGA MASIVA 2022 - Certificados B.xlsx", sheet_name="CARGA MASIVA 2022 - Certificado")

df_base_v1 = df_base_v1.loc[1770:3890,"PRIMER NOMBRE":"# DOCUMENTO"]
df_base_v1 = df_base_v1.drop(["TIPO DE DOCUMENTO"], axis=1)
df_cer_b = df_cer_b.loc[0:2117, "No documento":"Apellidos"]

#print(df_cer_b.head(-1))
#print(df_base_v1.head(-1))

df_base_v1["NOMBRES"] = df_base_v1["PRIMER NOMBRE"].astype(str) + " " + df_base_v1["SEGUNDO NOMBRE"].astype(str)

df_base_v1["APELLIDOS"] = df_base_v1["PRIMER APELLIDO"].astype(str) + " " + df_base_v1["SEGUNDO APELLIDO"].astype(str)

df_base_v1["NOMBRES Y APELLIDOS"] = df_base_v1["NOMBRES"].astype(str) + " " + df_base_v1["APELLIDOS"].astype(str)

df_cer_b["NOMBRES Y APELLIDOS"] = df_cer_b["Nombres"].astype(str) + " " + df_cer_b["Apellidos"].astype(str)

df_base_v1["NOMBRE COMPLETO Y CÉDULA"] = df_base_v1["NOMBRES Y APELLIDOS"].astype(str) + " " + df_base_v1["# DOCUMENTO"].astype(str)

df_cer_b["NOMBRE COMPLETO Y CÉDULA"] = df_cer_b["NOMBRES Y APELLIDOS"].astype(str) + " " + df_cer_b["No documento"].astype(str)

#print(df_base_v1["NOMBRES Y APELLIDOS"])

def limpiar_nan(cadena):
    return cadena !="nan"

lista_base_v1 = []
lista_base_cer_b = []
posibles_cedulas_confusas = []
posibles_cedulas_confusas_comparar = []

for persona in df_base_v1["NOMBRE COMPLETO Y CÉDULA"]:
    lista_base_v1.append(persona)

for persona in df_cer_b["NOMBRE COMPLETO Y CÉDULA"]:
    lista_base_cer_b.append(persona)

lista_base_v1 = [x.replace("nan", "") for x in lista_base_v1]
lista_base_v1 = [x.replace("  ", " ") for x in lista_base_v1]

#print(lista_base_v1)
#print(lista_base_cer_b[0])

for persona in lista_base_v1:
    if persona in lista_base_cer_b:
        pass
    else:
        posibles_cedulas_confusas.append(persona)

print(posibles_cedulas_confusas)
print(len(posibles_cedulas_confusas))