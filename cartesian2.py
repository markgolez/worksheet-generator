import numpy as np
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")


def polynomial_coefficients(xs, coeffs):
    """ Returns a list of function outputs (`ys`) for a polynomial with the given coefficients and
    a list of input values (`xs`).

    The coefficients must go in order from a0 to an, and all must be included, even if the value is 0.
    """
    order = len(coeffs)
    print(f'# This is a polynomial of order {order - 1}.')

    # Initialise an array of zeros of the required length.
    ys = np.zeros(len(xs))
    for i in range(order):
        ys += coeffs[i] * xs ** i
    return ys


# Change this range according to your needs. Start, stop, number of steps.
xs = np.linspace(0, 9, 10)
coeffs = [0, 0, 1]  # x^2

# xs = np.linspace(-5, 5, 100)  # Change this range according to your needs. Start, stop, number of steps.
# coeffs = [2, 0, -3, 4]  # 4*x^3 - 3*x^2 + 2

plt.gcf().canvas.set_window_title('Fun with Polynomials')  # Set window title
plt.plot(xs, polynomial_coefficients(xs, coeffs))
plt.axhline(y=0, color='r')  # Show xs axis
plt.axvline(x=0, color='r')  # Show y axis
plt.title("y =4*x^3 - 3*x^2 + 2")  # Set plot title
plt.show()
