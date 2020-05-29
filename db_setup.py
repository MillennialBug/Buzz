import sqlite3

db = sqlite3.connect('quizzes.db')
cur = db.cursor()

table_creates = ["""CREATE TABLE IF NOT EXISTS quizzes (
                 quiz_id INTEGER PRIMARY KEY,
                 owner INTEGER);""",
                 """CREATE TABLE IF NOT EXISTS questions (
                 question_id INTEGER PRIMARY KEY,
                 quiz_id INTEGER,
                 quiz_quest_num INTEGER,
                 question_text TEXT,
                 pic_url TEXT,
                 answer_text TEXT)""",
                 "CREATE TABLE IF NOT EXISTS playing "
                 "(owner INTEGER PRIMARY KEY, "
                 "quiz_id INTEGER, "
                 "questions INTEGER, "
                 "current_q INTEGER,"
                 "in_progress TEXT);"]

for table in table_creates:
    cur.execute(table)

db.commit()
# 470937192789966850 Bug
# 399527721161719809 Red
# cur.execute("INSERT INTO quizzes VALUES (?, ?)", (1, 399527721161719809))
cur.execute("INSERT INTO quizzes VALUES (?, ?)", (1, 399527721161719809))
cur.execute("INSERT INTO quizzes VALUES (?, ?)", (2, 399527721161719809))
cur.execute("INSERT INTO quizzes VALUES (?, ?)", (3, 399527721161719809))
cur.execute("INSERT INTO quizzes VALUES (?, ?)", (4, 399527721161719809))
cur.execute("INSERT INTO quizzes VALUES (?, ?)", (5, 399527721161719809))
db.commit()

