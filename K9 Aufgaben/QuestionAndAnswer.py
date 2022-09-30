from multiprocessing.connection import answer_challenge


class Question():

    def __init__(self, question, answer, credits):
        self.question = question
        self.answer = answer
        self.credits = credits


score = 0


class Game():
    score = 0

    def askAndAnswer(self, Question):

        if Question.answer == True:
            if input(Question.question).lower() == ("yes" or "correct"):
                self.score += Question.credits
                print("Thats correct\nGranted {} credits".format(Question.credits))
            else:
                print("NONONO thats WRONG!!!")
        else:
            if input(Question.question).lower() == ("no" or "wrong"):
                print("Thats correct\nGranted {} credits".format(Question.credits))
                self.score += Question.credits
            else:
                print("NONONO thats WRONG!!!")

    def startGame(self):
        question1 = Question("Am I blond ?", False, 10)
        question2 = Question("Is it sunny ?", False, 5)
        question3 = Question("Do I  have a Cat ?", True, 15)

        self.askAndAnswer(question1)
        self.askAndAnswer(question2)
        self.askAndAnswer(question3)
        print("Your final Score is {}".format(self.score))


game = Game()
game.startGame()
