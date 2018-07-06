#Class of key constants.
class Keys():
    def __init__(self):
        self.KEYCONSTANTS={KEYUP:'\uE013',
                           KEYDOWN:'\uE015',
                           KEYLEFT : '\uE012',
                           KEYRIGHT: '\uE014',
                           ENTER: '\uE007',
                           RETURN: '\uE006'
                           }

    @staticmethod
    def get_key(self,key):
        return self.KEYCONSTANTS[key]
