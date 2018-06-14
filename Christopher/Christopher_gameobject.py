'''gametemplate.py'''

#from gameobject import GameObject
import pygame
from constants import *

class GameTemplate(object):
    '''pygame object'''
    def __init__(self):
        pygame.init()
        '''abc'''
    def _startup(self):
	'''do startup routines'''
        return True

    def _update(self):
        '''input and time'''
        return True

    def _draw(self):
        '''base draw'''

    def _shutdown(self):
        '''shutdown the game properly'''