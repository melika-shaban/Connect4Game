from tkinter import *

#############FILE WRITING AND READING SECTION####################################################


###################################################################### Empty File Function #########################################################################################################
#PURPOSE - empty_file is a function that replaces the contents of a file with nothing ("") by using w (write) mode. The purpose of this function is to be used when a user attempts to save their progress, because then this function is used to first empty the file before the new progress goes in the file to avoir errors and complications.
#PARAMETERS - a text file (should end with .txt) in a string, that will be emptied. For instance, examples in this code include current_player.txt, saved_colours.txt and testing_file_two.txt.
#RETURNS - this function does not actually return anything. It's result will be emptying a text file and leave it with no text inside.
#Example: if i were to give testing_file_three.txt as an argument, it would end up empty, or really if I were to use any file, it would end up empty

def empty_file(file_name):
  with open(file_name, "w") as contents: #opening file in write mode and storing in var contents
    contents.write("") #replacing with empty string (aka nothing)


    ###################################################################### Writing list to file Function #########################################################################################################
    #PURPOSE - writing_list_to_file is a function that will take the contents of a 2D list and write it into another file in the correct format. The purpose of this function is to be used when a user attempts to save their progress, because then this function will write every index of a 2D list (aka another list) in a seperate line of the file, which means it is propery formatted so that later on when the program needs to read the contents of the file, every list item will be on a seperate line. Essentially, it saves the info regarding where pieces are.
    #PARAMETERS - the first parameter is file_name, which is a text file (should end with .txt) in a string, that will be emptied. For instance, examples in this code include current_player.txt, saved_colours.txt and testing_file_two.txt. The second is a list, which in this case should be a 2D list, meaning every list item is also a list. For instance, this includes red_list_pieces and community_gameboard.
  #RETURNS - this function does not actually return anything. It's result will be writing the 2D list contents to a file in the correct format.
#Example: if i were to use "red_saved_file.txt" as they fille name and the list looked like this:

# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 0, 0, 0]

#then the file would contain that exact list but in text form



def writing_list_to_file(file_name, list):
  with open(file_name, "w") as things: #opening in w mode, saving in var things
    for lines in list: #making it so that for every item in the list, it will individually print that item in the file. this makes it so that every list item has its own line in the file.
      print(str(lines), file = things) #printing list item that has been turned to a string, and specifying the file name as things.

###################################################################### Writing into file Function #########################################################################################################
#PURPOSE - writing_into_file is used to save all the information of a current game to files so that later on when the user loads the game, everything can remain the same. For instance, it will store info reagrding whos turn it is, the current colour mode, where both players pieces are, the entire gameboard, and disabled buttonos. It uses the w write mode, as well as other functions like empty_file and writing_list_to_file to facilitate the process.
#PARAMETERS - this function has zero parameters because all the variables it does happen to make use of (such as colour1, current_player_colour, etc) are all globalized. However, it can help to mention that the variables this function does require are red_list_pieces, blue_list_pieces, community_gameboard (all lists), colour1, current_player_colour (these two are strings), button_dict (a dictionary).
#RETURNS - this function does not actually return anything, and instead simply writes the proper info into the other files.
#Example: for examples, if my red_list_pieces, blue_list_pieces, and community_gamebaord all looked like the follows (respectively) then their respective follows would contain the exact same thing in text form
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 0, 1, 1]

# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 1]

# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 0, 0, 1]

# aditionally, if the theme was blue, then the word blue would be saved to the saved_colours.txt, if it was the first players turn, the number 1 would be in the current_player.txt, and since there are no disabled buttons, disabled_buttons.txt would be empty.

def writing_into_file():
  #using the empty_file function to empty every file I need to
  empty_file("red_saved_file.txt")
  empty_file("blue_saved_file.txt")
  empty_file("community_gameboard.txt")
  empty_file("current_player.txt")
  empty_file("saved_colours.txt")
  empty_file("disabled_buttons.txt")
  
  #using the writing list to file function to write the contents of my 3 2D lists (red_list_pieces, blue_list_pieces and community_gameboard) to their respective files.
  writing_list_to_file("red_saved_file.txt", red_list_pieces)
  writing_list_to_file("blue_saved_file.txt", blue_list_pieces)
  writing_list_to_file("community_gameboard.txt", community_gameboard)

  #to identify the current mode, i use an if statent to find out what colour1 currently is. For every mode, colour one has a different value which is why this function is helpful. Then, depending the mode, mode_variable will be assigned with a certain string value representing the colour mode.
  if colour1 == "red":
    mode_variable = "original"
  if colour1 == "white":
    print("hi")
    mode_variable = "blue"
  if colour1 == "#0A3F37":
    mode_variable = "emo"
  if colour1 == "#DB819F":
    mode_variable = "pink"

  #then, the function will write the string representing the saved colour mode (mode_variable) into the saved_colours.txt file.
  with open("saved_colours.txt", "w") as colour_file:
    print(mode_variable, file = colour_file)

  
  #it will then check if the current_player_colour is one of 4 options. it does this because it knows that these are all colours represnting player 1, so if the statement is true then the function can writing the string "1" to the file, but otherwise if it is false, it means it is currently the turn of a player two player, meaning "2" will be written. This is so that later on the program knows who should start when the game is loaded in.
  if current_player_colour == "red" or current_player_colour == "white" or current_player_colour == "#0A3F37" or current_player_colour == "#DB819F": #if current player colour is a player 1 colour
    with open("current_player.txt", "w") as player:
      print("1", file = player) #saves 1 in file to represent player 1

  else:
    with open("current_player.txt", "w") as player:
      print("2", file = player) #otherwise a 2 is saved for player 2

  with open("disabled_buttons.txt", "w") as disabled_buttons:
    for ints in range(0,7): #loops seven times
      if button_dict[ints]["state"] == DISABLED : #it uses the different integers in the loop above as keys in the button_dict dictionary to identify that if the button the key is representing is disabled, it will add the integer number to another file
        print(ints, file = disabled_buttons) #writes integer number to a file so that when the game is loaded later the same buttons can be disabled

###################################################################### Loading saved file Function #########################################################################################################
#PURPOSE - loading saved file is a function that will take the contents of a file (that should be containing a 2D list in text form) and turn in to an actual list in proper format by turning the strings to integers, removing new line characters, etc. It is important so that when the user attempts to load a saved game, the program can use the contents of a file to identify what has been saved.
#PARAMETERS - a text file (should end with .txt) in a string, that will be emptied. For instance, examples in this code include current_player.txt, saved_colours.txt and testing_file_two.txt.
#RETURNS - this function will return the 2D list that was in the file_name file in text form as a real 2D list. It should be a list with 6 list items that each contain 7 integers.
#Examples: If a file contained the following, this function would mmake it seem the exact samme, with the difference being that its actually a list
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 0, 0, 0]
      
def loading_saved_file(file_name):
  with open(file_name, "r+") as saved_file: #opening in r+ mode in saved_file var
    
    saved_list = saved_file.readlines() #making every line a list item, saving list to saved_list
    
    for items in saved_list:
      
      index = saved_list.index(items) #saved index of list item in index var
      
      saved_list[index] = items.replace('[', '').replace('],', '').replace(']', '').replace('\n', '') #replaces every list item with another string that no longer has the square brackets, commas or \n character, by using the replace method and replacing those characters with nothing ('')
      
      saved_list[index] = saved_list[index].split(",") #splitting every item of the list to become its own list, to turn it back into a 2d list
      
      for numbers in saved_list[index]:
        index_of_number = saved_list[index].index(numbers) #saving index once again in a variable
        saved_list[index][index_of_number] = int(saved_list[index][index_of_number]) #replacing the items in the lists (that are in the inital list) with an integer version as that is how its supposed to be formatted
  return saved_list 
  #returning that list

