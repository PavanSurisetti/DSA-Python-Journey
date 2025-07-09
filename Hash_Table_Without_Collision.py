class hashtable:
    def __init__(self):  # Constructor to initialize the hash table
        self.size=10  # Setting the fixed size of the hash table to 10
        self.table=[None]*self.size  # Creating a list with 10 None values (empty slots)

    def __hash__(self,key):  # Hash function to compute the index from the key
        return hash(key)%self.size  # Modulo operation ensures index is within table size

    def insert(self,key,value):  # Method to insert a key-value pair
        i=self.__hash__(key)  # Generate index using hash function
        if(self.table[i]==None):  # Check if the slot is empty
                self.table[i]=(key,value)  # If empty, insert the key-value pair
        else:
                print('collision occured!')  # If not empty, it means collision occurred

    def get(self,key):  # Method to retrieve value using a key
        i=self.__hash__(key)  # Get the index for the key
        if(self.table[i] is not None and self.table[i][0]==key):  # Check if key exists at the index
            return self.table[i][1]  # Return the value if key matches
        return None  # Return None if key not found

    def display(self):  # Method to display the hash table
        for i in range(self.size):  # Loop through each index in the table
            print(f'Index:{i} :{self.table[i]}')  # Print the index and the stored key-value pair or None

h=hashtable()  # Creating an instance of the hashtable class
h.insert('Ganesha',19)  # Inserting key 'Ganesha' with value 19
h.insert('Pavan',18)  # Inserting key 'Pavan' with value 18
h.insert('alex',20)  # Inserting key 'alex' with value 20
h.display()  # Display the contents of the hash table
