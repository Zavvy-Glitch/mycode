#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    trivia challenge """

import html

def main():


    trivia= {
            "category": "Entertainment: Film",
            "type": "multiple",
            "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
            "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
            "incorrect_answers": [
                "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                "&quot;Round up the usual suspects.&quot;"
            ]
        }   
        
    question = trivia["question"]
    correct = trivia["correct_answer"]
    incorrect1 = trivia["incorrect_answers"][0]
    incorrect2 = trivia["incorrect_answers"][1]
    incorrect3 = trivia["incorrect_answers"][2]

    print(f""" {html.unescape(question)} 
                        A - {html.unescape(incorrect1)}
                        B - {html.unescape(incorrect3)}
                        C - {html.unescape(incorrect2)}
                        D - {html.unescape(correct)} """)

    answer = input(">")

    correctAnswer = "d"
    if answer.lower() != correctAnswer :
        print(" Sorry, that's incorrect ")

    else:
        print(" Congrats, that's correct! " )

main()
