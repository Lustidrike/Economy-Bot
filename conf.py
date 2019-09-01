import logging
from configparser import ConfigParser

log = logging.getLogger(__name__)

__all__ = ('self.config')

class Config:
    """Server-specific self.configuration settings read from ini file stored on the server."""

    def __init__(self):
        try:
            self.config = ConfigParser()
            self.config.read('bot.ini')

            # Note: Default paths are given relative to the bot's root path
            # Feel free to specify absolute paths in your bot.ini to be clear
            self.bot_channel_id = int(self.config.get('Private', 'bot_channel_id', fallback=''))
            self.token = self.config.get('Private', 'token', fallback='')
            self.cogs_path = self.config.get('Private', 'cogs_path', fallback='Cogs')
            self.cogs_data_path = self.config.get('Private', 'cogs_data_path', fallback='Cogs/data')
            self.logfile = self.config.get('Private', 'logfile', fallback='economy.log')
            self.database = self.config.get('Private', 'database', fallback='economy.json')
            self.admins = self.config.get('Private', 'admins', fallback='').split(',')
            self.additional_error_message = self.config.get('Private', 'additional_error_message', fallback='')
            self.main_server = int(self.config.get('Private', 'main_server', fallback=''))
            self.additional_info_text = self.config.get('Private', 'additional_info_text', fallback='')

            self.timezone = self.config.get('General', 'timezone', fallback='CET') # Note: This is just a string to be printed. Doesn't actually affect displayed time.
            self.description = self.config.get('General', 'description', fallback='''My Test Economy''')
            self.name = self.config.get('General', 'name', fallback='Test Economy')
            self.currency_name = self.config.get('General', 'currency_name', fallback='Test Points')
            self.prefix = self.config.get('General', 'prefix', fallback='!')
            self.cogs = self.config.get('General', 'cogs', fallback='Economy,Holidays,Bounties,Gambling,Duel,BattleRoyale,Horserace,Labels,Polls,Stats,TimedTask,Misc,Shortcuts,Northmarker').split(',')
            self.forbidden_characters = self.config.get('General', 'forbidden_characters', fallback='`,@').split(',')
            self.check_ljust = int(self.config.get('General', 'check_ljust', fallback='39'))
            self.trivia_ljust = int(self.config.get('General', 'trivia_ljust', fallback='39'))
            self.season_ljust = int(self.config.get('General', 'season_ljust', fallback='40'))
            self.repost_attempts = int(self.config.get('General', 'repost_attempts', fallback='30'))

            log.info('Finished reading server self.configuration from file')
        except Exception as e:
            print('Error reading self.config file' + str(e))


    # For convenience
    def get(self, category, name, fallback):
        return self.config.get(category, name, fallback=fallback)



config = Config()
