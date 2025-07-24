def findPayment(loan, r, m):
    """
    Assumes: loan and r are floats, m is an integer
    Returns the monthly payment for a mortgage of size loan at a monthly rate
    of r for m months
    """
    return loan * ((r*(1 + r)**m)/((1 + r)**m - 1))

class Mortgage(object):
    """
    Abstract class for building different kinds of mortgages
    """
    def __init__(self, loan, annualRate, months):
        """ 
        Assumes: loan and annualRate are floats, months is integer
        Creates new mortgage of size loan, duration months and annual rate of annualRate 
        """
        self.loan = loan
        self.rate = annualRate / 12
        self. months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None # Description of mortgage

    def makePayment(self):
        """ Make a payment """
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1] * self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def getTotalPaid(self):
        """
        Returns the total amount paid so far
        """
        return sum(self.paid)
    
    def __str__(self):
        return self.legend
    
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(round(r * 100,2)) + '%'

class FixedWithPoints(Mortgage):
    def __init__(self, loan, r, months, points):
        Mortgage.__init__(self, loan, r, months)
        self.points = points
        self.paid = [loan * (points / 100)]
        self.legend = 'Fixed, ' + str(round(r * 100, 2)) + '%, '\
                      + str(points) + 'points.'

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r / 12
        self.legend = str(teaserRate * 100) + '% for ' + str(self.teaserMonths)\
                      + ' months, then ' + str(round(r * 100, 2)) + '%'
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1],
                                       self.rate,
                                       self.months - self.teaserMonths)
        Mortgage.makePayment(self)

def compareMortgages(amt, years, fixedRate, points, pointsRate, varRate1, varRate2, varMonths):
    """ Test to compare mortgages """
    totMonths = years * 12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPoints(amt, pointsRate, totMonths, points)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]

    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    
    for m in morts:
        print(m)
        print(' Total payment = $' + str(int(m.getTotalPaid())) + '\n')

compareMortgages(amt=500000, years=30, fixedRate=0.07, points=3.25, pointsRate= 0.05,
                 varRate1=0.045, varRate2=0.095, varMonths=48)