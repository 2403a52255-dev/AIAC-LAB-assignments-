import numpy as np
import matplotlib.pyplot as plt
def f(x):
    """
    Function f(x) = 2x³ + 4x + 5
    """
    return 2 * x**3 + 4 * x + 5
def df_dx(x):
    """
    Derivative of f(x) = 2x³ + 4x + 5
    f'(x) = 6x² + 4
    """
    return 6 * x**2 + 4
def gradient_descent(initial_x, learning_rate, num_iterations, tolerance=1e-6):
    """
    Gradient descent optimization to find minimum of f(x)    
    Args:
        initial_x: Starting point
        learning_rate: Step size for gradient descent
        num_iterations: Maximum number of iterations
        tolerance: Convergence tolerance
 
    Returns:
        x_min: x value at minimum
        f_min: Function value at minimum
        history: History of x values during optimization
    """
    x = float(initial_x)
    history = [x]   
    for i in range(num_iterations):
        # Calculate gradient
        gradient = df_dx(x)
            # Update x using gradient descent
        x_new = x - learning_rate * gradient     
        # Check for convergence
        if abs(x_new - x) < tolerance:
            print(f"Converged after {i+1} iterations")
            break           
        x = x_new
        history.append(x)    
    return x, f(x), history
def analyze_function():
    """
    Analyze the function f(x) = 2x³ + 4x + 5 mathematically
    """
    print("=" * 50)
    print("MATHEMATICAL ANALYSIS")
    print("=" * 50)
    print("Function: f(x) = 2x³ + 4x + 5")
    print("First derivative: f'(x) = 6x² + 4")
    print("Second derivative: f''(x) = 12x")
    print()   
    print("IMPORTANT OBSERVATION:")
    print("Since f'(x) = 6x² + 4, and x² ≥ 0 for all real x,")
    print("we have f'(x) = 6x² + 4 ≥ 4 > 0 for all real x.")
    print("This means the function is STRICTLY INCREASING everywhere!")
    print("Therefore, this function has NO MINIMUM value.")
    print()
    print("However, we can demonstrate how gradient descent works...")
    print("The algorithm will keep moving in the negative x direction.")
    print()
def main():
    try:
        # Analyze the function mathematically
        analyze_function()       
        # Gradient descent parameters
        initial_x = 2.0  # Starting point
        learning_rate = 0.01  # Step size
        num_iterations = 500    
        print("=" * 50)
        print("GRADIENT DESCENT DEMONSTRATION")
        print("=" * 50)
        print(f"Initial x: {initial_x}")
        print(f"Learning rate: {learning_rate}")
        print(f"Max iterations: {num_iterations}")
        print()       
        # Run gradient descent
        x_result, f_result, history = gradient_descent(initial_x, learning_rate, num_iterations)       
        print("RESULTS:")
        print(f"Final x: {x_result:.6f}")
        print(f"Final f(x): {f_result:.6f}")
        print(f"Final gradient f'(x): {df_dx(x_result):.6f}")
        print(f"Total iterations: {len(history)}")
        print()        
        # Test different starting points
        print("=" * 50)
        print("TESTING DIFFERENT STARTING POINTS")
        print("=" * 50)
        starting_points = [-5, -1, 0, 1, 5]     
        print(f"{'Start':<8} {'End':<12} {'f(End)':<12} {'Iterations':<12}")
        print("-" * 50)        
        for start_x in starting_points:
            x_end, f_end, hist = gradient_descent(start_x, learning_rate, 200)
            print(f"{start_x:<8.1f} {x_end:<12.4f} {f_end:<12.4f} {len(hist):<12}")       
        print()       
        # Create visualization
        print("Generating visualization...")        
        plt.figure(figsize=(15, 10))       
        # Plot 1: Function and gradient descent path
        plt.subplot(2, 3, 1)
        x_range = np.linspace(-4, 3, 1000)
        y_range = f(x_range)
        plt.plot(x_range, y_range, 'b-', linewidth=2, label='f(x) = 2x³ + 4x + 5')       
        # Plot gradient descent path
        history_y = [f(x) for x in history]
        plt.plot(history, history_y, 'ro-', markersize=3, linewidth=1, alpha=0.7, label='Gradient Descent Path')
        plt.plot(history[0], history_y[0], 'go', markersize=8, label=f'Start (x={history[0]:.1f})')
        plt.plot(history[-1], history_y[-1], 'ro', markersize=8, label=f'End (x={history[-1]:.2f})')      
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Function and Gradient Descent Path')
        plt.legend()
        plt.grid(True, alpha=0.3)       
        # Plot 2: Derivative
        plt.subplot(2, 3, 2)
        derivative_range = df_dx(x_range)
        plt.plot(x_range, derivative_range, 'g-', linewidth=2, label="f'(x) = 6x² + 4")
        plt.axhline(y=0, color='k', linestyle='--', alpha=0.5, label='y = 0')
        plt.xlabel('x')
        plt.ylabel("f'(x)")
        plt.title('Derivative (Always Positive!)')
        plt.legend()
        plt.grid(True, alpha=0.3)       
        # Plot 3: Convergence history (x values)
        plt.subplot(2, 3, 3)
        plt.plot(range(len(history)), history, 'b-o', markersize=2)
        plt.xlabel('Iteration')
        plt.ylabel('x value')
        plt.title('x Value Convergence')
        plt.grid(True, alpha=0.3)       
        # Plot 4: Function value history
        plt.subplot(2, 3, 4)
        plt.plot(range(len(history)), history_y, 'r-o', markersize=2)
        plt.xlabel('Iteration')
        plt.ylabel('f(x) value')
        plt.title('Function Value History')
        plt.grid(True, alpha=0.3)       
        # Plot 5: Gradient magnitude history
        plt.subplot(2, 3, 5)
        gradient_history = [df_dx(x) for x in history]
        plt.plot(range(len(gradient_history)), gradient_history, 'm-o', markersize=2)
        plt.xlabel('Iteration')
        plt.ylabel('Gradient f\'(x)')
        plt.title('Gradient Magnitude')
        plt.grid(True, alpha=0.3)       
        # Plot 6: Multiple starting points comparison
        plt.subplot(2, 3, 6)
        colors = ['red', 'blue', 'green', 'orange', 'purple']
        for i, start_x in enumerate(starting_points):
            _, _, hist = gradient_descent(start_x, learning_rate, 100)
            plt.plot(range(len(hist)), hist, color=colors[i], marker='o', markersize=1, 
                    linewidth=1, label=f'Start: {start_x}')        
        plt.xlabel('Iteration')
        plt.ylabel('x value')
        plt.title('Multiple Starting Points')
        plt.legend()
        plt.grid(True, alpha=0.3)      
        plt.tight_layout()
        plt.show()       
        # Summary
        print("=" * 50)
        print("SUMMARY AND KEY INSIGHTS")
        print("=" * 50)
        print("1. The function f(x) = 2x³ + 4x + 5 has NO minimum point")
        print("2. f'(x) = 6x² + 4 is ALWAYS positive (≥ 4)")
        print("3. The function is strictly increasing everywhere")
        print("4. Gradient descent moves toward negative infinity")
        print("5. All starting points lead to the same behavior")
        print("6. The algorithm stops when step size becomes very small")
        print()
        print("This demonstrates that gradient descent will not find")
        print("a minimum for functions that don't have one!")      
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please make sure numpy and matplotlib are installed:")
        print("pip install numpy matplotlib")
if __name__ == "__main__":
    main()
