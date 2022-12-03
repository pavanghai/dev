class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        # current_question = self.q_list[self.q_num]
        # input(f"Q.{self.q_num}: {current_question.text} (True/False)?: ")

        u_answer = input(f"Q.{self.q_num + 1}: {self.q_list[self.q_num].text} (True/False)?: ").lower()
        if self.q_list[self.q_num].answer.lower() == u_answer:
            self.score += 1
            self.q_num += 1
        print(self.score, self.q_num)

# TODO: Create the class
# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz
