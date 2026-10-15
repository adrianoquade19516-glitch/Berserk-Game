# Berserk

## 1. Tema e objetivo
Num mundo medieval devastado por demónios chamados Apóstolos, o jogador cria um
mercenário e percorre a Terra Sombria a caçar monstros. Ganha dinheiro e experiência
em combates e missões, compra armas e poções na loja e sobe de nível para enfrentar
inimigos cada vez mais fortes. Fica em 1.º no ranking quem tiver o nível mais alto,
desempatando por XP e depois por vitórias.

## 2. Classes de personagem
| Classe     | Vida | Ataque | Defesa | Energia |
|------------|------|--------|--------|---------|
| Espadachim | 130  | 14     | 8      | 100     |
| Besteiro   | 100  | 16     | 5      | 100     |
| Feiticeiro | 85   | 20     | 3      | 100     |

Dinheiro inicial: 300 moedas.

### Habilidades (usadas em combate no lugar do ataque normal)
| Classe     | Habilidade       | Nível | Custo energia | Efeito |
|------------|------------------|-------|---------------|--------|
| Knight Night | Golpe Brutal   | 1     | 15 | dano ×1,8 |
| Ebon Edge  | Fúria DOs Deuses | 3     | 20 | ataque +50% durante 3 turnos |
| Basilisk   | Tiro Certeiro    | 1     | 15 | dano ×1,6, ignora metade da defesa do alvo |
| Besteiro   | Chuva de Setas   | 3     | 25 | 3 disparos, cada um com dano ×0,7 |
| Hydra      | Bola de Fogo     | 1     | 20 | dano ×2,0 |
| Feiticeiro | Barreira Mística | 3     | 15 | defesa ×2 durante 2 turnos |

## 3. Experiência e níveis
- XP para passar ao nível seguinte: 100 × nível atual
- Ao subir de nível: +10 vida máxima, +2 ataque, +1 defesa, vida recupera toda
- Nível máximo: 20
- Formas de ganhar XP: combates, missões

## 4. Itens da loja
| Nome                | Tipo      | Preço | Stock | Efeito |
|---------------------|-----------|-------|-------|--------|
| Poção de Vida       | poção     | 50    | 100   | recupera 30 de vida |
| Freyjasgard         | Map       | 60    | 80    | Mapa para encontrar a cidade de Freyja |
| Furled Finger       | Invocador | 20.000| 20    | Poder invocar 50 zombies ao redor |
| Dragonslayer        | Espada    | 400.00| 5     | +10 ataque |
| Heart of Bayle      | Coração   | 1.000 | 5     | +50 FUria Da Noite |
| Armadura de Ferro   | armadura  | 3.550 | 8     | +7 defesa |

Regra de venda: a loja compra por 50% do preço.
Itens que se podem "usar": Poção de Vida e Elixir de Energia (consumidos ao usar).
Armas e armaduras ficam equipadas (máx. 1 arma e 1 armadura) e os bónus são permanentes enquanto equipadas.

## 5. Adversários
| Nome               | Nível | Vida | Ataque | Defesa | Dinheiro | XP  | Prob. crítico | Prob. fuga |
|--------------------|-------|------|--------|--------|----------|-----|---------------|------------|
| Bandido            | 1     | 40   | 8      | 3      | 30       | 40  | 5%            | 10%        |
| Lobo Demoníaco     | 2     | 70   | 12     | 5      | 60       | 70  | 8%            | 10%        |
| Troll da Floresta  | 3     | 120  | 18     | 10     | 120      | 120 | 10%           | 5%         |
| Apóstolo           | 5     | 300  | 30     | 20     | 400      | 300 | 15%           | 0%         |

## 6. Regras de combate
1. **Condições:** a personagem precisa de pelo menos 30% da vida máxima e de 10 de energia.
2. **Energia:** iniciar um combate gasta 10 de energia. Cada habilidade gasta ainda o seu custo.
   Se a energia não chegar para uma habilidade, só pode usar o ataque normal.
   A energia volta a 100 ao descansar na estalagem (20 moedas).
3. **Quem ataca primeiro:** a personagem. Depois alternam-se turnos.
4. **Dano:** `dano base = máx(1, Ataque do atacante − Defesa do alvo ÷ 2)`.
   As habilidades multiplicam este valor, conforme a tabela da secção 2.
5. **Sorte:** o dano é multiplicado por um valor aleatório entre 0,9 e 1,1.
   Há ainda a probabilidade de crítico do adversário (dano ×1,5). A personagem tem 5% de crítico.
6. **Fim do combate:** quando a vida de um lado chega a 0.
   Antes de cada turno do jogador, este pode tentar fugir: sucesso com a probabilidade de fuga do adversário
   (o combate termina sem ganhos nem perdas, além da energia gasta).
7. **Vitória:** ganha o dinheiro e o XP do adversário e +1 vitória.
   **Derrota:** perde 20% do dinheiro, fica com 1 de vida e não ganha XP.

### Teste de coerência (nível 1, Espadachim, ataque normal)
- Contra o Bandido (mais fraco): causa ~12,5 por turno, mata em 4 turnos; recebe ~4 por turno, ~16 de dano total de 130. **Vence sempre.**
- Contra o Apóstolo (mais forte): causa ~4 por turno (precisa de ~75 turnos); recebe ~26 por turno e morre em 5. **Perde sempre.**
- A sorte (±10%) só ajusta o resultado; quem decide é o atributo.

## 7. Missões
| Nome                  | Objetivo                    | Dificuldade | Dinheiro | XP  |
|-----------------------|-----------------------------|-------------|----------|-----|
| Limpar a estrada      | Derrotar 3 bandidos         | fácil       | 100      | 80  |
| A matilha da lua      | Derrotar 2 lobos demoníacos | média       | 200      | 150 |
| A ponte do troll      | Derrotar 1 troll            | difícil     | 400      | 300 |
| Caçada ao Apóstolo    | Derrotar 1 apóstolo         | extrema     | 1000     | 800 |

Estados de uma missão: Disponível, Em curso, Concluída, Falhada.
Uma missão falha quando a personagem é derrotada num combate contra o adversário-alvo da missão em curso.
Máximo de missões em curso ao mesmo tempo: 2.

## 8. Ranking
Critério de ordenação (por ordem de desempate):
1. Nível
2. XP
3. Vitórias

## 9. Tipos de utilizador
- **Jogador:** regista-se, faz login, cria e gere personagens, combate, compra/vende/usa itens, aceita missões, vê o ranking.
- **Administrador:** tudo o que o jogador faz mais criar/editar/remover itens, adversários e missões, repor stock e apagar utilizadores.
