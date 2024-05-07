"""
Question-3: Write a simple quote-of-the-day program. The program should contain a list of quotes, and
when the user runs the program, a randomly selected quote should be printed.

"""

import numpy as np

QOD=["You’re braver than you believe, and stronger than you seem, and smarter than you think.","Keep your face to the sunshine and you cannot see a shadow."
     ,"In every day, there are 1,440 minutes. That means we have 1,440 daily opportunities to make a positive impact.","The only time you fail is when you fall down and stay down.",
     "Happiness is an attitude. We either make ourselves miserable, or happy and strong. The amount of work is the same.","It’s not whether you get knocked down, it’s whether you get up.",
     "The struggle you’re in today is developing the strength you need tomorrow.","Happiness is the only thing that multiplies when you share it.",
     "The happiness of your life depends upon the quality of your thoughts.","Once you replace negative thoughts with positive ones, you’ll start having positive results.",
     "Positive thinking will let you do everything better than negative thinking will.","The way I see it, if you want the rainbow, you gotta put up with the rain.",
     "The more you praise and celebrate your life, the more there is in life to celebrate.","If you want light to come into your life, you need to stand where it is shining.",
     "The good life is a process, not a state of being. It is a direction, not a destination.","A truly happy person is one who can enjoy the scenery while on a detour.",
     "You’re off to great places, today is your day. Your mountain is waiting, so get on your way.","Winning doesn’t always mean being first. Winning means you’re doing better than you’ve done before."] #Quote of The Day

index=np.random.randint(0,18)

print("Quote Of The Day is: ")

print(QOD[index])