###################################################################### loaded game creator Function #########################################################################################################
#PURPOSE - loaded game creator is the function that will take the info saved in the various files and actually recreate the saved game. for instnace, some responsibilities include re assiging the colour variables with the right colours, putting the pieces in the right spot and displaying whos turn it is.
#PARAMETERS - a text file does not take any parameters. everything it uses is the info saved in the files.
#RETURNS - this function does not actually return anything. However, it does make all the graphics, re-update the lists that track where the players pieces are, and do other very important things like that.
#Example
#if disabled button txt has the number 1 in it, theme had "pink", current_player has 2, then this function would make the 2nd button disabled (index values), the theme would be pink, it would display that its the second players turn, and if the files red_saved_fillle, blue_saved_file and community_gameboardcontained the following text, it would turn the three into actual lists (stored in red_list_pieces, blue_list_pieces and community_gameboard)

# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 0, 1, 1]

# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 1]

# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [1, 0, 0, 0, 0, 0, 1]


def loaded_game_creator():
  global red_list_pieces, blue_list_pieces, community_gameboard, game_mode, current_player_colour, player_turn_title #globalizing variables

  # player_turn_title.destroy()
  
  with open("saved_colours.txt", "r") as colour_mode:
    saved_mode = colour_mode.read() #saving contents of file as a string in saved_mode var
    saved_mode = saved_mode.strip("\n") #removing newline character

  if saved_mode.isspace(): #checking if there is only whitespace
    no_saved_game_error_message() #if there is solely whitespace, the function calls on another function to tell the user there is no game saved, because if there was then there would be something saved in the saved_mode variable
    return None #stops function from running

  colour_assigner(saved_mode) #now that it knows the variable it uses the colour_assigner to assign the colour variables with the appropraite values depending on the mode.

  game_mode = "saved" #changes gamemode to saved so that whne the game_setup function is called, it does not create new empty 2D lists or re print the title representing whos turn it is.

  game_setup() #sets up game, buttons, etc

  with open("disabled_buttons.txt", "r") as disabled_buttons:
    buttons = disabled_buttons.readlines() #saves every line as an item in the list buttons
    for items in buttons:
      index_var = buttons.index(items) #saves index
      buttons[index_var] = int(items.strip("\n")) #makes button an integer and removes newline
    for integers in buttons:
      button_dict[integers]["state"] = DISABLED #will use the numbers that were saved in the file as a key for a ditionary to identify the button that needs to be disabled.


  with open("current_player.txt", "r") as player_turn:
    player = player_turn.read() #saving string to player var
    player = player.strip("\n") #striping of newline

  if player == "1": #if it is the first players turn
    current_player_colour = colour1 #piece colour will be first players
    player_turn_title = Label(game_page, text = "Player 1's turn", font = ("Courier", 35), bg = bg_colour, fg = button_colour) #title will update to display that it is the first players turn
    player_turn_title.pack()
    player_turn_title.place(x = 35, y = 20, anchor= "nw")
  else:
    current_player_colour = colour2 #otherwise instead it will be the second players colour and it will display that it is their turn
    player_turn_title = Label(game_page, text = "Player 2's turn", font = ("Courier", 35), bg = bg_colour, fg = button_colour)
    player_turn_title.pack()
    player_turn_title.place(x = 35, y = 20, anchor= "nw")

  

  
  #uses loading saved file to turn contents of red saved file txt to an actual 2D list.
  red_list_pieces = loading_saved_file("red_saved_file.txt")
  row_counter = 0 
  column_counter = 0
  for rows in red_list_pieces: #essentially, it usess variables representing the row and column to loop through every row in the list, and then for every row it will loop through every column so that every piece is checked
    for column in rows:
      if column == 1: #checks if list item is a one, which represents a piece
        
        piece_canvas.create_oval(list_of_coords[row_counter][column_counter], fill = colour1) #if there is a piece, since the function is aware of the column and row, it can use them with list of coords to find the coords and make the piece appear on the screen. since it has already found out which players turn it is, it will make the colour that players colour 
        
      column_counter += 1 #counters increase when appropriate
    column_counter = 0
    row_counter += 1

  #same as previous bit of code; checks through blue list pieces 2D list for instances of a one, meaning a piece is placed there, and if there is it uses the row and column variables to find the coordinates and make the piece appear with the right colours
  blue_list_pieces = loading_saved_file("blue_saved_file.txt")
  row_counter = 0
  column_counter = 0
  for rows in blue_list_pieces: #looping through
    for column in rows:
      if column == 1: 

        piece_canvas.create_oval(list_of_coords[row_counter][column_counter], fill = colour2) #making circles

      column_counter += 1
    column_counter = 0
    row_counter += 1
  
    
  community_gameboard = loading_saved_file("community_gameboard.txt") #assigns community_gameboard with the 2D list previously stored in communtiy gameboard. txtt

  game_mode = "unsaved" #finally, changes game_mode so that if the user were to play again, and the game setup functino is called, it does infact reset the 2D lists and make a new title.

  




###################################################################### no saved game error message function
#########################################################################################################
#PURPOSE - no saved game error messsage is a function that will display an error message telling a user that there is no saved game, and allows them to return back to the settings page. it is used when a user attempts to load a saved game, but there is nothing saved. technically, this function is only called when the files are manually emptied, or the first time the code is used (because i made sure to empty them.)
#PARAMETERS - this function has no parameters as all it actually does it display visuals.
#RETURNS - this function does not actually return anything. However, it should result in a window with thte error message and a button to return back.
#Example: if this function is called a window would appear with an error message and close button options.


def no_saved_game_error_message():
  global game_page

  try: #to minimize the amount of windows to 1, essentially anytime a function that makes a new window it called, it first attempts to destroy any previous windows, and uses a try and accept so if there aren't any there are no problems. it works because every window in named the same things so that it can always be deleted, and this causes no problems because once a user creates the new window they have no reason for the old one.
    game_page.destroy()
  except:
    pass

  game_page = Tk() #making window, determining size, colour, etc

  game_page.geometry("750x300")

  game_page.configure(bg = bg_colour)

  #making error title that lets user know what happened
  error_title = Label(game_page, text = "There is no saved game.", font = ("Courier", 35), bg = bg_colour, fg = button_colour) #creating label object of labe lclass with the appropraite window, text and colours and adding it to the screen
  error_title.pack()
  error_title.place(x = 375, y = 50, anchor= "center")

  #this button has the command of the settings page so that the user can return back after they have read the message

  go_to_home_button = Button(game_page, text = "Close", font = ("Courier", 30), bg = button_colour, fg = font_colour, command = settings_page) #makingg button object in rigbt window, with right text, colours, etc 
  go_to_home_button.pack()
  go_to_home_button.place(x= 375, y = 150, anchor = "center")





###################################visuals / piece section#################



###################################################################### make window Function #########################################################################################################
#PURPOSE - make window is a function that simply makes a window and canvas to go on top of it. it is used in other windows that display visuals as an easy way to already create the window with the right size and canvas already created on it. it is helpful because since the canvs is already made, its simple to create other canvas circles and whatnot.
#PARAMETERS - once again, this function does not have any parameters because it simply creates a window.
#RETURNS - this function does not actually return anything. But, it should result in a tkinter window, with a canvas on top of it coloured the colour stored in bg_colour, and it is supposed to be the same dimensions of the window.
#Example: if this function is called and the theme is pink, a big pink window would appear

