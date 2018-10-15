# Ask Question from data Dictionary (hash)
data = {"Q": "Is it an aquatic animal"}

# A simple Y/N validation function
# q_text = Question text
# Get question from data
q_txt = ''

def get_answer (q_txt):
    gotanswer = False
    while gotanswer == False:
        x = str(input(q_txt + '? [Y/N]: ')).upper()
        if x == 'Y':
            return True  
            gotanswer = True
        if x == 'N':
            return False
            gotanswer = True


# Ask question and define result
if get_answer(q_txt):
    print('Yes')
else:
    print('No') 