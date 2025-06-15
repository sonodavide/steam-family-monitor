import sqlite3
from typing import List

from Game import Game

class DbHelper:
    def __init__(self, db_path: str = "steamWebApiDB.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize database and create tables if they don't exist"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    userId VARCHAR(32) UNIQUE NOT NULL,
                    name VARCHAR(32)
                )
            ''')

            # Create games table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    appid TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL
                )
            ''')

            # Create user_games table for many-to-many relationship
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_games (
                    user_id INTEGER,
                    game_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (game_id) REFERENCES games (id),
                    PRIMARY KEY (user_id, game_id)
                )
            ''')
            
            conn.commit()

    def add_user(self, userId: str, name: str) -> int:
        """Add a new user and return their id"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (userId, name) VALUES (?, ?)', (userId, name))
            conn.commit()
            return cursor.lastrowid

    def add_game(self, appid: str, name: str) -> int:
        """Add a new game and return its id"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO games (appid, name) VALUES (?, ?)', (appid, name))
            conn.commit()
            return cursor.lastrowid

    def link_user_game(self, user_id: int, game_id: int):
        """Create a link between user and game"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO user_games (user_id, game_id) VALUES (?, ?)', 
                         (user_id, game_id))
            conn.commit()

    def get_user_games(self, userId: str) -> List[tuple]:
        """Get all games for a specific user"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT g.appid, g.name 
                FROM games g
                JOIN user_games ug ON g.id = ug.game_id
                JOIN users u ON u.id = ug.user_id
                WHERE u.userId = ?
            ''', (userId,))
            return cursor.fetchall()
    
    
    def update_user_games(self, userId: str, games: list[Game]):
        """
        Update user's games in database
        Args:
            userId: Steam user ID
            games: list of Game objects to add/update
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get or create user
            cursor.execute('SELECT id FROM users WHERE userId = ?', (userId,))
            user_result = cursor.fetchone()
            if not user_result:
                cursor.execute('INSERT INTO users (userId) VALUES (?)', (userId,))
                user_id = cursor.lastrowid
            else:
                user_id = user_result[0]

            # Process each game
            for game in games:
                # Check if game exists
                cursor.execute('SELECT id FROM games WHERE appid = ?', (game.appid,))
                game_result = cursor.fetchone()
                
                if not game_result:
                    # Add new game
                    cursor.execute('INSERT INTO games (appid, name) VALUES (?, ?)', 
                                (game.appid, game.name))
                    game_id = cursor.lastrowid
                else:
                    game_id = game_result[0]
                
                # Create relationship if it doesn't exist
                cursor.execute('''
                    INSERT OR IGNORE INTO user_games (user_id, game_id)
                    VALUES (?, ?)
                ''', (user_id, game_id))
            
            conn.commit()
    def get_new_games(self, userId: str, current_games: list[Game]) -> list[Game]:
        """
        Compare current games with stored ones and return only new games
        Args:
            userId: Steam user ID
            current_games: list of Game objects from API
        Returns:
            list of Game objects that are not in the database
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT g.appid, g.name
                FROM games g
                JOIN user_games ug ON g.id = ug.game_id
                JOIN users u ON u.id = ug.user_id
                WHERE u.userId = ?
            ''', (userId,))
            
            # Convert to set of appids for faster lookup
            existing_appids = [row[0] for row in cursor.fetchall()]
            # Return only games not in database
            return [game for game in current_games if game.appid not in existing_appids]