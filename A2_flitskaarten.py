import random

words = {
    #Fietsen
    "de fiets":"bicycle",
    "de fietsenmaker":"cycle repairman",
    "inderdaad":"indeed",
    "duidelijk":"clear",
    "lijken":"to appear / to seem (as)",
    "total loss":"a write-off",
    "gebeuren":"to happen",
    "vallen":"to fall",
    "regenen":"to rain",
    "glade (glad)":"slippery",
    "wegfietsen":"to cycle away",
    "fietsen":"to cycle",
    "de praktijk":"practice",
    "rechts afslaan":"turn right",
    "wegglijden":"to slip",
    "mankeren":"to be wrong",
    "zelf":"myself",
    "een slag in het wiel":"the wheel is crooked",
    "het wiel":"wheel",
    "het stuur":"handlebars",
    "het zadel":"seat",
    "staan":"to stand",
    "scheefe (scheef)":"crooked",
    "het ding":"thing",
    "zo'n":"such a",
    "de bagagedrager":"carrier",
    "afbreken":"to break",
    "bedoelen":"to refer/mean (smth)",
    "kapot":"broken",
    "de band":"tyres",
    "verstaan":"to understand (hearing)",
    "logisch":"logical",
    "helemaal":"completely",
    "rijden":"to ride",
    "de rem":"brakes",
    "controleren":"to check",
    "in order maken":"to make in order / to fix",
    "tiptop in orde":"in tip-top condition",
    "leren":"to learn",
    "de uitdrukking":"expression",
    "klaar":"ready",
    "Koningsdag":"King's Day",
    "de feestdag":"public holiday",
    "het feest":"party/celebration",
    "betekenen":"to mean (definition)",
    "sluiten":"closed",
    "het einde":"end",
    "ophalen":"to collect",

    # Naar de evenmentenhal
    "het station":"train station",
    "bent u hier bekend?":"do you know your way around here?",
    "bekenen":"to know",
    "de voorbijganger":"passerby",
    "de buschauffeur":"bus driver",
    "de bus":"bus",
    "lopen":"to walk",
    "te":"too",
    "zeker":"certainly",
    "vanaf":"from",
    "de tram":"tram",
    "de lijn":"transport line",
    "geluk hebben":"to be lucky",
    "aankomen":"to arrive",
    "net":"just",
    "direct":"straightaway",
    "instappen":"to get in",
    "het stuk":"short distance",
    "de ingang":"entrance",
    "oversteken":"to cross (the road)",
    "de balie":"information desk",
    "de hal":"hall",
    "de portier":"porter",
    "boven":"upstairs",
    "opgaan":"to go up",
    "de trap":"stairs",
    "rechtdoor" : "straight ahead",
    "tot":"as far as",
    "herkennen":"to recognize",
    "linksaf":"to the left",
    "rechts":"on the right",
    "meenemen":"to take",
    "de plattegrond":"map",
    "toiletten":"toilets",
    "beneden":"downstairs",
    "de hoek":"corner",
    "omgaan":"to turn",
    "afgaan":"to go down",
    "uitlopen":"to walk down",
    "vanzelf":"as a matter of course",
    "het bordje":"sign",
    "volgen":"to follow",
    "makkelijker":"easier",
}

def main():
    print("Welkom bij Flashcards!")
    new_word = input_new_word()
    while new_word == "j":
        random_key = pick_word()
        print_dutch_word(random_key)
        NL_response = input_NL_response()
        test_NL_response(random_key, NL_response)
        input_new_word()

def input_new_word():
    new_word = input("(Her)starten? (j/n)")
    if new_word == "j":
       return new_word
    else:
      print("Dankje wel voor gebruiken!")
      quit()  

#Selects a random key
def pick_word():
    random_key = random.choice(list(words.keys()))
    return random_key

#Accesses the corresponding value for the selected random_key
def print_dutch_word(random_key):
    print(words[random_key])

#Asks for the NL response
def input_NL_response():
    NL_response = input("NL: ")
    return NL_response

#Checks correctness of NL response with the corresponding key
def test_NL_response(random_key, NL_response):
    if NL_response == random_key:
        print("Goed!")
    else:
        print(f"Fout! De juiste antwoord is: {random_key}")
        NL_response_retest = input("Opnieuw: ")
        if NL_response_retest == random_key:
            print("Goed!")
        else:
            print("Nee! Probeer het nog eens!")
            while NL_response_retest != random_key:
                print("Fout!")
                NL_response_retest = input("Opnieuw: ")
                if NL_response_retest == random_key:
                    print("Goed!")
                    break

if __name__ == '__main__':
    main()