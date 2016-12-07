def recent_matches(api,summoner_id,active=False):
  if not active:
    print 'This program is inactive'
    print 'Exiting...'
    return
  
  recent_games=api.get_recent_games(summoner_id)
            
  match_list=[]
  match_number=1
  print 'Retrieving match data please wait...'.center(50)
  for match in recent_games['games']:
      champion = api.get_champion_name(match['championId'])['name']
      line = '  %d.) %s: %s' %(match_number,match['gameMode'].title(),champion)
      match_list.append(line)
      match_number+=1                   
  while True:                   
      print '\n'+'-'*50        
      print 'Recent Matches:'
      for match in match_list:
          print match
      print
      desired_match = raw_input('Please enter a match number: ')
      if desired_match =='stop':
          print 'Exiting'
          return            
      if not desired_match.isdigit() or int(desired_match)<1 or int(desired_match)>10 or len(desired_match)<1:
          print '-'*50+'\n'                        
          print 'Invalid match number'
          continue
      
      print 'Available filters: Damage | Kills | Teams | All'        #try multiple filters at once
      stat_filter=raw_input('Please enter a stat filter (enter multiple filters using commas): ').lower()
      
      if 'all' in stat_filter:
        stat_filter='all'      
      stat_filter=sorted(set(stat_filter.split(',')))
      
      match = recent_games['games'][int(desired_match)-1]
      ##creates comma seperated string for fetch summoner profile by id
   
      
      ##groups
      damage_dealt_taken_healed=['totalDamageDealt','  physicalDamageDealtPlayer','  magicDamageDealtPlayer','  trueDamageDealtPlayer','totalDamageDealtToChampions','  physicalDamageDealtToChampions','  magicDamageDealtToChampions','  trueDamageDealtToChampions','  largestCriticalStrike','totalDamageTaken','  physicalDamageTaken','  magicDamageTaken','  trueDamageTaken']    #spaces are for formatting
      kda=['championsKilled','numDeaths','assists','largestMultiKill','largestKillingSpree','minionsKilled']
      gold=[]
      items=['item0','item1','item2','item3','item4','item5',]                
      #print fellow_summoners
      print '\n'+'-'*50        
      
      for stat in stat_filter:
        if stat.strip().strip('s') in ['fellow player','fp','team','t','all']:
            summoner_ids=''
            blue_team=[]
            red_team=[]                        
            for player in match['fellowPlayers']:
                if player['teamId']==100:
                    blue_team.append(player)
                    summoner_ids+= '%d,' %(player['summonerId'])  
                    
                else:
                    red_team.append(player)
                    summoner_ids+= '%d,' %(player['summonerId'])  
            fellow_summoners=api.get_summoners_by_id(summoner_ids.strip(','))
            
            print 'Teams'.center(50)
            print 'Blue Team:'
            for player in blue_team:
                champion = api.get_champion_name(player['championId'])['name']
                print fellow_summoners[str(player['summonerId'])]['name']+':',champion
            print '\nRed Team:'    
            for player in red_team:
                champion = api.get_champion_name(player['championId'])['name']        
                print fellow_summoners[str(player['summonerId'])]['name']+':',champion
            print
            raw_input('Hit enter to continue...')
    
            #for stat in sorted(match['stats']):
            #print stat+':','{:,}'.format(match['stats'][stat]) 
        
        if stat.strip() in ['damage','d','all']:
            #print '\n'+'-'*50
            
            print 'Damage stats'.center(50) 
            for stat in damage_dealt_taken_healed:
                if 'total' in stat:
                    print
                if stat.strip() not in match['stats']:
                    print stat+':',0
                    continue
                print stat+':','{:,}'.format(match['stats'][stat.strip()])
            print
            raw_input('Hit enter to continue...')
            
            
        if stat.strip() in ['kills','k','all']:
            print 'Kill stats'.center(50)
            print
            for stat in kda:
                if stat.strip() not in match['stats']:
                    print stat+':',0                        
                    continue                    
                print stat+':','{:,}'.format(match['stats'][stat.strip()])
            print
            raw_input('Hit enter to continue...')
       


if __name__=='__main__':
  from RiotAPI import RiotAPI
      
  api = RiotAPI('3029076c-24d5-4b04-93cc-eda77e5ab23f')
  summoner = raw_input('Enter Summoner Name: ').replace(' ','').lower()
  #print 'Retrieving data please wait...'.center(50)
  r = api.get_summoner_by_name(summoner)
  summoner_id = r[summoner]['id']  
  while True:
    recent_matches(api,summoner_id,True)
    break
  
  
  '''
    timePlayed
    win
    largestCriticalStrike
    totalDamageDealt
    magicDamageDealtToChampions
    largestMultiKill
    largestKillingSpree
    magicDamageTaken
    item2
    item3
    item0
    item1
    item6
    item4
    minionsKilled
    championsKilled
    doubleKills
    trueDamageTaken
    assists
    physicalDamageDealtToChampions
    goldSpent
    level
    physicalDamageDealtPlayer
    totalHeal
    goldEarned
    turretsKilled
    totalDamageDealtToChampions
    totalUnitsHealed
    team
    numDeaths
    totalDamageTaken
    killingSprees
    magicDamageDealtPlayer
    physicalDamageTaken
                    timePlayed
    win
    totalTimeCrowdControlDealt
    wardKilled
    tripleKills
    doubleKills
    goldSpent
    level
    totalHeal
    goldEarned
    turretsKilled
    totalUnitsHealed
    team
    killingSprees
    '''          
  