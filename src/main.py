from src.garden import Garden
from src.gardener import Gardener, NEW_PLANT_COST, TOOL_FIX_COST, DECORATION_COST, SOIL_NORMALIZER_COST, \
    SOIL_FERTILIZER_COST
from src.plant import Plant
from src.recreation_area import RecreationArea

day: int = 1
gardener = Gardener()
print("You have your very own garden, and you've just bought your first plant.")
first_plant_name: str = input("Please give it a name: ")
first_plant = Plant(first_plant_name)
print("Nice!")
garden: Garden = Garden([first_plant])
recreation_area: RecreationArea = RecreationArea()

how_many_times_watered: int = 0
while True:
    print("")
    choice: str = input(f"""Day: {day}
Balance: ${gardener.get_money_amount()}
What would you like to do?
1) Get info on the garden
2) Water the plants
3) Weed the garden
4) Normalize soil acidity ({gardener.get_soil_normalizer_number()})
5) Fertilize the soil ({gardener.get_fertilizer_number()})
6) Tend to a plant
7) Go to the local shop
8) {'Build the recreation area ($1000)' if not recreation_area.is_built() else 'Rest in the garden (skip to the next day)'}
9) Work to earn money (skip to the next day)
0) Exit
Your choice: """)

    print("")
    match choice:
        case '1':
            garden.get_info()

        case '2':
            if how_many_times_watered < 3:
                garden.water()
                how_many_times_watered += 1
            else:
                print("The plants aren't thirsty anymore!")

        case '3':
            gardener.weed(garden)

        case '4':
            gardener.use_soil_normalizer(garden)

        case '5':
            gardener.use_soil_fertilizer(garden)

        case '6':
            plant_name = input(f"Which plant ({garden.get_plant_list_string()}) would you like to tend to? ")
            if garden.has(plant_name):
                plant = garden.get_plant(plant_name)
                plant.boost_mood()
            else:
                print("There's no such plant in the garden!")

        case '7':
            shop_choice: str = input(f"""Balance: ${gardener.get_money_amount()}
What would you like to do?
1) Buy a new plant (${NEW_PLANT_COST})
2) Fix your hoe (${TOOL_FIX_COST})
3) Buy a soil acidity normalizer (${SOIL_NORMALIZER_COST})
4) Buy a soil fertilizer (${SOIL_FERTILIZER_COST})
5) Buy a garden gnome (${DECORATION_COST})
0) Exit
Your choice: """)
            match shop_choice:
                case '1':
                    while True:
                        bought_plant_name: str = input("Give the name to the plant: ")
                        if not garden.has(bought_plant_name):
                            break
                        print("There's a plant with this name already!")
                    gardener.buy_plant(garden, bought_plant_name)
                case '2':
                    gardener.fix_hoe()
                case '3':
                    gardener.buy_soil_normalizer()
                case '4':
                    gardener.buy_soil_fertilizer()
                case '5':
                    gardener.decorate(garden)
                case '0':
                    pass
                case _:
                    print("Invalid choice!")

        case '8':
            if not recreation_area.is_built():
                gardener.build_recreation_area(recreation_area)
            else:
                garden.spend_day_if_user_rests()
                day += 1
                how_many_times_watered = 0

        case '9':
            gardener.work()
            garden.spend_day_if_user_works()
            day += 1
            how_many_times_watered = 0

        case '0':
            print("See you again sometime!")
            break

        case 'GIMMEMONEYPLS':
            gardener.cheat_boost()
            print("+ $ 999 999")

        case 'IDKFA':
            garden.cheat_boost()
            print("All plants and soil healed!")

        case _:
            print("Invalid choice!")
