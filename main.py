
from miner import StatMiner
from mlb_database import MlbDatabase

#TODO: add some data for the starting pitcher and catcher giving up stolen bases
mlbDatabase = MlbDatabase()
databaseSession = mlbDatabase.open_session()
#TODO: add some neural networks

statMiner = StatMiner(databaseSession)

statMiner.mine_day("http://mlb.mlb.com/gdcross/components/game/mlb/year_2015/month_07/day_09/")
#statMiner.mine_month("http://mlb.mlb.com/gdcross/components/game/mlb/year_2015/month_06/")
#statMiner.mine_season("2015")

databaseSession.close()

