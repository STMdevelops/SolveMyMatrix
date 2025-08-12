from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import Matrix, latex, solve_linear_system, Eq
import sympy as sp 
from IPython.display import display
import numpy as np

# ### EQUATION SOLVER ###
def equation_solver():    
    # This is a conversion loop, which converts a to an integer without throwing an error.
    while True:
        try: # Tests a code block, to see if it raises an error
            a1 = int(input("Enter the first coefficient, a: "))
            break # Accepts the code block if no error is thrown and exits the loop.
        except ValueError:
            print("Invalid entry. Datatype must be an integer.") # Prints a notice to the user and repeats the loop again. 

    while True:
        try:
            b1 = int(input("Enter the second coefficient, b: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")

    while True:
        try:
            c1 = int(input("Enter the constant, c: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")

    while True:
        try:
            a2 = int(input("Enter the first coefficient of equation 2, a2: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")

    while True:
        try:
            b2 = int(input("Enter the second coefficient of equation 2, b2: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")

    while True:
        try:
            c2 = int(input("Enter the second constant, c2: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
            
    eq1 = sp.Function('eq1')
    eq2 = sp.Function('eq2')

    x, y = sp.symbols('x y')

    # This system of LaTeX equations and output will not show up in the VSCode terminal but will in an environment configured to display LaTeX.
    eq1 = Eq(a1*x+b1*y,c1)
    eq2 = Eq(a2*x+b2*y,c2)
    display(eq1) # Search up how to get it to display using LaTex
    display(eq2)

    row1 = [a1,b1,c1]
    row2 = [a2,b2,c2]

    system = Matrix((row1, row2))
    display (system)

    matrix_form = ([[row1],[row2]])
    print(f"This is our numpy array:\n\n {matrix_form}\n\nIt is how we will compute this system of equations: using a matrix style computational method.")
    print("\nThe solution to this system of equations is:")
    display(solve_linear_system(system, x, y)) # Our system of linear equations has been solved in this instance.
    print()
if __name__ == '__main__.py': ## This line ensures the equation_solver function only runs when it is called in main.py, else it would run once the script is initialised.
    equation_solver()


### Matrix Solver ###
def matrix_solver():
    print("The current release (v0.1) only supports 3D matrices.\n" \
    "Please enter the matrix you wish to solve.")
    while True:
        try:
            a_00 = int(input("Enter value a_00: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            a_01 = int(input("Enter value a_01: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            a_02 = int(input("Enter value a_02: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            a_10 = int(input("Enter value a_10: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            a_11 = int(input("Enter value a_11: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            a_12 = int(input("Enter value a_12: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            a_20 = int(input("Enter value a_20: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            a_21 = int(input("Enter value a_21: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            a_22 = int(input("Enter value a_22: "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            s1 = int(input("Enter the first solution (RHS): "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            s2 = int(input("Enter the second solution (RHS): "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    while True:
        try:
            s3 = int(input("Enter the third solution (RHS): "))
            break
        except ValueError:
            print("Invalid entry. Datatype must be an integer.")
    user_matrix = ([[a_00,a_01,a_02],[a_10,a_11,a_12],[a_20,a_21,a_22]])
    s = ([s1,s2,s3])
    print(f"The following matrix has been inptted by the user: \n\n{user_matrix}\n\n")
    matrix_validator = input("Is this correct [Y/N]?\n")
    if matrix_validator == 'Y' or 'y':
        user_request = ("Would you like to continue with solving the matrix and/or finding the inverse [Y/N]?: ")
        if user_request == 'Y' or 'y':
            solution = np.linalg.solve(user_matrix,s)
            matrix_inv = np.linalg.inv(user_matrix)
            print(solution, matrix_inv) # update this to print separately...
        else:
            print ("Terminating Program... Please restart the session. ")
    else:
        print("Terminating Program... Please restart the session. ")
print()
if __name__ == '__main__.py':
    matrix_solver()
# Write out this function to solve 2D, 3D and 4D matrices input by the user. Please note, main.py will handle the user input, just write out the system of functions which will handle this.
# Maybe turn matrix_solver into a class instead and have each dimensionality be a separate function in the class.


## Tasks for next session: Finish the conditionals, create a loop, finalise the script (Comment out 3D tensors option in main.py), and mark as completed in project task list.
