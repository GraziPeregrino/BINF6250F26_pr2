# Introduction
This project implements a Markov chain text model, built up in stages: 
1. A simple 1st-order model (single-word memory)
2. A generalized Nth-order model (multi-word memory)
3. A text generator that samples from a trained model
4. Training on a full book ("All the Fish" — Dr. Seuss)
5. Training on a larger, structurally different text ("Pick Your Poison" — Shakespeare's Sonnets)


# Pseudocode
1. First implementation — 1st-order Markov model
```
Split new_text into a list of words
Add artificial states for start and end: '*S*' (start marker) to the front, '*E*' (end marker) to the end
For each consecutive pair (current_word, next_word) in the padded list:
    If current_word not in markov_model: create empty dict for it
    Increment markov_model[current_word][next_word]
Return markov_model
```
Calling code: 
```
markov_model = dict()
text = "one fish two fish red fish blue fish"
markov_model = build_markov_model(markov_model, text)
print (markov_model)
```
Recorded output - matched with expected output
```
{'*S*': {'one': 1}, 'one': {'fish': 1}, 'fish': {'two': 1, 'red': 1, 'blue': 1, '*E*': 1}, 'two': {'fish': 1}, 'red': {'fish': 1}, 'blue': {'fish': 1}}
```
2. Generalization — Nth-order Markov model
Why?
A 1st-order model only remembers one previous word. Real structure (e.g. codon triplets in DNA, or multi-word phrases in language) often needs more context. The Nth-order model implementation here is a strict superset of the 1st-order model — setting order=1 reproduces the same behavior, just with 1-tuples as keys instead of bare strings.
```
Split text into a list of words
Pad the front with `order` copies of '*S*', pad the end with one '*E*'
For i from 0 to (len(words) - order - 1):
    current_state = tuple of words[i : i+order]   # the last `order` words
    next_word = words[i + order]
    If current_state not in markov_model: create empty dict for it
    Increment markov_model[current_state][next_word]
Return markov_model
```
Calling code: 
```
markov_model = dict()
text = "one fish two fish red fish blue red fish blue"
markov_model = build_markov_model(markov_model, text, order=2)
markov_model
```
Recorded output: 
Note ('red', 'fish') → {'blue': 2} — "red fish" is followed by "blue" twice in this particular training sentence, which is why the count is 2 rather than 1.
```
{('*S*', '*S*'): {'one': 1},
 ('*S*', 'one'): {'fish': 1},
 ('one', 'fish'): {'two': 1},
 ('fish', 'two'): {'fish': 1},
 ('two', 'fish'): {'red': 1},
 ('fish', 'red'): {'fish': 1},
 ('red', 'fish'): {'blue': 2},
 ('fish', 'blue'): {'red': 1, '*E*': 1},
 ('blue', 'red'): {'fish': 1}}
```
Note #2: if we change the calling code to: 
```
markov_model = dict()
text = "one fish two fish red fish blue fish"
markov_model = build_markov_model(markov_model, text, order=2)
markov_model
```
then the recorded output will be as follows and matched the given expected output: 
```
{('*S*', '*S*'): {'one': 1},
 ('*S*', 'one'): {'fish': 1},
 ('one', 'fish'): {'two': 1},
 ('fish', 'two'): {'fish': 1},
 ('two', 'fish'): {'red': 1},
 ('fish', 'red'): {'fish': 1},
 ('red', 'fish'): {'blue': 1},
 ('fish', 'blue'): {'fish': 1},
 ('blue', 'fish'): {'*E*': 1}}
 ```
3. Generating text from the model –
Since Markov Models are generative models, we can use the probability states 
to generate output. 
```
def get_next_word(current_word, markov_model, seed=42)
    Look up the current state's transition dictionary
    Sum all observed transitions out of this state
    Build a list of possible next words
    For each possible next word:
        Convert raw frequency count into probability (count/total)
        Append to list of probabilities
    Randomly draw next word using calculated probability
    Return chosen word    
```
```
def generate_random_text(markov_model, seed=42)
    Define start and end tokens
    Determine model's order (from length of state key)
    Seed the RNG (reproducibility)
    Initialize current state with order number of start tokens
    Repeatedly:
        Get the next word (get_next_word)
        If next word is end token:
            Break out of loop
        Append generated word
        Slide window (drop oldest word, add new word)
    Join collected words into string and return    
```
Calling code:

4. "All the Fish" — training on the whole book
```
Open the file "data/one_fish_two_fish.txt"
Initialize empty markov model
For each line:
    Strip whitespace
    If the line is not blank:
        Update markov model (next word transitions)
Generate sentence from model (using a seed for reproducibility)    
```
5. "Pick Your Poison" — training on Shakespeare's Sonnets
```
Open the file "data/sonnets.txt"
    Read the whole file into one string
Make a list of sonnet chunks (divided by \n\n)
Loop through saved sonnet chunks:
    Strip whitespace
    Append to list
Loop through all sonnet chunks:
    Break sonnet chunks into individual lines (\n)
    Join them together with whitespace to make lingle-line version
    Update markov model (next word transitions)
Print generated random text from markov model
```
# Successes

# Struggles

# Personal Reflections
## Group Leader: Maggie Wenger


## Other member: Trang Do 
Other members' reflections on the project


# Generative AI Appendix


