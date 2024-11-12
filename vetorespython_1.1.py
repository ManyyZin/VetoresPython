import math
import numpy as np


class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def produto_escalar(self, outro):
        return self.x * outro.x + self.y * outro.y

    def angulo_entre(self, outro):
        produto = self.produto_escalar(outro)
        magnitudes = self.magnitude() * outro.magnitude()
        cos_theta = produto / magnitudes
        cos_theta_clipped = np.clip(cos_theta, -1.0, 1.0)
        angulo_rad = math.acos(cos_theta_clipped)
        return math.degrees(angulo_rad)


    def produto_vetorial(self, outro):
        return self.x * outro.y - self.y * outro.x

    def verificar_ortogonalidade(self, outro):
        produto_escalar = self.produto_escalar(outro)
        return produto_escalar == 0

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
        print("3. Calcular ângulo")
        print("4. Calcular produto vetorial")
        print("5. Calcular magnitude")
        print("6. Verificar ortogonalidade")
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
            idx1 = int(input("Escolha o índice do primeiro vetor: "))
            idx2 = int(input("Escolha o índice do segundo vetor: "))
            resultado = sistema.vetores[idx1].produto_vetorial(sistema.vetores[idx2])
            print(f"Produto vetorial: {resultado}")

        elif escolha == '5':
            sistema.listar_vetores()
            idx = int(input("Escolha o índice do vetor: "))
            resultado = sistema.vetores[idx].magnitude()
            print(f"Magnitude do vetor: {resultado:.2f}")

        elif escolha == '6':
            sistema.listar_vetores()
            idx1 = int(input("Escolha o índice do primeiro vetor: "))
            idx2 = int(input("Escolha o índice do segundo vetor: "))
            if sistema.vetores[idx1].verificar_ortogonalidade(sistema.vetores[idx2]):
                print(f"Os vetores são ortogonais.")
            else:
                print(f"Os vetores não são ortogonais.")

        elif escolha == '7':
            print("Saindo do programa.")
            break


if __name__ == "__main__":
    main()