# =====================================================
# MIXINS EXTRAS
class RastreadorGPS:
    """Permite rastrear a localização do veículo"""
    def __init__(self):
        self.localizacao = "Desconhecida"

    def atualizar_localizacao(self, local):
        self.localizacao = local
        return f"{self.__class__.__name__} agora está em {self.localizacao}"

    def rastrear(self):
        return f"{self.__class__.__name__} localizado em {self.localizacao}"


class Conectividade:
    """Permite conectar o veículo a redes Wi-Fi"""
    def __init__(self):
        self.conectado = False

    def conectar_wifi(self, rede):
        self.conectado = True
        return f"{self.__class__.__name__} conectado à rede {rede}"

    def desconectar_wifi(self):
        self.conectado = False
        return f"{self.__class__.__name__} desconectado da rede"


class SistemaSeguranca:
    """Adiciona sistema de alarme e segurança"""
    def __init__(self):
        self.alarme_ativo = False

    def ativar_alarme(self):
        self.alarme_ativo = True
        return f"{self.__class__.__name__} com alarme ativado!"

    def desativar_alarme(self):
        self.alarme_ativo = False
        return f"{self.__class__.__name__} com alarme desativado!"

# CLASSE BASE VEÍCULO
class Veiculo:
    """Classe base para todos os veículos"""
    qtd_veiculos = 0  # Contador de veículos instanciados

    def __init__(self, nome, capacidade, combustivel):
        self.nome = nome
        self.capacidade = capacidade
        self.combustivel = combustivel
        self.ligado = False
        Veiculo.qtd_veiculos += 1  # Incrementa contador

    def ligar(self):
        self.ligado = True
        return f"{self.nome} foi ligado."

    def desligar(self):
        self.ligado = False
        return f"{self.nome} foi desligado."

    def mover(self):
        """Método polimórfico: pode ser sobrescrito"""
        return f"{self.nome} está se movendo."

    @classmethod
    def total_veiculos(cls):
        """Retorna total de veículos criados"""
        return f"Total de veículos criados: {cls.qtd_veiculos}"

    def __str__(self):
        return f"{self.nome} - Capacidade: {self.capacidade} pessoas - Combustível: {self.combustivel}"

# VEÍCULOS TERRESTRES
class VeiculoTerrestre(Veiculo):
    """Classe intermediária para veículos terrestres"""
    def __init__(self, nome, capacidade, combustivel, rodas):
        super().__init__(nome, capacidade, combustivel)
        self.rodas = rodas

    def __str__(self):
        return f"{super().__str__()} - Rodas: {self.rodas}"


class Carro(VeiculoTerrestre):
    """Herança simples: Carro"""
    def __init__(self, nome, capacidade, combustivel, portas):
        super().__init__(nome, capacidade, combustivel, rodas=4)
        self.portas = portas

    def __str__(self):
        return f"{super().__str__()} - Portas: {self.portas}"


class Moto(VeiculoTerrestre):
    """Herança simples: Moto"""
    def __init__(self, nome, capacidade, combustivel, cilindrada):
        super().__init__(nome, capacidade, combustivel, rodas=2)
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()} - Cilindrada: {self.cilindrada}cc"


class Caminhao(VeiculoTerrestre):
    """Herança simples: Caminhão"""
    def __init__(self, nome, capacidade, combustivel, carga_maxima):
        super().__init__(nome, capacidade, combustivel, rodas=6)
        self.carga_maxima = carga_maxima

    def __str__(self):
        return f"{super().__str__()} - Carga Máxima: {self.carga_maxima} toneladas"


class Onibus(VeiculoTerrestre):
    """Herança simples: Ônibus"""
    def __init__(self, nome, capacidade, combustivel, tipo):
        super().__init__(nome, capacidade, combustivel, rodas=8)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} - Tipo: {self.tipo}"

# VEÍCULOS AÉREOS
class VeiculoAereo(Veiculo):
    """Classe intermediária para veículos aéreos"""
    def __init__(self, nome, capacidade, combustivel, alcance):
        super().__init__(nome, capacidade, combustivel)
        self.alcance = alcance

    def __str__(self):
        return f"{super().__str__()} - Alcance: {self.alcance} km"


class JatoExecutivo(VeiculoAereo):
    """Herança simples: Jato Executivo"""
    def __init__(self, nome, capacidade, combustivel, alcance, luxo):
        super().__init__(nome, capacidade, combustivel, alcance)
        self.luxo = luxo

    def __str__(self):
        return f"{super().__str__()} - Luxo: {self.luxo}"


class Helicoptero(VeiculoAereo):
    """Herança simples: Helicóptero"""
    def __init__(self, nome, capacidade, combustivel, alcance, rotores):
        super().__init__(nome, capacidade, combustivel, alcance)
        self.rotores = rotores

    def __str__(self):
        return f"{super().__str__()} - Rotores: {self.rotores}"

# VEÍCULOS FERROVIÁRIOS
class VeiculoFerroviario(Veiculo):
    """Classe intermediária para veículos ferroviários"""
    def __init__(self, nome, capacidade, combustivel, trilhos):
        super().__init__(nome, capacidade, combustivel)
        self.trilhos = trilhos

    def __str__(self):
        return f"{super().__str__()} - Trilhos: {self.trilhos}"


