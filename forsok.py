# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 01:53:46 2022

@author: lisas
"""

def finn_avtale(liste, tittel = " "):
    f_avtaler = []
    for tittel in liste:
        if tittel in liste:
            a = liste.find(tittel) # Prøvde å finne noe annet her siden .find ikke fungerer
            f_avtaler.append(a)
            return f_avtaler
        else:
            print("Sorry, ingen avtaler med denne tittelen")
        
l1 = ["ape", "katt", "hund", "ape"]
finn_avtale(l1, "katt")


