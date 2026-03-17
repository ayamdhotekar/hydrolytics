def moving_average_forecast(values, window_size=3):
    """
    Predict next value using moving average.
    """

    if len(values) < window_size:
        raise ValueError("Not enough data for forecasting")

    window = values[-window_size:]
    prediction = sum(window) / window_size

    return prediction