class Trem(VeiculoFerroviario):
    """Herança simples: Trem"""
    def __init__(self, nome, capacidade, combustivel, tipo):
        super().__init__(nome, capacidade, combustivel, trilhos=True)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} - Tipo: {self.tipo}"

# VEÍCULOS MARÍTIMOS
class VeiculoMaritimo(Veiculo):
    """Classe intermediária para veículos marítimos"""
    def __init__(self, nome, capacidade, combustivel, tamanho):
        super().__init__(nome, capacidade, combustivel)
        self.tamanho = tamanho

    def __str__(self):
        return f"{super().__str__()} - Tamanho: {self.tamanho}"

class Navio(VeiculoMaritimo):
    """Herança simples: Navio"""
    def __init__(self, nome, capacidade, combustivel, tamanho, tipo):
        super().__init__(nome, capacidade, combustivel, tamanho)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} - Tipo: {self.tipo}"

class Barco(VeiculoMaritimo):
    """Herança simples: Barco"""
    def __init__(self, nome, capacidade, combustivel, tamanho, finalidade):
        super().__init__(nome, capacidade, combustivel, tamanho)
        self.finalidade = finalidade

    def __str__(self):
        return f"{super().__str__()} - Finalidade: {self.finalidade}"

# VEÍCULOS ANFÍBIOS (HERANÇA MÚLTIPLA)
class VeiculoAnfibio(Veiculo):
    """Herança múltipla simplificada: pode se mover em terra e água"""
    def __init__(self, nome, capacidade, combustivel, rodas, tamanho):
        self.nome = nome
        self.capacidade = capacidade
        self.combustivel = combustivel
        self.rodas = rodas
        self.tamanho = tamanho
        self.ligado = False

    def mover(self):
        return f"{self.nome} pode se mover tanto em terra quanto na água."

    def __str__(self):
        return f"{self.nome} - Capacidade: {self.capacidade} - Combustível: {self.combustivel} - Rodas: {self.rodas} - Tamanho: {self.tamanho}"

# VEÍCULOS ESPACIAIS
class VeiculoEspacial(Veiculo):
    """Classe intermediária para veículos espaciais"""
    def __init__(self, nome, capacidade, combustivel, alcance, carga):
        super().__init__(nome, capacidade, combustivel)
        self.alcance = alcance
        self.carga = carga

    def lancar(self):
        return f"{self.nome} foi lançado ao espaço com {self.carga}"

    def __str__(self):
        return f"{super().__str__()} - Alcance: {self.alcance} km - Carga: {self.carga}"


class Foguete(VeiculoEspacial):
    """Herança simples: Foguete"""
    pass

# VEÍCULOS MILITARES
class VeiculoMilitar(Veiculo):
    """Classe base para veículos militares"""
    def __init__(self, nome, capacidade, combustivel, tipo):
        super().__init__(nome, capacidade, combustivel)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} - Tipo Militar: {self.tipo}"


class Tanque(VeiculoMilitar):
    """Herança simples: Tanque"""
    def __init__(self, nome, capacidade, combustivel, tipo, calibre):
        super().__init__(nome, capacidade, combustivel, tipo)
        self.calibre = calibre

    def atirar(self):
        return f"{self.nome} disparou um projétil de {self.calibre}mm!"

    def __str__(self):
        return f"{super().__str__()} - Calibre: {self.calibre}mm"


class Submarino(VeiculoMilitar):
    """Herança simples: Submarino"""
    def __init__(self, nome, capacidade, combustivel, tipo, profundidade_maxima):
        super().__init__(nome, capacidade, combustivel, tipo)
        self.profundidade_maxima = profundidade_maxima

    def lancar_torpedo(self):
        return f"{self.nome} lançou um torpedo!"

    def __str__(self):
        return f"{super().__str__()} - Profundidade máxima: {self.profundidade_maxima}m"


class PortaAvioes(VeiculoMilitar):
    """Herança simples: Porta-aviões"""
    def __init__(self, nome, capacidade, combustivel, tipo, aeronaves):
        super().__init__(nome, capacidade, combustivel, tipo)
        self.aeronaves = aeronaves

    def lancar_aviao(self):
        return f"{self.nome} lançou um avião de combate!"

    def __str__(self):
        return f"{super().__str__()} - Aeronaves a bordo: {self.aeronaves}"


class DroneMilitar(VeiculoAereo):
    """Herança simples: Drone Militar"""
    def __init__(self, nome, capacidade, combustivel, alcance, armamento):
        super().__init__(nome, capacidade, combustivel, alcance)
        self.armamento = armamento

    def atacar(self):
        return f"{self.nome} disparou {self.armamento}!"

    def __str__(self):
        return f"{super().__str__()} - Armamento: {self.armamento}"


