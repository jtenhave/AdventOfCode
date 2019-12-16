
# A class that represents a possible elf password consisting of 6 digits.
class Password:

    def __init__(self, digits, maxDigits):
        self.digits = digits
        self.maxDigits = maxDigits

    # Increment the password to the next valid value.
    def increment(self):
        i = 5
        while True:
            digit = self.digits[i] + 1

            # Check if the digit overflows.
            if digit > 9:
                i -= 1
            else:
                for j in range (i, 6):
                    self.digits[j] = digit
                break;

    # Check if the password has any two of the same digits in a row.
    def hasDouble(self):
        for i in range (1, 6):
            if self.digits[i] == self.digits[i - 1]:
                return True

        return False

    # Check if the password has any two - but not more- of the same digits in a row.
    def hasNonSequenceDouble(self):

        # Check the first 2 digits.
        if self.digits[0] == self.digits[1] and self.digits[0] != self.digits[2]:
            return True

        # Check the middle 4 digits.
        for i in range (1, 4):
            if self.digits[i] == self.digits[i + 1] and self.digits[i] != self.digits[i + 2] and self.digits[i] != self.digits[i - 1]:
                return True

        # Check the last 2 digits.
        if self.digits[4] == self.digits[5] and self.digits[4] != self.digits[3]:
            return True

        return False

    # Check if the password is still in range of the given max value.
    def inRange(self):
        for i in range(0, 6):
            if self.digits[i] < self.maxDigits[i]:
                return True
        
        if self.digits == self.maxDigits:
           return True

        return False
