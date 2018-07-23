import json
class SessionData():
    def __init__(self,session):
        self.session = session
    def get_session_id(self,session):
        return json.loads(session)['sessionId']

