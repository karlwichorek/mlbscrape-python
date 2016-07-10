from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship
from pitcher_entry import PitcherEntry
from datetime import date
from mlb_database import Base


class GameEntry(Base):

    __tablename__ = 'game_entries'

    game_date = Column(String, primary_key=True)
    home_team = Column(String, primary_key=True)
    away_team = Column(String, primary_key=True)
    game_time = Column(String, primary_key=True)

    game_hitter_entries = relationship("PregameHitterGameEntry", backref="game_entries")
    game_pitcher_entries = relationship("PregamePitcherGameEntry", backref="game_entries")


    def __init__(self):
        """ Constructor
        Copy the Pitcher object into the PitcherGameEntry fields
        :param pitcher: Pitcher object
        """
        super(PregamePitcherGameEntry, self).__init__()

        self.predicted_draftkings_points = 0
        self.draftkings_salary = 0

        # Season stats
        self.season_bf = 0
        self.season_ip = 0
        self.season_so = 0
        self.season_wins = 0
        self.season_losses = 0
        self.season_er = 0
        self.season_h = 0
        self.season_bb = 0
        self.season_hr = 0

        # Career stats
        self.career_bf = 0
        self.career_ip = 0
        self.career_so = 0
        self.career_wins = 0
        self.career_losses = 0
        self.career_er = 0
        self.career_h = 0
        self.career_bb = 0
        self.career_hr = 0

        # Versus stats
        self.vs_bf = 0
        self.vs_so = 0
        self.vs_er = 0
        self.vs_h = 0
        self.vs_bb = 0
        self.vs_hr = 0

        # Month stats
        self.recent_bf = 0
        self.recent_ip = 0
        self.recent_so = 0
        self.recent_er = 0
        self.recent_h = 0
        self.recent_bb = 0
        self.recent_hr = 0

    def __repr__(self):
        """
        :return: string representation identifying the Pitcher entry
        """
        return "<Pitcher PreGame Entry(name=%s %s, team='%s', id='%s', salary=%i, $/point=%f)>" %\
               (self.pitcher_entries.first_name,
                self.pitcher_entries.last_name,
                self.pitcher_entries.team,
                self.rotowire_id,
                self.draftkings_salary,
                float(self.draftkings_salary) / self.predicted_draftkings_points)

    def to_input_vector(self):
        """ Convert the entry to a vector
        :return: a list representation of the entry
        """
        return [self.season_bf, self.season_ip, self.season_so, self.season_wins, self.season_losses, self.season_er,
                self.season_h, self.season_bb, self.season_hr,
                self.career_bf, self.career_ip, self.career_so, self.career_wins, self.career_losses, self.career_er,
                self.career_h, self.career_bb, self.career_hr,
                self.vs_bf, self.vs_so, self.vs_er, self.vs_h, self.vs_bb, self.vs_hr,
                self.recent_bf, self.recent_ip, self.recent_so, self.recent_er, self.recent_h, self.recent_bb,
                self.recent_hr]

    @staticmethod
    def get_all_daily_entries(database_session, game_date=None):
        if game_date is None:
            game_date = date.today()
        return database_session.query(PregamePitcherGameEntry).filter(PregamePitcherGameEntry.game_date == game_date)




