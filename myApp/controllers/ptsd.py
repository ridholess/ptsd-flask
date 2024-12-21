from flask import Blueprint, render_template, request, redirect, url_for
# from myApp.models.ptsd import PTSD


def index():
    return render_template('index.html')

def login():
    return render_template('login.html')

def register():
    return render_template('register.html')