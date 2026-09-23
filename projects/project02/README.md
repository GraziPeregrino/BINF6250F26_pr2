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
def build_markov_model(markov_model, new_text)
    Split new_text into a list of words
    Add artificial states for start and end: '*S*' (start marker) to the front, '*E*' (end marker) to the end
    For each consecutive pair (current_word, next_word) in the padded list:
        If current_word not in markov_model: create empty dict for it
        Increment markov_model[current_word][next_word]
    Return markov_model
```

2. Generalization — Nth-order Markov model
Why?
A 1st-order model only remembers one previous word. Real structure (e.g. codon triplets in DNA, or multi-word phrases in language) often needs more context. The Nth-order model implementation here is a strict superset of the 1st-order model — setting order=1 reproduces the same behavior, just with 1-tuples as keys instead of bare strings.
```
def build_markov_model(markov_model, text, order=1)
    Split text into a list of words
    Pad the front with `order` copies of '*S*', pad the end with one '*E*'
    For i from 0 to (len(words) - order - 1):
        current_state = tuple of words[i : i+order]   # the last `order` words
        next_word = words[i + order]
        If current_state not in markov_model: create empty dict for it
        Increment markov_model[current_state][next_word]
    Return markov_model
```
Note: we experienced output slightly different from the assignment expected output for this segment. After reviewing carefully, we decided to trust the algorithm's integrity and document the discrepancy in our project02.ipynb file. You will find our code, along with an alternative calling code that would lead to the given expected output in the original assignment. 
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

- **Understanding Markov CHain Process:** 
- **Implementing Markov Chain:** 
- **GitHub:** Overall, we had success with GitHub. We were able to navigate the PR request page, and successfully work collaboratively.

# Struggles

- **Jupyter Notebook Upload:** For some reason, we were having trouble uploading our Jupyter notebook to GitHub at first. It took us removing the file and reuploading it to stop showing up as "invalid".

# Personal Reflections
## Group Leader: Maggie Wenger
Overall this project went way more smoothly than the first one for me. I am definitely starting to get the hang of GitHub
and managing pull requests in the dedicated PR page. Our team worked really well together, and we were able to provide 
advice and suggestions for suggested code to each other.

If given more time, something that we could implement would be taking into account the ends of the "paragraphs" in the sonnets.
It would be interesting to see if that would affect the output of our generated text, and if we could generate sonnets
with the correct spacing.

## Other member: Trang Do 
We were able to understand Markov Chain quite thoroughly, I liked that our team member was sharing multiple useful readings that broke down the concept and make it digestible. We were then each worked on our own implementation, shared it with other member in team chat, and were able to offer correction / different ways of thinking and coding and overall learnt from each other. We ended up agreeing and uploading the finalized version on here. 
As a collaborator, I like that we continue to have the opportunity to practice using Github. It does get easier each time. 



# Generative AI Appendix


