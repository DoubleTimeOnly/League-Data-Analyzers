URL = {
  
  'base':'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
  'summoner_by_name': 'v{version}/summoner/by-name/{summonerNames}',
  'summoners_by_id':'v{version}/summoner/{summonerIds}',
  'stats_summary':'v{version}/stats/by-summoner/{summonerId}/summary',
  'stats_ranked':'v{version}/stats/by-summoner/{summonerId}/ranked',
  'recent_games': 'v{version}/game/by-summoner/{summonerId}/recent',
  
  'observer_base':'https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/{url}',
  'current_game':'{platformId}/{summonerId}',
  
  'static_base': 'https://global.api.pvp.net/api/lol/static-data/{region}/{url}',
  'champion_id' : 'v{version}/champion/{champ_id}'
  
}
 
API_VERSIONS = {
    'summoner':'1.4',
    'stats':'1.3',
    'champion':'1.2',
    'static_data':'1.2',
    'recent_games':'1.3'
}

REGIONS = {
    'north_america':'na'
}