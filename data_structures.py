#append
#A method to add an item to the end of a list

topics_app=['modules', 'functions', 'data structures', 'keyword arguements']
topics_app.append('decision making')
print(topics_app)


#extend
#A method to extend the list by appending all the items from the iterable

topics_ext=['modules', 'functions', 'data structures', 'keyword arguements']
new_topics_ext=['lists as stacks']
topics_ext.extend(new_topics_ext)
print(topics_ext)


#insert
#A method that inserts an item at a given position with the first argument being the index of the element before which to insert
topics_ins=['modules', 'functions', 'data structures', 'keyword arguements']
topics_ins.insert(4, 'lists as queues')
print(topics_ins)


#remove
#A method that removes the first item from the list whose value is equal to a value specified

topics_rem=['modules', 'functions', 'data structures', 'keyword arguements', 'lists as queues']
topics_rem.remove('lists as queues')
print(topics_rem)


#pop
#A method that remove the item at the given position (i) in the list, and return it. If no index (i) is specified, the method removes and returns the last item in the list

topics_lpop=['modules', 'functions', 'data structures', 'keyword arguements', 'lists as queues']
print(topics_lpop.pop(4))


#clear
#A method that removes all the items from the list

topics_clr=['modules', 'functions', 'data structures', 'keyword arguements', 'lists as queues']
topics_clr.clear()
print(topics_clr)


#index
#A method that removes zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

topics_ind=['modules', 'functions', 'data structures', 'keyword arguements', 'lists as queues']
print(topics_ind.index('lists as queues'))


#count
#A method that returns the number of times a value appears in the list.

topics_cnt=['modules', 'functions', 'data structures', 'keyword arguements', 'lists as queues', 1, 3, 4, 3, 7, 4, 8, 6]
print(topics_cnt.count(3))


#sort
# A method that sorts the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

topics_srt=['modules', 'functions', 'data structures', 'keyword arguements', 'lists as queues']
topics_srt.sort(reverse=True)
print(topics_srt)


#reverse
#A method that reverses the elements of the list in place.

topics_rvs=['data structures','modules', 'functions', 'keyword arguements', 'lists as queues']
topics_rvs.reverse()
print(topics_rvs)


#copy
#A method that returns a shallow copy of the list.

topics_cpy=['data structures','modules', 'functions', 'keyword arguements', 'lists as queues']
new_topics_cpy=topics_cpy.copy()
new_topics_cpy.append('confirmation of copy method')
print(topics_cpy)
print(new_topics_cpy)


#list comprehensions
#They provide a concise way to create lists. 

list_comps=[]
for x in range(100):
    if x%2==0:
        list_comps.append(x)


print(list_comps)