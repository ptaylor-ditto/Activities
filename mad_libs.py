def madlibs():
    import PySimpleGUI as sg
    import os
    os.system('cls')
    def madlib1():
        madlib1 = [
            [sg.Text('Animal: '), sg.InputText(key='animal')],
            [sg.Text('Profession: '), sg.InputText(key='profession')],
            [sg.Text('Cloth: '), sg.InputText(key='cloth')],
            [sg.Text('Thing: '), sg.InputText(key='thing')],
            [sg.Text('Name: '), sg.InputText(key='name')],
            [sg.Text('Place: '), sg.InputText(key='place')],
            [sg.Text('Verb: '), sg.InputText(key='verb')],
            [sg.Text('Food: '), sg.InputText(key='food')],
            [sg.Button('Results'), sg.Button('Leave')]
        ]
        window = sg.Window("Mad Libs 1", madlib1)
        while True:
            event, values = window.read()
            if event == "Results":
                food = values['food']
                name = values['name']
                animals = values['animal']
                profession = values['profession']
                cloth = values['cloth']
                thing = values['thing']
                verb = values['verb']
                place = values['place']
                window.close()
                print(f'Say {food}, the photographer said as the camera flashed! {name} and I had gone to {place} to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as {animals} pretending to be a {profession}. When we saw the second photo, it was exactly what I wanted. We both looked like {thing} wearing {cloth} and {verb} --exactly what I had in mind.')
            elif event == 'Leave':
                window.close()
                break
    def madlib2():
        madlib2 = [
            [sg.Text('Adjective: '), sg.InputText(key='adjective')],
            [sg.Text('Color: '), sg.InputText(key='color')],
            [sg.Text('Thing: '), sg.InputText(key='thing')],
            [sg.Text('Place: '), sg.InputText(key='place')],
            [sg.Text('Person: '), sg.InputText(key='person')],
            [sg.Text('Another Adjective: '), sg.InputText(key='adjective1')],
            [sg.Text('Food: '), sg.InputText(key='food')],
            [sg.Text('Verb: '), sg.InputText(key='verb')],
            [sg.Text('Insect: '), sg.InputText(key='insect')],
            [sg.Button('Results'), sg.Button('Leave')]
        ]
        window = sg.Window("Mad Libs 2", madlib2)
        while True:
            event, values = window.read()
            if event == "Results":
                adjective = values['adjective']
                color = values['color']
                thing = values['thing']
                place = values['place']
                person = values['person']
                adjective1 = values['adjective1']
                food = values['food']
                verb = values['verb']
                insect = values['insect']
                window.close()
                print(f'Last night I dreamed I was a {adjective} butterfly with {color} splothes that looked like {thing}.I flew to {place} with my bestfriend and {person} who was a {adjective1} {insect}.We ate some {food} when we got there and then decided to {verb} and the dream ended when I said-- lets {verb}.')
            elif event == 'Leave':
                window.close()
                break
    def madlib3():
        madlib3 = [
            [sg.Text('Person: '), sg.InputText(key='person')],
            [sg.Text('Color: '), sg.InputText(key='color')],
            [sg.Text('Food: '), sg.InputText(key='foods')],
            [sg.Text('Adjective: '), sg.InputText(key='adjective')],
            [sg.Text('Thing: '), sg.InputText(key='thing')],
            [sg.Text('Place: '), sg.InputText(key='place')],
            [sg.Text('Verb: '), sg.InputText(key='verb')],
            [sg.Text('Adverb: '), sg.InputText(key='adverb')],
            [sg.Text('Food: '), sg.InputText(key='food')],
            [sg.Text('Thing: '), sg.InputText(key='things')],
            [sg.Button('Results'), sg.Button('Leave')]
        ]
        window = sg.Window("Mad Libs 3", madlib3)
        while True:
            event, values = window.read()
            if event == "Results":
                person = values['person']
                color = values['color']
                foods = values['foods']
                adjective = values['adjective']
                thing = values['thing']
                place = values['place']
                verb = values['verb']
                adverb = values['adverb']
                food = values['food']
                things = values['things']
                window.close()
                print(f"Today we picked apple from {person}'s Orchard. I had no idea there were so many different varieties of apples. I ate {color} apples straight off the tree that tasted like {foods}. Then there was a {adjective} apple that looked like a {thing}.When our bag were full, we went on a free hay ride to {place} and back. It ended at a hay pile where we got to {verb} {adverb}. I can hardly wait to get home and cook with the apples. We are going to make appple {food} and {things} pies!.")
            elif event == 'Leave':
                window.close()
                break
    layout = [
        [sg.Button('The Photographer'), sg.Button('Apple and Apple'), sg.Button('The Butterfly')],
        [sg.Button('Leave')]
    ]
    window = sg.Window("Main Page", layout)
    event, values = window.read()
    if event == "The Photographer":
        madlib1()
    elif event == "Apple and Apple":
        madlib3
    elif event == "The Butterfly":
        madlib2
    elif event == "Leave":
        window.close()
madlibs()