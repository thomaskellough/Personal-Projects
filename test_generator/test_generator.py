import openpyxl
import random

path = 'ENTER_PATH_TO_EXCEL_FILE_HERE'


class MyTestGenerator:
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column
    max_row = sheet_obj.max_row

    questions_and_answers = {}
    test_key = {}
    current_unit_list = []
    previous_unit = []
    not_shuffled_answer_choices = []

    def __init__(self, current_unit, current_unit_num_questions, previous_unit_num_questions):
        self.current_unit = current_unit
        self.current_unit_num_questions = current_unit_num_questions
        self.previous_unit_num_questions = previous_unit_num_questions

    def create_random_test(self):
        for row in range(2, self.max_row + 1):
            if self.sheet_obj.cell(row=row, column=3).value != self.current_unit:
                self.previous_unit.append(self.sheet_obj.cell(row=row, column=1).value)
            else:
                self.current_unit_list.append(self.sheet_obj.cell(row=row, column=1).value)
        current_unit_unique_id = random.sample(self.current_unit_list, self.current_unit_num_questions)
        previous_unit_unique_id = random.sample(self.previous_unit, self.previous_unit_num_questions)
        all_questions_unique_id = previous_unit_unique_id + current_unit_unique_id

        for row in range(2, self.max_row + 1):
            answer_choices = []
            if self.sheet_obj.cell(row=row, column=1).value in all_questions_unique_id:
                question = self.sheet_obj.cell(row=row, column=4).value
                for occurrence in [' I.', ' II.', ' III.']:
                    question = question.replace(occurrence, '\n\t' + occurrence)
                for column in range(5):
                    answer = self.sheet_obj.cell(row=row, column=column + 5).value
                    answer_choices.append(answer)
                self.questions_and_answers.update({question: answer_choices})

    def write_test(self):
        test_file_obj = open('test_file.txt', 'w')
        test_file_obj.write('Name:\nDate:\nFinal Exam\n\n')

        for count, (key, value) in enumerate(self.questions_and_answers.items()):
            question = f'{key}'
            shuffled = value
            self.not_shuffled_answer_choices.append(value[0])
            random.shuffle(value)
            test_file_obj.write(f'\n{count + 1}. {question}\n')
            for choice, answer in enumerate(['A', 'B', 'C', 'D', 'E']):
                if shuffled[choice] == self.not_shuffled_answer_choices[count]:
                    self.test_key.update({count + 1: answer})
                test_file_obj.write(f'\t\t{answer}) {shuffled[choice]}\n')
        test_file_obj.write('\nAnswer Key\n\n')
        for key, value in self.test_key.items():
            test_file_obj.write(f'{key}) {value}\n')
        self.wb_obj.close()
        test_file_obj.close()


if __name__ == '__main__':
    p = MyTestGenerator(current_unit='Taxonomy', current_unit_num_questions=6, previous_unit_num_questions=4)
    p.create_random_test()
    p.write_test()
