from pynput import keyboard
import random
import os

from data import characters
from views import output_hidden_skills, show_partner

quantity = len(characters)
index = random.randint(1, quantity - 1)
partner = characters[index]

position = 0
successes = {'.', ','}
vowels = {
    'a': 'á',
    'e': 'é',
    'i': 'í',
    'o': 'ó',
    'u': 'ú'
}


def render():
    os.system("cls")
    output_hidden_skills(partner, position, successes)


def increment_position():
    global position
    position += 1


def decrement_position():
    global position
    position -= 1
    if position < 0:
        position = 0


def is_match(letter):
    if letter.lower() == partner.get('skills')[position].lower():
        successes.add(letter.lower())
        if letter.lower() in 'aeiou':
            if vowels.get(letter.lower()) in partner.get('skills'):
                successes.add(vowels.get(letter.lower()))

    elif letter.lower() in 'aeiou':
        if vowels.get(letter.lower()) == partner.get('skills')[position].lower():
            successes.add(vowels.get(letter.lower()))
            successes.add(letter.lower())


def is_winner() -> bool:
    skills: str = ''
    skills = partner.get('skills').replace(' ', '')
    skills = skills.replace('.', '')
    skills = skills.replace(',', '')
    skills = skills.lower()
    only_letters = successes.copy()
    only_letters.discard('.')
    only_letters.discard(',')
    return len(only_letters) >= len(set(skills))


def on_press(key):
    try:
        is_match(key.char)
    except AttributeError:
        pass


def on_release(key):
    os.system("cls")
    if key == keyboard.Key.esc:
        return False
    elif key == keyboard.Key.right:
        increment_position()
    elif key == keyboard.Key.left:
        decrement_position()
    render()
    if is_winner():
        show_partner(partner)


render()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)

listener.start()
