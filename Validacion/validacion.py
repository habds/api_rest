from flask import Flask, request, make_response
import jwt

def login():
    #asdgashjdgahjsgdajds
    auth= request.authorization

    if auth.username=='usuario' and auth.password=='password':
        token = jwt.encode({'user' : auth.username}

        