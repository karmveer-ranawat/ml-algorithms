# Alpha Beta Pruning

class Node:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children if children is not None else []
        self.value = value

def evaluate(node):
    return node.value

def is_terminal(node):
    return node.value is not None

def get_children(node):
    return node.children

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal(node):
        return evaluate(node)
   
    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(node):
            eval = alpha_beta_pruning(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(node):
            eval = alpha_beta_pruning(child, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Create the game tree
D = Node('D', value=3)
E = Node('E', value=5)
F = Node('F', value=6)
G = Node('G', value=9)
H = Node('H', value=1)
I = Node('I', value=2)

B = Node('B', children=[D, E, F])
C = Node('C', children=[G, H, I])

A = Node('A', children=[B, C])

# Run the alpha-beta pruning algorithm
maximizing_player = True
initial_alpha = float('-inf')
initial_beta = float('inf')
depth = 3  # Maximum depth of the tree

optimal_value = alpha_beta_pruning(A, depth, initial_alpha, initial_beta,
maximizing_player)
print(f"The optimal value is: {optimal_value}")








# First order logic

from sympy import symbols
from sympy.logic.boolalg import Implies, And, Or, Not
from sympy.logic.inference import satisfiable

# Define predicates (functions that return True/False)
Human = symbols('Human')  # x is a Human
Mortal = symbols('Mortal')  # x is Mortal

# Define a rule: "All humans are mortal" (∀x Human(x) → Mortal(x))
rule = Implies(Human, Mortal)

# Example instance: "Socrates is a human" (Human(Socrates))
Socrates = symbols('Socrates')
fact = And(Human)  # Socrates is a Human

# Query: "Is Socrates mortal?"
query = Mortal

# Check if the knowledge base entails the query
kb = And(rule, fact)  # Knowledge Base
result = satisfiable(And(kb, Not(query)))  # Check if query is false

if result is False:
    print("Socrates is Mortal (Provable)")
else:
    print("Cannot prove that Socrates is Mortal")






# Propositional Logic
from sympy import symbols
from sympy.logic.boolalg import Implies, And, Or, Not
from sympy.logic.inference import satisfiable

# Define propositional variables
P = symbols('P')  # "It is raining"
Q = symbols('Q')  # "The ground is wet"

# Define logical rules
rule = Implies(P, Q)  # If it rains, then the ground is wet.

# Define facts
fact = P  # "It is raining"

# Define query: Is the ground wet?
query = Q

# Knowledge Base (KB)
kb = And(rule, fact)  # All known facts and rules

# Check if KB entails the query
result = satisfiable(And(kb, Not(query)))  # If KB &amp; ¬Q is unsatisfiable, Q is provable

if result is False:
      print("The ground is wet (Provable)")
else:
    print("Cannot prove that the ground is wet")








# Forward Chaining
global_facts = [["plant", "mango"], ["eating", "mango"], ["seed", "sprouts"]]

global_is_changed = True

def assert_fact(fact):
    global global_facts
    global global_is_changed
    if fact not in global_facts:
        global_facts.append(fact)
        global_is_changed = True

while global_is_changed:
    global_is_changed = False  
    for A1 in global_facts:  
        if A1[0] == "seed":
            assert_fact(["plant", A1[1]])

        if A1[0] == "plant":
            assert_fact(["fruit", A1[1]])

        if A1[0] == "plant" and ["eating", A1[1]] in global_facts:
            assert_fact(["human", A1[1]])

print(global_facts)





# Backward Chaining
# Define initial facts
global_facts = [["vertebrate", "duck"], ["flying", "duck"], ["mammal", "cat"]]

# Define rules as functions
def is_fact_known(fact):
"""Check if a fact is already in the known facts."""
  return fact in global_facts

def backward_chain(goal):
"""Try to prove a goal using known facts and inference rules."""

  # If the fact is already known, return True
  if is_fact_known(goal):
    return True

  entity = goal[1] # The subject (e.g., "duck")

# Rule 1: "mammal" → "vertebrate"
  if goal[0] == "vertebrate":
    if backward_chain(["mammal", entity]): # Check if entity is a mammal
      return True

  # Rule 2: "vertebrate" → "animal"
  if goal[0] == "animal":
    if backward_chain(["vertebrate", entity]): # Check if entity is a vertebrate
      return True
  
  # Rule 3: "vertebrate" + "flying" → "bird"
  if goal[0] == "bird":
    if backward_chain(["vertebrate", entity]) and backward_chain(["flying", entity]):
      return True

  return False # If no rule applies, return False

# Example queries
query1 = ["bird", "duck"] # Is a duck a bird?
query2 = ["animal", "cat"] # Is a cat an animal?

# Check results
print(f"Is a duck a bird? {backward_chain(query1)}") # Should return True
print(f"Is a cat an animal? {backward_chain(query2)}") # Should return True
print(f"Is a duck a mammal? {backward_chain([&#39;mammal&#39;, &#39;duck&#39;])}") # Should return False
