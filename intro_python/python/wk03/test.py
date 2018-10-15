# Ask Question from data Dictionary (hash)
# Amend hash data add key pairs
#  - goto record fo YES
#  - goto record for NO 
data = {
    "1":{"Q": "Is it an aquatic animal", "Y":"2", "N":"3"},
    "2":{"Q": "Is it a fish", "Y":"4", "N":"5"},
    "3":{"Q": "Does it eat meat", "Y":"6", "N":"7"},
    "4":{"A": "All work and no play makes Matthew a dull boy"},
    "5":{"A": "Seal"},
    "6":{"A": "Dog"},
    "7":{"A": "Cow"},
}

# A simple Y/N validation function
# q_text = Question text
# Get question from data

# Set my starting question id
q_id = '1'

# I start without an answer
ans = 'N'

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
while ans == 'N':
    if "Q" in data[q_id]:
        q_txt = data[q_id]['Q']
        if get_answer(q_txt):
            q_id = data[q_id]["Y"]
            # Get next record ID
        else:
            q_id = data[q_id]["N"]
            # Get next record ID
    else:
        print (data[q_id]['A'])
        

    # Is this an answer? 
    # If so print out and stop
    # If so print out and stop
   
