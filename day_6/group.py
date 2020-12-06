from day_6.member import Member


class Group:
    def __init__(self, group_entries):
        self.group_members = []
        self.add_group_members(group_entries)

    def add_group_members(self, group_entries):
        for member_entry in group_entries:
            self.group_members.append(Member(member_entry))

    def questions_anyone_answered_with_yes_in_group(self):
        already_answered_questions = []
        for member in self.group_members:
            for char in member.questions_answered_with_yes:
                already_answered_questions.append(char)
        return sorted(list(dict.fromkeys(already_answered_questions)))

    def questions_everybody_answered_with_yes_in_group(self):
        answered_questions = self.questions_anyone_answered_with_yes_in_group()
        answered_questions_from_everybody = []
        for char in answered_questions:
            keep_question = True
            for member in self.group_members:
                keep_question = keep_question and member.member_answered_same_questions_with_yes(char)
            if keep_question:
                answered_questions_from_everybody.append(char)
        return answered_questions_from_everybody
