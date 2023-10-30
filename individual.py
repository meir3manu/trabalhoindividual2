# Função para criar uma lista de candidatos com resultados
def criar_lista_de_candidatos():
    candidatos = [
        "Joao_e5_t4_p3_s2",
        "Maria_e4_t3_p5_s1",
        "Pedro_e3_t4_p2_s5",
        "Ana_e4_t4_p4_s4",
    ]
    return candidatos

# Função para buscar candidatos com base nos critérios
def buscar_candidatos(candidatos, criterios):
    resultados = []
    for candidato in candidatos:
        partes = candidato.split("_")
        avaliacoes = [int(partes[1]), int(partes[3]), int(partes[5]), int(partes[7])]
        
        if all(avaliacoes[i] >= criterios[i] for i in range(4)):
            resultados.append(candidato)
    
    return resultados

# Função principal
def main():
    candidatos = criar_lista_de_candidatos()
    
    print("Lista de candidatos:")
    for candidato in candidatos:
        print(candidato)
    
    criterios = []
    for i in range(4):
        criterio = int(input(f"Digite o critério mínimo para a etapa {i + 1}: "))
        criterios.append(criterio)
    
    candidatos_selecionados = buscar_candidatos(candidatos, criterios)
    
    print("Candidatos que atendem aos critérios:")
    for candidato in candidatos_selecionados:
        print(candidato)

if __name__ == "__main__":
    main()