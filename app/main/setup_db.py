import uuid, getpass
from app.main import db
from app.main.models.specie import Specie
from app.main.models.breed import Breed

def generate_id():
    new_id = str(uuid.uuid4())

    return new_id

def setup_petKindList():
    specie_list = []
    breed_list = []

    print("Since your database is new, we must first insert data in the specie and breed tables for the dependent servers to be ready of usage.")

    specieList_len = int(input("Please input desired length of specie list: "))

    for count in range(specieList_len):
        specie_obj = {}

        if count+1 == 1:
            specie_name = str(input("Input 1st specie name: "))
        elif count+1 == 2:
            specie_name = str(input("Input 2nd specie name: "))
        elif count+1 == 3:
            specie_name = str(input("Input 3rd specie name: "))
        elif count >= 3:
            specie_name = str(input("Input {}th specie name: ").format(count+1))

        specie_obj["specie_name"] = specie_name
        specie_obj["public_id"] = generate_id()

        specie_list.append(specie_obj)

    for count, specie in enumerate(specie_list):
        specieBreedsList_len = int(input("Please input desired length of {} breed list: ".format(specie["specie_name"])))

        for count in range(specieBreedsList_len):
            breed_obj = {}
            breed_name = ""

            if count+1 == 1:
                breed_name = str(input("Input 1st breed name: "))
            elif count+1 == 2:
                breed_name = str(input("Input 2nd breed name: "))
            elif count+1 == 3:
                breed_name = str(input("Input 3rd breed name: "))
            elif count >= 3:
                breed_name = str(input("Input {}th breed name: ").format(count+1))

            breed_obj["breed_name"] = breed_name
            breed_obj["public_id"] = generate_id()
            breed_obj["specie_id"] = specie["public_id"]

            breed_list.append(breed_obj)

    for count, specie in enumerate(specie_list):
        specie = Specie(specie_name=specie["specie_name"], public_id=specie["public_id"])
            
        db.session.add(specie)
        db.session.commit()

    for count, breed in enumerate(breed_list):
        breed = Breed(breed_name=breed["breed_name"], public_id=breed["public_id"], specie_id=breed["specie_id"])

        db.session.add(breed)
        db.session.commit()

    username = getpass.getuser()

    print("Populated the databases successfully. Thank you, {}.".format(username))