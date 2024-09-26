import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
MORSE_CODE_DICT = { 'a':'.-',
                    'b':'-...',
                    'c':'-.-.',
                    'd':'-..',
                    'e':'.',
                    'f':'..-.',
                    'g':'--.',
                    'h':'....',
                    'i':'..',
                    'j':'.---',
                    'k':'-.-',
                    'l':'.-..',
                    'm':'--',
                    'n':'-.',
                    'o':'---',
                    'p':'.--.',
                    'q':'--.-',
                    'r':'.-.',
                    's':'...',
                    't':'-',
                    'u':'..-',
                    'v':'...-',
                    'w':'.--',
                    'x':'-..-',
                    'y':'-.--',
                    'z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----',
                    ', ':'--..--',
                    '.':'.-.-.-',
                    '?':'..--..',
                    '!':'-.-.--',
                    '"':'.-..-.',
                    '&':'.-...',
                    ':':'---...',
                    ';':'-.-.-.',
                    '/':'-..-.',
                    '-':'-....-',
                    '_':'..--.-',
                    '=':'-...-',
                    '+':'.-.-.',
                    '$':'...-..-',
                    '@':'.--.-.',
                    '(':'-.--.',
                    ')':'-.--.-',
                    '’':'.----.',
                    ' ':'/'
                    }
