from flask import Flask, render_template
import random

app = Flask(__name__)

stories = [
    {
        'image': 'story1.png',
        'title': 'Nuttig is mijn naam, onzeker mijn bestaan.',
        'answer': 'Onesimus in de brief van Paulus aan Filemon. Onesimus betekent nuttig en was een weg gelopen slaaf die, met een brief van Paulus, terug ging naar zijn meester Filemon.'
    },
    {
        'image': 'story2.jpeg',
        'title': 'Mijn komst is geprofeteerd maar in Israel wordt ik niet vereerd',
        'answer': 'Kores. Kores wordt in Jesaja 45:1 genoemd als de gezalfde van God. Hij was het die de Joden toestemming gaf om terug te keren naar Jeruzalem.'
    },
    {
        'image': 'story3.jpeg',
        'title': 'Mamma is de baas en samen zijn we overdonderend.',
        'answer': 'Jacobes en Johannes. De gebroederes van de donder genoemd(boanerges) in Markus 3:17'
    },
    {
        'image': 'story4.png',
        'title': 'Ooit was ik groot en blij. Nu is het onrustig met mij in de wei',
        'answer': 'Nebukadnezar. In Daniël 4:30 wordt Nebukadnezar de koning van Babel genoemd. Hij was de koning die een tijd(7 jaar) als een beest leefde.'
    },
    {
        'image': 'story5.jpeg',
        'title': 'Het is goed voor een mens om geen vrouw aan te raken.',
        'answer': '1 Korinthe 7 vers 1. Paulus vind het beter als een mens geen vrouwen aanraakt.'
    },
    {
        'image': 'story6.jpeg',
        'title': 'Verzuchtend en verdwaast zocht hij buiten naar wat extra tijd voor zijn uurwerk.',
        'answer': 'Een Egyptenaar die die zijn zandloper bijvult ten tijde van Hizkia;s langere dag. Jesaja 38:8'
    },
    {
        'image': 'story7.jpeg',
        'title': 'Ik gebruikte mijn vrouw zijn om niet te hoeven staan.',
        'answer': 'Genesis 31:35: Rachel verstopte de afgoden van haar vader Laban onder haar zitvlak en zei dat ze niet kon opstaan omdat ze ongesteld was.'
    },
    {
        'image': 'story8.jpeg',
        'title': 'Deze droom is een natuurkundig fenomeen geworden.',
        'answer': "De jacob's ladder. Genesis 28:12. Je kunt een jacob's ladder maken met een hoogspanningsbron en twee metalen staven."
    },
    # {
    #     'image': 'story9.jpeg',
    #     'title': 'Ik kon harder rennen dan de koning',
    #     'answer': "Elia. 1 Koningen 18:46. Elia rende voor de regen uit en kwam eerder aan in Jizreël dan de koning."
    # },
]

@app.route('/')
def index():
    story = random.choice(stories)
    return render_template('index.html', story=story)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
