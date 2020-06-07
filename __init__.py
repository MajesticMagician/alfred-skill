from mycroft import MycroftSkill, intent_file_handler


class Alfred(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alfred.intent')
    def handle_alfred(self, message):
        self.speak_dialog('alfred')


def create_skill():
    return Alfred()