def make_window():
  global piece_canvas, game_page

  try:
    game_page.destroy() #once again gets rid of previous windows so that theres only one at a time
  except:
    pass
    
  game_page = Tk() #making window, determining size, etc

  game_page.geometry("750x650")


  # makes canvas object in correct window, with the right coour and size
  piece_canvas = Canvas(game_page, bg = bg_colour, width = 750, height = 650)

  #places canvas at proper coords with right anchor (north west)
  piece_canvas.place  (x = 0, y = 0, anchor = "nw")

###################################################################### winner Function #########################################################################################################
#PURPOSE - winer is a function that shows up when a player wins or draws. It should display who won, or if there was a draw, and additionaly create a button that allows the user to return home.
#PARAMETERS - optional is a parameter that can technially be anything. It's sole purpose is so that when there is a draw and a function is called, the program can detect that it is a draw by using a conditional to check what the value of draw is. When there is a draw, optional should be the string "Draw", however, in any other instance as long as the argument is anything other than draw, the program should print the winner instead as it will run the code in the else block. 
#RETURNS - this function does not actually return anything. It's result will be a window with text at the top, either saying who won or if there was a draw, and it should also create a button that can take the user back home.
#Example: if this function is called with the argument "Draw", the the final page would display that it was a draw and there would be a button for the user to return home. If player 1 had gotten four in a row though, then it would display that player 1 won and there would still be a button to return home.

def winner(optional):
  global game_page, champion #(champion is globailzed for testing puposes later)


  try: #once again gets rid of previous windows so that theres only one at a time
    game_page.destroy()
  except:
    pass

  game_page = Tk() #making window, determining size, colour, etc

  game_page.geometry("750x300")

  game_page.configure(bg = bg_colour)


  if optional == "Draw": #checks if the optional argument is draw, meaning that it should display the draw message
    draw_title = Label(game_page, text = "Draw!", font = ("Courier", 35), bg = bg_colour, fg = button_colour) #label object in proper window, right text, colours, etc
    draw_title.pack()
    draw_title.place(x = 375, y = 50, anchor= "center")

  else: #if optional is anything but Draw, then it means that the function was called because a player won!

    if current_player_colour == colour1: #it first checks if the current_player_colour variables's value is equal to colour 1 or 2, so that it can identify if it was player ones turn when they won (represented by colour1) or vice versa.
      champion = "Player 1"
    else:
      champion = "Player 2"

    #it then creates a label displaying the winner
    winner_title = Label(game_page, text = f"{champion} won!", font = ("Courier", 35), bg = bg_colour, fg = button_colour) #window, text, font, and colour parameters
    winner_title.pack()
    winner_title.place(x = 375, y = 50, anchor= "center") #placed at proper coords with center anchor

  #this button is made regardless so that the user knows 
  home_button = Button(game_page, text = "Back to home page", font = ("Courier", 30), bg = button_colour, fg = font_colour, command = lambda: home_page(bg_colour, piece_colour, button_colour, font_colour, title_colour, colour1, colour2)) #specifies colours, command, etc
  home_button.pack()
  home_button.place(x= 375, y = 150, anchor = "center") #placed at proper coords with center anchor

  
###################################################################### colour window Function #########################################################################################################
#PURPOSE - colour window is a function that creates the window that a user sees when they go to settings and select the colour mode, as it creates all the various buttons that allows users to pick between the modes.
#PARAMETERS - this function takes no parameters. It does made use of other global variables though, including bg_clour and font_colour so that it can add the correct colours.
#RETURNS - this function does not actually return anything. It's result will be a window with a title and four button options; blue, pink, original and emo mode. There will also be an aditional button that allows the user to return to the home page.
#Example: if the user selected the emo mode, then once they clicked the back button and returned home, everything would be dark
  
def colour_window():
  global game_page
  
  try: #again, if it exists, it attemptps to delete the previous window, otherwise the except catches the error
    game_page.destroy()
  except:
    pass

  game_page = Tk() #making window object with right size and colour

  game_page.geometry("750x300")

  game_page.configure(bg = bg_colour)

  #first a title is made with the label class, which simply says colour mode to explain what the window is for
  colour_title = Label(game_page, text = "Colour mode", font = ("Courier", 35), bg = bg_colour, fg = button_colour)
  colour_title.pack()
  colour_title.place(x = 375, y = 50, anchor= "center")

  #the original mode will call on the colour_assigner with the argument "original" so that the colour variables will then be assigned with values representing this mode.
  original_button = Button(game_page, text = "Original mode", font = ("Courier", 15), bg = button_colour, fg = font_colour, command = lambda: colour_assigner("original"))
  original_button.pack()
  original_button.place(x= 375, y = 100, anchor = "center")

   #the pink mode will call on the colour_assigner with the argument "pink" so that the colour variables will then be assigned with values representing this mode.
  pink_button = Button(game_page, text = "Pink mode", font = ("Courier", 15), bg = button_colour, fg = font_colour, command = lambda: colour_assigner("pink"))
  pink_button.pack()
  pink_button.place(x= 375, y = 140, anchor = "center")

   #the blue mode will call on the colour_assigner with the argument "blue" so that the colour variables will then be assigned with values representing this mode.
  blue_button = Button(game_page, text = "Blue mode", font = ("Courier", 15), bg = button_colour, fg = font_colour, command = lambda: colour_assigner("blue"))
  blue_button.pack()
  blue_button.place(x= 375, y = 180, anchor = "center")

   #the emo mode will call on the colour_assigner with the argument "emo" so that the colour variables will then be assigned with values representing this mode. personally, this is my favourite (or maybe the pink one)
  
  emo_button = Button(game_page, text = "Emo mode", font = ("Courier", 15), bg = button_colour, fg = font_colour, command = lambda: colour_assigner("emo"))
  emo_button.pack()
  emo_button.place(x= 375, y = 220, anchor = "center")

  back_button = Button(game_page, text = "Back", font = ("Courier", 15), bg = button_colour, fg = font_colour, command = lambda: home_page(bg_colour, piece_colour, button_colour, font_colour, title_colour, colour1, colour2))
  back_button.pack()
  back_button.place(x= 375, y = 260, anchor = "center")

###################################################################### colour assigner Function #########################################################################################################
#PURPOSE - colour assigner is a function that will assign various variables used for colour, including bg_colour, piece_colour, button_colour, etc, with the correct colour name or code in regards to the theme they pick. It's helpful because then if the user selects a theme, my program can make everything in the game, such as any windows, buttons, labels, etc, follow the colour mode as they all mmake use of the same variables. 
#PARAMETERS - a string represting the colour mode the user wants. The sole purpose is to be used with an if conditional to determine which colours the variabels should be assigned. For example, the options should be either "pink", "original", "emo" and "blue"
#RETURNS - this function does not actually return anything. It's result will be emptying a text file and leave it with no text inside.
#Example: if this function is called the argument "pink", then the following variables would be assigned with these values:
# bg_colour = "pink"
# piece_colour = "pink"
# button_colour = "#F389AD"
# font_colour = "white"
# title_colour = "#F389AD"
# colour1 = "#DB819F"
# colour2 = "#E0BDE6"
# current_player_colour = colour1

