print("I am your personal tutor, Sol," \
" and at present, I have limited functionality.\n\nThis application is currently in alpha, \nHowever, I aim to guide you through this application so you can learn, or revise, mathematics for machine learning" \
" and leave with a solid grasp of these complex concepts.\n")
print("There are 3 overaching sub-disciplines in mathematics for machine learning: Linear Algebra, Calculus, and PCA. SolveMyMatrix currently runs through the key concepts in linear algebra:"
    "\nVectors, Matrices, Dot product, Matrix Multiplication, Linear Mappings, Bases, Rank and more...")

def vectors ():
    print("Linear algebra is the study of vectors. In general, vectors are special objects" \
    " that can be added and multiplied by scalars to create another object of the same kind. From an abstract mathematical perspective" \
    " any object that satisfies these two properties can be considered a vector.\n" \
    "The vector type which we will focus on is one of the more abstract types: 'tuples of n real numbers'")
    print()
    print("e.g.,    a = [1,2,3], \nwhich is an element of R^3\n\n")
    print("Linear algebra plays an important role in machine learning and mathematics. A valuable resource is 'The Essence of Linear Algebra' Series by 3Blue1Brown\n\n")
    print("Systems of linear equations can be written as vectors:")
    print("The equation: \n\nV: ax + by + c = s\n\nWhere a = 2, b = 1, c = 2\nSuch that\n\nV = 2x + y + 2\n\nCan be written as the vector V=[2,1,2]\n\n It is important to note that this array would be the row" \
    " of the matrix, not to be confused with the transpose of a column vector. Numpy is written up using this notation.")
vectors()
