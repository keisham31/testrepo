"""
A witch story with user input
Mad-Libs style
"""
def witchStory(firstName, lastName, gender, address, verb):
    """ create a witch story """

    # create the story
    start = "Once there was a " + gender + " named " + firstName + "."
    next1 = "A good " + gender + " living at " + address + "."
    next2 = "One day, a wicked witch came to the " + lastName + " house."
    next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
    ending = "But " + firstName + " was smart and avoided the wicked witch."

    # put the story together
    # the \n characters are new lines so that each part will be printed on its
    # own line
    story = start + "\n" + next1 + "\n" + next2 + "\n" + next3 + "\n" + ending

    # return a string that tells the story
    return(story)


def get_gender_choice():
    """ get gender choice using a validation loop
        user must choose boy or girl """
    gender = input("What gender (boy or girl): ")
    while(gender not in ['boy', 'girl']):
        print("Sorry, but you must select boy or girl. ")
        print("Try again and select one of those.")
        gender = input("What gender (boy or girl): ")

    return(gender)


def main():
    # get user input
    fname = input("Enter a first name: ")
    lname = input("Enter a last name: ")
    gender = get_gender_choice()
    address = input("Enter an address: ")
    verb = input("Enter a verb: ")

    # invoke the witchStory function
    my_story = witchStory(fname, lname, gender, address, verb)

    # display the story (notice that it displays on multiple lines because of the \n characters)
    print(my_story)

# invoke the main() function
main()# Write your code here :-)
