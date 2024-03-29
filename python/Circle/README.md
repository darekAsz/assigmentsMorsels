The circle should have a radius, a diameter, and an area. It should also have a nice string representation.

For example:

>>> c = Circle(5)

>>> c

Circle(5)

>>> c.radius

5

>>> c.diameter

10

>>> c.area

78.53981633974483


Additionally the radius should default to 1 if no radius is specified when you create your circle:

>>> c = Circle()

>>> c.radius

1

>>> c.diameter

2

There are three bonuses for this exercise.

Bonus 1

For the first bonus, make sure when the radius of your class changes that the diameter and area both change as well: ✔️

>>> c = Circle(2)

>>> c.radius = 1

>>> c.diameter

2

>>> c.area

3.141592653589793

>>> c

Circle(1)

Bonus 2

For the second bonus, make sure you can set the diameter attribute in your Circle class and the radius will update and also that you cannot set the area (setting area should raise an AttributeError): ✔️

>>> c = Circle(1)

>>> c.diameter = 4

>>> c.radius

2.0

Bonus 3

For the third bonus, make sure your radius cannot be set to a negative number: ✔️

>>> c = Circle(5)

>>> c.radius = 3

>>> c.radius = -2

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
Hints

Hints for when you get stuck (hover over links to see what they're about):

How do I write a class in Python?
Where to find the value of pi
Creating a string representation for your class
How to make diameter and area auto-update
Updating the diameter
Making attributes read-only
Tests

Automated tests for this week's exercise can be found here. You'll need to write your function in a module named circle.py next to the test file. To run the tests you'll run "python test_circle.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.

If you'd like a hint for solving this one, search for getter and setter methods in Python and see what the Internet says (there's a more specific name for these but I'm only going to give you this hint right now).
