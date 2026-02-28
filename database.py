# Database models and connection management for Chess Game

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    games = relationship("Game", back_populates="player")

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="games")
    game_data = Column(String)

class GameStatistic(Base):
    __tablename__ = 'game_statistics'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    moves = Column(String)
    result = Column(String)

# Database connection management
DATABASE_URL = "sqlite:///chess.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Create all tables
Base.metadata.create_all(engine)