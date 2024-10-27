# Create a list of tuples that include states and electoral votes
states = [('AL', 9),('AK', 3),('AZ', 11),('AR', 6),('CA', 54),('CO', 10),('CT', 7),('DE', 3),('DC', 3),('FL', 30),('GA',16),('HI', 4),('ID', 4),('IL', 19),('IN', 11),('IA', 6),('KA', 6),('KY', 8),('LA', 8),('ME', 4),('MD', 10),('MA', 11),('MI', 15),('MN', 10),('MS', 6),('MO', 10),('MT', 4),('NE', 5),('NV', 6),('NH', 4),('NM', 5),('NJ', 14),('NY', 28),('NC', 16),('ND', 3),('OH', 17),('OK', 7),('OR', 8),('PA', 19),('RI', 4),('SC', 9),('SD', 3),('TN', 11),('TX', 40),('UT', 6),('VT', 3),('VA', 13),('WA', 12),('WV', 4),('WI', 10),('WY', 3)]
# Set the starting value of the user's total electoral votes to zero
total_votes = 0
# create and define the variable "find_state", which computes and returns the user's selected state, the electoral vote count of the selected state, and the user's total amount of accumulated electoral votes

def find_state(selected_states):
    for i in range(0, len(states), 1):
        if states[i][0] == selected_states:
            found_state = selected_states
            state_vote = states[i][1]
            return found_state, state_vote, i
    return None, None, None
# create a loop that repeats the process of state selecting until the user reaches 270 electoral votes
while total_votes < 270:
    print("Available states are:")
    # prints the available states   
    for state in states:
        print(state)
    # prints out for the user the state they selected, the vote count of the state they selected, and their new total of votes    
    if total_votes > 0:
        print(f"\nYour state: {found_state}. It's electoral votes: {state_vote}. Your total electoral votes: {total_votes}.")
    # retrieves the user's input (selected state)
    selected_states = input("\n\nAvailable states are shown above.\nType in a state's abbreviation to select a state:")
    found_state, state_vote, i = find_state(selected_states)
    # adds the electoral vote count of the user's selected state to the user's overall total vote count
    if found_state:
        total_votes = total_votes + state_vote
    # removes the user's selected state from the list of tuples (states)   
        states.pop(i)
    # tells the user to reselect a state if they type an incorrect abbreviation
    else:
        print("\nThat is not a valid choice. Please try again.") 
# final print statement that congratulates the user when they reach 270 electoral votes
print(f"\nYou have reached 270 electoral votes. Congratulations! Your total electoral votes: {total_votes}")
    
      










   