def colour_assigner(theme):
  global bg_colour, piece_colour, button_colour, font_colour, title_colour, colour1, colour2, current_player_colour #globalizing all the colour variables to be used with other functions
  
  if theme == "pink": #if the argument was pink all the variables will be given the correct string value for the graphics to follow the pink theme
    bg_colour = "pink"
    piece_colour = "pink"
    button_colour = "#F389AD"
    font_colour = "white"
    title_colour = "#F389AD"
    colour1 = "#DB819F"
    colour2 = "#E0BDE6"
    current_player_colour = colour1
  
  if theme == "original": #if the argument was original all the variables will be given the correct string value for the graphics to follow the original theme
    bg_colour = "blue"
    piece_colour = "black"
    button_colour = "white"
    font_colour = "black"
    title_colour = "white"
    colour1 = "red"
    colour2 = "yellow"
    current_player_colour = colour1
    
  if theme == "emo": #if the argument was emo all the variables will be given the correct string value for the graphics to follow the emo theme
    bg_colour = "black"
    piece_colour = "gray"
    button_colour = "gray"
    font_colour = "white"
    title_colour = "gray"
    colour1 = "#0A3F37"
    colour2 = "#014275"
    current_player_colour = colour1
    
  if theme == "blue": #if the argument was blue all the variables will be given the correct string value for the graphics to follow the blue theme
    bg_colour = "white"
    piece_colour = "#1E88E5"
    button_colour = "#90CAF9"
    font_colour = "white"
    title_colour = "#90CAF9"
    colour1 = "white"
    colour2 = "#90CAF9"
    current_player_colour = colour1


  ###################################################################### home page Function #########################################################################################################
  #PURPOSE - home page is a function that will make the home page everytime it is called. this function is extremely important because the home page is what helps the user navigate and find the rest of the code, for instance, to acces any settings features, they must first be on the home able to be able to access the settings button. or, they must click the start button to start a new connect 4 game.
  #PARAMETERS - this function takes a total of seven parameters. each one is simply a string reprenting a colour, for example it can be a colour name like "red", "blue", etc, or a hex code. the reason the function actually takes colour parameters wheras everything else simply works with colour variabes is because this funtion is how the game actually starts, as it needs to be called to load everything else, therefore there are parameters so that the first time the game runs, it can use the argument colours, but after that everytime it is called it works with variables.
  #RETURNS - this function does not actually return anything. It's result will be a window with a title welcoming the user to connect 4, a start button to start a new game and load that screen, and a settings button for the user to access the various options in settings.
#Example: this function will create the same things every single time. Although I can't really give an "example", i can say that when it is called a window with a welcome title, start button, and settings button appears. If the user were to select start it would start a brand new connect 4 game, and if they selected settings it would take them to the settings window.

def home_page(bg, piece, button, font, title, first_col, second_col):
  global game_page, bg_colour, piece_canvas, piece_colour, button_colour, font_colour, title_colour, colour1, colour2, current_player_colour, game_mode #again, the reason why this functions globalizes all these variables is because since everything else works with colour variables, when the game the game first begins there are still colours that can be used

  
  try: #attempting to get rid of previous window (even though this is the first function needed to start the game, i still destroy older windows because if it is called again than it needs to get rid of old ones)
    game_page.destroy()
  except:
    pass

  game_mode = "not_saved" #changes game mode to not saved in case for same reason it was not changed back after the old game has been loaded in
  
  bg_colour = bg #assiging all the colours to variables
  piece_colour = piece
  button_colour = button
  font_colour = font
  title_colour = title
  colour1 = first_col
  colour2 = second_col
  current_player_colour = colour1
  
  game_page = Tk() #making window, determining size and colour

  game_page.geometry("750x300")

  game_page.configure(bg = bg_colour)

  #title welcoming user to conect 4 with appropraite font sizes, coordinates, etc
  title = Label(game_page, text = "Welcome to Connect Four!", font = ("Courier", 35), bg = bg_colour, fg = button_colour)
  title.pack()
  title.place(x = 375, y = 50, anchor= "center")

  #start button that calls game_setup to set up the screen for a new game, coordinates place this button in the middle of the window
  start_button = Button(game_page, text = "Start", font = ("Courier", 50), bg = button_colour, fg = font_colour, command = game_setup)
  start_button.pack()
  start_button.place(x= 375, y = 150, anchor = "center")

  #settings button that calls the settings page comand to create the settings window with its various options (colour and load saved game), coords allow this button to be at the bottom the screen
  settings_button = Button(game_page, text = "Settings", font = ("Courier", 20), bg = button_colour, fg = font_colour, command = settings_page)
  settings_button.pack()
  settings_button.place(x= 375, y = 250, anchor = "center")


###################################################################### settings page Function #########################################################################################################
#PURPOSE - settings page is a function that will make the settings page everytime it is called. it allows the user to click the button that will load a previous game, or the button that will take the user to the colour window
#PARAMETERS - this function takes no parameters.
#RETURNS - this function does not actually return anything. It's result will be a window with a title labelling the window as the settings page and two buttons (load saved game and colours).
#Example: if the user selects the colour option, it would direct them to the colours page. If they select the load saved game, it would attempt to load the game, but if not it would bring up the error screen. hitting the back button takes the user back to the previous page.

def settings_page(): 
  global game_page
  
  try: #attempting to destroy previous windows
    game_page.destroy()
  except:
    pass

  game_page = Tk() #making window, with appropraite size and colours

  game_page.geometry("750x300")


  game_page.configure(bg = bg_colour)

  #making label obejct for window title, with proper text, font, colour, coordinates, etc
  settings_title = Label(game_page, text = "Settings", font = ("Courier", 30), bg = bg_colour, fg = button_colour)
  settings_title.pack()
  settings_title.place(x = 375, y = 50, anchor= "center")

  #back button at the button of the screen that allows the use to return to the home page by calling the home page functoin
  back_button = Button(game_page, text = "Back", font = ("Courier", 15), bg = button_colour, fg = font_colour, command = lambda: home_page(bg_colour, piece_colour, button_colour, font_colour, title_colour, colour1, colour2))
  back_button.pack()
  back_button.place(x= 375, y = 250, anchor = "center")

  #colour option button calls on the colour window function to create thw window so that the user can select the mode they like
  colour_option_button = Button(game_page, text = "Colours", font = ("Courier", 15), bg = button_colour, fg = font_colour, command = colour_window)
  colour_option_button.pack()
  colour_option_button.place(x= 375, y = 190, anchor = "center")

  #load saved game will call on the loaded game creator function that once again will access all the info in the various .txt files and load the game
  load_saved_game = Button(game_page, text = "Load saved game", font = ("Courier", 15), bg = button_colour, fg = font_colour, command = loaded_game_creator)
  load_saved_game.pack()
  load_saved_game.place(x= 375, y = 130, anchor = "center")

###################################################################### List of coords
#########################################################################################################

#list of coords is not a function, but instead a list. it is extremely useful as it can work perfectly with the other 2D lists. Essentially, every row in my connect 4 game is represented by an item or list in the inital list, and then every list in that list has 4 coordinates represting where the circle pieces for my game should go. It is extremely useful because it is formatted the same way as the other 2D lists, therefore the index values to access any item in those lists can be used with this list to obtain the exact coordinates of that spot. The coordinates are odd, but essentially the first of is the x coordinate of the top left corner, the second one is the y of the top left corner, the third one is the x of the bottom right corners, and the last is the y of the bottom right corner. 

#ps. i actually first had placed 42 individual tkinter canvas ovals to know exactly where each circles needs to go. then, after i just put all the coordinates into a list and loop through it to create the inital circles when the game first starts. 


