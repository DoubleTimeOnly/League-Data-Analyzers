from RiotAPI import RiotAPI
from recent_matches import recent_matches
from stat_search import stat_search
from champion_search import champion_search
from current_game import current_game

def main():
    ##active modules
    rm_active=True
    ss_active=True
    cs_active=True
    cg_active=True
    
    api = RiotAPI('3029076c-24d5-4b04-93cc-eda77e5ab23f')
    summoner = raw_input('Enter Summoner Name: ').replace(' ','').lower()
    print 'Retrieving data please wait...'.center(50)
    r = api.get_summoner_by_name(summoner)
    summoner_id = r[summoner]['id']
    #print summoner_id

#Program Select-------------------------------------------------------------------   
    while True:
        print '\n'+'-'*50
        print 'Available programs: Champion Search (CS) | Stat Search (SS) | Recent Matches (RM) | Current Game (CG)'
        choice=raw_input('What program do you wish to run?: ').lower()
        if choice =='stop':
            print 'Exiting'
            break
        if choice not in ['cs','champion search','ss','stat search','rm','recent matches','cg','current game']:
            print '-'*50+'\n'
            print 'Invalid program'
            continue
        
    #recent_matches---------------------------------------------------------------        

        if True and choice=='rm' or choice=='recent matches':
            recent_matches(api,summoner_id,rm_active)
            
    #current_game_info------------------------------------------------------------
    
        if True and choice == 'cg' or choice == 'current game':
            current_game(api,summoner_id,cg_active)
                  
    #searching stats by champion--------------------------------------------------
    
        if True and choice == 'cs' or choice == 'champion search':
            champion_search(api,summoner_id,cs_active)
    
    #searching champions by stat--------------------------------------------------
    
        if True and choice == 'ss' or choice == 'stat search':
            stat_search(api,summoner_id,ss_active)
   
        
if __name__ == '__main__':
    main()