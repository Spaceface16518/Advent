#  Copyright (c) 2019 Amrit Rathie
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
import sys

import yaml

if __name__ == '__main__':
    path = sys.argv[1]  # TODO: handle index error
    file = open(path, mode='r')  # Load file
    story_doc = yaml.safe_load(file)  # Parse file into YAML
    index = 0  # The index of the current question
    while True:
        frame = story_doc[index]  # The actual current question
        print(str(frame['question']))  # Print the question
        try:
            answers = dict(frame[
                               'answers'])  # If there are answers, build
            # them into a dictionary
        except LookupError:
            break  # If there's no answer field, this is an end question
        print("Choices: %s" % [choice_text for choice_text in
                               answers.keys()])  # Print the answer choices
        next_question_index = -1  # Because an index cannot be -1
        for i in range(0, 5):
            choice_input = str(
                input("Choose an answer: "))  # Get the user input
            try:
                next_question_index = int(
                    answers[choice_input])  # Parse the input
            except LookupError:
                print("That wasn't an answer choice, dummy!\nTry again! You "
                      "have %i more tries until this program crashes" % (4 -
                                                                         i))
                continue
            break
        if next_question_index == -1:
            print("You insist on being stupid? Fine. I'm done")
            raise TimeoutError(
                "Number of input tries exceeded")  # TODO: different error?
        else:
            index = next_question_index - 1  # Our data is 0-index
