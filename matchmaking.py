import datetime

from dbconnector import DBConnector

class Matcher(object):
    def __init_(self):
        self._db_name = 'matchmaking'
        self._collection_name = 'match_queue'
        self._db_conn = DBConnector(self._db_name, self._collection_name)
        self._allowed_platforms = 'pc', 'ps4', 'xb', 'any'
        
    def add_player_to_queue(self, player, platform):
        if platform_is_valid(platform):
            return False
        notice = {"player": player,
                 "platform": platform,
                 "date": datetime.datetime.utcnow()}
        self.get_db_conn().get_collection().insert_one(notice)
        return True

    def check_queue_for_players(self, platform='any'):
        if platform is not 'any':
            return self.get_db_conn().get_collection().find({"platform":platform})
        else:
            return self.get_db_conn().get_collection().find()

    def remove_players_from_queue(self, players):
        for player in players:
            self.get_db_conn().get_collection().remove({"player":player})

    def platform_is_valid(self, platform):
        if platform not in self._allowed_platforms:
            return False
        else:
            return True

    def get_db_conn(self):
        return self._db