list_of_coords = [[[35, 80, 100, 145],
  [135, 80, 200, 145],
  [235, 80, 300, 145],
  [335, 80, 400, 145],
  [435, 80, 500, 145],
  [535, 80, 600, 145],
  [635, 80, 700, 145]],

  [[35, 175, 100, 240],
  [135, 175, 200, 240],
  [235, 175, 300, 240],
  [335, 175, 400, 240],
  [435, 175, 500, 240],
  [535, 175, 600, 240],
  [635, 175, 700, 240]],

  [[35, 270, 100, 335],
  [135, 270, 200, 335],
  [235, 270, 300, 335],
  [335, 270, 400, 335],
  [435, 270, 500, 335],
  [535, 270, 600, 335],
  [635, 270, 700, 335]],

  [[35, 365, 100, 430],
  [135, 365, 200, 430],
  [235, 365, 300, 430],
  [335, 365, 400, 430],
  [435, 365, 500, 430],
  [535, 365, 600, 430],
  [635, 365, 700, 430]],

  [[35, 460, 100, 525],
  [135, 460, 200, 525],
  [235, 460, 300, 525],
  [335, 460, 400, 525],
  [435, 460, 500, 525],
  [535, 460, 600, 525],
  [635, 460, 700, 525]],

  [[35, 555, 100, 620],
  [135, 555, 200, 620],
  [235, 555, 300, 620],
  [335, 555, 400, 620],
  [435, 555, 500, 620],
  [535, 555, 600, 620],
  [635, 555, 700, 620]]]


#The class piece is extremely important and essentially, it can find exactly where a piece needs to go simply by knowing the column. it is extremelt useful because it also creates colour, row and column attributes. this way, when an obejct is created, later on i simply have to use a conditional to figure out its colour to identify which list to add the piece in, and the row and column are also extremely useful because then i am able to access the coordinates of every piece with the list_of_coords list, and then make that an attribtue also.

class piece_class:
  def __init__(self, colour, column): #all objects created in the piece class require a specified colour and column
    global row #row is gloablized to be used later on
    self.colour = colour #colour attribute is simply the specified colour
    z = 1 #z and counter both keep track of the row were
    counter = 5
    for x in community_gameboard: #looping through the the rows in the gammeboard
      if community_gameboard[-z][column] == 1: #if the last index of a row list (hence the -z) is one, that means there is a piece there. it starts at the 5th row (counter starts at five) because the pieces always fall to the bottom first
        pass
      else: #it knowss that if there is in fact NOT a piece at the row it just checked, that means it's an empty space and the piece can fall there
        row = counter - (z-1) #the row is saved in the row variables  by subtracting z - 1 because z is the row variable, but since we went backwards, we need to subtract 1 from z and then subtract that from counter, because if counter was 5, then because a list index starts a 0, meaning if we were to subtract z from counter, than we would only be accesing the fouth row, therefore subtracting 1 would turn z into 0, meaning we would be accesing the 6th row, represented by the 5th index. 
        break
      z += 1
      counter - 1 #otherwise counters are changed
    self.row = row #row and column attributes made
    self.column = column
    self.coordinates = list_of_coords[row][column] #using the identified row and columbs, coordinates are also made an attribute


    ###################################################################### game_setup Function #########################################################################################################
    #PURPOSE - game setup is a function that will recreate the game board everytime it is called. it is used both when loading in a saved game or when the start button is clicked to start a new game. It will create all 42 empty game spots, all the buttons to place pieces, the as well as the home and saved progress butons. What's also nice is that depending on whether or not the function is being used to load in a previous game or not, it will use a conditional with the game_mode variable, and if the mode is not in saved mode, it will also make new empty 2D lists with only zeros and also the title representing that layer one should begin.
    #PARAMETERS - once again, this function does not take any parameters. in fact, for the most part it simply makes new things.
    #RETURNS - this function does not actually return anything. that said, it results in a window with 42 spots for pieces to be placed (they may be filled if the function is used to load a new game), 7 click here buttons to place pieces, and a home and saved progress button. Once again, depending on the game mode, there may also be a title determining whos turn it is.
#Example: if this function is called and game mode is NOT saved, then it would make a new window with 42 circles representing the spots, 7 buttons to place pieces, a title at the top saying its player 1s turn, 3 new 2D grids (both players and the community one) and then two buttons in the top right corner. Clicking the home one will take you home and the save progress will save the progress.

def game_setup():
  global player_turn_title, community_gameboard, red_list_pieces, blue_list_pieces
  try:
    game_page.destroy() #destroying old window if possible
  except:
    pass
    
  make_window()

  if game_mode != "saved": #if the game mode is not saved, meaning if the program isn't currently loading in an old gamem, new gameboards and a new player title is made because the game is starting over a player 1 always starts.
    community_gameboard = [[0,0,0,0,0,0,0], #empty community gameboard
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0]]

    red_list_pieces = [[0,0,0,0,0,0,0], #empty first player board
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0]]

    blue_list_pieces = [[0,0,0,0,0,0,0], #empty second player board
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0]]

    #player turn title is made to display that its player ones turn
    player_turn_title = Label(game_page, text = "Player 1's turn", font = ("Courier", 35), bg = bg_colour, fg = button_colour)
    player_turn_title.pack()
    player_turn_title.place(x = 35, y = 20, anchor= "nw")

  #loopping through the list of coords so that for every coordinate in the list, a new circle piece is made. these represent the empty spots on the board that the player can place their piece in
  for x in list_of_coords:
    for i in x: #for the items in the row lists in the coordinate list
      piece_canvas.create_oval(i, fill = piece_colour) #i make a circle with the coordinates and with the piece_colour colour var.


      
  button_maker() #button maker is called to create all the buttons


  #homme page button is made with the command to take the user back to the home page
  second_button = Button(game_page, text = "Back to home", fg = font_colour, font = ("Courier", 12), width = 14, bg = button_colour, command = lambda: home_page(bg_colour, piece_colour, button_colour, font_colour,  title_colour, colour1, colour2))
  second_button.pack()
  second_button.place(x = 500, y = 9, anchor = "nw")

  #the save progress button allows the user to save all their progress into files using the writing_into_file function
  third_button = Button(game_page, text = "Save progress", fg = font_colour, font = ("Courier", 12), width = 14, bg = button_colour, command = writing_into_file)
  third_button.pack()
  third_button.place(x = 500, y = 41, anchor = "nw")

  
  ###################################################################### button maker Function #########################################################################################################
  #PURPOSE - button maker function is a function that will make the buttons for the user to place their pieces. It is easy to use in other functions like game setup, so that all seven buttons can immediately apear. It also creates a dictionary which is useful because then every button can have an integer representing it, which makes it easy when disabling buttons as they can be accessed through a key.
  #PARAMETERS - button maker does not have any parameters.
  #RETURNS - this function does not actually return anything. It's result will be seven buttons lined up on the bottom of the window horizontally, and also a dictionary. the result of the buttons will be a piece that is played.
#Example: This function will simply do the same thing every time, therefore I cannot really give an example (it will just make the buttons)

