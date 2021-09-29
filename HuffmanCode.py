import numpy as np
from Node import *

english_alphabet = ['a', 'b', 'c', 'd', "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]


# ------------------ Functions to show to screen ----------------------------------

# Shows the list of main functions that can be run, and the user chooses one of them.
def option_menu():
    print("---- HUFFMAN CODES (EXERCISE 3.2) " + "-" * 100 + "\n")
    print("List of available functions:")
    print("1) Generate an excellent instantaneous code.")
    print("2) Decoding.")
    print("3) Exit.\n")
    try:
        chosen_function = get_input("\U0000270F Select the number of the function to run: ")
        if 1 <= chosen_function <= 3:
            return chosen_function
        else:
            print("\nYou must enter a number from 1 to 3\n")
    except ValueError:
        print("\nYou must enter a number from 1 to 3\n")


# Shows the two ways you can generate the code for the decoding part.
def code_generation_menu():
    print("\n" + "*" * 40)
    print("Possible choices to generate the code:")
    print("1) Huffman Code.")
    print("2) Generic Prefix-Free Code.")
    is_correct = False
    while not is_correct:
        try:
            chosen_sub_function = get_input("\n\U0000270F Select the number of the code generation: ")
            if 1 <= chosen_sub_function <= 2:
                is_correct = True
                return chosen_sub_function
            else:
                print("\nYou must enter a number from 1 to 2\n")
        except ValueError:
            print("\nYou must enter a number from 1 to 2\n")


# Shows the two ways you can generate the alphabet distribution.
def alphabet_distribution_menu():
    print("\n" + "*" * 55)
    print("Possible choices to generate the alphabet distribution:")
    print("1) English Alphabet Distribution.")
    print("2) Random Alphabet Distribution.")
    is_correct = False
    while not is_correct:
        try:
            chosen_sub_function = get_input("\n\U0000270F Select the number of the method of generating "
                                            "the distribution of the alphabet: ")
            if 1 <= chosen_sub_function <= 2:
                is_correct = True
                return chosen_sub_function
            else:
                print("\nYou must enter a number from 1 to 2\n")
        except ValueError:
            print("\nYou must enter a number from 1 to 2\n")


# Gets input from the user and executes.
def get_input(message):
    choice = int(input(message))
    return choice

# --------------------------------------- End -------------------------------------------------


# Generates the Huffman code by taking input nodes.
def huffman_codes(nodes):
    # A cycle is performed until the last root node remains, i.e. all the deepest nodes have been processed.
    while len(nodes) > 1:
        # An initial value that is greater than 1.
        min_prob = 2
        # Searches for the two nodes every time with the lowest probability.
        # First the left node.
        for node in nodes:
            if node.prob < min_prob:
                left_node = node
                min_prob = node.prob
        nodes.remove(left_node)

        # And then the right node.
        min_prob = 2
        for node in nodes:
            if node.prob < min_prob:
                right_node = node
                min_prob = node.prob

        # Generates the parent node, which will have a probability equal to the sum of the two nodes.
        parent_key = left_node.prob + right_node.prob
        new_node = left_node.insert_parent_with(right_node, parent_key)

        # Removes the nodes from the list, which have already been considered.
        nodes.remove(right_node)
        nodes.append(new_node)

    code = nodes[0].visit(nodes[0])[1]

    return code


# Generates a distribution for the alphabet.
def alphabet_distribution(n_letter, choice):
    distribution = np.zeros(n_letter)
    if choice == 1:
        distribution = np.array([0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0075,
                                 0.0403, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0104,
                                 0.0237, 0.0015, 0.0197, 0.0007])
        distribution = distribution[:n_letter]

    elif choice == 2:
        # Generates a random distribution for letters.
        distribution = np.random.rand(1, n_letter)
        distribution = (distribution / np.sum(distribution))[0]
    return distribution


# Generates the leaf nodes associated with each letter.
def generate_nodes(distribution):
    nodes = []
    # Consider key = probability.
    for i, key in enumerate(distribution):
        nodes.append(Node(prob=key))
        nodes[i].set_leaf(english_alphabet[i])
    return nodes


# Creates the initial tree.
def build_initial_tree(current_node, depth, level=0):
    if level == depth:
        current_node.leaf = True
        return
    sx = Node()
    sx.code = "0"
    sx.parent = current_node
    dx = Node()
    dx.code = "1"
    dx.parent = current_node
    current_node.left = sx
    current_node.right = dx
    build_initial_tree(sx, depth, level + 1)
    build_initial_tree(dx, depth, level + 1)


# Finds the tree leaf nodes.
def find_leaves(current_node, leaves=[]):
    if current_node.leaf:
        current_node.letter = "x"
        leaves.append(current_node)
        return leaves
    leaves = find_leaves(current_node.left, leaves)
    leaves = find_leaves(current_node.right, leaves)

    return leaves


# Creates the marked tree (Generate the tree to create the prefix code free).
# Personal implementation choice.
def build_marked_tree(alphabet_symbols):
    tree_depth = alphabet_symbols
    root = Node()

    # Generates the initial binary tree from which to start.
    build_initial_tree(root, tree_depth)

    # Looks for leaf nodes recursively
    leaves = find_leaves(root)

    # Chooses in a random way of the 'x' leaves from marking.
    code_length = tree_depth
    marked_leaves = np.ones(code_length)
    not_marked_leaves = np.zeros((2 ** tree_depth) - code_length)
    marked_leaves = np.concatenate([marked_leaves, not_marked_leaves]) == 1
    np.random.shuffle(marked_leaves)

    for i, marked in enumerate(marked_leaves):
        if marked:
            leaves[i].marked = True

    return root


# Generates a prefix-free code (i.e. if no codeword is a prefix of another codeword in the code).
def prefix_free_codes(node, alphabet, code="", prefix_free_code={}):
    if node is None:
        return

    # First performs recursively on the left node.
    if node.left is not None:
        code += node.left.code
        code, prefix_free_code, alphabet = prefix_free_codes(node.left, alphabet, code, prefix_free_code)

        code = code[:-1]

    # And then on the right node.
    if node.right is not None:
        code += node.right.code
        code, prefix_free_code, alphabet = prefix_free_codes(node.right, alphabet, code, prefix_free_code)
        code = code[:-1]

    if node.marked:
        prefix_free_code[alphabet[0]] = code
        alphabet = alphabet[1:]

    return code, prefix_free_code, alphabet


# Converts words from strings to binary.
def convert_string_to_binary(prefix_free_code, plaintext):
    binary_string = ""
    for i in plaintext:
        binary_string += prefix_free_code[i]
    return binary_string


# Decodes the binary string and the plaintext returns.
def binary_string_decoding(prefix_free_code, binary_string):
    key_list = list(prefix_free_code.keys())
    val_list = list(prefix_free_code.values())
    check_code = ""
    plaintext = ""
    for c in binary_string:
        check_code += c
        if check_code in prefix_free_code.values():
            plaintext += key_list[val_list.index(check_code)]
            check_code = ""
    return plaintext


# ---------------------- Setting of All Functions ---------------------------------

# Sets all the parameters to create a Huffman code
def set_huffman_code():
    n_letters = get_input("\n\U0000270F Insert desired number of letters (max 26): ")
    while not (1 <= n_letters <= 26):
        print("\nYou must enter a value between 1 and 26\n")
        n_letters = get_input("\U0000270F Insert desired number of letters (max 26): ")

    # The user can choose how to generate the distribution of the alphabet.
    choice = alphabet_distribution_menu()
    alp_dist = alphabet_distribution(n_letters, choice)
    if choice == 1:
        print("\n\U00002022 English Alphabet Distribution: ")
    elif choice == 2:
        print("\n\U00002022 Random Alphabet Distribution: ")
    for i, dist in enumerate(alp_dist):
        print(english_alphabet[i], ":", dist)

    nodes = generate_nodes(alp_dist)
    code = huffman_codes(nodes)
    print("\n\U00002022 Huffman code generated:", dict(sorted(code.items())), "\n")


# Auxiliary function to check that all the letters of a word belong to the code.
def check_letters_in_code(word, code):
    for letter in word:
        if letter not in code.keys():
            return False
    return True


# Sets all the parameters to perform the string decoding.
def set_decoding():
    n_letters = get_input("\n\U0000270F Insert desired number of letters (max 26): ")
    while not (1 <= n_letters <= 26):
        print("\nYou must enter a value between 1 and 26\n")
        n_letters = get_input("\U0000270F Insert desired number of letters (max 26): ")

    # The user can choose how to generate the prefix-free code (Huffman code or a generic prefix-free code).
    code_generation_choice = code_generation_menu()
    code = {}
    if code_generation_choice == 1:
        print("\nYou have chosen: Huffman Code!")
        # The user can choose how to generate the distribution of the alphabet.
        alp_dist_choice = alphabet_distribution_menu()
        alp_dist = alphabet_distribution(n_letters, alp_dist_choice)
        nodes = generate_nodes(alp_dist)
        code = huffman_codes(nodes)

    elif code_generation_choice == 2:
        print("\nYou have chosen: Generic Prefix-Free Code!")
        tree_root = build_marked_tree(n_letters)
        _, prefix_free_code, _ = prefix_free_codes(tree_root, english_alphabet)
        code = prefix_free_code

    print("\n\U00002022 Huffman code generated:", dict(sorted(code.items())), "\n")

    plaintext = input("\U0000270F Insert the string that you want to convert into a binary string (don't use letters"
                      " that are not available in the code): ").lower()

    # Checks that all the word letters belong to the code
    check = check_letters_in_code(plaintext, code)
    while not check:
        print("\nYou must enter only letters in the code.\n")
        plaintext = input("\U0000270F Insert the string that you want to convert into a binary string "
                          "(don't use letters that are not available in the code): ").lower()
        check = check_letters_in_code(plaintext, code)

    binary_string = convert_string_to_binary(code, plaintext)
    print("\n\U00002022 Binary string:", binary_string, "\n")

    decoded_string = binary_string_decoding(code, binary_string)
    print("\U00002022 Plaintext decoded:", decoded_string, "\n")


# Exposes all the functions for the various choices.
def main():
    while True:
        # Asks the user what function wants to run.
        choice = option_menu()

        # Executes the function requested by the user.
        try:
            if choice == 1:
                set_huffman_code()
            elif choice == 2:
                set_decoding()
            elif choice == 3:
                exit(0)
        except ValueError:
            print("\nYou must enter an integer\n")
        input("Press Enter to return to the Main menu.\n")


if __name__ == '__main__':
    main()
