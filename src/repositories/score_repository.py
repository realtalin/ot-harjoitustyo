from database.database_connection import get_connection


class ScoreRepository:
    """Class for saving scores to a database
    """
    def __init__(self, connection):
        """Constructor for the class

        Args:
            connection: The database connection
        """
        self._connection = connection

    def fetch_all(self):
        """Fetches all scores from the database

        Returns:
            list: A list of dictionaries, each representing a score.
                Each score dictionary has 2 keys and values, ["username"] (str) and ["score"] (int)
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM scores")

        rows = cursor.fetchall()

        return [{"username": row["username"], "score": row["score"]} for row in rows]

    def save(self, score: dict):
        """Adds a score to the database

        Args:
            score (dict): A dictionary with 2 keys and values,
                          ["username"] (str) and ["score"] (int)

        Returns:
            score: The added score dictionary
        """
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO scores (username, score) values (?, ?)",
                       (score["username"], score["score"]))

        self._connection.commit()

        return score

    def delete_all(self):
        """Deletes all scores from the database
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM scores")

        self._connection.commit()


score_repository = ScoreRepository(get_connection())
