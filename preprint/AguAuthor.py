class AguAuthor:

    def __init__ (self, fullName, emailAddress):
        self.emailAddresses = []
        self.fullName = fullName
        parts = fullName.split(",")
        self.lastName = parts[0].strip()

        # may not have initials
        if ( len(parts) == 1 ):
            self.initials = ""
        else:
            self.initials = parts[1].strip()
        self.emailAddresses.append( emailAddress )

    def addEmailAddress (self, emailAddress ):
        if ( emailAddress in self.emailAddresses ):
            return False
        else:
            self.emailAddresses.append( emailAddress )
            return True

    def getLastName(self):
        return self.lastName

    def getInitials(self):
        return self.initials

    def getFullName(self):
        return self.fullName
    
    def getAddressCount(self):
        return len(self.emailAddresses)

    def getEmailAddresses(self):
        return self.emailAddresses
