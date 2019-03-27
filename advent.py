import sys

import yaml

if __name__ == '__main__':
    path = str(sys.argv[1])  # TODO: handle index error
    file = open(path, mode='r')  # Load file
    story_doc = yaml.safe_load(file)  # Parse file into YAML
    index = 0  # The index of the current question
    while True:
        question = dict(story_doc[index])  # The current question object
        print(str(question['question']))  # Print the question
        try:
            answers = dict(question['answers'])  # If there are answers, build them into a dictionary
        except LookupError:
            break  # If there's no answer field, this is an end question
        print('Choices: %s' % [str(choice_text) for choice_text in answers.keys()])  # Print the answer choices
        next_question_index = -1  # Because an index cannot be -1
        for i in range(0, 5):
            choice_input = str(input('Choose an answer: '))  # Get the user input
            try:
                next_question_index = int(answers[choice_input])  # Parse the input
            except LookupError:
                print(
                    f"That wasn't an answer choice, dummy!\nTry again! You have {4 - i:d} more tries until this "
                    f"program crashes")
                continue
            break
        if next_question_index == -1:
            print('You insist on being stupid? Fine. I\'m done')
            raise TimeoutError('Number of input tries exceeded')  # TODO: different error?
        else:
            index = next_question_index - 1  # Our data is 0-index
