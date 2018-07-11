import pprint
import datetime
import logging

from dbconnector import DBConnector

logging.basicConfig(level=logging.INFO)

class Matcher(object):
    def __init__(self, logger):
        self._logger = logger
        self._logger.info('Initting matchmaking')
        self._db_name = 'matchmaking'
        self._collection_name = 'match_queue'
        self._db_conn = DBConnector(self._db_name, self._collection_name)
        self._allowed_platforms = 'pc', 'ps4', 'xb', 'any'

    def add_player_to_queue(self, player, platform):
        if self.platform_is_valid(platform):
            return False
        notice = {"player": player,
                 "platform": platform,
                 "date": datetime.datetime.utcnow()}
        self.get_db_conn().get_collection().insert_one(notice)
        return True

    def check_queue_for_players(self, platform='any'):
        self._logger.info('Checking for players in queue...')
        if platform != 'any':
            return pprint.pprint(self.get_db_conn().get_collection().find({"platform":platform}))
        else:
            return pprint.pprint(self.get_db_conn().get_collection().find())

    def remove_players_from_queue(self, players):
        for player in players:
            self.get_db_conn().get_collection().remove({"player":player})

    def platform_is_valid(self, platform):
        if platform not in self._allowed_platforms:
            return False
        else:
            return True

    def get_db_conn(self):
        return self._db_conn