def button_maker():
  global button_dict, first_button, second_button, third_button, fourth_button, fifth_button, sixth_button, seventh_button

  #the following buttons are all placed along the bottom of the screen, with the only difference being that they are placed at different spots and that the playing_function is called with a specific integer argument to represent a certain column in the gameboard

  #first button
  first_button = Button(game_page, text = "Click", height = 1, width = 5, bg = button_colour, fg = font_colour, font = ("Courier", 9), command = lambda: playing_function(0))
  first_button.pack()
  first_button.place(x = 35, y = 620, anchor = "nw")


  #second button
  second_button = Button(game_page, text = "Click", height = 1, width = 5, bg = button_colour, fg = font_colour, font = ("Courier", 9), command = lambda: playing_function(1))
  second_button.pack()
  second_button.place(x = 135, y = 620, anchor = "nw")

  #third button
  third_button = Button(game_page, text = "Click", height = 1, width = 5, bg = button_colour, fg = font_colour, font = ("Courier", 9), command = lambda: playing_function(2))
  third_button.pack()
  third_button.place(x = 235, y = 620, anchor = "nw")

  #fouth button
  fourth_button = Button(game_page, text = "Click", height = 1, width = 5, bg = button_colour, fg = font_colour, font = ("Courier", 9), command = lambda: playing_function(3))
  fourth_button.pack()
  fourth_button.place(x = 335, y = 620, anchor = "nw")

  #fifth button
  fifth_button = Button(game_page, text = "Click", height = 1, width = 5, bg = button_colour, fg = font_colour, font = ("Courier", 9), command = lambda: playing_function(4))
  fifth_button.pack()
  fifth_button.place(x = 435, y = 620, anchor = "nw")

  #sixth button
  sixth_button = Button(game_page, text = "Click", height = 1, width = 5, bg = button_colour, fg = font_colour, font = ("Courier", 9), command = lambda: playing_function(5))
  sixth_button.pack()
  sixth_button.place(x = 535, y = 620, anchor = "nw")

  #seventh button
  seventh_button = Button(game_page, text = "Click", height = 1, width = 5, bg = button_colour, fg = font_colour, font = ("Courier", 9), command = lambda: playing_function(6))
  seventh_button.pack()
  seventh_button.place(x = 635, y = 620, anchor = "nw")

  #button dictionary that pairs every button with an integer key
  button_dict = {0 : first_button, 1: second_button, 2 : third_button, 3 : fourth_button, 4: fifth_button, 5 : sixth_button, 6: seventh_button}


###################################################################### playing function Function #########################################################################################################
#PURPOSE - playing function is a function that pretty much keeps the game moving when two players are playing. It is called everytime a button to place a piece is clicked, and to sum things up, it determines where the button needs to fall, will update the 2D lists, will visually show where the piece has fallen, and will also update colours, disable buttons if they can no longer be used, check for wins and additionally update the title that states whos turn it is.
#PARAMETERS - the only parameter this function takes in column, which is an integer representing which column the piece is supposed to go in. Essentially, depending on which button is click, the function will use the parameter to determine which column the piece is going in, and then use the 2D lists to identify what the closest empty spot to the bottom row is (using the piece class) and placed it there.
#RETURNS - this function does not actually return anything. However, it does make a lot of visual changes to the board, including a new piece, possibly displaying the win window or draw window, changing whos turn it is, etc. It also updates the 2D lists. 
#Examples: If the user gets for in a row they will be directed to the win page
#If the users fill the entire board there will be a draw page
# If one user plays regularly then the function will make sure to swtich whos turn it is, update the 2D lists and disable buttons if neccesary
#For more detail i recommend reading the testing file.

def playing_function(column):
  global red_list_pieces, blue_list_pieces, community_gameboard, current_player_colour, player_turn_title

  player_turn_title.destroy() #destroys the previous player title so that it doesn't overlap with the new one
  
  playing_piece = piece_class(current_player_colour, column) #makes a piece calss object with the currennt colour and column based on the button the user clicked

  community_gameboard[playing_piece.row][playing_piece.column] = 1 #replaced the communtiy gameboard spot with a 1 to represent a filled piece

  piece_canvas.create_oval(playing_piece.coordinates, fill = current_player_colour) #creates a circle at the coordinates that the piece class has identified

  #if the current player colour is one, then it will add the piece to the first players list, and other wise it will go to the second players list
  if current_player_colour == colour1:
    red_list_pieces[playing_piece.row][playing_piece.column] = 1
  else:
    blue_list_pieces[playing_piece.row][playing_piece.column] = 1


  #if there are no spots left at the top row (aka row 0 as the specific column specified), it also knows that the button is disabled.
  if community_gameboard[0][column] == 1:
    button_dict[column]["state"] = DISABLED

    #if will then check if all the buttons are disabled, and if they are it will call the winner function with a draw argument to display that there has been a draw (checks with if statement)
    if first_button["state"] == DISABLED and second_button["state"] == DISABLED and third_button["state"] == DISABLED and fourth_button["state"] == DISABLED and fifth_button["state"] == DISABLED and sixth_button["state"] == DISABLED and seventh_button["state"] == DISABLED:
      winner("Draw") #calls winner function with "draw"
      return None #ends function

  if current_player_colour == colour1: #check whos turn it in (by checking if current player colour's value is currently colour 1 or colour 2), and then depending on that will it will assign the player turn function with a string displaying whos turn it is
    player_turn = "Player 2's turn"
  else:
    player_turn = "Player 1's turn"

  #makes a title that will display whoevers turnn it is, by using the previous_turn variable to display the player
  player_turn_title = Label(game_page, text = player_turn, font = ("Courier", 35), bg = bg_colour, fg = title_colour)
  player_turn_title.pack()
  player_turn_title.place(x = 35, y = 20, anchor= "nw")

  #then, it calls the win checkers function with both player 2D lists to check if ther has been a winner, and uses an if to see if it returns true or not
  if win_checker(red_list_pieces) or win_checker(blue_list_pieces):
    winner("na") #if it is true, it calls winner with a random string argument, because the argument simply has to be anything other than Draw so that it does not display the draw message
    return None #it returns nothing so the function stops

  if current_player_colour == colour1: #if it's currently colour1s turn saved in the current_player_colour then it will switch it to colour2
    current_player_colour = colour2
  else:
    current_player_colour = colour1 #otherwise it will switch to colour1

 
home_page("white", "#1E88E5", "#90CAF9", "white", "#90CAF9", "white", "#90CAF9")

########################## win checkers############################


#EXPLANATION: horizontal_checker is a function that checks a 2D list representing a connect 4 board to catch if there are any four consecutive pieces going horizontally. If it does, then it will return true. This function is meant to be used in another function, win_checker, to identify if a player has gotten four in a row in any way. It works by starting at the beginning of each row and checks if the following 3 integers are 1's and it does so by adding 1 to the variable representing the column item (counter).
#PARAMETERS: The parameter list_of_zeros must be a 2D list with 6 items (lists) that also contain 6 items (integers). The list should consist of 1's and 0's, because this function works to consider the integer 1 as a player token put in place, and 0 as an empty spot (however the zeros don't actually matter - only the ones do.)
#RETURNS: If the function identifies that there are 4 pieces in a row (aka 4 1s in a row horizontally), it returns true. Otherwise, it returns fasle. 
#Example:
[1, 0, 1, 0, 1, 0, 1]
[1, 0, 1, 0, 1, 1, 0]
[1, 0, 0, 1, 0, 1, 0]
[0, 1, 1, 1, 0, 1, 0]
[0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 0, 1, 0]
#would return FALSE
[0, 0, 1, 0, 1, 0, 1]
[0, 0, 1, 0, 1, 1, 0]
[0, 0, 0, 1, 0, 1, 0]
[0, 1, 1, 1, 1, 1, 0]
[0, 1, 0, 1, 0, 1, 0]
[0, 0, 1, 0, 0, 1, 0]
#would return TRUE

def horizontal_checker(list_of_zeros):
  counter = 0 #the counter starts at zero and represents the different columns in every row
  for x in list_of_zeros: #then it loops through every row in the 2D list
    counter = 0
    for i in x: #for every item in the row lists
      if counter > 3: #it first checks if the counter is above four, because if it is at 4, then that will mean that if it runs the code below it would be an index error, because adding 4 and 3 would result in seven, and the lists only go up to an index of seven
        break
      if x[counter] == 1 and x[counter+1] == 1 and x[counter+2] == 1 and x[counter+3] == 1: #it checks if the item at the current index of counter and the folloiwng 3 spots are filled with pieces (represented by 1)
        return True #if the conditional if true, then it ill return true
      counter += 1 #otherwise the counter is increased to move on to the next column
  return False #if no four in a ro wis found it returns false