sentence_list = ['Good morning!', 'What time is it?', 'Can you help me with this?', 'I’m sorry for the delay.', 'Could you please repeat that?', 'What’s your name?', 'How are you today?', 'They attend concerts.', 'You participate in marathons.', 'Where are you from?', 'Nice to meet you.', 'How was your day?', 'I’m hungry. Let’s grab something to eat.', 'Excuse me, where is the nearest restroom?', 'Can you recommend a good book?', 'Where is the nearest ATM?', 'I’m not feeling well.', 'How was your weekend?', 'I can’t find my keys.', 'Can you give me a hand?', 'That’s a great idea!', 'I’m so excited!', 'What’s your favorite music genre?', 'Have a safe trip!', 'How much does it cost?', 'How would you like steaks to be cooked?', 'I want to go to the metro station.', 'I want to go to the hospital.', 'I want to introduce myself.', 'Have you ever had a pet?', 'What is your favorite season?', 'My favorite actor is Shah Rukh Khan.', 'She prefers coffee.', 'They met him.', 'I’m sorry, I couldn’t call you.', 'I sent that yesterday.', 'Make my apologies.', 'She feels that too.', 'She learned Arabic.', 'Get up early.', 'Go and play.', 'Listen to me.', 'Do you have any homework?', 'Have your breakfast.', 'What’s going on?', 'Comb your hair.', 'You may fall down.', 'Enjoy yourself.', 'See you next time.', 'Bye, See you again!', 'They go on sightseeing tours.', 'You attend pottery workshops.', 'Can you please repeat that?', 'What do you do for a living?', 'Hurrah! I won!', 'Stop making such a noise!', 'Walk carefully.', 'Go slow from the crowd.', 'How do you feel?', 'I am very strict on this matter.', 'I am busy at the moment.', 'It has to be done.', 'What is your favorite subject?', 'All my calculations went wrong.', 'Please clean the board.', 'Why are you late?', 'Are you lying?', 'Don’t abuse him.', 'Are the books put in the bag?', 'Mam, I haven’t done my homework.', 'Sorry, for being late.', 'Who is your class teacher?', 'You will not be able to deal with him.', 'Did you get my point?', 'I have a lot to talk about.', 'Please clean the board.', 'Please come as soon as possible.', 'Can you turn the volume up?', 'What do you think?', 'What did you succeed in?', 'Sorry for the inconvenience.', 'Your name is on the list.', 'Not the least!', 'What is going on?', 'The advantages of this are many.', 'it is a lovely day.', 'That’s so kind of you.', 'Where is your office?', 'You’re driving too fast.', 'Have a good weekend.', 'I don’t like long talks.', 'His words have weight.', 'Would you please speak slowly?', 'What are you doing?', 'Rod is the logic of fools.', 'A crease is formed on the cloth.', 'I shall reach by the 5.30 train.', 'What are you doing today?', 'It’s very thoughtful of you.', 'The temperature will come down tomorrow.', 'Have a good trip.', 'Do you understand me?', 'What nonsense!', 'I am going to the playground.', 'It is very hot today. Isn’t it?', 'I want more money.', 'What an idea!', 'Thanks for this honor.', 'No, not at all.', 'go swimming.', 'I need to clean my room.', 'I need to fix my computer.', 'I need to buy some groceries.', 'Can you lend me a hand?', 'Can you help me with this math problem?', 'How’s your day going so far?', 'I’m really proud of you.', 'I’m not feeling well today.', 'I’m so glad to see you!', 'I’ll be there in a few minutes.', 'Let’s have a picnic.', 'Can you pass me the remote?', 'How was your weekend?', 'What’s your favorite hobby?', 'What’s your favorite TV show?', 'take a break.', 'I’m attending a wedding next week.', 'We have backyard BBQs.', 'How do you spell that word?', 'Are you free this weekend?', 'I’m feeling stressed out.', 'Let’s go for a bike ride.', 'I’m taking a cooking class.', 'I am sorry.', 'well done! Keep it up!', 'I did not understand.', 'What do you mean?', 'What are you talking about?', 'I am feeling tired today', 'You very much.', 'What can I do for you?', 'What is happening here?', 'Could you please pass me the salt?', 'Have a great day!', 'You are my reason for living.', 'crying.', 'When is the train leaving?', 'It’s on the tip of my tongue', 'I don’t like tall talk.', 'He will not refrain from speaking.', 'Do as I say.', 'What is your job?', 'My mind is reeling.', 'Did you get my point?', 'Where do you live?', 'I really appreciate it.', 'Would you like a drink?', 'How do you feel about…?', 'I’m returning your call.', 'Can you tell me…?', 'I’ll pay.', 'I don’t want that.', 'How’s work going?', 'Don’t take it personally', 'I hate you!', 'It’s for the best.', 'I talked with him.', 'What is your contact number?', 'What do you want to do?', 'Are you there?', 'Write with an improved hand.', 'What would you like to have?', 'Forget it', 'Who will cooperate with you?', 'It was nice to talk with you.', 'Can you please repeat that?', 'Don’t worry!', 'How are things going?', 'What do we call this in English?', 'This is not a joke.', 'I hope so.', 'I don’t want to.', 'Which date falls on Sunday?', 'I am very pleased to meet you.', 'am feeling tired today.', 'Sorry for the inconvenience.', 'Why are you upset?', 'Good day to you, Sir!', 'Follow me', 'You turn.', 'He owes the shopkeeper fifty rupees.', 'What a bother!', 'Do me a favor.', 'We will break, but not bend.', 'I don’t have a single paisa.', 'Read the sentences carefully.', 'That’s so kind of you.', 'Good heavens!', 'It’s none of your business.', 'I beg your pardon.', 'It’s all yours.', 'How disgraceful!', 'I’m at the office.', 'He had no money.', 'His words have weight.', 'Would you please speak slowly?', 'It’s my pleasure.', 'No, I don’t want it.', 'But he did not budge an inch.', 'Excuse me!', 'Do you understand me?', 'There is something wrong with his brain.', 'You are my responsibility.', 'As you please.', 'Well done, dear!', 'Where are you?', 'How can I go to the town center?', 'He has a nasal accent.', 'Can I ask you something?', 'I’m at home.', 'I’m sorry I can’t assist you.', 'See you next time!', 'Don’t involve me in this matter.', 'Do you agree with me?', 'What’s your e-mail address?', 'Good night!', 'That/He is against me.', 'Have a nice day.', 'I am tired.', 'Believe me.', 'You dance in classes.', 'I go on photo shoots.', 'We explore festivals.', 'They embark on road trips.', 'You ski in winter.', 'I join book clubs.', 'We watch movies.', 'They birdwatch.', 'You volunteer at shelters.', 'shall reach by 5.30 train.', 'What are you doing today?', 'Go up!', 'He has a bad headache.', 'It was nice meeting you.', 'What do you need?', 'His luck took a turn.', 'Get ready to go to school.', 'Could you help me?', 'I just made it', 'My watch is out of order.', 'How are you?', 'Are you done?', 'All worship the rising sun.', 'Stop making so much noise.', 'I don’t have time', 'Hurry up!', 'Is everything OK?', 'What time does the next train leave?', 'He is still not well.', 'What are you up to?', 'I would love to.', 'Fetch water from the well.', 'How can I help you?', 'What are your hobbies?', 'I apologize.', 'It has rained excessively today.', 'Could you give me some money?', 'What’s the weather like?', 'You are going too fast.', 'It’s a good beginning.', 'He / She abused me.', 'Will you now beat him to death?', 'Where did you get it?', 'Speak what is true.', 'I do not want to know anything.', 'Do come!', 'How long will you stay?', 'Please credit this amount to my account.', 'Talk to you later.', 'Rest assured.', 'I cannot agree with your opinions.', 'You have brought me to shame.', 'Well done! Keep it up!', 'Anything else?', 'I don’t agree.', 'What do you want?', 'Please write down this address.', 'Stop kidding.', 'Are you sure?', 'No, I don’t want.', 'It is a strange thing.', 'Could you show me your answer sheet?', 'I’m sorry to interrupt you.', 'Allow me!', 'Will you go there or shall I?', 'I made it.', 'How can I go to the city?', 'All are not like you?', 'Make my apologies.', 'Sorry, I can’t give you a lift.', 'We have lost our way.', 'We disagree about it.', 'My car has broken down.', 'They disappeared quickly.', 'The tire of the car burst.', 'How did you come to school on foot?', 'Hello, how can I help you?', 'Glad to meet you.', 'Did your friend come to school today?', 'All of you please stand up and make a move.', 'Don’t sit idle!', 'How did you come to know?', 'Which side are you on?', 'Take a look at this.', 'I’m quite exhausted today.', 'Do not be childish.', 'It’s not like that.', 'It’s a good thing.', 'It’s your choice.', 'Who called you?', 'May I say something?', 'Who said this?', 'Do it again.', 'Get off the way.', 'Relax!', 'Slow down.', 'What happened?', 'See him off.', 'Not you.', 'He is kind.', 'Pray to God.', 'Don’t worry.', 'I can’t say.', 'What is the time?', 'How much?', 'Absolutely not.', 'I wake up early.', 'We eat breakfast together.', 'They drive to work.', 'You walk to school.', 'I brush my teeth.', 'We cook dinner.', 'They watch TV.', 'You listen to music.', 'I take a shower.', 'We clean the house.', 'They visit their grandparents.', 'You play soccer.', 'I read a book.', 'We go grocery shopping.', 'They go for a walk.', 'You talk to your friend.', 'I water the plants.', 'We go on vacation.', 'They study together.', 'You go to the gym.', 'I cook dinner.', 'We watch a movie.', 'They go to bed.', 'You help your siblings.', 'I go for a run.', 'We go hiking.', 'They go swimming.', 'You meet your friends.', 'I go to the cinema.', 'We have a picnic.', 'I commute by bus.', 'We study together.', 'They play games.', 'You jog in the park.', 'I study at the library.', 'We tidy up.', 'They watch movies.', 'You walk the dog.', 'I practice piano.', 'We ride bikes.', 'They visit museums.', 'You attend yoga.', 'I take photos.', 'We have a BBQ.', 'They attend concerts.', 'You take your kids out.', 'I learn languages.', 'We camp outdoors.', 'They volunteer.', 'You learn cooking.', 'You shop for groceries.', 'I meet friends for lunch.', 'We enjoy sunsets.', 'They hike trails.', 'You attend workshops.', 'We picnic outdoors.', 'They fish at the lake.', 'You meditate.', 'I buy fresh produce.', 'We go on a cruise.', 'They participate in runs.', 'You swim laps.', 'I admire art.', 'We host BBQs.', 'They taste wines.', 'I run marathons.', 'They go wine tasting.', 'You learn dance moves.', 'I go on photo expeditions.', 'We enjoy potlucks.', 'They go on safaris.', 'You learn cooking.', 'I enjoy botanical gardens.', 'We go camping.', 'I take photography classes.', 'We attend festivals.', 'They run for charity.', 'You go swimming.', 'I visit galleries.', 'We have backyard BBQs.', 'How dare you?', 'Let’s catch up!', 'I volunteer at a garden.', 'We organize picnics.', 'They visit art exhibits.', 'You cook new recipes.', 'I visit parks.', 'We host dinner parties.', 'They go on wildlife tours.', 'You practice instruments.', 'I explore new trails.', 'We attend live performances.', 'They engage in outdoor activities.', 'You attend cooking classes.', 'I participate in community events.', 'We plan family outings.', 'They try new hobbies.', 'You relax at home.', 'I attend cultural festivals.', 'We celebrate birthdays.', 'They go on historical tours.', 'You enjoy nature walks.', 'I join fitness classes.', 'We visit local markets.', 'They take leisurely strolls.', 'You attend art workshops.', 'I learn about local history.', 'We have picnics in parks.', 'They go on brewery tours.', 'You practice mindfulness.', 'I explore new neighborhoods.', 'We host game nights.', 'They attend pottery classes.', 'You take part in craft fairs.', 'I explore farmers’ markets.', 'We organize beach outings.', 'They go on city tours.', 'You attend photography workshops.', 'I try new cuisines.', 'have movie marathons.', 'They go on camping trips.', 'I attend music festivals.', 'We enjoy garden walks.', 'They go on ghost tours.', 'You explore countryside trails.', 'I attend wellness retreats.', 'We host barbecues.', 'They go on sightseeing tours.', 'You attend pottery workshops.', 'I explore local landmarks.', 'We organize hiking trips.', 'They go on wine tastings.', 'You practice meditation techniques.', 'I take part in art exhibitions.', 'We enjoy outdoor concerts.', 'They attend food festivals.', 'You explore nature reserves.', 'I attend cooking demonstrations.', 'We go on nature walks.', 'They visit historical landmarks.', 'You attend wellness workshops.', 'I commute by bus.', 'We study together.', 'They play games.', 'You jog in the park.', 'I study at the library.', 'We tidy up.', 'They watch movies.', 'You walk the dog.', 'I practice piano.', 'We ride bikes.', 'They visit museums.', 'You attend yoga.', 'I take photos.', 'We have a BBQ.', 'They attend concerts.', 'You take your kids out.', 'I learn languages.', 'We camp outdoors.', 'They volunteer.', 'You shop for groceries.', 'I meet friends for lunch.', 'We enjoy sunsets.', 'They hike trails.', 'You attend workshops']

