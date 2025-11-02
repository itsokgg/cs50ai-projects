people = ["ben", "david"]
probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

for person in probabilities:
    for dist in probabilities[person]:
        for value in probabilities[person][dist]:
            print(probabilities[person][dist][value])
        print("next dist")