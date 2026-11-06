def mean_squared_error(y_true, y_pred):
    residuals_squared = []

    for y_value in range(len(y_true)):
        residuals_squared.append((y_true[y_value] - y_pred[y_value]) ** 2)

    residual_sum = sum(residuals_squared)

    print(f"Mean Squared Error: {residual_sum / len(y_true)}")
    return residual_sum / len(y_true)