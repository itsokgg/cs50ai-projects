# 🧠 Parser  
[_CS50AI Project 6/parser_](https://cs50.harvard.edu/ai/projects/6/parser/)

## 📖 Overview  
**Parser** is a natural language parser built using [NLTK](https://www.nltk.org/).  
It reads a sentence, parses it according to a **context-free grammar (CFG)**, and identifies **noun phrase (NP) chunks** within the parsed structure.

```bash
$ python parser.py sentences/8.txt
['holmes', 'sat', 'down', 'and', 'lit', 'his', 'pipe']
                     S
   __________________|_____________
  |         |        |    |        NP
  |         |        |    |        |
  |         |        |    |      DetNP
  |         |        |    |    ____|____
  NP        VP       |    VP  |         NP
  |      ___|___     |    |   |         |
  N     V      Adv  Conj  V  Det        N
  |     |       |    |    |   |         |
holmes sat     down and  lit his       pipe

Noun Phrase Chunks
holmes
his pipe
pipe
```

---

## ⚙️ Features and Structure
- **`sentences/`** — sample text files to test the parser.  
- **`parser.py`** — main program file containing:
  - `TERMINALS`: defines the terminal symbols (words)- feel free to add your own.  
  - `NONTERMINALS`: defines the grammar production rules.  
  - `preprocess(sentence)`: tokenizes and normalizes input text.  
  - `np_chunk(tree)`: extracts all minimal noun phrase chunks from the syntax tree.  
- Grammar follows [NLTK’s CFG format](https://www.nltk.org/howto/grammar.html).

---

## 🚀 Usage
1. Clone Repository:
   ```bash
   git clone https://github.com/itsokgg/cs50ai-projects/tree/main/parser
   ```
2. Install dependencies:
   ```bash
   cd parser
   pip install -r requirements.txt
   ```
   You might need to download 'punkt_tab':
   ```bash
   # enter the python interpretor
   python
   # run in python interpretor
   >>> import nltk
   >>> nltk.download('punkt_tab')
3. Run the parser on a sentence file:
   ```bash
   python parser.py sentences/[1-10].txt
   ```
   OR   
   Run the parser on a custom sentence(words must be in `TERMINALS` variable in `parser.py`):
   ```bash
   python parser.py
   ```
   you will pe prompted:
   ```bash
   sentence:
   ```
4. Observe the parsed syntax tree and extracted NP chunks.

---

## 🧪 Learning Objectives
This project demonstrates:
- Building **CFGs** for English grammar.
- Parsing with **recursive descent** using NLTK.
- Identifying **constituent phrases** from parse trees.

