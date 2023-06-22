# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line



Weather = ['rainy', 'sunny', 'windy', 'neutral']
Time_of_day = ['day', 'night']
Cow_milking_status = [True, False]
Location_of_the_cows = ['pasture', 'cowshed']
Season = ['winter', 'spring', 'summer', 'fall']
Slurry_tank = [True, False]
Grass_status = [True, False]

def print_main_action(Location_of_the_cows, main_action):
    if Location_of_the_cows == 'cowshed':
        return (main_action)
    else:
        Location_of_the_cows == 'pasture'
        return ('"""take cows to cowshed' + '\n' +  main_action +  '\n'+ 'take cows back to pasture""')

def farm_action (Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
        if Location_of_the_cows == 'pasture' and (Time_of_day == 'night'or Weather == 'rainy'):
            main_action = 'take cows to cowshed'
            return (print_main_action(Location_of_the_cows, main_action))
        elif Cow_milking_status == True and Location_of_the_cows == 'cowshed': 
              main_action = 'milk cows'
              return (print_main_action(Location_of_the_cows, main_action))
#optie 1        
        # elif Cow_milking_status == True and Location_of_the_cows == 'pasture':    
        #       main_action = 'milk cows'
        #       return (print_main_action(Location_of_the_cows, main_action))
        elif Slurry_tank == True and (Location_of_the_cows == 'cowshed' and Weather != ('sunny' or 'windy')):
              main_action = 'fertilize pasture'
              return (print_main_action(Location_of_the_cows, main_action))
        elif Grass_status == True and Season == 'spring' and Weather == 'sunny' and Location_of_the_cows != 'pasture':
                main_action = 'mow grass'
                return (print_main_action(Location_of_the_cows, main_action))
#optie 2        
        # if Location_of_the_cows == 'pasture':
        #     return ('take cows to cowshed' + '\n' +  main_action +  '\n'+ 'take cows back to pasture')
        # else:
        #     return (main_action)
        #return ('mow grass')
#optie 3
        # elif "":
        #     action_before = 'take cows to cowshed'
        #     main_action = 'test' 
        #     action_after = 'take cows back to pasture'
        #     if {farm_action == 'milk cows' or farm_action == 'fertilize pasture' or farm_action == 'mow grass'} and Location_of_the_cows == 'pasture':
        #         return (action_before, "\n" ,  main_action,  '\n',action_after)
        #     elif Location_of_the_cows == 'cowshed':
        #           return (main_action)
        else:
              return('wait')  

print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))

#variable input: 
# print(farm_action(Weather[1], Time_of_day[0], Cow_milking_status[0], Location_of_the_cows[0], Season[1], Slurry_tank[1], Grass_status[0]))

#optie 4
# if farm_action('sunny', 'day', True, 'pasture', 'spring', False, True) == ('milk cows' or 'fertilize pasture' or 'mow grass') and Location_of_the_cows == 'pasture':
#       print ('Test')
# else: 
#     print('Test2')








