from Multiset import Multiset

def main():
    while True:
        print('''
                Enter multiset in the following format: A = {a, b, {c, d}, a}
                Available commands:
                    list            check list of multisets
                    delete a        remove element from multiset
                    ndelete a:2     remove a specified number of instances of an element
                    is empty A      check for empty multiset
                    cardinality A   count cardinality A
                    rm A            remove multiset A
                    A + B           union A and B
                    A += B          save result union in A
                    A - B           substract from A to B
                    A -= B          save result substaction in A
                    A * B           intersection between A and B
                    A *= B          save result intersection in A
                    bolen A         create bolean from A
                    exit            stop programm
                ''')
    
        choice = input('')