import random
hangman_stages = [
    """
       +---+
           |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
       |   |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
      /|   |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
      /|\  |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
      /|\  |
      /    |
           |
           |
    =========
    """,
    """
       +---+
       O   |
      /|\  |
      / \  |
           |
           |
    =========
    """
]
City = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Visakhapatnam", "Patna","Agra", "Nashik", "Ranchi",
    "Coimbatore", "Vijayawada", "Chandigarh", "Mysore", "Guwahati", "Rajkot",
    "Jodhpur", "Madurai", "Raipur", "Kochi", "Thiruvananthapuram", "Aurangabad",
     "Meerut", "Amritsar", "Varanasi", "Allahabad", "Gwalior", "Jammu",
    "Noida", "Tirupati", "Udaipur", "Shimla", "Manali", "Pondicherry", "Vellore", "Jamshedpur",
     "Dehradun", "Bhubaneswar", "Puri", "Shillong", "Gangtok",
    "Kharagpur", "Guntur", "Mangalore", "Warangal", "Srinagar","Panaji", "Haridwar", "Mathura",
    "Alleppey", "Dharamsala", "Ooty", "Kodaikanal", "Darjeeling", "Nainital", "Mussoorie",
    "Bilaspur", "Kurnool", "Imphal","Visakhapatnam", "Vijayawada", "Guntur", "Tirupati", "Nellore",
    "Kurnool", "Kakinada", "Rajahmundry", "Eluru",
    "Chittoor", "Ongole", "Kadapa", "Srikakulam", "Anantapur", "Machilipatnam", "Vizianagaram", "Bhimavaram",
    "Narasaraopet", "Gudivada", "Palasa", "Bapatla", "Narasapuram", "Tuni", "Macherla","Sompeta", "Srikalahasti", "Pithapuram",
    "Repalle", "Palakollu", "Tanuku", "Chirala", "Kanigiri", "Nandigama", "Ramachandrapuram",
    "Bobbili", "Parvathipuram", "Salur", "Narsipatnam", "Bhimli", "Amudalavalasa",
     "Gajuwaka", "Anakapalle",]
word=(random.choice(City)).upper()
print("Welcome to Hangman's Game")
display=[]
Lives=0
for i in word:
    display+='_'
print(display)
print(hangman_stages[0])
game=True
same=""
while game:
    guess = (input("Enter a word")).upper()
    if guess not in same:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print(display)
    else:
        Lives += 1
        print(hangman_stages[Lives])
    same+=guess
    if guess not in word:
        Lives+=1
        print(hangman_stages[Lives])
    if '_' not in display:
        print("      You Win")
        print("     😎😎😎😎😎")
        print("     😎😎😎😎😎")
        print("     😎😎😎😎😎")
        print("     😎😎😎😎😎")
        print("     😎😎😎😎😎")
        game=False
    if Lives==6:
        print("      You Lose")
        print("     You Are Dead")
        print("     😭😭😭😭😭")
        print("     😭😭😭😭😭")
        print("     😭😭😭😭😭")
        print("     😭😭😭😭😭")
        print("     😭😭😭😭😭")
        game=False
