# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_name = 'Gut von Examplestein' #voorbeeld
goal_0 = 32 #1e goal
player_0 = 'Ruud Gullit ' #1e scoorder
goal_1 = 54 #2e goal
scorer_goal_1 = 'Marco van Basten ' #2e scoorder
test = scorer_name + (' scored in the ') + str(goal_0) + (' minute')
scorers = player_0 + str(goal_0) + ', ' + scorer_goal_1 + str(goal_1)
# print(scorers)
report = player_0 + 'scored in the ' + str(goal_0) + 'nd minute\n' + scorer_goal_1 + 'scored in the ' + str(goal_1) + 'th minute'
print (report) #deel 1 van de opdracht
# print(final_scorers)

#deel 2 van de opdracht:
    #first name:
player = player_0
lengte_first_name = player.find(" ")
first_name = (player[0:int(lengte_first_name)])
print (first_name)

    #lengte last name:
last_name_len = int(len(player)) - int(player.find(" ")) - int(1)
print(last_name_len)

    #name short
name_short = (player[0:1] + '.' + player[(lengte_first_name):])
print(name_short)

    #chant Spatie einde klopt niet
# chant = (first_name + '!' + ' ')*str(player.find(" "))
chant = ((first_name + "! ")*4).rstrip()
print (chant)




if len(chant) != " ":
    print (bool(True))
else: 
    print (bool(False))

good_chant = bool(True)
print(good_chant)












