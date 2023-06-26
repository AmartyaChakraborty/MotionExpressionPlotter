#Importing the libraries
#
import numpy as np
import matplotlib.pyplot as plt

# DEFINING MATHEMATICAL FUNCTIONS

# defining a function for defferentiation of expressions

def differentiate(expression, variable):
    # Performing differentiation here and returning the result
    # You can use libraries like SymPy or implement your own differentiation logic
    # Example: Using SymPy
    from sympy import symbols, diff

    t = symbols(variable)
    result = diff(expression, t)

    return result


def integrate(expression, variable):
    # Perform integration here and return the result
    # You can use libraries like SymPy or implement your own integration logic
    # Example: Using SymPy
    from sympy import symbols, integrate

    t = symbols(variable)
    result = integrate(expression, t)

    return result


# FUNTION TO CONVERT x(t),v(t), or a(t) into the rest
# This function would also request funtion plot_function to graph the function

def convert_function():
    function_type = input("Select a type of function [ a(t), v(t), or x(t) ]: ")

    if function_type == "a(t)":
        a_t = input("Enter the function a(t): ")
        v_t = integrate(a_t, 't')  # Convert a(t) to v(t) by integrating
        x_t = integrate(v_t, 't')  # Convert v(t) to x(t) by integrating

    elif function_type == "v(t)":
        v_t = input("Enter the function v(t): ")
        a_t = differentiate(v_t, 't')  # Convert v(t) to a(t) by differentiating
        x_t = integrate(v_t, 't')  # Convert v(t) to x(t) by integrating

    elif function_type == "x(t)":
        x_t = input("Enter the function x(t): ")
        v_t = differentiate(x_t, 't')  # Convert x(t) to v(t) by differentiating
        a_t = differentiate(v_t, 't')  # Convert v(t) to a(t) by differentiating

    else:
        print("Invalid function type.")
        run()
    
    # requesting plot_function to  plot
    
    function_plot = input('Select a type of function function to plot [ a(t),v(t), or x(t) ]:')
    
    if function_plot == "a(t)":
        function = a_t
        
    elif function_plot == "v(t)":
        function = v_t
        
    elif function_plot == "x(t)":
        function = x_t
        
    else:
        print('invalid function type')
        
    plot_function(function,function_type)
           

# FUNTION TO PLOT A FUNCTION

def plot_function(expression,yLabel):

    # Create a numpy array of x values
    t = np.linspace(-10, 10, 400)

    try:
        # Evaluate the function expression
        y = eval(expression)

        # Plot the function
        plt.plot(t, y)
        plt.xlabel('t')
        #label of y changes wrt function
        if yLabel == "a(t)":
            plt.ylabel('a')
        if yLabel == "v(t)":
            plt.ylabel('v')
        if yLabel == "x(t)":
            plt.ylabel('x')
            
        plt.title('Plot of ' + expression)
        plt.grid(True)
        plt.show()
    except:
        print("Invalid function expression!")
        run()

# Defining function run which would run the code/ rerun the code if errors appear

def run():
    re = input('restart? (y/n):')
    if re == 'y':
        convert_function()
    else:
        print('function ended')

# calling the function        
convert_function()