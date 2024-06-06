import random
import openai

"""
Flash cards
Other features I would add
- menu selection between sentences and translations
- make a multiselect feature for multiple dictionaries
- Make an OpenAI integration so that I could make AI-generated sentences 
"""

h8_bij_de_maakelaar = {
    "laten zien":"show", 
    "de computer":"computer",
    "derde":"third",
    "de verdieping":"floor/storey",
    "oude (oud)":"old",
    "de buurt":"neighborhood",
    "ver":"far",
    "het centrum":"city center",
    "dicht bij":"close to",
    "het park":"park",
    "de woonkamer":"living room",
    "de vierkante meter":"square meters",
    "vierkante (vierkant)":"square (adj.)",
    "de meter":"meter",
    "open":"open",
    "de keuken":"kitchen",
    "ruime (ruim)":"spacious",
    "slaapkamers (de slaapkamer)":"bedroom",
    "het balkon":"balcony",
    "het westen":"west",
    "de gang":"passage(way)",
    "de wc":"toilet",
    "eenvoudige (eenvoudig)":"simple",
    "de badkamer":"bathroom",
    "de douche":"shower",
    "hoeven":"need",
    "het bad":"bath",
    "gebruiken":"use",
    "geschikte (geschikt)":"suitable",
    "huizen (het huis)":"houses",
    "want":"because",
    "te huur":"to let",
    "huur (huren)":"rent",
    "het huisje (het huis)":"house",
    "verhuren":"to let out",
    "gemeubileerd":"furnished",
    "kasten (de kast)":"cupboards",
    "bedden (het bed)":"beds",
    "stoelen (de stoel)":"chairs",
    "het bureau":"desk",
    "de bank":"sofa/couch",
    "het voordeel":"advantage",
    "niets":"nothing",
    "zonnige (zonnig)":"sunny",
    "de kamer":"room",
    "benedewoning":"ground-floor flat",
    "dat lijkt me fantastisch":"that sounds great",
    "waar":"true",
    "overleggen":"discuss",
    "bel (bellen)":"call",
    "zo snel mogelijk":"as soon as possible",
    "nieuwe (nieuw)":"new",
    "een bepaald type woning":"a particular type of house",
    "de woning":"house 1",
    "het huis":"house 2",
    "de flat":"flat",
    "het appartement":"appartment",
    "de bovenwoning":"upstairs flat",
    "de benedenwoning":"ground-floor flat",
    "in en bij het huis":"in and around the house",
    "de slaapkamer":"bedroom",
    "de keuken":"kitchen",
    "ruime (ruim)":"spacious",
    "slaapkamers (de slaapkamer)":"bedrooms",
    "het balkon":"balcony",
    "het westen":"west",
    "de gang":"passage(way)",
    "de wc":"toilet",
    "eenvoudige (eenvoudig)":"simple",
    "de badkamer":"bathroom",
    "de douche":"shower",
    "hoeven":"need",
    "het bad":"bath",
    "het raam":"window",
    "de deur":"door",
    "de tuin":"garden",
    "het schuurtje":"small shed",
    "de garage":"garage",
    "het raam":"window",
    "de tafel":"table",
    "de stoel":"chair",
    "het bed":"bed",
    "de kast":"cupboard",
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
    random_key = random.choice(list(h8_bij_de_maakelaar.keys()))
    return random_key

#Accesses the corresponding value for the selected random_key
def print_dutch_word(random_key):
    print(h8_bij_de_maakelaar[random_key])

#Asks for the NL response
def input_NL_response():
    NL_response = input("NL: ")
    return NL_response

#Checks correctness of NL response with the corresponding key
def test_NL_response(random_key, NL_response):
    if NL_response == random_key:
        print("Juist!")
    else:
        print(f"Ontjuist! De juist antwoord is: {random_key}")

if __name__ == '__main__':
    main()