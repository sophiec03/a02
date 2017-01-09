"""
    Problem:

        The function `season` should take the first three letters of the
        name of a month and print the season it is in. For this program,
        assume that Dec-Feb is winter, Mar-May is spring and so on.

        If an unknown month is entered, print "Month not recognised"

    Tests:

        >>> season("jan")
        Winter
        >>> season("feb")
        Winter
        >>> season("mar")
        Spring
        >>> season("apr")
        Spring
        >>> season("may")
        Spring
        >>> season("jun")
        Summer
        >>> season("jul")
        Summer
        >>> season("aug")
        Summer
        >>> season("sep")
        Autumn
        >>> season("oct")
        Autumn
        >>> season("nov")
        Autumn
        >>> season("dec")
        Winter
        >>> season("abc")
        Month not recognised

"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)


def season(month):

    if month.lower() == "dec" or month.lower() == "jan" or month.lower() == "feb":
        print("Winter")

    elif month.lower() == "mar" or month.lower() == "apr" or month.lower() == "may":
        print("Spring")

    elif month.lower() == "jun" or month.lower() == "jul" or month.lower() == "aug":
        print("Summer")

    elif month.lower() == "sep" or month.lower() == "oct" or month.lower() == "nov":
        print("Autumn")

    else:
        print("Month not recognised")


