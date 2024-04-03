# Linked Lists

Lists will always be used in almost all projects because they are amazing at holding related data into one variable. Because lists are so essential programmers have developed the linked list which is a major part of many coding projects because of its many use cases as well as efficiency that out performs normal lists in many ways.

Navigating and using a linked list cannot be learned as quickly as normal arrays or lists, but once mastered it will be a skill that you will use the rest of the time you are coding.

Each list is composed of a `head` and a `tail` and each value in the list will either point towards another value or a a null value if it is at the beginning or end of the list which would mean it is the `head` or `tail` value respectively. Each value is a `node` which can point to the previous value and the next value. Here is an image to represent a basic doubly pointed list meaning that each piece of data has a previous value as well as a next value. 

![Doubly Linked List](images/doubly_linked_list.png)

## Performance

Here is a table describing the performance of a normal array compared to a linked list to show why it is a good choice when making programs

|Function     |Array Performance|Linked List Performance|
|-------------|-----------------|-----------------------|
|Insert Front |O(n)             |<b>O(1)                |
|Insert Middle|O(n)             |O(n)                   |
|Insert End   |O(1)             |O(1)                   |
|Remove Front |O(n)             |<b>O(1)                |
|Remove Middle|O(n)             |O(n)                   |
|Remove End   |O(1)             |O(1)                   |

As you can see the linked list either matches or beats the performance of a normal array especially when involving the front of a list. I bolded the performances that were better than the array performance.

## Making a Node

As I mentioned before every linked list is made up of a head and tail with values in between them all called as nodes.

To create a node in Python the most common way is to create a class that will define the characteristics of the node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

This function sets the default prev and next values as None so that later functions in the linked list class can assign each value correctly.

## Class and Functions for a Linked List

All of the functions that will be used to populate a linked list will be within the `"class LinkedList:"` code. Buckle up because in order to make a linked list have all the functionality a normal list has you need to create some basic functions.

At the bottom of all these functions I will include a link to a Python file that will have all the functions pasted for easy use.

### Initiate Linked List Function

This function will initiate the linked list by assigning the head and tail values as None since nothing has been added yet.

```python
def __init__(self):
    self.head = None
    self.tail = None
```

### Head and Tail Functions

For the following functions we use the Node values `.next` and `.prev` to point every Node to the Node before or after it. I will use the term `next point` or `prev point` in the comments to clarify which way the specific Node is being pointed. This will make a doubly pointed linked list with a head and tail. Use the comments to understand what each line of code is doing. 

```python
def insert_head(self, data):
    new_node = Node(data) # create new Node

    # If list is empty then both head and tail will be set to the new node.
    if self.head is None:
        self.head = new_node 
        self.tail = new_node
    else:
        new_node.next = self.head # next point new Node to old head
        self.head.prev = new_node # prev point old head to new Node
        self.head = new_node      # set head to new Node
```


```python
def insert_tail(self, data):
    new_node = Node(data)
    # If list is empty then both head and tail will be set to the new node.
    if self.tail is None:
        self.tail = new_node
        self.head = new_node
    else:
        new_node.prev = self.tail # prev point new Node to old tail
        self.tail.next = new_node # next point old tail to new Node
        self.tail = new_node      # set tail to new Node
```

```python
def remove_head(self):

    # if only one item in list set head and tail to None
    if self.head == self.tail:
        self.head = None
        self.tail = None
    else:
        self.head.next.prev = None # prev point the Node the head was pointing to to None
        self.head = self.head.next # set the head as the Node the head was previously pointing to
```

```python
def remove_tail(self):

    # if only one item in list set tail and head to None
    if self.tail == self.head:
        self.tail = None
        self.head = None
    else:
        self.tail.prev.next = None # next point the Node the tail was pointing to to None
        self.tail = self.tail.prev # set the tail as the Node the tail was previously pointing to
```

### Inner Node Functions

These functions are a little bit harder to follow, but I drawing out inserting the value into the list and assigning where each value needs to go helps me understand the process. Here is an image to help show what is happening when inserting a Node after another Node.

![Insert After Node](images/insert_after_linked_list.png)

```python
def insert_after(self, data, new_data):
    # start search at the head value
    current = self.head

    # keep iterating until tail is reached
    while current is not None:

        if current.data == data:

            # use logic from previous function if the Node is at the tail
            if current == self.tail:
                self.insert_tail(new_data)
            else:
                new_node = Node(new_data) # create new Node with the new value
                new_node.prev = current   # prev point new Node to the current Node
                new_node.next = current.next # next point new Node to the Node that was after the current Node
                current.next.prev = new_node # prev point the Node was was after the current Node to the new Node
                current.next = new_node   # next point the current Node to the new Node
            return    
        current = current.next # if not right value go to next Node in list
```
To remove a Node you just need to have the Nodes before and after the Node being removed pointed to each other.

```python
def remove(self, data):
    # start search at the head value
    current = self.head

    # keep iterating until tail is reached
    while current is not None:

        if current.data == data:

            # use logic from previous function if the value is at the head
            if current == self.head:
                self.remove_head()

            # use logic from previous function if the value is at the tail
            elif current == self.tail:
                self.remove_tail()
            else:
                current.prev.next = current.next # next point the Node before the current Node to the Node after the current Node
                current.next.prev = current.prev # prev point the Node after the current Node to the Node before the current Node
            return
        current = current.next # if not right value go to next Node in list
```
To replace a Node's value just set the current Node's value to the new value.

```python
def replace(self, data, new_data):
    # start search at the head value
    current = self.head

    # keep iterating until tail is reached
    while current is not None:
        if current.data == data:
            current.data = new_data # set current data value to the new value
            return
        current = current.next # if not right value go to next Node in list
```

### Print List Function


```python
def print_list(self):
    # start search at the head value
    current = self.head

    # keep iterating until tail is reached
    while current is not None:
        print(current.data, end=', ')
        current = current.next
    print()
```
All of these functions together can make a linked list with a lot of useful qualities. To use all of the functions you will just need to type create a class object for example: `linked_list = LinkedList()` and then call a function by typing `"linked_list.<function>"`.

Here is a Python file with all of the classes and functions: [Python Classes and Functions](python_examples/linked_list_classes_functions.py)

## Example : To do List

This code makes a simple to do list with different tasks that someone has in a day. We can use most of the functions that we defined previously to accomplish the list.

```python
# ^^^ paste classes and functions above ^^^

# Create a linked list object
to_do_list = LinkedList()

# Add tasks to the to-do list
to_do_list.insert_tail("Buy groceries")
to_do_list.insert_tail("Finish homework")
to_do_list.insert_tail("Go for a run")

# Print the to-do list
print("To-Do List:")
to_do_list.print_list()

# Remove a task from the to-do list
to_do_list.remove("Finish homework")

# Replace a task in the to-do list
to_do_list.replace("Go for a run", "Walk the dog")

# Print the updated to-do list
print("\nUpdated To-Do List:")
to_do_list.print_list()

```

## Problem to Solve : Playlist

Create a playlist where you can add, remove, and replace songs. As an extra challenge code an extra function that will print the list of songs in reverse order to get practice with iterating through a linked list.

### Test Cases:

For all of the test cases have a `playlist.print_list()` to make sure that items are being added and removed correctly.

- Add an item to your playlist
- Remove an item from your playlist
- Replace a song from your playlist
- Add a few songs to a playlist and use the reverse function that you created to verify that it printed out in the reverse order that you put it in.

You can check your code with the solution here: [Solution](python_examples/linked_list.py)

[Back to Welcome Page](welcome.md)


