import random


from data import characters
from views import output_hidden_skills

quantity = len(characters)
index = random.randint(1, quantity - 1)
partner = characters[index]
print(partner.get('name'))

output_hidden_skills(partner)
