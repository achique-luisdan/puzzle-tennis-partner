
def output_hidden_skills(partner: dict, position: int, successes: set):
    skills: str = partner.get('skills')
    skills_not_space = partner.get('skills').replace(' ', '')
    print('Aciertos:', len(successes) - 2, '/', len(skills_not_space))
    if skills[position] != ' ' and not skills[position].lower() in successes:
        skills = skills.replace(
            skills[position], '🔤'
        )
    if skills[position].lower() in successes:
        skills = skills.replace(
            skills[position], '✅'
        )
    for letter in skills:
        if letter.lower() in successes:
            print(letter, end="")
        elif letter == '🔤':
            print('🔤', end="")
        elif letter == '✅':
            print('✅', end="")
        elif letter != ' ':
            print('_', end="")
        else:
            print(letter, end="")
    print('')


def show_partner(partner: dict):
    print(partner.get('emoji'), print(partner.get('name')))
    print('\n')
    print(partner.get('skills'))
