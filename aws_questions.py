from ques import Questions

prompt_questions = [
    """----------------------------------------------------------------------------------------------------
    \nWhy is AWS more economical than traditional data centers for applications with varying compute workloads?
    \n(A) Amazon EC2 costs are billed on a monthly basis
    \nB) Users retain full administrative access to their Amazon EC2 instances.
    \nC) Amazon EC2 instances can be launched on demand when needed.
    \nD) Users can permanently run enough instances to handle peak workloads.
    \n\nAnswer : """,
    """\n----------------------------------------------------------------------------------------------------\nWhich AWS service would simplify the migration of a database to AWS?\n
    \nA) AWS Storage Gateway
    \nB) AWS Database Migration Service (AWS DMS)
    \nC) Amazon EC2
    \nD) Amazon AppStream 2.0
    \n\nAnswer : """
]

questions = [
    Questions(prompt_questions[0], "b"),
    Questions(prompt_questions[1], "b")
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    
    quotient = (score/(len(questions)))
    percentage = int(quotient * 100)
    percentage = str(percentage)
    
    print("You got " + str(score) + "/" + str(len(questions)) + " correct - " + percentage + "%")
   
run_test(questions)