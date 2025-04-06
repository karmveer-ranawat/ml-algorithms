print("""Knowledge Representation first order logic""")
S =True
T=True
M =True
Y = S
K = T
C = M
print(f"Alice is young: {Y}")
print(f"Bob is knowledgeable: {K}")
print(f"Carol is creative: {C}")





print("""knowledge representation propositional logic""")
class Animal:
def init (self, name):
self.name = name
self.characteristics = set()
def add_characteristic(self, characteristic):
self.characteristics.add(characteristic)
lion = Animal("Lion")
tiger = Animal("Tiger")
elephant = Animal("Elephant")
lion.add_characteristic("Carnivore")
lion.add_characteristic("wild")
tiger.add_characteristic("Carnivore")
tiger.add_characteristic("Striped")
elephant.add_characteristic("Herbivore")
elephant.add_characteristic("Large")
print(f"{lion.name}: {',".join(lion.characteristics)}")
print(f"{tiger.name}: {',".join(tiger.characteristics)}")
print(f"{elephant.name}: {,".join(elephant.characteristics)}")
