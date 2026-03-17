import time as time
import random as rand
play = True
questions = []
choices = []
answers = []
qdone=0
qs = 0
with open("1.se") as f:
  for x in f:
    print(x)
def menu():
        
        print("Welcome to the game")
        if int(input("1. Start Quiz \n2. Quit\n")) == 2:
                exit(0)
        else:
                 qs = int(input("How many questions would you like? "))
        print("Starting quiz in 3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)


def question():
        num = rand.randrange(0,49)
        ans = input(questions[num] + "\n" + choices[num])
        if ans == answers[num]:
                print("Correct yipee")
                score += 1 

questions = ["What is the capital city of France?", "What is the largest mammal on Earth?", "What is the chemical symbol for gold?", "Who wrote the novel 1984?", "What process do plants use to make food from sunlight?", "What is the hardest natural substance?", "What is the smallest prime number?", "Which instrument typically has 88 keys?", "On which continent is the Sahara Desert located?", "At sea level, water boils at what temperature in Celsius?", "What is the approximate speed of light in vacuum?", "What is the currency of Japan?", "Which gas is most abundant in Earth's atmosphere?", "Who was the first President of the United States?", "What is the official language of Brazil?", "Who painted The Starry Night?", "Which organ pumps blood through the human body?", "What is the square root of 144?", "What is traditionally considered the longest river in the world?", "Which planet currently has the most confirmed moons?", "Who is credited with inventing the telephone?", "What is the largest hot desert in the world?", "Which metal is liquid at room temperature?", "What component is often called the brain of the computer?", "Who wrote Hamlet?", "What is the nearest star to Earth after the Sun?", "What is decimal 2 in binary?", "What is the largest planet in our solar system?", "Which is the heaviest naturally occurring element?", "The Pythagorean theorem applies to which type of triangle?", "Which ocean lies between Africa and Australia?", "Which gas do humans primarily breathe in to survive?", "What is the freezing point of water in Celsius?", "What is the Roman numeral for 50?", "Which country is known as the Land of the Rising Sun?", "What is the largest internal organ in the human body?", "Which device measures earthquake waves?", "What is the first month of the Gregorian calendar?", "Which planet is famous for its rings?", "What is the currency of the United Kingdom?", "Who developed the theory of relativity?", "What is the longest bone in the human body?", "Which protocol is commonly used for secure web browsing?", "How many chambers does a human heart have?", "What is the largest island in the world?", "How many continents are there on Earth?", "Which programming language is known for indentation-based syntax?", "Who discovered penicillin?", "What is the unit of electrical resistance?", "What is the tallest mountain above sea level?"]
choices = ["A. Madrid\nB. Rome\nC. Paris\nD. Berlin\n", "A. African elephant\nB. Blue whale\nC. Giraffe\nD. Orca\n", "A. Au\nB. Ag\nC. Gd\nD. Go\n", "A. Aldous Huxley\nB. Ernest Hemingway\nC. Jane Austen\nD. George Orwell\n", "A. Respiration\nB. Photosynthesis\nC. Transpiration\nD. Fermentation\n", "A. Quartz\nB. Steel\nC. Diamond\nD. Granite\n", "A. 2\nB. 1\nC. 3\nD. 0\n", "A. Violin\nB. Piano\nC. Flute\nD. Trumpet\n", "A. Asia\nB. Europe\nC. Africa\nD. South America\n", "A. 90\nB. 100\nC. 80\nD. 120\n", "A. 150,000 km/s\nB. 30,000 km/s\nC. 3,000 km/s\nD. 300,000 km/s\n", "A. Yen\nB. Won\nC. Yuan\nD. Dollar\n", "A. Oxygen\nB. Carbon dioxide\nC. Nitrogen\nD. Hydrogen\n", "A. Thomas Jefferson\nB. George Washington\nC. John Adams\nD. Abraham Lincoln\n", "A. Spanish\nB. English\nC. French\nD. Portuguese\n", "A. Vincent van Gogh\nB. Claude Monet\nC. Pablo Picasso\nD. Salvador Dali\n", "A. Lungs\nB. Brain\nC. Heart\nD. Liver\n", "A. 10\nB. 12\nC. 14\nD. 16\n", "A. Nile\nB. Amazon\nC. Yangtze\nD. Mississippi\n", "A. Jupiter\nB. Mars\nC. Uranus\nD. Saturn\n", "A. Nikola Tesla\nB. Alexander Graham Bell\nC. Thomas Edison\nD. James Watt\n", "A. Gobi Desert\nB. Arabian Desert\nC. Sahara Desert\nD. Kalahari Desert\n", "A. Mercury\nB. Aluminum\nC. Copper\nD. Iron\n", "A. RAM\nB. SSD\nC. GPU\nD. CPU\n", "A. Charles Dickens\nB. William Shakespeare\nC. Leo Tolstoy\nD. Mark Twain\n", "A. Sirius\nB. Alpha Centauri A\nC. Proxima Centauri\nD. Betelgeuse\n", "A. 10\nB. 01\nC. 11\nD. 100\n", "A. Earth\nB. Saturn\nC. Jupiter\nD. Neptune\n", "A. Lead\nB. Uranium\nC. Gold\nD. Platinum\n", "A. Equilateral triangle\nB. Isosceles triangle\nC. Scalene triangle\nD. Right-angled triangle\n", "A. Pacific Ocean\nB. Indian Ocean\nC. Atlantic Ocean\nD. Arctic Ocean\n", "A. Oxygen\nB. Nitrogen\nC. Helium\nD. Carbon monoxide\n", "A. 32\nB. -10\nC. 0\nD. 10\n", "A. L\nB. X\nC. C\nD. V\n", "A. China\nB. Japan\nC. South Korea\nD. Thailand\n", "A. Skin\nB. Stomach\nC. Brain\nD. Liver\n", "A. Thermometer\nB. Barometer\nC. Seismograph\nD. Altimeter\n", "A. January\nB. March\nC. June\nD. December\n", "A. Venus\nB. Saturn\nC. Mercury\nD. Earth\n", "A. Euro\nB. Dollar\nC. Franc\nD. Pound sterling\n", "A. Isaac Newton\nB. Galileo Galilei\nC. Albert Einstein\nD. Niels Bohr\n", "A. Femur\nB. Tibia\nC. Humerus\nD. Radius\n", "A. FTP\nB. HTTPS\nC. SMTP\nD. HTTP\n", "A. 2\nB. 3\nC. 4\nD. 5\n", "A. Madagascar\nB. Borneo\nC. New Guinea\nD. Greenland\n", "A. 7\nB. 5\nC. 6\nD. 8\n", "A. Java\nB. Python\nC. C\nD. Ruby\n", "A. Louis Pasteur\nB. Marie Curie\nC. Alexander Fleming\nD. Gregor Mendel\n", "A. Ohm\nB. Volt\nC. Ampere\nD. Watt\n", "A. K2\nB. Kangchenjunga\nC. Lhotse\nD. Mount Everest\n"]
answers = ["C", "B", "A", "D", "B", "C", "A", "B", "C", "B", "D", "A", "C", "B", "D", "A", "C", "B", "A", "D", "B", "C", "A", "D", "B", "C", "A", "C", "B", "D", "B", "A", "C", "A", "B", "D", "C", "A", "B", "D", "C", "A", "B", "C", "D", "A", "B", "C", "A", "D"]

while play == True:
        score = 0

        menu()

        while qdone != qs:
               question()
               qdone+= 1
        
        if input("\nPlay again?\n1.Yes\n2.No") == '1':
                print("Yay")
        else: quit(0)