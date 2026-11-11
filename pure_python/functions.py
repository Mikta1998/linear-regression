LEARNING_RATE = 0.001



def mean_squared_error(y_true, y_pred):
    residuals_squared = []

    for y_value in range(len(y_true)):
        residuals_squared.append((y_true[y_value] - y_pred[y_value]) ** 2)

    residual_sum = sum(residuals_squared)

    return residual_sum / len(y_true)



def calculate_slope_gradient(x_values, y_true, m, b):
    sample_gradients = []
    for index in range(len(y_true)):
        sample_gradients.append((-2*x_values[index]*(y_true[index] - m*x_values[index] - b)))

    gradient_sum = sum(sample_gradients)

    return gradient_sum / len(y_true)



def calculate_intercept_gradient(x_values, y_true, m, b):
    sample_gradients = []
    for index in range(len(y_true)):
        sample_gradients.append((-2*(y_true[index] - m*x_values[index] - b)))

    gradient_sum = sum(sample_gradients)

    return gradient_sum / len(y_true)



def update_slope(x_values, y_true, m, b, learning_rate=LEARNING_RATE):
    slope_gradient = calculate_slope_gradient(x_values, y_true, m, b)
    m = m - learning_rate * slope_gradient
    return m



def update_intercept(x_values, y_true, m, b, learning_rate=LEARNING_RATE):
    intercept_gradient = calculate_intercept_gradient(x_values, y_true, m, b)
    b = b - learning_rate * intercept_gradient
    return b