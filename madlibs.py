from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Python Mad Libs!'))
def celebrity_fun():
	cel1 = input("Please enter a celebrity's name:\n")
	cel2 = input("Please enter another celebrity's name:\n")
	movie = input("Please enter a movie\n")
	print(f"{cel1} is rumored to be starring in a remake of the classic movie {movie} and will be starring opposite {cel2}!")

def political_fun():
	pol1 = input("Please enter a politician or celebrity\n")
	pol2 = input("Please enter another politician or celebrity\n")
	print(f"It was announced today that {pol1} is entering the 2020 Presidential race! {pol2} is rumored to be a potential future running mate!")

def fight_fun():
	fight1 = input("Please enter a fighter's name\n")
	nick = input("Please enter the nickname of the above fighter\n")
	fight2 = input("Please enter another fighter's name\n")
	loc = input("Please enter a city\n")
	move = input("Please enter a fighting strike or hold\n")
	print(f"{fight1} is scheduled to face {fight2} in {loc} this coming Saturday! The {nick} hopes to use the {move} to earn a victory.")
print("Please choose a story!")
print("Press 1 for celebrity news.")
print("Press 2 for political news")
print("Press 3 for fight news!")

user = input("Please enter your selection:\n")

if user == '1':
	celebrity_fun()
elif user == '2':
	political_fun()
elif user == '3':
	fight_fun()
else:
	print("Error!! Not a valid choice")

