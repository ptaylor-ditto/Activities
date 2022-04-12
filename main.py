import os, random
os.system('cls')
import PySimpleGUI as sg
#from loading import loading
sg.LOOK_AND_FEEL_TABLE['Theming'] = {
    'BACKGROUND': '#f4ffbd',
    'TEXT': '#000000',
    'INPUT': '#ababab',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#000000',
    'BUTTON': ('#ffffff', '#ff0000'),
    'PROGRESS': ('#D1826B', '#CC8019'),
    'BORDER': 1, 'SLIDER_DEPTH': 0, 
    'PROGRESS_DEPTH': 0,
}
themes = ['HotDogStand', 'Theming', 'SystemDefault']
sg.theme(random.choice(themes))
layout = [
    [sg.Text('Welcome to the home screen. What would you like to do?')],
    [sg.Button('Hearts'), sg.Button('War'), sg.Button('Contacts'), sg.Button('Mad Libs'), sg.Button('Wordle'), sg.Button('Ping Pong'), sg.Button('Paint'), sg.Button('Life')],
    [sg.Button('Choose Your Own Adventure'), sg.Button('Hangman'), sg.Button('Blackjack'), sg.Button('Timer'), sg.Button('Pacman'), sg.Button('Memory')],
    [sg.Button('Mastermind'), sg.Button('Temp Converter'), sg.Button('2048'), sg.Button('Rock Paper Scissors'), sg.Button('Cannon'), sg.Button('Maze')],
    [sg.Button('2 Player Game'), sg.Button('Tic Tac Toe'), sg.Button('Acronym Creator'), sg.Button('Flames'), sg.Button('Connect Four'), sg.Button('Tiles')],
    [sg.Button('Spinner'), sg.Button('Spell Check'), sg.Button('Snake'), sg.Button('Currency Converter'), sg.Button('Loading'), sg.Button('Tron')],
    [sg.Button('Check Password Strength'), sg.Button('Calculator'), sg.Button('Encoder/Decoder'), sg.Button('Flappy'), sg.Button('Simon Says')],
    [sg.Button('Leave')]
]
def main():
    window = sg.Window('Home Page', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Leave':
            break
        elif event == 'Hearts':
            window.close()
            from heart import hearts
            hearts()
        elif event == 'War':
            window.close()
            from wars import war
            war()
        elif event == 'Contacts':
            window.close()
            from contacts import contacts
            contacts()
        elif event == 'Mad Libs':
            window.close()
            from mad_libs import madlibs
            madlibs()
        elif event == 'Choose Your Own Adventure':
            window.close()
            from cyoa import cyoa
            cyoa()
        elif event == 'Hangman':
            window.close()
            from hangman import hangman
            hangman()
        elif event == 'Blackjack':
            window.close()
            from blackjack import blackjack
            blackjack()
        elif event == 'Timer':
            window.close()
            from countdown import countdown
            countdown()
        elif event == 'Mastermind':
            window.close()
            from mastermind import mastermind
            mastermind()
        elif event == '2048':
            window.close()
            from game2048 import game2048
            game2048()
        elif event == 'Flames':
            window.close()
            from flames import flames
            flames()
        elif event == 'Rock Paper Scissors':
            window.close()
            from rock_paper_scissors import rps
            rps()
        elif event == '2 Player Game':
            window.close()
            from p2game import p2game
            p2game()
        elif event == 'Tic Tac Toe':
            window.close()
            from tic_tac_toe import ttt
            ttt()
        elif event == 'Acronym Creator':
            window.close()
            from acronyms import acronyms
            acronyms()
        elif event == 'Temp Converter':
            window.close()
            from f_to_c import converter
            converter()
        elif event == 'Spinner':
            window.close()
            from spinner import spinner
            spinner()
        elif event == 'Spell Check':
            window.close()
            from spell_check import spellcheck
            spellcheck()
        elif event == 'Snake':
            window.close()
            from snake import snake
            snake()
        elif event == 'Currency Converter':
            window.close()
            from currency_conv import curconv
            curconv()
        elif event == 'Check Password Strength':
            window.close()
            from cps import cps
            cps()
        elif event == 'Calculator':
            window.close()
            from gui_calculator import calc
            calc()
        elif event == 'Encoder/Decoder':
            window.close()
            from encoder import encoder
            encoder()
        elif event == 'Wordle':
            window.close()
            from wordle import wordle
            wordle()
        elif event == 'Ping Pong':
            window.close()
            from pong import pong
            pong()
        elif event == 'Loading':
            window.close()
            from loading import loading
            loading()
        elif event == 'Paint':
            window.close()
            from paint import paint
            paint()
        elif event == 'Pacman':
            window.close()
            from pacman import pacman
            pacman()
        elif event == 'Cannon':
            window.close()
            from cannon import cannon
            cannon()
        elif event == 'Connect Four':
            window.close()
            from connect_four import cfour
            cfour()
        elif event == 'Flappy':
            window.close()
            from flappy import flappy
            flappy()
        elif event == 'Memory':
            window.close()
            from memory import memory
            memory()
        elif event == 'Maze':
            window.close()
            from maze import maze
            maze()
        elif event == 'Life':
            window.close()
            from life import life
            life()
        elif event == 'Tron':
            window.close()
            from tron import tron
            tron()
        elif event == 'Tiles':
            window.close()
            from tiles import tiles
            tiles()
        elif event == 'Simon Says':
            window.close()
            from ss import ss
            ss()
main()