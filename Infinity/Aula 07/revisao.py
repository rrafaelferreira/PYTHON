# Você tem uma lista de registros de notas: registros = [('Matemática', 8.5), ('História', 9.0), ('Matemática', 7.0)]. Use um laço for para converter essa lista de tuplas em um dicionário, onde as chaves são as matérias e os valores são as notas. Se houver notas duplicadas para a mesma matéria, a última nota deve ser a que prevalece. Use um set comprehension para criar um set contendo todas as matérias únicas. Imprima o dicionário final e o set de matérias únicas.

registros = [('Matemática', 8.5), ('História', 9.0), ('Matemática', 7.0)]
notas = {}

for materia, nota in registros:
    notas[materia] = nota  

materias_unicas = {materia for materia, _ in registros}

print(notas)
print(materias_unicas)