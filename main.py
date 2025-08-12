import numpy as np
import matplotlib as plt 
from sympy import Matrix, latex
import solvers.solver as sol
import study.tutor as tutor




print()
print("Welcome to SolveMyMatrix!\nYour One-Stop-Shop for all things Matrix & Vector Mathematics\n") # This line introduces the program.

# Currently working on getting this code block working in jupyter 'unit_tests'
knowledge_level = input("""Before we proceed what is your current level of understanding in Mathematics for Machine Learning?
                        a. Beginner
                        b. Intermediate
                        c. Expert\n""")
if knowledge_level in ('Beginner', 'a', 'beginner','1','A'):
    overview=input("Would you like a brief overview of vector mathematics before proceeding [Y/N]: ?")
    pass
    # if overview in ('Y', 'y','yes','Yes'):
    #     study.tutor.prompt_a()
elif knowledge_level in ('Intermediate','intermediate','b','B','2'):
    pass
elif knowledge_level in ('Expert','expert','c','C','3'):
    pass
else:
    print("Invalid input!")

print("What would you like to work on today?:")

# Next is to iterate over this conditional 'if' statement so that the program only runs if a valid input is selected.
user_task = input("""
                 [1] Equation Solver
                 [2] Matrix Operations
                 [3] Explore 3D Tensors 
                  Select a task by entering the corresponding task value: """)

if user_task  == '1':
    print("You have chosen 'Equation Solver'")
    sol.equation_solver()
elif(user_task) == '2':
    print("You have chosen 'Matrix Operations'")
    sol.matrix_solver()
elif(user_task) == '3':
    print("""This feature is in alpha.
          You have chosen a feature that is in development, and not currently available.
          Terminating program... """)
    quit
else:
    print("You have entered an invalid input.\n Terminating program...")