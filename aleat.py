#!/usr/bin/python3

"""
Nerea Del Olmo Sanz - GITT
Ejercicio 14.6

Servidor de aplicaciones
Herencia de clases
URLs aleatorias

"""

import webapp
import random


class aleatApp (webapp.webApp):

    def process(self, parsedRequest):
        randNum = 100000000 * random.random()
        randomURL = ("<html><a href=" + str(randNum) + ">Dame otra</a><html>")
        return ("200 OK", randomURL)

if __name__ == "__main__":
    testwebApp = aleatApp("localhost", 1234)
