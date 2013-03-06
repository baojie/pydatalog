from pyDatalog import pyDatalog
# OUT: pyDatalog version 0.12.0

# create some atoms. an atomic could a symbol, varaiable (and others)
pyDatalog.create_atoms('people, alice, bob')

# insert a fact
+ people(alice)

# 'people' is a symbol
print people
# OUT: <pyDatalog.pyParser.Symbol object at 0x93e744c>

# declare a variable
pyDatalog.create_atoms('X')

# query the instances of people
print(people(X))
# OUT: [('alice',)]
# it's a unary tuple

for i in people(X): print i
# OUT: ('alice',)

# add more instance of people
+ people(bob)
for i in people(X): print i
# OUT: ('alice',)
# OUT: ('bob',)

# you can see from below, an atom may be a symbol or a var
# symbol starts with lowercase
# var starts with uppercase

type(bob)
# OUT: <class 'pyDatalog.pyParser.Symbol'>
type(people)
# OUT: <class 'pyDatalog.pyParser.Symbol'>
type(X)
# OUT: <class 'pyDatalog.pyDatalog.Variable'>

# 'people(x)' is a query!
print type(people(X))
# OUT: <class 'pyDatalog.pyParser.Query'>

# now test metamodeling: 'people' is both a peridate name and a symbol
# This is very RDF-ish and Pythonic
# Python is naturally a superset of RDF 
# Why? Python is Lisp-ish, and the inventor of RDF is the inventor of Lisp

pyDatalog.create_atoms('label')
# use 'people' as a symbol
# remember: previous it's used as a predicate
+ label(people, 'a person')

pyDatalog.create_atoms('Y')
print label(X,Y)
# OUT: [('people', 'a person')]
print label(X,Y)[0]
# OUT: ('people', 'a person')
# this is a binay tuple

# now, we query a predicate name, then construct a query from its result
# it's dynamic metamodeling

pyDatalog.create_atoms('Z')

g=label(X,Y)[0][0]
print g
# OUT: 'people'

# use eval to contruct a query from string
print eval(g)
# OUT: people
print eval(g)(Z)
# OUT: [('alice',), ('bob',)]
