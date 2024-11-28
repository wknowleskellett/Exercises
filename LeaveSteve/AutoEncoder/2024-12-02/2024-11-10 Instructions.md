# Exercises for 2024-12-02

For this week, Ryan has specific things he requested we work on. These are:

- Functions
- Classes
- Examples of New Pointers

There is one additional thing I want to do:

- First step toward Machine Learning

## Functions

Towers of Hanoi

You are given four disks, each 1, 2, 3, or 4 inches wide, respectively. The disks each have a peg-sized hole in the middle, and initially are stacked together on the first of three pegs.

Here is how we will represent this problem in code:

```python
peg_a = [4, 3, 2, 1]
peg_b = []
peg_c = []
```

Your task is to stack all the disks on a peg other than `peg_a` by moving the disks from peg to peg one at a time, while following these constraints:

- You can only move the rightmost disk from one peg, appending it to the rightmost spot on another peg.
- Each peg must remain with its disks sorted in descending order by size. In other words, you can never move a disk onto a peg that already contains a smaller disk.

If you can't solve this problem with four disks, try it with one, two, or three.

## Classes

For the previous problem, you used a class I wrote. Now it's your turn.

### Motivation

We're doing an exercise in immutability. We're going to make an immutable array that will mimic the immutability of strings.

> We discussed on the 2024-11-24 stream that when you copy a primitive type variable into a new variable, editing the copy never edits the original. We also discussed that while Strings are not a primitive type, editing copies of strings also doesn't edit the original because they are "immutable." When you think you're editing a string you're actually making a whole new string.
> 
>```python
>a = 'Hello'
>
># Here we copy `a` (the variables share the same pointer)
>b = a
># Here, although we don't say to make `b` a whole new string,
># by editing a string we have implicitly replaced it with a new, edited >copy, with a new pointer.
>b += ', World!'
>
># prints 'Hello'
>print(a)
># prints 'Hello, World!'
>print(b)
>```

Our array will be immutable in the same way that strings are:

- you won't be able to add or remove items after creation
- you will be able to use the data in the list

### Syntax

As an example, suppose we're coding a storybook character. Here's what it might look like. Skim this example and make note of things you do and don't recognize.

```python
class Character():
    def __init__(self, name, backstory):
        self.age = 0
        self.name = name
        self.backstory = backstory
    
    # Increase age by a specified number of years.
    # Default number of years if not specified is 1.
    def grow(self, years=1):
        if years < 0:
            raise ValueError(f'Years was {years}. Must be at least 0.')
        
        self.age += years
    
    # Return the name and backstory as a string,
    # separated by a line break.
    def get_bio(self):
        # This is an f-string. It just means if you put an "f"
        # before a string, you can use curly braces and type code
        # straight into the string.
        return f'{self.name}\n{self.backstory}'
    
    # Print the bio in the format specified in
    # `get_bio`
    def print_bio(self):
        print(self.get_bio())
```

You can skip the rest of the syntax section for now. Don't forget that it's here! Come back when you need it.

I'm going to go rapid-fire through the tools we're going to use, starting with the most basic. 

- `self`

A variable called `self` will pop up a lot. This variable is a box. You got something to do with the class? It goes in the box. It's where we store any information or functions associated with this class.

`self` is the pointer to the object itself you're coding. That's why all the functions need it - without it, they'd be lost trying to find all the stuff in the class.

- `__init__`

This function, called the "constructor," makes "instances" of your class. When you "instantiate" your class (make a new object of its type),these steps happen:

1. You call `Character('Sammie', 'Grew up as a baker')`. Notably you are not providing the `self` parameter. Sammie hasn't been instantiated yet, so there is no pointer value to provide.
2. Python looks at the `Character` class and makes an appropriate spot in memory for a new character. It makes a pointer to that memory, stores it in the variable `self`, and calls `Character.__init__(self, 'Sammie', 'Grew up as a baker')`.
3. `__init__` processes those inputs however it sees fit. It doesn't return anything, but the `Character()` function returns the pointer to the object.

At the end of the day you can ignore that those steps are happening, and just write:

```python
sammie = Character('Sammie', 'Grew up as a baker')
```

Feel free to assume that `self` appears in `__init__` and also is returned automatically by pure magic, and you will not have to know anything more.

> - "Class" - Your class is a template for representing something, like a character in a story might have an age, a name, and a backstory.
> - "Instance" - Instances are the specific object. A single instance of the `Character` class represents a single character. If you have two different characters in your story, you call the constructor twice, and get two instances.

- Calling instance methods (`self.my_method(item_a, item_b)`)

`self` has to be the first parameter in the function definition, but you don't include it when you call the function. 

Here's an excerpt from `Character`:

```python
# Return the name and backstory as a string,
# separated by a line break.
def get_bio(self):
    return f'{self.name}\n{self.backstory}'

# Print the bio in the format specified in
# `get_bio`
def print_bio(self):
    print(self.get_bio())
```

Take a close look at `print_bio`. It calls `get_bio` with nothing between the parenthesis, even though `get_bio` is defined with the parameter `self`. That's because `self` is implied by python to be the first argument when you write `self.get_bio()`, or `self.anything(even, with, parameters)`, for that matter.

> In Python, double underscores indicate variables or functions that have special behavior defined by the language. You should never name your own stuff using double underscores around it - only use the predifined ones.
> 
> The underscores are sometimes pronounced as "dunder," like "dunder init." It's not super common but you might hear me say it.

### Exercise

Make an immutable list. Go through this list of things mutable lists do and identify for each item whether it should be possible for an immutable list (one which cannot be modified after creation).

- Make it in the first place
- Append a new item to the end
- Insert a new item anywhere else in the list
- Find out the length of the list
- Find out the value at an index
- Remove an item from the end and return it
- Remove an item from an index and return it

Once you've identified which functions should be available, move on to the next step.

Write the basic structure of your `ImmutableList` class, including the `__init__` function that takes two parameters, `self` and `initial_list`. The body of the function should transfer a copy of `initial_list` into a "self dot" variable.

> This is the simplest syntax for copying an array:
> `array_copy = my_array[:]`

From there, add additional functions for each feature you think the `ImmutableList` should have. Each function should have the `self` parameter first, but you're responsible for adding your own parameters if the person calling the function needs to specify an index or something. You are also responsible for adding appropriate return values.

We're going to add one piece of functionality on top of the things a normal list can do - write an `as_list` function that returns a copy of the array.