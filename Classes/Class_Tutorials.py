import datetime
virat={'first_name':
'virat','last_name':
'kohli','birth_year':
1988,'scores':[]}
virat['scores'].append(80)
virat['scores'].append(100)
virat['scores'].append(0)

david={'first_name':
'david','last_name':
'warne','birth_year':
1987,'scores':[]}

def get_average_score(player):
    return sum(player['scores'])/len(player['scores'])
def age_ofplayer(player):
    now=datetime.datetime.now()
    return now.year-player['birth_year']
print(get_average_score(virat),age_ofplayer(david))



