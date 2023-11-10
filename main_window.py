import tkinter as tk
from tkmacosx import Button
import random
# Import messagebox separately
from tkinter import messagebox
from all_words import ALL_WORDS


# Implement game statistics
GUESS_COUNT = 6
games_stats = []
remaining_guesses = GUESS_COUNT
list_of_row_lists = []
current_guess = ""
letter_count = 0
games_played = 0
words_list = ['пакет', 'курка', 'буква', 'чайка', 'берег', 'башта', 'архів', 'зірка', 'кобза', 'ліжко', 'сусід', 'узвар', 'цегла', 'хімія', 'фінал', 'юрист', 'халва', 'поїзд', 'обʼєм', 'горло', 'опіум', 'синус', 'мокро', 'фарба', 'учень', 'зріст', 'група', 'шинка', 'пошук', 'трава', 'свиня', 'обвал', 'туман', 'форма', 'склад', 'щогла', 'утиск', 'лицар', 'вітер', 'голка', 'аорта', 'вафля', 'етика', 'земля', 'базар', 'ртуть', 'хунта', 'фініш', 'мойра', 'пугач', 'кошти', 'буття', 'жінка', 'разом', 'бісер', 'вазон', 'напад', 'жрець', 'тонус', 'мавпа', 'цифра', 'лимон', 'злива', 'добро', 'аркуш', 'баран', 'особа', 'обрив', 'епоха', 'ожина', 'двері', 'цукат', 'гроно', 'діжка', 'ворог', 'акула', 'зеніт', 'річка', 'назва', 'табун', 'анонс', 'бідон', 'пекло', 'рибак', 'хвиля', 'горіх', 'килим', 'намул', 'жменя', 'дзиґа', 'медіа', 'олень', 'шинок', 'читач', 'живіт', 'допис', 'кухар', 'таксі', 'опора', 'норма', 'зерно', 'короп', 'цвіль', 'гідра', 'злоба', 'коала', 'обмін', 'хруст', 'чохол', 'знать', 'плита', 'ринок', 'чавун', 'еклер', 'думка', 'праця', 'намір', 'горох', 'осока', 'лиман', 'гвинт', 'дієта', 'блуза', 'ґвалт', 'дошка', 'кювет', 'зміна', 'буряк', 'щастя', 'павич', 'арена', 'втома', 'аґрус', 'обсяг', 'колія', 'докір', 'розум', 'буфет', 'хмара', 'дикун', 'цукор', 'чобіт', 'радар', 'титан', 'осика', 'магія', 'вузол', 'запас', 'голод', 'увага', 'журба', 'фазан', 'крило', 'майор', 'пусто', 'носій', 'дотик', 'мотор', 'наука', 'жнива', 'огида', 'пасок', 'спирт', 'унція', 'обряд', 'груша', 'озеро', 'кіоск', 'нація', 'бутон', 'дрова', 'залік', 'еліта', 'синяк', 'касир', 'пацюк', 'гілля', 'кошик', 'рядок', 'аргон', 'череп', 'торік', 'життя', 'буйок', 'школа', 'лишай', 'отвір', 'марка', 'слива', 'армія', 'зшити', 'какао', 'філія', 'зошит', 'пучок', 'емаль', 'гамір', 'натяк', 'ангар', 'секта', 'гроші', 'ляпас', 'атлет', 'копія', 'естет', 'вигук', 'кабан', 'адепт', 'ордер', 'точка', 'окріп', 'комар', 'замша', 'мопед', 'книга', 'серце', 'агент', 'океан', 'черга', 'масло', 'весна', 'ложка', 'кефір', 'набір', 'салон', 'зрада', 'нафта', 'казан', 'обгін', 'князь', 'аташе', 'торба', 'батон', 'карма', 'манго', 'пасаж', 'зебра', 'алмаз', 'чарка', 'кожух', 'літак', 'пудра', 'заєць', 'щітка', 'пункт', 'ідеал', 'логік', 'чумак', 'страх', 'клоун', 'гумор', 'усміх', 'палій', 'мумія', 'злука', 'атлас', 'пошта', 'фішка', 'гість', 'кішка', 'майно', 'бочка', 'квант', 'осінь', 'морда', 'завше', 'мазут', 'сталь', 'мряка', 'обруч', 'мозок', 'ліцей', 'квота', 'палка', 'ліміт', 'ціпок', 'ікона', 'збори', 'атака', 'окунь', 'каска', 'лазня', 'балка', 'факел', 'інжир', 'омлет', 'поділ', 'ручка', 'магма', 'бренд', 'пласт', 'пісок', 'дятел', 'сором',  'миска', 'лінза', 'номер', 'канва', 'дзвін', 'онука', 'паска', 'азарт', 'спина', 'щебет', 'іспит', 'зброя', 'астма', 'олово', 'жупан', 'дамба', 'тирса', 'запах', 'хвіст', 'метал', 'фасон', 'брила', 'вуаль', 'лаваш', 'намет', 'напій', 'губка', 'товар', 'попіл', 'мʼясо', 'драма', 'робот', 'шкіра', 'порох', 'оазис', 'монах', 'олімп', 'гроза', 'зміст', 'вокал', 'криво', 'орден', 'мавка', 'індик', 'плече', 'нетрі', 'чвари', 'вдома', 'алібі', 'успіх', 'попит', 'кажан', 'віяло', 'абзац', 'озноб', 'цезій', 'олива', 'вгорі', 'збоку', 'іскра', 'папір', 'цинга', 'кавун', 'булка', 'орган', 'чашка', 'ватра', 'любов', 'ранок', 'гуляш', 'екран'];

