from hydrolytics.analytics import (
    load_water_usage,
    calculate_average_usage,
    max_usage,
    moving_average_forecast
)

DATA_FILE = "data/sample_water_usage.csv"


def main():
    usage = load_water_usage(DATA_FILE)

    avg = calculate_average_usage(usage)
    peak = max_usage(usage)

    print("Hydrolytics Report")
    print("------------------")
    print(f"Average Usage: {avg:.2f} liters")
    print(f"Peak Usage: {peak:.2f} liters")
    prediction = moving_average_forecast(usage)

print("\nForecast")
print("--------")
print(f"Predicted Next Usage: {prediction:.2f} L/day")


if __name__ == "__main__":
    main()
