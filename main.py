# python3
import random
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class Hashing:
    multiplier=random.randint(100,200)
    prime=1000003
    def __init__(self, n):
        self.bucket_count=n
        self.buckets=[]
        for i in range(n):
            self.buckets.append([])

    def h_func(self, string):
        result = 0
        for ch in reversed(string):
            result = (result * self.multiplier + ord(ch)) % self.prime
        return result % self.bucket_count

    def add(self, query):
        hashed = self.h_func(str(query.number))
        bucket = self.buckets[hashed]
        for c in bucket:
            if c.number == query.number:
                c.name = query.name
                return
        bucket.append(query)

    def delete(self, query):
        hashed = self.h_func(str(query.number))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i].number == query.number:
                bucket.pop(i)
                return
    
    def find(self, query):
        hashed = self.h_func(str(query.number))
        bucket = self.buckets[hashed]
        for c in bucket:
            if c.number == query.number:
                return c.name
        return 'not found'
            



def read_queries(n):
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    n=len(queries)
    contacts = Hashing(n)

    result = []

    for cur_query in queries:
        if cur_query.type == 'add':
            contacts.add(cur_query)
        elif cur_query.type == 'del':
            contacts.delete(cur_query)
        else:
            response = contacts.find(cur_query)
            result.append(response)

#    print()
#    for bucket in contacts.buckets:
#        for c in bucket:
#            print(c.number, c.name, end="; ")
#        print()
#    print()
    return result

if __name__ == '__main__':
    n=int(input())
    write_responses(process_queries(read_queries(n)))

