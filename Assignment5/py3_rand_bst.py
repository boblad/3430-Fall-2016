from BSTNode import BSTNode
from BSTree import BSTree
import random

## bugs to vladimir dot kulyukin at gmail dot com

## implement this method
def gen_rand_bst(num_nodes, a, b):
    bst = BSTree()
    for num in range(0, num_nodes):
        bst.insertKey(random.randint(a, b))
    return bst

def get_list_prob(rbst_list):
    count = 0.0
    for rbst in rbst_list:
        if rbst.isList() == True:
            count = count + 1
    return count / len(rbst_list)

## implement this method
def estimate_list_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b):
    rbst_list = [ gen_rand_bst(num_nodes, a, b) for num in range(0, num_rbsts)]
    prob = get_list_prob(rbst_list)
    print( 'Prob of list: ', prob)
    return prob

def estimate_list_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_rbsts, a, b):
    d = {}
    for num_nodes in range(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_list_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b)
    return d

## implement this method
def estimate_balance_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b):
    rbst_list = [ gen_rand_bst(num_nodes, a, b) for num in range(0, num_rbsts)]
    return (get_list_prob(rbst_list), rbst_list)

def estimate_balance_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_rbsts, a, b):
    d = {}
    for num_nodes in range(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_balance_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b)
        display_balanced(d)
    return d

def display_balanced(d):
    for k, v in d.iteritems():
        print('probability of balance in rbsts with %d nodes = %f' % (k, v[0]))


rbst = gen_rand_bst(5, 0, 100)
print( rbst.isList())
print( rbst.isBalanced())
print( rbst.displayInOrder())

# d = estimate_list_probs_in_rand_bsts(5, 200, 1000, 0, 1000000)
# d = estimate_balance_probs_in_rand_bsts(5, 200, 1000, 0, 1000000)