def choose_word():
    return random.choice(words_list)

current_word = choose_word()

def main():

    game = tk.Tk()

    # Set a title
    game.title("Ukrainian WORDLE")
    game.geometry('800x1000')
    game.configure(bg='#D2E8E3')


    def color_letter(letter, color, position):
        # Color keyboard - probably put keyboard keys in some array
        for keys_row in keys_list:
            for key in keys_row:
                if key.cget("text") == letter.upper():
                    if key.cget("bg") == "#7DB777":
                        pass
                    else:
                        key.config(bg=color, fg="#f5f9f6")


        # Color boxes
        global remaining_guesses
        current_row = GUESS_COUNT - remaining_guesses
        global list_of_row_lists
        list_of_row_lists[current_row][position].config(bg=color, fg="#f5f9f6")


    # Insertion
    def letter_insert(this_letter):
        this_letter = this_letter.lower()
        # Check if the word is no longer than 5 letters
        global letter_count
        if letter_count == 5:
            return

        # Find current row
        global remaining_guesses
        current_row = GUESS_COUNT - remaining_guesses

        # Insert char into label cell
        global list_of_row_lists
        list_of_row_lists[current_row][letter_count].config(text = this_letter.upper())

        # Update stats
        letter_count += 1
        global current_guess
        current_guess += this_letter


    def delete_letter():
        global letter_count
        if letter_count > 0:
            global list_of_row_lists
            global remaining_guesses
            current_row = GUESS_COUNT - remaining_guesses

            # Remove letter from the cell
            list_of_row_lists[current_row][letter_count-1].config(text = "")
            letter_count -= 1

            # REMOVE IT FROM GUESS
            global current_guess
            current_guess = current_guess[:-1]

        else:
            return


    def check_input():
        # Check if the word is long enough
        global letter_count
        if too_short(letter_count):
        # if letter_count < 5:
            messagebox.showinfo("Помилка", "Недостатньо букв!")
            return

        # Check if the word exhists
        global current_guess
        if not word_exists(current_guess):
        # if current_guess not in ALL_WORDS:
            messagebox.showinfo("Помилка", "Такого слова не існує!")
            return

        # Check letters position - enumarate + pass index of the letter in word to color letter
        global current_word
        for count, char in enumerate(current_guess):
            if char not in current_word:
                color_letter(char, "#71797E", count)
            else:
                if char == current_word[count]:
                    color_letter(char, "#7DB777", count)
                else:
                    color_letter(char, "#E6B000", count)


        global games_played
        global games_stats
        # Check if the guess is correct - return message + final pop-up play more  + update wins count + games playes + sleep
        if current_word == current_guess:

            games_played += 1
            games_stats.append(True)
            game_end("Молодець", "Перемога!")
            return

        else:
            # Update fields before new attempt
            global remaining_guesses
            remaining_guesses -= 1
            current_guess = ""
            letter_count = 0

            # Check if we have any guesses remaining - if not - game over + update games played + pop-up play more
            if remaining_guesses == 0:
                games_played += 1
                games_stats.append(False)
                message = f"Слово дня — {current_word}"
                game_end("Гру закінчено", message)
                return



    def move_to_start():

        # Clear guess count
        global remaining_guesses
        remaining_guesses = GUESS_COUNT

        global current_guess
        current_guess = ""
        # Set new guess word (check if it sets)
        global current_word
        current_word = random.choice(words_list)

        global letter_count
        letter_count = 0


        # Clear keyboard + color and input of letter boxes
        for keys_row in keys_list:
            for key in keys_row:
                key.config(bg="#C8C8C8", fg="#013939")

        for letter_row in list_of_row_lists:
            for letter_box in letter_row:
                letter_box.config(bg="#D2DFD2", fg="#014C4C", text="")



    # Add header
    def open_rules():
        # Create a window
        rules_info = tk.Toplevel(game)
        rules_info.title("Правила")
        rules_info.geometry("460x490")

        # Add multiple label for text data
        tk.Label(rules_info, text="Вгадайте СЛОВО за 6 спроб!", font=("Arial", 20)).place(x=100, y=5)
        tk.Label(rules_info, text="Кожна спроба має містити справжнє слово з 5 літер.").place(x=10, y=45)
        tk.Label(rules_info, text="Натисніть Enter щоб підтвердити спробу").place(x=10, y=70)
        tk.Label(rules_info, text="Після кожної спроби колір клітинок змінюватиметься,").place(x=10, y=95)
        tk.Label(rules_info, text="щоб показати наскільки близькою до правильної була ваша спроба.").place(x=10, y=120)
        tk.Label(rules_info, text="Спроба може містити лише слова в словниковій формі.").place(x=10, y=145)
        tk.Label(rules_info, text="Приклади:", font=("Arial", 18)).place(x=20, y=176)

        # Examples
        tk.Label(rules_info, text="В", highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), padx=3).place(x=45, y=213)
        tk.Label(rules_info, text="Е", highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), padx=3).place(x=77, y=213)
        tk.Label(rules_info, text="Ч", highlightthickness=2, highlightbackground="#027373", bg="#7DB777", font=("Arial", 20), padx=3).place(x=109, y=213)
        tk.Label(rules_info, text="І", highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), padx=7).place(x=141, y=213)
        tk.Label(rules_info, text="Р", highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), padx=3).place(x=173, y=213)

        tk.Label(rules_info, text="Буква Ч є в слові і знаходиться на правильному місці.").place(x=18, y=250)

        tk.Label(rules_info, text="Р",highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), padx=3).place(x=45, y=280)
        tk.Label(rules_info, text="И",highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), padx=3).place(x=77, y=280)
        tk.Label(rules_info, text="Б",highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), padx=3).place(x=109, y=280)
        tk.Label(rules_info, text="А",highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), padx=4).place(x=141, y=280)
        tk.Label(rules_info, text="К",highlightthickness=2, highlightbackground="#027373", font=("Arial", 20), bg="#E6B000", padx=5).place(x=173, y=280)

        tk.Label(rules_info, text="Буква К є в слові але розташована в іншому місці.").place(x=18, y=315)

        tk.Label(rules_info, text="П", font=("Arial", 20), highlightthickness=2, highlightbackground="#027373", padx=3).place(x=45, y=350)
        tk.Label(rules_info, text="И", font=("Arial", 20), highlightthickness=2, highlightbackground="#027373", bg="#71797E", padx=3).place(x=77, y=350)
        tk.Label(rules_info, text="Р", font=("Arial", 20), highlightthickness=2, highlightbackground="#027373", padx=3).place(x=109, y=350)
        tk.Label(rules_info, text="І", font=("Arial", 20), highlightthickness=2, highlightbackground="#027373", padx=7).place(x=141, y=350)
        tk.Label(rules_info, text="Г", font=("Arial", 20), highlightthickness=2, highlightbackground="#027373", padx=5).place(x=173, y=350)

        tk.Label(rules_info, text="Слово не містить цієї букви.").place(x=18, y=385)

        # Close window button
        close_rules_button = Button(rules_info, text="Закрити", bg='#B6CEC6', fg='#00203F', bordercolor="#A49E91", activebackground='#76A17D',
                activeforeground='#2a452e',  borderless=1, command=lambda: rules_info.destroy(), pady=8, padx=5).place(x=170, y=425)


    def game_end(title, message):
        end_logo = tk.Toplevel(game)
        end_logo.title(title)
        end_logo.geometry("400x200")
        tk.Label(end_logo, text=message, font=("Arial", 18), highlightthickness=1, highlightbackground="#026B6B", padx=4, pady=2).place(x=155, y=30)

        new_game_btn = Button(end_logo, text="Нова гра", bg='#B6CEC6', fg='#00203F', bordercolor="#A49E91", activebackground='#76A17D',
                activeforeground='#2a452e',  borderless=1, command=lambda: [move_to_start(), end_logo.destroy()], pady=8, padx=5).place(x=65, y=125)

        check_stats_btn = Button(end_logo, text="Статистика", bg='#B6CEC6', fg='#00203F', bordercolor="#A49E91", activebackground='#76A17D',
                activeforeground='#2a452e',  borderless=1, command=lambda: [open_stats(), end_logo.destroy(), move_to_start()], pady=8, padx=5).place(x=210, y=125)


    def open_stats():
        # Create a window

        stats_info = tk.Toplevel(game)
        stats_info.title("Статистика")
        stats_info.geometry("400x200")


        # Use game data to calculate statistics data - games count and wins %
        tk.Label(stats_info, text="Всього", font=("Arial", 18)).place(x=50, y=42)
        tk.Label(stats_info, text=games_played, font=("Arial", 18)).place(x=70, y=80)
        tk.Label(stats_info, text="% Перемог", font=("Arial", 18)).place(x=250, y=42)

        if len(games_stats) == 0:
            wins_data = "Немає даних"
        else:
            wins_count = 0
            for gameplay in games_stats:
                if gameplay == True:
                    wins_count +=1
            wins_data = round(wins_count * 100 / games_played)
        tk.Label(stats_info, text=wins_data, font=("Arial", 17)).place(x=250, y=80)


        # Close window button
        close_stats_button = Button(stats_info, text="Закрити", bg='#B6CEC6', fg='#00203F', bordercolor="#A49E91", activebackground='#76A17D',
                activeforeground='#2a452e',  borderless=1, command=lambda: stats_info.destroy(), pady=8, padx=5).place(x=145, y=125)



    # Rules button
    rules_button = Button(game, text="Правила", bg='#B6CEC6', fg='#00203F', bordercolor="#A49E91", activebackground='#76A17D',
                activeforeground='#2a452e',  borderless=1, command=open_rules, pady=8, padx=5)
    rules_button.place(x=5, y=3)


    # Title
    title = tk.Label(game, text="WORDLE UA", bg="#D2E8E3", fg="#012626", font=("Arial", 25), pady=8, padx=5)
    title.place(x=320, y=3)

    # Stats button
    stats_button = Button(game, text="Статистика", bg='#B6CEC6', fg='#00203F', bordercolor="#A49E91", activebackground='#76A17D',
                activeforeground='#2a452e', borderless=1, command=open_stats, pady=8, padx=5)
    stats_button.place(x=670, y=3)


    # Make sections
    guess_area = tk.LabelFrame(game, bg="#D2E8E3", relief=tk.FLAT, width=300, height=400).place(x=250, y=75)

    y_position = 70

    for i in range(6):
        # Add row to the list of rows
        new_list = []
        list_of_row_lists.append(new_list)
        x_position = 250
        for k in range(5):
            label_item = tk.Label(guess_area, text="", bg="#D2DFD2", fg="#014C4C", highlightthickness=2, highlightbackground="#027373", font=("Futura", 24))
            # Add label to the row
            list_of_row_lists[i].append(label_item)
            label_item.place(x=x_position, y=y_position, width=40, height=55)
            x_position += 55
        y_position += 70



    keyboard = tk.Frame(game, bg="#D2E8E3", relief=tk.FLAT, width=600, height=230).place(x=100, y=500)

    alphabet_row_1 = ["ʼ", "Й", "Ц", "У", "К", "Е","Н", "Г", "Ш", "Щ", "З", "Х", "Ї"]
    alphabet_row_2 = ["Ф", "І", "В", "А", "П", "Р","О", "Л", "Д", "Ж","Є"]
    alphabet_row_3 = ["Ґ", "Я", "Ч", "С", "М", "И", "Т","Ь", "Б", "Ю"]
    keys_list = [[] for x in range(3)]


    coord_x = 140
    coord_y = 525
    for letter in range(len(alphabet_row_1)):
        current_letter = alphabet_row_1[letter]
        add_command = lambda x=current_letter: letter_insert(x)
        letter_i = Button(keyboard, text=current_letter, bg='#C8C8C8',
                fg='#013939', borderless=1,
                activebackground='#A2AFA2',
                width=35, height=45, command=add_command, font=("Helvetica", 20))
        keys_list[0].append(letter_i)
        letter_i.place(x=coord_x, y=coord_y)
        coord_x = coord_x + 40

    coord_x = 180
    coord_y = 590
    for letter in range(len(alphabet_row_2)):
        current_letter = alphabet_row_2[letter]
        add_command = lambda x=current_letter: letter_insert(x)
        letter_i = Button(keyboard, text=current_letter, bg='#C8C8C8',
                fg='#013939', borderless=1,
                activebackground='#A2AFA2',
                width=35, height=45, command=add_command, font=("Helvetica", 20))
        keys_list[1].append(letter_i)
        letter_i.place(x=coord_x, y=coord_y)
        coord_x = coord_x + 40

    coord_x = 200
    coord_y = 655
    for letter in range(len(alphabet_row_3)):
        current_letter = alphabet_row_3[letter]
        add_command = lambda x=current_letter: letter_insert(x)
        letter_i = Button(keyboard, text=current_letter, bg='#C8C8C8',
                fg='#013939', borderless=1,
                activebackground='#A2AFA2',
                width=35, height=45, command=add_command, font=("Helvetica", 20))
        keys_list[2].append(letter_i)
        letter_i.place(x=coord_x, y=coord_y)
        coord_x = coord_x + 40

    # Delete button
    Button(keyboard, text="Back", bg='#C8C8C8',
                fg='#013939', borderless=1, activebackground='#A2AFA2',
                width=75, height=45, font=("Helvetica", 18), command=delete_letter).place(x=120, y=655)

    #Enter button
    Button(keyboard, text="Enter", bg='#C8C8C8',
                fg='#013939', borderless=1, activebackground='#A2AFA2',
                width=75, height=45, font=("Helvetica", 18), command=check_input).place(x=600, y=655)



    # Footer
    footer = tk.Label(game, text="CS50P, Oksana Marushchak", font=("Arial", 16), fg='#00203F', bg="#D2E8E3")
    footer.place(x=50, y=755)

    # Play the game
    game.mainloop()


def word_exists(word):
    if word in ALL_WORDS:
        return True
    else:
        return False


def too_short(counter):
    if counter < 5:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