#EXPLANATION: vertical_checker is a function that checks a 2D list representing a connect 4 board to catch if there are any four consecutive pieces going vertically. If it does, then it will return true. This function is meant to be used in another function, win_checker, to identify if a player has gotten four in a row in any way. It works by starting at the beginning of each row and checks if the items of the same index in the following 3 rows are 1's and it does so by adding 1 to the variable representing the row item.
#PARAMETERS: The parameter list_of_zeros must be a 2D list with 6 items (lists) that also contain 7 items (integers). The list should consist of 1's and 0's, because this function works to consider the integer 1 as a player token put in place, and 0 as an empty spot (however the zeros don't actually matter - only the ones do.)
#RETURNS: If the function identifies that there are 4 pieces in a row (aka four 1s in a row vertically), it returns true. Otherwise, it returns fasle. 
#Example:
# [1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 1, 0]
# [1, 0, 0, 1, 0, 1, 0]
# [0, 1, 1, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 0]
# [1, 0, 1, 0, 0, 1, 0]
#would return true

# [1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 0, 0, 0]
# [1, 0, 0, 1, 0, 1, 0]
# [0, 1, 1, 1, 0, 0, 0]
# [0, 1, 0, 1, 0, 1, 0]
# [1, 0, 1, 0, 0, 1, 0]
#false

def vertical_checker(list_of_zeros):
  row_counter = 0 #there are row and spot (aka column) counters set to 0
  spot_counter = 0
  for x in list_of_zeros: #for the rows in list of zeros
    if row_counter > 2: #if the row counter reaches three, then the loop breaks because then in the code below when it attempts to add 3, it would technically be the seventh 7 (or sixth index) and there are only 6 rows, or five index values
      break
    for i in x: #for every spot in a row
      #the function then checks if for the piece at the current roww and column it is at, if the same column folloing rows is also filled for a piece, and it does so by simply checking the item at an increased row, but the same spot
        if list_of_zeros[row_counter][spot_counter] == 1 and list_of_zeros[row_counter+1][spot_counter] == 1 and list_of_zeros[row_counter+2][spot_counter] == 1 and list_of_zeros[row_counter+3][spot_counter] == 1:
          return True
        spot_counter += 1 #if the above conditional is not true, then the spot counter is increased to move on to the next column
    spot_counter = 0 #otherwise, the spot counter is set to 0 again to start at the first column, and the row counter is increased to check starting at the next row
    row_counter += 1
  return False #if nothing is found at all it returns false

#EXPLANATION: diagonal_checker is a function that checks a 2D list representing a connect 4 board to catch if there are any four consecutive pieces going diagonally. If it does, then it will return true. This function is meant to be used in another function, win_checker, to identify if a player has gotten four in a row in any way. This function checks in two different ways. The first way starts at the top most row in the 2D list (aka the 0th index) and checks if the values of the items in the following three rows going diagonally towards the right are 1s (it does so by adding 1 to the row counter var and 1 to the column counter var). It also checks by starting at the bottom most row and checks if the values of the items in the preceeding three rows diagonally towards the right are 1's (it does so by subtracting 1 to the row counter var and adding 1 to the column counter var.)
#PARAMETERS: The parameter list_of_zeros must be a 2D list with 6 items (lists) that also contain 7 items (integers). The list should consist of 1's and 0's, because this function works to consider the integer 1 as a player token put in place, and 0 as an empty spot (however the zeros don't actually matter - only the ones do.)
#RETURNS: If the function identifies that there are 4 pieces in a row (aka four 1s in a row diagonally), it returns true. Otherwise, it returns fasle. 
#Example:
#diagonal checker
# [1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 1, 0]
# [1, 0, 0, 1, 0, 1, 0]
# [0, 1, 1, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 0]
# [1, 0, 1, 0, 0, 1, 0]
#would return true

[1, 0, 1, 0, 1, 0, 1]
[1, 0, 1, 0, 1, 1, 0]
[1, 0, 0, 1, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0]
[0, 0, 0, 1, 0, 0, 0]
[1, 0, 1, 0, 0, 1, 0]
#would return false

def diagonal_checker(list_of_zeros):
  row_counter = 0 #row and spot counters
  spot_counter = 0

  for x in list_of_zeros: #loops through the items in the list
    if row_counter > 2: #it first checks if the row counter is not above two, because once again if it were to be three, and then the above three added three to that, it would be attempting to access an index that doesn't exist and then would cause an index error, because the board onlyl has six rows/fix index values
      break
    for i in x: #for the items in each row
      if spot_counter > 3: #because it is also increasing the column counter, we also ahve to check that it does not increase 3, because if we were to reach 4, and then we added 3 due to the code below, we would be trying to access an index of seven that does not exist
        spot_counter = 0
        break
        #i check diagonally by checking by increasing the column and row counters by 1 each to access the item thats one to the side of the current one of the following list, which is essentially "diagonal"
      if list_of_zeros[row_counter][spot_counter] == 1 and list_of_zeros[row_counter+1][spot_counter+1] == 1 and list_of_zeros[row_counter+2][spot_counter+2] == 1 and list_of_zeros[row_counter+3][spot_counter+3] == 1:
        return True
      spot_counter += 1 #if it the conditional does not return true then the counters will increase
    row_counter += 1 #then after a row is complete it will move on the next one


  #the next block of code is for checking the other way. the previous way checked for top left to bottom right, whereas this one checks for bottom left to top right
  
  row_counter = 5 #the row counter is set to five this time so we can start at the bottom row and work our way down.
  spot_counter = 0

  for x in list_of_zeros:
    if row_counter < 3: #one again we try to avoid an index error by setting the limit to 3
      break
    for i in x: 
      if spot_counter > 3: #another conditional set to avoid index errors
        spot_counter = 0
        break
        #the sole difference is that this time, the row counter decreases so that it checks for the row above. therefore, it will check if there is a piece at a specific index, and then it will check the column to the right of the above row, and so on.
      if list_of_zeros[row_counter][spot_counter] == 1 and list_of_zeros[row_counter-1][spot_counter+1] == 1 and list_of_zeros[row_counter-2][spot_counter+2] == 1 and list_of_zeros[row_counter-3][spot_counter+3] == 1:
        return True
      spot_counter += 1 # counters are increased if needed
    row_counter -= 1
  return False #if no wins are found amongst both blocks of code, the function returns false

#EXPLANATION: win checker checks for 4 in a row. win checker simply calls the three four in a row checker functions (vertical, horizontal and diagonal checker), with it's list argument as the argument for those funtions. If one of the three returns true true, then it knows that the user has achieved four in a row in some way. otherwise, it returns false.
#PARAMETERS: The parameter list_of_zeros must be a 2D list with 6 items (lists) that also contain 7 items (integers). The list should consist of 1's and 0's, because this function works to consider the integer 1 as a player token put in place, and 0 as an empty spot (however the zeros don't actually matter - only the ones do.)
#RETURNS: If any of the three functions called in this function return true, then the function will return true. otherwise, it will return false.
#Example:
# [1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 1, 0]
# [1, 0, 0, 1, 0, 1, 0]
# [0, 1, 1, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 0]
# [1, 0, 1, 0, 0, 1, 0]

# [1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 1, 0]
# [1, 0, 1, 1, 1, 1, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 1, 0, 1, 0, 0, 0]
# [1, 0, 1, 0, 0, 1, 0]

