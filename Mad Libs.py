# Mad Libs- Simulates A Game Of Mad Libs

def madlibs (): # Basic Madlibs game
    print ("When Prompted, Enter Required Input \n") # Instructions to user

    nn_1 = input("Plural Noun: \n") # nn <-- noun
    adj_1 = input("Adjective: \n") # adj <-- adjective
    nn_2 = input("Plural Noun: \n")
    adj_2 = input("Adjective: \n")
    vrb = input("Verb (Past Tense): \n") # vrb <-- verb
    adj_3 = input("Adjective: \n")

    print( """
            %s are %s
            %s are %s
            I've never %s anyone
            As %s as you
            """
            % (nn_1, adj_1, nn_2, adj_2, vrb, adj_3) ) # String Concatenation

madlibs()
