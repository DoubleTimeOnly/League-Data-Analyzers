

def current_game(api,summoner_id,active=False):
    if active==False:
        print 'This program is inactive'
        print 'Exiting...'
        return
    
    current_game_data = api.get_current_game(summoner_id)
    for stat in current_game_data:
        print stat,current_game_data[stat]
    print current_game_data['gameMode']
    summoner_ids=''
    blue_team=[]
    red_team=[]                        
    for player in current_game_data['participants']:
        if player['teamId']==100:
            blue_team.append(player)
            
        else:
            red_team.append(player)
    current_map=''
    maps={11:'Summoner\'s Rift',12:'Howling Abyss'}
    if current_game_data['mapId'] in maps:
        current_map=maps[int(current_game_data['mapId'])]
    
    
    print '\n'+'-'*50
        
    game_mode= 'Game Mode: %s | %s' %(current_game_data['gameMode'],current_map)
    print game_mode.center(50)    
    print 'Blue Team'.center(50) 
    for player in blue_team:
        champion = api.get_champion_name(player['championId'])        
        print '%s: %s' %(player['summonerName'],champion['name'])
        
    print '\nRed Team'.center(50) 
    for player in blue_team:
        champion = api.get_champion_name(player['championId'])        
        print '%s: %s' %(player['summonerName'],champion['name'])    
    
    

if __name__=='__main__':
    from RiotAPI import RiotAPI
    
    api = RiotAPI('3029076c-24d5-4b04-93cc-eda77e5ab23f')
    summoner = raw_input('Enter Summoner Name: ').replace(' ','').lower()
    print 'Retrieving data please wait...'.center(50)
    r = api.get_summoner_by_name(summoner)
    summoner_id = r[summoner]['id']    

    current_game(api,summoner_id,True)