import tkinter as tk
import random
from wordlist import thewordlist
#guess=""
#5:50 PM Jan 31
numbs = ["One", "Two", "Three", "Four", "Five", "Six"]
colorrs = ["green", "#ebb813", "#3d3d3d"]
colors = ['black', 'black', 'black', 'black', 'black']
import requests
#theywon=False
window = tk.Tk()
window.title('neha wordle')
window.configure(bg="#ffffff")
#window.mainloop()
#window.geometry("410x100")
# #for i in range(6):
labelframe = tk.Frame(master=window, borderwidth=1, pady=5)
labelframe.configure(bg="#ffffff")
labelframe.grid(row=0, column=0, columnspan=5)

helloworld = tk.Label(master=labelframe,
                      text="Guess One: ",
                      fg="black",
                      bg="#ffffff",
                      font=("Arial", 10))
helloworld.pack(padx="160")
guessentry = tk.Entry(master=labelframe)
guessentry.pack()

#validguesses=0
validguesses = 0
theword = random.choice(thewordlist)
colors = ['black', 'black', 'black', 'black', 'black']


def submitaction():
    global validguesses
    global theword
    global colors
    #print(validguesses)

    try:
        msg.config(text="")
        guess = guessentry.get()
        if not isinstance(guess, str) or len(guess) != 5:
            raise ValueError

        url = requests.get(
            "https://dictionaryapi.com/api/v3/references/collegiate/json/" +
            guess + "?key=REPLACE_WITH_YOUR_API_KEY")
        url_json = url.json()
        ourdef = url_json[0].get("shortdef")
        guess = guess.upper()

        allused = []
        for j in range(len(guess)):
            if guess[j] == theword[j]:  #if it's the right location
                allused.append(guess[j])
                colors[j] = "green"
        for j in range(len(guess)):
            if guess[j] in theword and guess[j] != theword[j]:
                jintheword = theword.count(guess[j])
                jinguess = guess.count(guess[j])
                #if it's in the word but Not right location

                if allused.count(guess[j]) < jintheword:
                    #so this means like. if the number of that letter that has been colored is less than the number of those in the word
                    #if jinguess == jintheword:

                    colors[j] = "#ebb813"
                    allused.append(guess[j])
        for j in range(5):
            frame = tk.Frame(master=window, borderwidth=1)
            frame.grid(row=validguesses + 1, column=j, pady=5)
            label = tk.Label(master=frame,
                             text=guess[j],
                             height=2,
                             width=4,
                             bg=colors[j],
                             fg="white",
                             font=("Arial", 16))
            label.pack()
            #print(validguesses)
        #print(validguesses)
        if validguesses < 5 and not colors == [
                "green", "green", "green", "green", "green"
        ]:
            helloworld.config(text="Guess " + numbs[validguesses + 1] + ":  ")
        validguesses += 1

        if colors == ["green", "green", "green", "green", "green"]:
            msg.config(fg="green")
            msg.config(text="Congrats! You won!")
            #print("Congrats! You won!")
            validguesses = 6
        elif validguesses == 6:
            msg.config(fg="#ba0202")
            msg.config(text="Sorry, the word was " + theword + ".")
            #print("Sorry, the word was " + theword + ".")
        else:
            colors = ["black", "black", "black", "black", "black"]
        if validguesses == 6:
            submit['state'] = tk.DISABLED
            guessentry.config(state="disabled")
    except (AttributeError, ValueError):
        msg.config(fg="#ba0202")
        msg.config(text="Invalid guess")
        #print("Invalid guess")

    guessentry.delete(0, 'end')


submit = tk.Button(master=labelframe,
                   text="SUBMIT",
                   bg="#80b0ff",
                   activebackground="#b5d1ff",
                   command=submitaction,
                   disabledforeground="#545454")
submit.pack(pady="5")

msg = tk.Label(master=labelframe,
               text="",
               fg="black",
               bg="#ffffff",
               font=("Arial", 10))
msg.pack()
