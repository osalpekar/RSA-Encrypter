'''
Receiver class does the following:
    - key generation
    - encryption
    - decryption

'''
from random import randint

class Receiver:
    
    UPPER_BOUND = pow(2, 512)

    def __init__(self):
        p, q = self.handle_prime()
        N = self.calc_N(p,q)
        e = self.calc_e(p,q)
        self.public_key = (N, e)
        self.private_key = self.calc_d(e, p, q)
  
    #handle_prime returns 2 unequal numbers that are prime with high probability
    def handle_prime(self):
        p = self.get_prime()
        q = self.get_prime()

        if p != q:
            return p, q
        else:
            while not self.fermat_test(q+1):
                q+=1
            return p, q
    
    #get_prime generates a random prime number and calls fermat_test to test for primality
    def get_prime(self):
        x = randint(2, self.UPPER_BOUND)
        while not self.fermat_test(x):
            x+=1
        return x
        
    #fermat_test uses the probabilstic Fermat test to determine whether a number is prime
    def fermat_test(self, x):
        a = randint(1, x)

        while self.extended_euclid(a, x)[0] != 1:
            a+=1
        
        if pow(a, x-1, x) != 1:
            return False
        else:
            return True
    
    #extended_euclid implements Euclid's algorithm, which returns the GCD of 2 numbers as well as
    #the x,y that satisfy ax + by = gcd(a,b)
    def extended_euclid(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, x, y = self.extended_euclid(b % a, a)
            new_x = y - (x * (b // a))
            new_y = x
            return (gcd, new_x, new_y)
    
    #calc_N finds the N for the public key
    def calc_N(self, p, q):
        return p*q

    #calc_e finds e such that e is co-prime to the Eulerian totient
    def calc_e(self, p, q):
        totient = (p-1)*(q-1)
        e = randint(1, totient)

        while self.extended_euclid(e, totient)[0] != 1:
            e+=1
        
        return e

    #calc_d finds the private key using Euclid's algorithm
    def calc_d(self, e, p, q):
        totient = (p-1)*(q-1)
        gcd, x, y = self.extended_euclid(e, totient)

        if gcd == 1:
            return x % totient 
        else:
            return None
    
    #encrypt coverts the message to a list of integers, then encrypts each as x^e mod N
    def encrypt(self, message):
        message = [ord(ch) for ch in message]
        return [pow(ch, self.public_key[1], self.public_key[0]) for ch in message]
    
    #decrypt decrypts each integer performing x^d mod N, then converts the list back to a string
    def decrypt(self, message):
        char_list = [chr(pow(ch, self.private_key, self.public_key[0])) for ch in message]
        return ''.join(char_list)

