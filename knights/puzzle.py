from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A can be a knight or a knave
    Or(AKnight, AKnave),
    # A cant be both 
    Or(Not(AKnight), Not(AKnave)),
    # ---
    #  A is a knight and he is both or A is not a Knight
    Or(And(AKnight, AKnave), Not(AKnight)),
    # A is a knave and he is not both or A is not a knave
    Or(
        Or(
            Not(AKnight), 
            Not(AKnave)
        ), 
        Not(AKnave)
    )
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A can be a knight or a knave
    Or(AKnight, AKnave),
    # A cant be both 
    Or(Not(AKnight), Not(AKnave)),
    # B can be a knight or a knave
    Or(BKnight, BKnave),
    # B cant be both 
    Or(Not(BKnight), Not(BKnave)),
    
    # ---
    # A is a knight therefore he is saying the truth and they are both knaves or A is not a knight
    Or(And(AKnave, BKnave), Not(AKnight)),
    # A is a knave and he isnt both or he is not a knave
    Or(Or(Not(AKnave), Not(BKnave)), Not(AKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A can be a knight or a knave not both
    Or(
        And(AKnave, Not(AKnight)),
        And(AKnight, Not(AKnave))
    ),
    # B can be a knight or a knave not both
    Or(
        And(BKnave, Not(BKnight)),
        And(BKnight, Not(BKnave))
    ),
    # ---
    # A says we are both the same
    Or(
        # A is a Knight so they are both knights or both knaves
        And(
            And(AKnight, BKnight), 
            And(AKnave, BKnave)
        ),
        # or A isnt a knight
        Not(AKnight)
    ),
    Or(
        # A is A Knave so they arent both knights or both knaves
        And(
            Or(Not(AKnight), Not(BKnight)),
            Or(Not(AKnave), Not(BKnave))
        ),
        # or A isnt a Knave
        Not(AKnave)
    ),

    # B says we arent the same
    Or(
        # B is a Knight so they arent both knights or knaves
        And(
            Or(Not(AKnight), Not(BKnight)),
            Or(Not(AKnave), Not(BKnave))
        ),
        # or B isnt a knight
        Not(BKnight)
    ),
    Or(
        # B is a Knave so they are both knights or both knaves
        Or(
            And(AKnight, BKnight), 
            And(AKnave, BKnave)
        ),
        # or B isnt a knave
        Not(BKnave)
    )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A can be a knight or a knave
    Or(AKnight, AKnave),
    # A cant be both 
    Or(Not(AKnight), Not(AKnave)),
    # B can be a knight or a knave
    Or(BKnight, BKnave),
    # B cant be both 
    Or(Not(BKnight), Not(BKnave)),
    # C can be a knight or a knave
    Or(CKnight, CKnave),
    # C cant be both 
    Or(Not(CKnight), Not(CKnave)),
    # ---

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    
    # B says "A said 'I am a knave'."
    # B is a knight so A said "I am a knave" or B is not a knight
    Or(
        # A said A is a Knave, or B isnt a knight
        And(
            # BKnight
            Or(AKnave, Not(AKnight)),
            Or(AKnight, Not(AKnave))
        ),
        Not(BKnight)
    ),
    # B is a knave so A said "I am a Knight" or B is not a Knave
    Or(
        # A said A is a Knight, or B isnt a Knave
        And(
            Or(AKnight, Not(AKnight)),
            Or(AKnave, Not(AKnave)) 
        ),
        Not(BKnave)
    ),

    # B says "C is a knave."
    Or(CKnave, Not(BKnight)),
    Or(CKnight, Not(BKnave)),

    # C says "A is a knight."
    # C is a knight so A is a Knight, or c is not a knight
    Or(AKnight, Not(CKnight)),
    # C is a knave so A is a knave, or C is not a knave
    Or(AKnave, Not(CKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