class CacaMilitar(VeiculoAereo):
    """Herança simples: Caça militar"""
    def __init__(self, nome, capacidade, combustivel, alcance, velocidade_maxima):
        super().__init__(nome, capacidade, combustivel, alcance)
        self.velocidade_maxima = velocidade_maxima

    def manobra(self):
        return f"{self.nome} realizou uma manobra evasiva supersônica!"

    def __str__(self):
        return f"{super().__str__()} - Velocidade máxima: {self.velocidade_maxima} km/h"

# VEÍCULOS INTELIGENTES (HERANÇA MÚLTIPLA + MIXINS)
class CarroInteligente(Carro, RastreadorGPS, Conectividade, SistemaSeguranca):
    """Herança múltipla: Carro Inteligente"""
    def __init__(self, nome, capacidade, combustivel, portas):
        Carro.__init__(self, nome, capacidade, combustivel, portas)
        RastreadorGPS.__init__(self)
        Conectividade.__init__(self)
        SistemaSeguranca.__init__(self)

class NavioInteligente(Navio, RastreadorGPS, Conectividade, SistemaSeguranca):
    """Herança múltipla: Navio Inteligente"""
    def __init__(self, nome, capacidade, combustivel, tamanho, tipo):
        Navio.__init__(self, nome, capacidade, combustivel, tamanho, tipo)
        RastreadorGPS.__init__(self)
        Conectividade.__init__(self)
        SistemaSeguranca.__init__(self)

class DroneInteligente(DroneMilitar, RastreadorGPS, Conectividade, SistemaSeguranca):
    """Herança múltipla: Drone Inteligente"""
    def __init__(self, nome, capacidade, combustivel, alcance, armamento):
        DroneMilitar.__init__(self, nome, capacidade, combustivel, alcance, armamento)
        RastreadorGPS.__init__(self)
        Conectividade.__init__(self)
        SistemaSeguranca.__init__(self)

# CÓDIGO PRINCIPAL
if __name__ == "__main__":

    # Criando todos os veículos
    veiculos = [
        Carro("Fusca", 4, "gasolina", 2),
        Moto("Honda CG", 2, "gasolina", 160),
        Caminhao("Scania", 3, "diesel", 30),
        Onibus("Marcopolo", 50, "diesel", "urbano"),
        JatoExecutivo("Gulfstream", 12, "querosene", 6000, "alto luxo"),
        Helicoptero("Esquilo", 6, "querosene", 800, 1),
        Trem("Trem Bala", 600, "eletricidade", "passageiros"),
        Navio("Titanic", 3000, "carvão", "gigante", "passageiros"),
        Barco("Barco de Pesca", 10, "diesel", "pequeno", "pesca"),
        VeiculoAnfibio("DuckWheels", 6, "diesel", 4, "médio"),
        Foguete("Falcon 9", 50, "querosene", 28000, "satélite Starlink"),
        Tanque("Leopard 2", 4, "diesel", "pesada", 120),
        Submarino("U-Boat", 50, "nuclear", "grande", 500),
        PortaAvioes("USS Nimitz", 5000, "nuclear", "gigante", 90),
        DroneMilitar("Predator", 2, "querosene", 1000, "mísseis Hellfire"),
        CacaMilitar("F-22 Raptor", 1, "querosene", 3000, 2400),
        CarroInteligente("Tesla Model S", 5, "elétrico", 4),
        NavioInteligente("Sea Explorer", 200, "diesel", "grande", "carga"),
        DroneInteligente("Drone X", 1, "eletricidade", 50, "câmera HD")
    ]

    # TESTE DE MÉTODOS
    print("\n=== TESTANDO MÉTODOS DE VEÍCULOS ===")
    for v in veiculos:
        print(v.ligar())
        print(v.mover())
        print(v.desligar())
        
        # Testando métodos de veículos militares
        if isinstance(v, Tanque):
            print(v.atirar())
        if isinstance(v, Submarino):
            print(v.lancar_torpedo())
        if isinstance(v, PortaAvioes):
            print(v.lancar_aviao())
        if isinstance(v, DroneMilitar):
            print(v.atacar())
        if isinstance(v, CacaMilitar):
            print(v.manobra())

        # Testando mixins
        if isinstance(v, (CarroInteligente, NavioInteligente, DroneInteligente)):
            print(v.atualizar_localizacao("Base Alpha"))
            print(v.rastrear())
            print(v.conectar_wifi("RedeSegura"))
            print(v.ativar_alarme())

    # TABELA DE VISÃO GERAL
    print("\n=== TABELA DE VISÃO GERAL DE VEÍCULOS ===")
    print(f"{'NOME':<20} {'TIPO':<20} {'CAPACIDADE':<10} {'COMBUSTÍVEL':<12} {'CARACTERÍSTICAS':<50}")
    print("-" * 120)
    for v in veiculos:
        tipo = v.__class__.__name__
        caracteristicas = str(v).replace(str(v.nome)+" - ", "")
        print(f"{v.nome:<20} {tipo:<20} {v.capacidade:<10} {v.combustivel:<12} {caracteristicas:<50}")

    # Total de veículos criados
    print("\n=== TOTAL DE VEÍCULOS CRIADOS ===")
    print(Veiculo.total_veiculos())
