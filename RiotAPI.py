import RiotConsts as Consts
import requests
class RiotAPI(object):
    def __init__(self,api_key,region=Consts.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region
    
    def _request(self,api_url,params={}):
        args={'api_key':self.api_key}
        for key,value in params.items():
            if key not in args:
                args[key]=value
        response=requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
                ),
            params=args
            )
        #print response.url
        return response.json()
    
    def get_summoner_by_name(self,name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            summonerNames=name
            )
        return self._request(api_url)
    
    def get_summoners_by_id(self,summoner_ids):
        api_url = Consts.URL['summoners_by_id'].format(
            version=Consts.API_VERSIONS['summoner'],
            summonerIds=summoner_ids
            )
        return self._request(api_url)
    
    def get_stats_summary(self,summoner_id):
        api_url = Consts.URL['stats_summary'].format(
            version=Consts.API_VERSIONS['stats'],
            summonerId=summoner_id
            )
        return self._request(api_url)
    
    def get_stats_ranked(self, summoner_id):
        api_url = Consts.URL['stats_ranked'].format(
            version=Consts.API_VERSIONS['stats'],
            summonerId=summoner_id
            )
        return self._request(api_url)
    
    def get_champion(self,champion_id):
        api_url = Consts.URL['champion_id'].format(
            version=Consts.API_VERSIONS['champion'],
            champ_id=champion_id
        )
        return self._request(summoner_id)        
    
    def get_recent_games(self,summoner_id):
        api_url = Consts.URL['recent_games'].format(
            version=Consts.API_VERSIONS['recent_games'],
            summonerId=summoner_id
        )
        return self._request(api_url)            
    
    def _request_static(self,api_url,params={}):
        args={'api_key':self.api_key}
        for key,value in params.items():
            if key not in args:
                args[key]=value
        response_static=requests.get(
            Consts.URL['static_base'].format(
                region=self.region,
                url=api_url
                ),
            params=args
            )
        return response_static.json()
    
    def get_champion_name(self,champion_id):
        api_url = Consts.URL['champion_id'].format(
            version=Consts.API_VERSIONS['static_data'],
            champ_id=champion_id
        )
        return self._request_static(api_url)           
    
    def get_current_game(self,summoner_id,platformId='NA1',params={}):
        args={'api_key':self.api_key}
        for key,value in params.items():
            if key not in args:
                args[key]=value
        
        api_url = Consts.URL['current_game'].format(
            platformId=platformId,
            summonerId=summoner_id
        )        
        response_static=requests.get(
            Consts.URL['observer_base'].format(
                url=api_url
                ),
            params=args
        )
        return response_static.json()        