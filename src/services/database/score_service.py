from repositories.score_repository import score_repository


class ScoreService:
    def __init__(self, repository):
        self._repository = repository

    def fetch_all(self):
        return self._repository.fetch_all()

    def save(self, username, score_int):
        if score_int <= 0:
            return False

        if username == "":
            username = "Nimetön"

        score = {"username": username, "score": score_int}

        return self._repository.save(score)


score_service = ScoreService(score_repository)
