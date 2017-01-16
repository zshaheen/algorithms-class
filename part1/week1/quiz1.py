'''
1. Social network connectivity. Given a social network containing n members and
a log file containing m timestamps at which times pairs of members formed
friendships, design an algorithm to determine the earliest time at which all
members are connected (i.e., every member is a friend of a friend of a friend
... of a friend). Assume that the log file is sorted by timestamp and that
friendship is an equivalence relation. The running time of your algorithm should
be mlogn or better and use extra space proportional to n.
'''

# n = memebers
# m = timestamps for friendships, sorted by timestamp.
# design an algo to determine the earliest time at which all members are connected.
# ALL MEMEBERS ARE CONNECTED WHEN THEY ALL HAVE THE SAME ROOT
class UnionFind():
    def __init__(self, n):
        self.id = [x for x in xrange(n)]  # id[i] is the root of node i
        self.sz = [1 for x in xrange(n)]  # sz[i] is the number of elements connected to i
        self.largest = [x for x in xrange(n)]  # largest[i] is the largest value connected to root(i)

    def root(self, p):
        current = p
        while self.id[current] != current:
            current = self.id[current]
        return current

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        if self.sz[p] >= self.sz[q]:  # connect q
            # make the root of q the root of p
            self.id[self.root(q)] = self.id[self.root(p)]
            self.sz[p] += self.sz[q]
        else:
            # make the root of p the root of q
            self.id[self.root(p)] = self.id[self.root(q)]
            self.sz[q] += self.sz[p]
        # IDK IF THIS IS RIGHT?
        self.largest[p] = max(self.largest[self.root(p)], self.largest[(self.root(q)])

    def all_connected(self):  # should be log n
        the_root = self.root(self.id[0])
        for x in xrange(1, len(self.id)):
            if self.root(x) != the_root:
                return False
        return True

    def find_slow(self, i): # is n, b/c we go through each element of self.id
        # get the elements connected to i, then return the max
        # QUESTION: HOW TO MAKE THIS log n OR BETTER?
        root_i = self.root(i)
        max_elt = i
        for element in range(0, len(self.id)):
            if self.root(element) == root_i:
                if max_elt < element:
                    max_elt = element
        return max_elt

    def find_fast(self, i): #This is constant time, while union is still O(lg n)
        return self.largest[i]

def question1(n, filename='logfile'):
    tree = UnionFind(n)
    for timestamp in open(filename):
        person1, person2, timestmp = parse_timestamp(timestamp)
        if not tree.connected(person1, person2):
            tree.union(person1, person2)
            if tree.all_connected():
                return timestmp
    return '00:00:00:00:00'

'''
2. Union-find with specific canonical element. Add a method find() to the
union-find data type so that find(i) returns the largest element in the connected
component containing i. The operations, union(), connected(), and find() should all
take logarithmic time or better.

For example, if one of the connected components is {1,2,6,9}, then the find()
method should return 9 for each of the four elements in the connected components.
'''

tree = UnionFind(10)
tree.union(1,2)
tree.union(1,6)
tree.union(6,9)

print tree.find_slow(1)
print tree.find_slow(2)
print tree.find_slow(6)
print tree.find_slow(9)
print tree.find_slow(4)

'''
3. Successor with delete. Given a set of N integers S={0,1,...,N−1} and a
sequence of requests of the following form:
- Remove x from S
- Find the successor of x: the smallest y in S such that y≥x.
design a data type so that all operations (except construction) should take
logarithmic time or better.
'''

class SucessorDelete():
    def __init__(self, n):
        self.s = list(xrange(0, n))

    def delete(x): # O(1)
        self.s.remove(x)

    def sucessor(x):
        # use binary search to find the element to the right of x.