def english_to_morse_code(sentence): #Translates the english answer to morse_code
    morse_sentence = ''
    for letter in list(sentence):
        letter = letter.lower()
        if morse_sentence != '':
            morse_sentence = morse_sentence + ' ' + MORSE_CODE_DICT[letter]
        else:
            morse_sentence = MORSE_CODE_DICT[letter]
    return(morse_sentence)

def make_popup(sentence, answer): #Make pop up with tkinter and checks answer
    def check_answer():
        user_answer = entry.get()
        if user_answer.lower() == answer.lower():
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong! The correct answer is: {answer}")
        root.destroy() # Close the quiz after answering

    root = tk.Tk()
    root.title("Daily Morse!")
    root.geometry("400x200")
    label = tk.Label(root, text=sentence, font=("Helvetica", 20))
    label.pack(pady=20)
    entry = tk.Entry(root, font=("Helvetica", 16))
    entry.pack(pady=20)
    button = tk.Button(root, text="Submit", command= check_answer, font=("Helvetica", 16))
    button.pack(pady=20)

    root.mainloop()

def main():
    sentence1, sentence2 = random.choices(sentence_list, k=2)
    # print(sentence1, sentence2)
    ans_1 = english_to_morse_code(sentence1)
    ans_2 = english_to_morse_code(sentence2)
    make_popup(sentence1, ans_1)
    make_popup(ans_2, sentence2)

if __name__ == '__main__': #Lets me use code on startup
    main()

