from database.database_connection import get_connection

class ScoreRepository:
    def __init__(self, connection):
        self._connection = connection

    def fetch_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM scores")

        rows = cursor.fetchall()

        return [{"username": row["username"], "score": row["score"]} for row in rows]

    def save(self, score: dict):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO scores (username, score) values (?, ?)",
        (score["username"], score["score"]))

        self._connection.commit()
        
        return score

score_repository = ScoreRepository(get_connection())
