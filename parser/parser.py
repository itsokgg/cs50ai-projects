import nltk
import sys
import re

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | NP VP NP | NP VP Conj NP VP | NP VP NP Conj NP VP | NP VP NP Conj NP VP NP | NP VP Conj VP NP | NP VP NP Conj VP NP
NP -> N | DetNP | PNP | AdjNP | NPNP | NPAdv
DetNP -> Det NP
PNP -> P NP
AdjNP -> Adj NP
NPNP -> NP NP
NPAdv -> NP Adv
VP -> V | V Adv | Adv V | VPNP
VPN -> VP NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    s = nltk.tokenize.word_tokenize(sentence.lower())
    for word in s:
        # check that each word contains a letter
        if not re.search(r"[a-z]", word):
            s.remove(word)
    print(s)
    return s


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    nps = []
    # get noun phrases
    for word in tree.subtrees(filter=lambda tree: tree.label() == "NP"):
        nps.append(word)
    
    # remove non noun phrase chunks
    for np in nps:
        for np2 in nps:
            # if np is a substring of np2, remove np2
            if re.search(rf"({str(" ".join(np.flatten()))}.+) | (.+{str(" ".join(np.flatten()))})", str(" ".join(np2.flatten()))):
                nps.remove(np2)
    return nps


if __name__ == "__main__":
    main()
