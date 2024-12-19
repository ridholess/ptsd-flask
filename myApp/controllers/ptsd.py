from flask import Blueprint, render_template, request, redirect, url_for
# from myApp.models.ptsd import PTSD


def index():
    return render_template('index.html')