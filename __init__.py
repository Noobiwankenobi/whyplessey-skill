from mycroft import MycroftSkill, intent_file_handler


class Whyplessey(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('whyplessey.intent')
    def handle_whyplessey(self, message):
        self.speak_dialog('whyplessey')


def create_skill():
    return Whyplessey()

