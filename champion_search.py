def champion_search(api,summoner_id,active=False):
  if not active:
    print 'This program is inactive'
    print 'Exiting...'
    return
  
  stat_ranked = api.get_stats_ranked(summoner_id)     #won't work if you haven't played ranked before
  
  ranked_champions={}
  count=1
  for champion in stat_ranked['champions']:
    if champion['id']==0:
      continue
    
    champion_info = api.get_champion_name(champion['id'])   #find a way to get names off of champion.json
    ranked_champions[champion_info['name'].lower()]=champion['stats']
    print 'Loading champion %d data...'.center(50) %(count)
    count+=1  
  
  while True:
    print '\n'+'-'*50
    print 'Champions played:'
    for name in sorted(ranked_champions):
        print ' '*2+name.title()
    print
    answer=raw_input('Please enter a champion: ').lower()
    
    ##stops program
    if answer=='stop':
        print 'Exiting'
        return
    
    ##detects if the champion is in ranked_champions
    if answer not in ranked_champions:
        print '-'*50+'\n'            
        print 'Invalid champion'        
        continue
    
    ##can filter some of the champion's stats so that only desired ones are seen
    champ_filter=raw_input('Please enter a filter: ').lower().replace(' ','')
    valid=False     ##Boolean set to see if given filter is in the possible stats for ranked champs
    
    for stat in ranked_champions[answer]:
        if champ_filter in stat.lower():
            valid=True
            break
    if valid==False:
        print '-'*50+'\n'
        print 'Invalid filter'            
        continue
    
    print '-'*50+'\n'
    print answer.title()
    for stat in sorted(ranked_champions[answer]):
        if champ_filter in stat.lower():
            print stat.replace('total','').replace('most','')+':','{:,}'.format(ranked_champions[answer][stat])
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
    champion_search(api,summoner_id,True)
    
    break
  
  
 