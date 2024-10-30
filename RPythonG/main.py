from random import randint, random

# Função para seleção de classe
def classe():
    escolha = input("Escolha a classe (guerreiro ou ladino): ").strip().lower()
    
    if escolha == "guerreiro":
        return {
            "nome": "Thorin Quebramontes",
            "level": 1,
            "exp": 0,
            "expMax": 50,
            "hp": 200,
            "hpMax": 200,
            "dano_base": 8,  # Base do dano como 1d8
            "chance_critico": 0.1,
            "dano_critico": 1,
            "força": 10,
        }
    elif escolha == "ladino":
        return {
            "nome": "Lira Mãos-Leves",
            "level": 1,
            "exp": 0,
            "expMax": 50,
            "hp": 140,
            "hpMax": 140,
            "dano_base": 8,  # Base do dano como 1d8
            "chance_critico": 0.3,
            "dano_critico": 1.5,
            "força": 10,
        }
    else:
        print("Classe inválida! Tente novamente.")
        return classe()
    
player = classe()

# Função para criar um novo NPC baseado no nível do jogador
def criar_npc(level):
    return {
        "nome": f"Goblin de Nível {level}",
        "level": level,
        "dano_base": 8,
        "chance_critico": 0.1,
        "dano_critico": 1.7,
        "hp": 100 + (28 * level),
        "hpMax": 100 + (28 * level),
        "exp": 10 + (2 * level)
    }

# Função para exibir informações do jogador
def exibir_player():
    print(f"Nome: {player['nome']} || Level: {player['level']} || Dano Base: {player['dano_base']} || HP: {player['hp']}/{player['hpMax']} || EXP: {player['exp']}/{player['expMax']}")

# Função para calcular dano com dados variáveis e chance de crítico
def calcular_dano(agente):
    num_dados = 1 + (agente["level"] // 10)  # 1d8 +1d8 a cada 10 níveis
    dano = sum(randint(1, 8) for _ in range(num_dados))  # Calcula o dano com o dado
    
    # Calcula o dano crítico
    if random() < agente["chance_critico"]:
        print("Dano Crítico!")
        dano *= agente["dano_critico"]
    
    return int(dano)

# Funções de batalha
def iniciar_batalha():
    npc = criar_npc(player['level'])
    print(f"A batalha contra {npc['nome']} começa!")
    
    while player['hp'] > 0:
        # Loop de batalha entre o jogador e o NPC atual
        atacar_npc(npc)
        if npc["hp"] <= 0:
            print(f"{npc['nome']} foi derrotado!")
            player["exp"] += npc["exp"]
            level_up()
            if player["level"] == 50:
                print("-------------------\n")
                print(f"Parabéns! Você atingiu o nível 50 e derrotou todos os goblins!")
                print("-------------------\n")
                break
            npc = criar_npc(player['level'])  # Cria um novo NPC com o nível atualizado do jogador
            player['hp'] = player['hpMax']  # Reseta o HP do jogador
            print(f"Um novo {npc['nome']} apareceu!")
            exibir_player()
        
        atacar_player(npc)
        
        if player['hp'] <= 0:
            print(f"{player['nome']} foi derrotado! GAME OVER")
            break
        
        exibir_info_batalha(npc)
    print("-------------------\n")

def atacar_npc(npc):
    dano = calcular_dano(player)
    npc['hp'] -= dano
    print(f"{player['nome']} ataca {npc['nome']} causando {dano} de dano!")

def atacar_player(npc):
    dano = calcular_dano(npc)
    player['hp'] -= dano
    print(f"{npc['nome']} ataca {player['nome']} causando {dano} de dano!")

def level_up():
    if player['exp'] >= player['expMax']:
        player['level'] += 1
        player['exp'] = 0
        player['expMax'] = round(player['expMax'] + 10)
        player['hpMax'] = round(player['hpMax'] + 30)
        player['hp'] = player['hpMax']
        player['dano_base'] = round(player['dano_base'] + 10)    
        print(f"{player['nome']} subiu de nível! Agora está no nível {player['level']}.")

def exibir_info_batalha(npc):
    print(f"Player: {player['nome']} | HP: {player['hp']}/{player['hpMax']}")
    print(f"NPC: {npc['nome']} | HP: {npc['hp']}/{npc['hpMax']}")
    print("-------------------\n")

# Inicialização do jogo e batalha infinita até a morte do jogador
while player['hp'] > 0:
    iniciar_batalha()
    if player['level'] == 50:
        print(f"Você chegou ao nível 50 e derrotou os goblins!")
        break
    else:
        print(f"Game over!")
