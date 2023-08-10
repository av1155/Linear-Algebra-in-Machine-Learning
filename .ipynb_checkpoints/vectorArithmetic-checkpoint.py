import numpy as np

a = np.array([20, 40, 60])
b = np.array([10, 40, -15])
c = np.array([11, 31, 72, 28])

# Vector Addition
print(f"The addition of vectors a and b is: {a + b}")

try:
    print(a + c)  # Error because dimensions are not the same.
except Exception as e:
    print(
        f"The {e}because the dimensions of the vectors are not the same... they cannot be added."
    )

print()  # Space

# Vector Subtraction
print(f"The difference between the vectors a and b is: {a - b}")

try:
    print(a - c)  # Error because dimensions are not the same.
except Exception as e:
    print(
        f"The {e}because the dimensions of the vectors are not the same... they cannot be subtracted."
    )

print()  # Space

# Vector Multiplication
print(f"The multiplication of array a and b is: {a * b}")

print()  # Space

# Vector Division
print(f"The division of vectors a and b is: {a / b}")

print()  # Space

# Vector Scalar Multiplication
scalar = 2
list_a = [10, 11, 12, 13, 14, 15]

print(f"Scalar: {scalar}")
print(f"List: {list_a}")

print()  # Space

# Convert and print the regular list to a numpy array list and multiply by scalar.
list_as_array = np.array(list_a)
print(f"A scalar multiplied by an array list results in: {scalar * list_as_array}")
# Each number in the list is multiplied by the scalar and the list is modified with the new values.

print()  # Space

# The following is `not` vector scalar multiplication, it is just a list being multiplied by a number, in this case, 2.
print(f"A scalar multiplied by a list results in: {scalar * list_a}")

vectorAsList = [1, 2, 3, 4, 5]
vectorAsArray = np.array([1, 2, 3, 4, 5])
rowVector = np.array([[1, 2, 3, 4, 5]])
columnVector = np.array([[1], [2], [3], [4], [5]])


"""
Question 1 of 3
What is the difference between a scalar and a vector?

a scalar is a number and a vector is an ordered list of numbers that has both dimensionality and orientation
Correct

Question 2 of 3
What are the correct ways to define a vector? 

A. vectorAsTuple = [(1,2,3,4,5)]

B. vectorAsList = [1,2,3,4,5]

C. vectorAsArray = np.array([1,2,3,4,5])

D. columnVector = np.array([ [1,2],[3,4],[5]])

E. rowVector = np.array([ [1,2,3,4,5] ])

B,C,E
Correct

Question 3 of 3
In which case will the direction of the vector change in a case of vector scalar multiplication?

in the case scalar is negative
Correct

"""
print()  # Space

# Vector Dot Product
# The dot product is the sum of the products of the corresponding entries of the two sequences of numbers.
# The dot product of two vectors is a scalar.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# a_dot_b = 1*4 + 2*5 + 3*6 = 32
a_dot_b = np.dot(a, b)

print(f"The dot product of a and b (a.b) is: {a_dot_b}")

# There are three different ways to represent the dot product of two vectors.
"""
a**T*b
a.b
< a, b >

"""


'''
QUIZ 2:

Question 1 of 3
Which function do we use to calculate a magnitude of a vector?

- lng.norm()
Correct

Question 2 of 3

What is the property of the basis vectors?

- They aren't unique.

- They are linearly independent.

- all of these answers
Correct

- They span the whole space.

Question 3 of 3
What is a property of the dot product? 

A. It is a commutative.

B. It has the same dimensionality.

C. It is distributive over addition.

D. It has orientation and dimensionality.


- A,C
Correct

'''