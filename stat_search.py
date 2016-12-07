def stat_search(api,summoner_id,active=False):
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
                
    name=sorted(ranked_champions)[0]
    
    print 'Stats available:'
    for stat in sorted(ranked_champions[name]):
        print ' '*2+stat
    print
    sortby=raw_input('Please Enter a Stat: ').lower().replace(' ','')
    
    if sortby=='stop':
        print 'Exiting'
        return
    
    valid=False
             
    for stat in ranked_champions[name]:
        if sortby == stat.lower():
            sortby=stat
            valid=True
            break
            
    if valid==False:
        print '-'*50+'\n'
        print 'Invalid stat'            
        continue        
    
    sorted_ranked_champion={}       
    for champion in sorted(ranked_champions):
        if ranked_champions[champion][sortby] in sorted_ranked_champion:
            sorted_ranked_champion[ranked_champions[champion][sortby]] += ', '+champion
        else:
            sorted_ranked_champion[ranked_champions[champion][sortby]] = champion
    
    print '-'*50+'\n'                
    print 'Champions sorted by %s' %(sortby)
    for sortby_value in sorted(sorted_ranked_champion,reverse=True):
        print sorted_ranked_champion[sortby_value].title()+':','{:,}'.format(sortby_value)
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
    stat_search(api,summoner_id,True)
    
    break
  
  
 