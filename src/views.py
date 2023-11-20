def show_header():
    print('\t\t DESCUBRE A TU COMPAÑER@\n')
    print(' 🏆 Torneo de Mario Tennis: Ultra Smash')
    print('  Descifra este texto que describe sus habilidades:\n')


def output_hidden_skills(partner: dict, position: int, successes: set):
    skills: str = partner.get('skills')
    skills_not_space = partner.get('skills').replace(' ', '')
    skills_not_space = skills_not_space.replace('.', '')
    skills_not_space = skills_not_space.replace(',', '')
    skills_not_space = skills_not_space.lower()
    show_header()
    print('\t' * 6, end='')
    print('Aciertos:', len(successes) - 2, '/', len(set(skills_not_space)))
    print('\n')
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
    print('\n\n')


def show_partner(partner: dict):
    print('')
    print('-' * 79)
    print(partner.get('emoji'), partner.get('name'))
    print('')
    print(partner.get('skills'))
    print('-' * 79)
    return False