questions = {1: (1, 1, "What is the national capital city of Canada?", "", "Ottawa"),
             2: (1, 2, "On a clothing label, what is symbolized by a circle with a cross running through it?", "",
                 "Do not dry clean"),
             3: (1, 3, "What is meant by the term 'on the rocks' on a drinks menu?", "", "It is served with ice"),
             4: (1, 4, "Which famous corporation uses the motto 'Just Do It'?", "", "Nike"),
             5: (1, 5, "What is the opening line to Michael Jackson's song 'Man in the Mirror'?", "",
                 "\"Gonna make a change, For once in my life\""),
             6: (1, 6, "Which country does Easter Island belong to?", "", "Chile"),
             7: (1, 7, "Which country's currency is the peso?", "", "Mexico"),
             8: (1, 8, "Who is the Greek god of the sea? ", "", "Poseidon"),
             9: (1, 9, "Can you name all the pieces used in a game of chess?", "",
                 "King, Queen, Bishop, Knight, Rook, Pawn"),
             10: (1, 10, "Can you name two American states consisting of only four letters?", "", "Ohio, Utah, Iowa"),
             11: (1, 11, "If  you were looking at the exchange rate of the USD to INR, which two currencies would you "
                         "be looking at?", "", "United States Dollar, Indian Rupee "),
             12: (1, 12, "At what age does Harry Potter learn that he's a wizard?", "", "11"),
             13: (1, 13, "Which three oceans are collectively known as the Southern Ocean?", "", "Pacific, Atlantic and"
                                                                                                 " Indian Oceans"),
             14: (1, 14, "Lacharophobia is a fear of which type of food?", "", "Vegetables"),
             15: (1, 15, "How many sides does a heptagon have?", "", "7"),
             16: (1, 16, "What was the name of the Smurfs’ evil nemesis?", "", "Gargamel"),
             17: (1, 17, "Mortimer was the original name that was given to which famous Disney character?", "",
                  "Mickey Mouse"),
             18: (1, 18, "What is Canadian artist Abel Makkonen Tesfaye better known as?", "", "The Weeknd"),
             19: (1, 19, "What is JFK’s full name?", "", "John Fitzgerald Kennedy"),
             20: (1, 20, "What is the name of the highest mountain in Europe?", "", "Mount Elbrus"),
             21: (2, 1, "What is the only country that is named after a tree?", "", "Brazil"),
             22: (2, 2, "What is CAPTCHA an acronym for?", "", "Completely Automated Public Turing Test To Tell "
                                                               "Computers and Humans Apart"),
             23: (2, 3, "How many stars are there on the Australian flag?", "", "6"),
             24: (2, 4, "Name the wives of King Henry VIII?", "", "Catherine of Aragon, Anne Boleyn, Jane "
                                                                  "Seymour, Anne of Cleves, Catherine Howard, a"
                                                                  "nd Catherine Parr"),
             25: (2, 5, "What is the largest island in the Caribbean?", "", "Cuba"),
             26: (2, 6, "What is dermatophobia the fear of?", "", "Skin disease"),
             27: (2, 7, "What was the middle name of Wolfgang Mozart?", "", "Amadeus"),
             28: (2, 8, "Guess the lyrics!\n\"This love has taken its toll on me; She said goodbye too many "
                        "times before.\"", "", "Maroon 5 - This Love"),
             29: (2, 9, "What is the third most common gas in the earth’s atmosphere after Nitrogen and Oxygen?", "",
                  "Argon"),
             30: (2, 10, "Solve this maths problem.\n2*6/3+5-2 = ?\n_No calculators allowed._", "", "7"),
             31: (2, 11, "What are the five boroughs in New York City?", "", "Staten Island, Queens, Manhattan, "
                                                                             "Brooklyn and The Bronx"),
             32: (2, 12, "The combination of star anise, cloves, fennel, cinnamon and Sichuan pepper "
                         "is commonly known as what?", "", "Chinese 5 spice"),
             33: (2, 13, "Which three colours are found on the Hungarian flag?", "", "Red, white, green."),
             34: (2, 14, "What is the name of Sherlock Holmes' older brother?", "", "Mycroft"),
             35: (2, 15, "Can you name this celebrity in their younger years?", "https://i.imgur.com/xJD7Q7E.jpg",
                  "Stephen Colbert"),
             36: (2, 16, "What’s the name of the first pink property on the London Monopoly board?", "", "Pall Mall"),
             37: (2, 17, "What’s the first animal in the English dictionary?", "", "Aardvark"),
             38: (2, 18, "What musicians' real name is Reginald Dwight?", "", "Elton John"),
             39: (2, 19, "Which European city consists of 90 islands and 1,500 bridges?", "", "Amsterdam"),
             40: (2, 20, "What movie did Tom Hanks get his first Academy Award nomination for?", "", "Big"),
             41: (3, 1, "What are the two main ingredients in a bellini cocktail?", "", "Prosecco and peach puree."),
             42: (3, 2, "Which animals' name means river horse?", "", "Hippopotamus."),
             43: (3, 3, "Which country has the longest coastline in the world?", "", "Canada."),
             44: (3, 4, "In the movie Dirty Dancing, what is Baby's first name?", "", "Frances."),
             45: (3, 5, "In the phonetic alphabet, which word is used for the letter F?", "", "Foxtrot."),
             46: (3, 6, "Which city hosted the Olympics in 2000?", "", "Sydney."),
             47: (3, 7, "In which sport would you use a shuttlecock?", "", "Badminton."),
             48: (3, 8, "What is the biggest state in America?", "", "Alaska."),
             49: (3, 9, "What is a box brownie?", "", "A type of camera."),
             50: (3, 10, "Marble is a common name for which chemical compound?", "", "Calcium carbonate."),
             51: (3, 11, "In which country did the Enchilada originate?", "", "Mexico."),
             52: (3, 12,
                  "Humbert Humbert and Dolores Haze are central characters of which controversial novel?", "",
                  "Lolita."),
             53: (3, 13, "Honey, Apidae and Carpenter are types of what?", "", "Bees."),
             54: (3, 14,
                  "In the movie, Se7en, what’s in the box that Brad Pitt finds?", "", "His wife’s decapitated head."),
             55: (3, 15,
                  "Eye-spy..which male celebrities' eyes are these?", "https://i.ibb.co/hCT6BPm/featured20.jpg",
                  "Nicholas Cage."),
             56: (
                 3, 16, "Which country's flag is this?", "https://i.ibb.co/xGSXWS6/0-THP-CHP-070520-SLUG-2371-JPG.jpg",
                 "Seychelles."),
             57: (3, 17, "In which nursery rhyme does the cow jump over the moon?", "", "Hey Diddle Diddle."),
             58: (3, 18, "In Roman mythology, who was the god of the Sun?", "", "Apollo."),
             59: (3, 19,
                  "Complete this lyric from the Cell-block Tango from Chicago the Musical.\n"
                  "\"So I took the shotgun off the wall and I fired two warning shots into...\"",
                  "", "His head."),
             60: (3, 20, "Which Bond movie poster have Coffee and Red recreated here?",
                  "https://i.ibb.co/199MX1x/61-RXZ-Tucg-L-AC-SL1024.jpg", "Spectre (2015)."),
             61: (4, 1, "Bodhrán, Conga and Snare are all types of which musical instrument?", "", "Drum."),
             62: (4, 2, "Rafiki, Timon and Zazu are all characters from which Disney musical?", "", "The Lion King."),
             63: (4, 3, "What year was Yorkshire Building Society founded?", "", "1864."),
             64: (4, 4,
                  "Before he became a legendary bodybuilder and world-famous actor, Arnold Schwarzenegger was already "
                  "a successful businessman. He began his rags-to-riches journey in which profession?",
                  "https://manofmany.com/wp-content/uploads/2019/03/Arnold-Schwarzeneggers-Diet-and-Workout-Plan.jpg",
                  "Brick-laying."),
             65: (4, 5,
                  "According to McDonalds’ official website, how many calories does a portion of 6 chicken nuggets "
                  "contain? Closest answer wins.",
                  "", "259"),
             66: (4, 6, "What are the two main ingredients in a bellini cocktail?", "", "Prosecco and peach puree."),
             67: (4, 7, "In the NATO phonetic alphabet, which word is used for the letter M?", "", "Mike."),
             68: (4, 8, "Who is this celebrity in their younger years?",
                  "https://i.ibb.co/b19gbfV/12.jpg ", "Tom Hanks."),
             69: (4, 9, "On a clothing label, what is symbolized by a circle with a cross running through it?", "",
                  "Do not dry clean."),
             70: (4, 10, "Prior to Mike Regnier, who was Yorkshire Building Society’s CEO?", "", "Chris Pilling."),
             71: (4, 11,
                  "Which country's flag is this?", "https://www.worldatlas.com/r/w1200-h701-c1200x701/upload/20/55/fb/"
                                                   "shutterstock-179853023.jpg",
                  "Seychelles."),
             72: (4, 12, "Who is the Greek god of the sea?", "", "Poseidon."),
             73: (4, 13, "Which famous company uses the motto 'Just Do It'?", "", "Nike."),
             74: (4, 14, "What is this a close up picture of?",
                  "https://i.ibb.co/3Twc62f/7616410-1-1479026018-650-32e9147584-1479194465.jpg", "Paperclip."),
             75: (4, 15, "How many sides does a heptagon have?", "", "7."),
             76: (4, 16, "What is the capital of Thailand?", "", "Bangkok."),
             77: (4, 17, "What was JFK’s full name?", "", "John Fitzgerald Kennedy."),
             78: (4, 18, "In which nursery rhyme does the cow jump over the moon?", "", "Hey Diddle Diddle."),
             79: (4, 19,
                  "In what movie does Meryl Streep play the ruthless and cynical magazine editor called Miranda "
                  "Priestly?",
                  "https://media.vanityfair.com/photos/576c585744d93e6e4482bb27/master/pass/"
                  "meryl-streep-devil-wears-prada.jpg",
                  "The Devil Wears Prada."),
             80: (4, 20, "In Greek mythology, Aphrodite is the goddess of?", "", "Beauty, love, passion."),
             81: (5, 1, "What is a group of Pandas called?", "", "An embarrassment."),
             82: (5, 2, "What is the only animal born with horns?", "", "A giraffe."),
             83: (5, 3, "What is this a close up of?", "https://i.ibb.co/C8Lg7ML/Close-Up.jpg", "Cornflakes."),
             84: (5, 4, "What is the heaviest human organ?", "", "The skin."),
             85: (5, 5, "Name this celebrity in their younger years.",
                  "https://i.ibb.co/Q66L8kg/celebrities-when-they-were-young-8.jpg", "Eminem."),
             86: (5, 6, "In which year did Twitter launch?", "", "2006."),
             87: (5, 7, "What movie is this vehicle from?", "https://i.ibb.co/gVKzDGr/Bus-jump.jpg", "Speed."),
             88: (5, 8, "Which side of the road do people drive on in Australia?", "", "Left."),
             89: (5, 9, "What movie is this opening shot from?", "https://i.ibb.co/w6fVknN/image0.jpg",
                  "American Psycho."),
             90: (5, 10, "What are the two main ingredients of a Dark and Stormy cocktail?", "https://images.ctfassets"
                                                                                             ".net/3s5io6mnxfqz/1PCfdN3"
                                                                                             "mQyGbvoGwMI2tLH/68219a26e"
                                                                                             "a1199ae8a93a79eff19bbea/A"
                                                                                             "dobeStock_190239173.jpeg",
                  "Dark rum and ginger beer."),
             91: (5, 11, "Can you identify this flag?", "https://i.ibb.co/FWVw4TP/Flag.jpg", "Botswana."),
             92: (5, 12, "Who was the 40th President of the USA?", "", "Ronald Regan."),
             93: (5, 13, "Which is the only vowel not used as the first letter in a US State?", "", "E."),
             94: (5, 14, "Which country is the world’s largest producer of cheese?", "", "USA."),
             95: (5, 15, "Which movie has the best-selling soundtrack of all time?", "", "The Bodyguard. (1992)."),
             96: (5, 16, "Which two animals feature on the coat of arms of Australia?", "", "Kangeroo and emu."),
             97: (5, 17, "Pupaphobia is the fear of what?", "", "Puppets."),
             98: (5, 18, "On a roulette wheel, what colour is the pocket numbered zero?", "", "Green."),
             99: (5, 19, "Can you identify this movie poster without the text?",
                  "https://i.ibb.co/72kGFCf/24-The-Exoricist.jpg", "The Exorcist."),
             100: (5, 20, "What was the name of Ross's pet monkey in Friends?",
                   "https://vignette.wikia.nocookie.net/friends/images/f/f7/Marcelandross.jpg/revision/latest/top-crop/"
                   "width/360/height/360?cb=20080803123627",
                   "Marcel.")}

for q in questions.values():
    cur.execute('INSERT INTO questions (quiz_id, quiz_quest_num, question_text, pic_url, answer_text) '
                'VALUES (?, ?, ?, ?, ?)', q)

db.commit()
