from repositories.score_repository import score_repository


class ScoreService:
    """Service for saving and fetching scores
    """

    def __init__(self, repository):
        """The constructor for the score service

        Args:
            repository (ScoreRepository): The score repository to use
        """
        self._repository = repository

    def fetch_all(self):
        """Gets a list of all scores

        Returns:
            list: A list of dictionaries, each representing a score.
                  Each score dictionary has 2 keys and values,
                  ["username"] (str) and ["score"] (int)
        """
        return self._repository.fetch_all()

    def save(self, username, score_int):
        """Saves a score, if it is greater than 0.
           If the username is left blank, it defaults to "Nimetön"

        Args:
            username (str): The players name
            score_int (int): The achieved score

        Returns:
            dict: A dictionary representing the score.
                  It has 2 keys and values, ["username"] (str) and ["score"] (int)
        """

        if score_int <= 0:
            return False

        if username == "":
            username = "Nimetön"

        score = {"username": username, "score": score_int}

        return self._repository.save(score)


score_service = ScoreService(score_repository)
