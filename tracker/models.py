from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import requests
from tracker2 import config



class Trackers(models.Model):
    __tablename__ = 'trackers'

    user = models.ForeignKey(User)
    steam_id = models.CharField(max_length=100, primary_key=True)
    start_playtime = models.IntegerField(default=0)
    start_date = models.DateField(default=timezone.now())
    time_limit = models.IntegerField()
    current_playtime = models.IntegerField(default=0)
    notified = models.BooleanField(default=False)

    def playtime(self):
        url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}&format=json'.format(
            config.steam_key, self.steam_id)
        response = requests.get(url).json()
        games = response['response']['games']
        time_played = sum([games[i]['playtime_forever'] for i in range(len(games))])
        return time_played

    def minutes_played_this_session(self):
        return self.playtime() - self.start_playtime

    def over_limit(self):
        return self.minutes_played_this_session() / 60 >= self.time_limit

    def notify_user(self):
        return requests.post(config.mail_url, auth=config.mail_key,
                             data={
                                 "from": "Mailgun Sandbox <postmaster@sandbox5ec3142264ec408ca87618cb784f58d9.mailgun.org>",
                                 "to": self.user.email,
                                 "subject": "Limit Reached",
                                 "text": "You have exceeded your Steam Limit."})

    def reset_user(self):
        self.start_playtime = self.playtime()
        self.start_date = timezone.now()
        self.notified = False

    def __str__(self):
        return self.steam_id[:9]