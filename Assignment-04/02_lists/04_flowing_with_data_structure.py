# In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

# However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

# Here is an example run of this program (user input in bold italics):

# Enter a message to copy: Hello world!

# List before: []

# List after: ['Hello world!', 'Hello world!', 'Hello world!']

# (Note. The concept of immutable/mutable data types is called mutability. Be careful because different programming languages have different rules regarding mutability!)