# [1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1, 1, 0]
# [0, 0, 0, 1, 0, 0, 0]
# [0, 1, 1, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 0, 0]
# [1, 0, 1, 1, 0, 1, 0]

# all of these would return true

# [0, 0, 1, 0, 1, 0, 1]
# [0, 0, 1, 0, 1, 1, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0, 1, 0]

# this would return false

def win_checker(list_of_zeros):
  if horizontal_checker(list_of_zeros) or vertical_checker(list_of_zeros) or diagonal_checker(list_of_zeros): #if any of the three functions return true, it means that in some way theres a four in a row
    return True
  else: #if none of them return true, it means that there are no four in a rows and therefore the function returns false
    return False

mainloop()

testCount = 1
passed = 0
failed = 0

def test(actual, expected):  
  global testCount
  global passed
  global failed
  if actual == expected:
    print("Test ", testCount, "passed")
    passed +=1
  else:
    print("Test ", testCount, "failed")
    failed +=1
  testCount+=1

def printResults():
  print(passed, " tests passed, and ", failed, " tests failed")

def colour_assigner_checker(theme, bg, piece, button, font, title, first_col, second_col, current):
  colour_assigner(theme)
  global testCount
  global passed
  global failed
  if bg == bg_colour and piece == piece_colour and button == button_colour and font == font_colour and title == title_colour and first_col == colour1 and second_col == colour2 and current == current_player_colour:
    print("Test ", testCount, "passed")
    passed +=1
  else:
    print("Test ", testCount, "failed")
    failed +=1
  testCount += 1




################# WIN CHECKERS #########################################################

#DIAGONAL FUNCTION CHECKERS

#TRUE EXAMPLES

test(diagonal_checker([[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), True)

test(diagonal_checker([[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), True)

test(diagonal_checker([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0], [0,0,0,1,0,0,0]]), True)

test(diagonal_checker([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0], [0,0,0,1,0,0,0]]), True)

test(diagonal_checker([[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,1,0,0,0],[0,0,1,0,0,0,0], [0,1,0,0,0,0,0]]), True)

test(diagonal_checker([[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,1,0,0,0],[0,0,1,0,0,0,0], [0,1,0,0,0,0,0]]), True)

test(diagonal_checker([[0,1,0,"hello",0,1,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0], ["hi",0,0,0,0,1,0]]), True)

#FALSE EXAMPLES

test(diagonal_checker([[0,1,0,"hello",0,1,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0], ["hi",0,0,0,0,1,0]]), False)

test(diagonal_checker([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0], [0,0,0,1,0,0,0]]), False)

test(diagonal_checker([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

#VERTICAL FUNCTION CHECKERS

#TRUE EXAMPLES

test(vertical_checker([[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), True)

test(vertical_checker([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1], [0,0,0,0,0,0,1]]), True)

test(vertical_checker([[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0], [0,0,0,0,0,0,0]]), True)

test(vertical_checker([[1,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[0,1,0,1,0,0,0],[0,0,0,1,0,0,0], [0,0,0,0,0,1,0]]), True)

test(vertical_checker([[1,"hey",0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,"hi",1],[0,1,"baaaaa",1,0,0,0],[0,0,0,1,0,0,0], [0,0,0,0,0,1,0]]), True)

test(vertical_checker([[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), True)

#FALSE EXAMPLES

test(vertical_checker([[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

test(vertical_checker([[0,1,0,0,1,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,1],[1,0,0,0,0,0,0],[0,0,0,0,0,1,0], [0,1,0,0,1,0,0]]), False)

test(vertical_checker([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

test(vertical_checker([[1,0,0,"bye",0,0,0],[1,0,0,0,0,0,0],["1",0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,"hey",0], [0,0,0,0,0,0,0]]), False)

#HORIZONTAL FUNCTION CHECKERS

#TRUE EXAMPLES

test(horizontal_checker([[1,1,1,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), True)

test(horizontal_checker([[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,1,1,1,1,0,0]]), True)

test(horizontal_checker([[1,0,0,0,1,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,0,0,1,0,0,0], [0,0,0,0,1,0,0]]), True)

test(horizontal_checker([[1,0,0,0,0,0,0],[0,0,0,0,"asdkjf",0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,"hello",0,0,0,0], [0,1,1,1,1,0,0]]), True)

#FALSE EXAMPLES

test(horizontal_checker([[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

test(horizontal_checker([[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

test(horizontal_checker([[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,"bye",0,0],[1,0,0,0,"2938",0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

test(horizontal_checker([[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,"1",0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

test(horizontal_checker([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

#WIN_CHECKER FUNCTION CHECKERS

#TRUE EXAMPLES

test(win_checker([[1,1,1,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), True)

test(win_checker([[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), True)

test(win_checker([[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), True)

#FALSE EXAMPLES

test(win_checker([[1,0,0,0,0,0,0],["hiii",0,0,0,0,0,0],[0,0,0,7,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,18,0], [0,0,0,0,0,0,0]]), False)

test(win_checker([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]), False)

#LOADING_SAVED_FILE FUNCTION CHECKERS

test(loading_saved_file("testing_file_one.txt"), [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]])

test(loading_saved_file("testing_file_two.txt"), [[1,0,0,1,0,0,0], [0,0,0,0,0,1,0], [0,1,0,0,0,0,0], [0,0,0,1,0,0,0], [0,1,0,0,0,0,0], [0,0,0,0,0,1,0]])

test(loading_saved_file("testing_file_three.txt"), [[0,0,0,0,0,0,1], [0,0,0,0,1,0,0], [0,0,0,1,0,0,0], [0,0,1,0,0,0,0], [0,1,0,0,0,0,0], [1,0,0,0,0,0,0]])

colour_assigner_checker("pink", "pink", "pink", "#F389AD", "white", "#F389AD", "#DB819F", "#E0BDE6", "#DB819F")

colour_assigner_checker("original", "blue", "black", "white", "black", "white", "red", "yellow", "red")

colour_assigner_checker("emo", "black", "gray", "gray", "white", "gray", "#0A3F37", "#014275", "#0A3F37")

colour_assigner_checker("blue", "white", "#1E88E5", "#90CAF9", "white", "#90CAF9", "white", "#90CAF9", "white")

####### WRITING LIST TO FILE AND LOADING SAVED FILE#######################

#these two functions can technically be used to test eachother, because if writing list to file is properly writing the list, and loading save file is properly loading it, then the original list argument and the returned list should be the same

def alternate_tester(file_name, list):
  global testCount
  global passed
  global failed
  writing_list_to_file(file_name, list)

  if loading_saved_file(file_name) == list:
    print("Test ", testCount, "passed")
    passed +=1
  else:
    print("Test ", testCount, "failed")
    failed +=1
  testCount += 1

alternate_tester("testing_file_four.txt", [[0,0,0,0,0,0,1], [0,0,0,0,1,0,0], [0,0,0,1,0,0,0], [0,0,1,0,0,0,0], [0,1,0,0,0,0,0], [1,0,0,0,0,0,0]])

alternate_tester("testing_file_five.txt", [[0,0,0,0,0,0,1], [0,0,0,0,1,0,0], [0,0,0,1,0,0,0],  [0,0,1,0,0,0,0], [0,1,0,0,0,0,0], [1,0,0,0,0,0,0]])                
alternate_tester("testing_file_six.txt", [[1,0,1,0,1,0,1], [1,0,1,0,1,1,0], [1,0,0,1,0,1,0],  [0,1,1,1,0,1,0], [0,1,0,1,0,1,0], [1,0,1,0,0,1,0]]) 




  




