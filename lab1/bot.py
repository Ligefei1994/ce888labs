from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    emodetect=emo.detect_emotion_in_raw(trigger)
    print(trigger, emodetect,trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
