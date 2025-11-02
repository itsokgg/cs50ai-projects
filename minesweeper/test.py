from minesweeper import MinesweeperAI, Sentence

ai = MinesweeperAI()


ai.add_knowledge((2, 3), 1)
print("1")

ai.add_knowledge((3, 2), 2)
print("2")
ai.add_knowledge((2, 1), 1)
print("3")
ai.add_knowledge((5, 2), 0)
print("4")
ai.add_knowledge((0, 1), 0)

for sentence in ai.knowledge:
    print(sentence)


print("Mines inferred:", ai.mines)
print("Expected:", {(3, 1), (3, 3)})