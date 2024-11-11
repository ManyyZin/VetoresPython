import math
import numpy as np

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2) # calcula "math.sqrt"  matriz

    def produto_escalar(self, outro):
        return self.x * outro.x + self.y * outro.y

    def angulo_entre(self, outro):
        produto = self.produto_escalar(outro)
        magnitudes = self.magnitude() * outro.magnitude()
        angulo_rad = math.acos(produto / magnitudes)
        return math.degrees(angulo_rad)

    def vetor_ortogonal(self):
       return Vetor(self.y, self.x)

    def produto_vetorial(self, outro):
        return self.x * outro.y - self.y * outro.x


    def __str__(self):
        return f"Vetor({self.x}, {self.y})"

class SistemaVetores:
    def __init__(self):
        self.vetores = []

    def adicionar_vetor(self, vetor):
        self.vetores.append(vetor)

    def listar_vetores(self):
        for i, vetor in enumerate(self.vetores):
            print(f"{i}: {vetor}")

def main():
    sistema = SistemaVetores()

    while True:
        print("\nMenu:")
        print("1. Adicionar vetor")
        print("2. Calcular produto escalar")
        print("3. Calcular ângulo entre vetores")
        print("4. Calcular vetor ortogonal")
        print("5. Calcular produto vetorial")
        print("6. Calcular magnitude de um vetor")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            x = float(input("Insira a coordenada x do vetor: "))
            y = float(input("Insira a coordenada y do vetor: "))
            vetor = Vetor(x, y)
            sistema.adicionar_vetor(vetor)
            print(f"Vetor {vetor} adicionado.")

        elif escolha == '2':
            sistema.listar_vetores()
            idx1 = int(input("Escolha o índice do primeiro vetor: "))
            idx2 = int(input("Escolha o índice do segundo vetor: "))
            resultado = sistema.vetores[idx1].produto_escalar(sistema.vetores[idx2])
            print(f"Produto escalar: {resultado}")

        elif escolha == '3':
            sistema.listar_vetores()
            idx1 = int(input("Escolha o índice do primeiro vetor: "))
            idx2 = int(input("Escolha o índice do segundo vetor: "))
            resultado = sistema.vetores[idx1].angulo_entre(sistema.vetores[idx2])
            print(f"Ângulo entre os vetores: {resultado:.2f} graus")

        elif escolha == '4':
            sistema.listar_vetores()
            idx = int(input("Escolha o índice do vetor: "))
            ortogonal = sistema.vetores[idx].vetor_ortogonal()
            print(f"Vetor ortogonal: {ortogonal}")

        elif escolha == '5':
            sistema.listar_vetores()
            idx1 = int(input("Escolha o índice do primeiro vetor: "))
            idx2 = int(input("Escolha o índice do segundo vetor: "))
            resultado = sistema.vetores[idx1].produto_vetorial(sistema.vetores[idx2])
            print(f"Produto vetorial: {resultado}")

        elif escolha == '6':
            sistema.listar_vetores()
            idx1 = int(input("Escolha o índice do primeiro vetor: "))
            idx2 = int(input("Escolha o índice do segundo vetor: "))
            if sistema.vetores[idx1].verificar_ortogonalidade(sistema.vetores[idx2]):
                print("Os vetores são ortogonais.")
            else:
                print("Os vetores não são ortogonais.")

        elif escolha == '7':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
