# Define a class for Hash Table
class hashTable:
    # Constructor to initialize size and the table
    def __init__(self,size):
        self.size = size  # Store the size of the hash table
        self.table = [None] * self.size  # Create a list (hash table) with None values
    
    # Hash function to calculate index using modulo
    def hash(self, key):
        return (key % self.size)

    # Function to insert a key-value pair into the hash table
    def inserting(self, key, value):
        i = self.hash(key)  # Get index using hash function
        original_key = i    # Store original index to check if we've looped the entire table

        # Loop to find the next available empty slot
        while (self.table[i] is not None):
            i = (i + 1) % self.size  # Move to next index (circular using modulo)
            if (i == original_key):  # If we come back to the original position, table is full
                print('Hash Table Full!')
                return

        # Found an empty slot, insert the key-value pair
        self.table[i] = (key, value)

    # Function to display the hash table
    def display(self):
        for i in range(self.size):
            print(f'{i}:{self.table[i]}')  # Print index and its value

# Create a hash table of size 10
h = hashTable(10)

# Insert key-value pairs into the hash table
h.inserting(2, 4)
h.inserting(12, 2)  # Collision with key 2; handled by linear probing

# Display the hash table contents
h.display()
