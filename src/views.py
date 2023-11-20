
def output_hidden_skills(partner: dict):
    skills: str = partner.get('skills')
    for letter in skills:
        if letter != ' ':
            print('_', end="")
        else:
            print(letter, end="")
    print('')
