from AguAuthor import AguAuthor

def subset(lastName, fullName, authors):
    sub = []
    for a in authors.values():
        if ( (a.getLastName() == lastName) and (a.getFullName() != fullName) ):
            sub.append(a)
    return sub
        
def main():

    # directory holding the raw data
    directory = "/Users/narock/Desktop/AGU_Graph/"

    # list containing all the AGU section abbreviations
    sections = ["A", "AE", "B", "C", "DI", "ED", "EP", "G", "GC", "GP", "H", "IN","MR",
                "NG","NH", "NS","OS", "P", "PA", "PP", "S", "SA", "SH","SM","T","U","V"]

    # output file for match count
    matchFile = open(directory + "/exactMatchCount", "w", encoding="utf8")
    matchFile.write("Section, Exact Matches, Partial Matches\n")

    # loop over all the sections
    for section in sections:

        # list to avoid double counting someone
        # place the people we've seen already in this list and check it each time we look at a new name
        exclude = []

        # an empty dictionary that will hold the data we read from the AGU section files
        authors = {}

        # open the next file for reading
        nodeFile = open(directory + section + "/nodesFile_" + section, "r", encoding="utf8")

        # open exact match output file for this section
        outFile = open(directory + section + "/exactMatches_" + section, "w", encoding="utf8")
        
        # loop over all the people in the file
        for line in nodeFile:
            parts = line.strip().split(":")
            email = parts[0].strip()
            name = parts[1].strip()

            # have we seen this person before? This name may have occured
            # already with a different email address
            if ( name in authors ):
                
                # get the object and check emailAddress
                a = authors.get(name)
                a.addEmailAddress(email) # method checks if email already exists, if no it adds it
                
                # put back into dictionary
                authors[name] = a

            # we haven't seen this name before
            else:
                
                # create a new object and add email address
                a = AguAuthor( name, email )
                authors[name] = a # add object to the authors dictionary

        # close the node file
        nodeFile.close()
        
        # just some parameters to see how far we are in our checking
        # used to print out status updates
        count = 0
        print("Section ", section)
        ten = round(0.1 * len(authors))
        twenty = round(0.20 * len(authors))
        thirty = round(0.30 * len(authors))
        fourty = round(0.40 * len(authors))
        fifty = round(0.50 * len(authors))
        sixty = round(0.60 * len(authors))
        seventy = round(0.70 * len(authors))
        eighty = round(0.80 * len(authors))
        ninety = round(0.90 * len(authors))

        # variables to hold partial and exact match counts
        partial = 0
        exact = 0

        # another loop - this one over all the authors now in our dictionary
        for a in authors.values():

            # I need some status updates printed to the screen to convince me
            # things are working as expected. Prints out how far along we are
            # in the processes
            if ( count == ten ):
                print("  10% completed...")
            if ( count == twenty ):
                print("  20% completed...")
            if ( count == thirty ):
                print("  30% completed...")
            if ( count == fourty ):
                print("  40% completed...")
            if ( count == fifty ):
                print("  50% completed...")
            if ( count == sixty ):
                print("  60% completed...")
            if ( count == seventy ):
                print("  70% completed...")
            if ( count == eighty ):
                print("  80% completed...")
            if ( count == ninety ):
                print("  90% completed...")
                
            # Case 1: Exact Name Match - Names are exact match but different email addresses
            # This is found where an author object has more than one email address
            if ( a.getAddressCount() > 1 ):
                exact += 1

                # print out the matches
                ea = a.getEmailAddresses()
                line = a.getFullName() + "," 
                for e in ea:
                    line += e + ","
                line = line[:-1] # remove the last unneeded comma
                outFile.write(line + "\n")
                
            # Case 2: Partial Name Match - Last names are exactly the same, first initials are only partial match, and
            # email addresses are different - example: Narock, T (tnarock@umbc.edu) and Narock, T W (tnarock@ndm.edu)
            if ( a.getFullName() not in exclude ):
                
                # find all the authors with the same last name (excluding exact match)
                sub = subset( a.getLastName(), a.getFullName(), authors )
            
                # loop over everyone in the subset
                for s in sub:

                    # add this person to the exclude list
                    exclude.append(s.getFullName())

                    # compare first initials
                    firstInitial1 = a.getInitials().strip()
                    firstInitial2 = s.getInitials().strip()
                    if ( len(firstInitial1) > 0 and len(firstInitial2) > 0 ):
                        if ( firstInitial1[0] == firstInitial2[0] ):
                            partial += 1
                    
            count += 1 # counter to keep track of how many people we've looked at already

        # close the output file for this section
        outFile.close()

        #
        line = section + "," + str(exact) + "," + str(partial) + "\n"
        matchFile.write(line)

    # close the match count file
    matchFile.close()
        
main()
