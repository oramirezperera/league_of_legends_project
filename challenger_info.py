import cassiopeia as cass
#import roleml


def get_APIkey():
    f = open("api_key.txt", "r")
    return f.read()

def getChallengerPlayers():
    ranked_type = cass.Queue.ranked_solo_fives

    challenger_league = cass.get_challenger_league(queue=ranked_type)

    summoner = challenger_league[0].summoner
    match_history = summoner.match_history(queues={ranked_type}, begin_index=0, end_index=4)

    for match in match_history:
        print(match_duration)

cass.set_riot_api_key(get_APIkey)
cass.set_default_region("NA")