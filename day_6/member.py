class Member:
    def __init__(self, member_entry):
        self.questions_answered_with_yes = member_entry

    def member_answered_same_questions_with_yes(self, questions):
        member_answered_same_questions = True
        for char in questions:
            member_answered_same_questions = member_answered_same_questions and char in self.questions_answered_with_yes
        return member_answered_same_questions
