Loops
A loop is a useful construct for when you'd like to repeat the same actions any number of times.
Whether you have a list or a dictionary, with 100 items or a million items, you can use a loop to help you work with that data.

For Loops
A for loop is useful when you'd like to iterate over each item in a list. The for loop allows you to repeat your action for every item in the list or for a specified number of items in the list.

Another example of a for loop that we can try is looping over a range of numbers.
We'll take a look at the Python range function as we do this.
First, we'll start with our for statement and then we'll name our individual variable number.
What we are asking this loop to do is to go over a range of numbers — range is a built-in Python function.
We can assign the range by assigning the first number, a comma, and then assigning the ending number. The ending number is not included.

While Loop-
A while loop will run any time a condition remains true.
Let's do a sample of a while loop.
In this script that we write, we will set a temperature in Fahrenheit to 40 degrees.
Then we'll make a loop that says, "while the temperature is greater than 32 degrees, we can print a message."
If we run this program now, we will have an infinite loop.
An infinite loop is a loop that doesn't have any stopping point. It just keeps going.
So, I'm going to go ahead and stop this loop and clear the console.
I need to create a way for this loop to stop and for the temperature variable to change.
For this sample, I'm going to use the Python decrement operator (-=), and all that does is decrease the variable by whatever number I choose.
I'm going to choose to decrease the temperature by 1 for this script.

Loop Control
You can control the flow of a loop with some loop statements. Python includes break, continue, and pass.
The **break** statement indicates that when you see it, the loop should end and go on to the next statement in the program that is outside of the loop.
The **continue** statement skips the current part of the loop and moves on to the next part of the loop.
The **pass** statement skips any part of the loop where pass appears. This is best used for testing code, but make sure you don't forget to remove the pass statement when you're ready for your code to go into production.
`