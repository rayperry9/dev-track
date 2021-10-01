#!/usr/local/bin/python3


def get_input(systolic_value, diastolic_value):
    SYSTOLICMIN = 70
    SYSTOLICMAX = 190
    DIASTOLICMIN = 40
    DIASTOLICMAX = 100

    try:
        systolic_value = int(systolic_value)
        if systolic_value not in range(SYSTOLICMIN, SYSTOLICMAX):
            bprisk = "Invalid Systolic Value, please re-enter value."
            return bprisk
        diastolic_value = int(diastolic_value)
        if diastolic_value not in range(DIASTOLICMIN, DIASTOLICMAX):
            bprisk = "Invalid Diastolic Value, please re-enter value."
        else:
            bprisk = get_results(systolic_value, diastolic_value)
        return bprisk
    except ValueError:
        bprisk = "Please only enter numbers"
        return bprisk


def get_results(systolic_value, diastolic_value):
    if systolic_value >= 140 and systolic_value < 190 and diastolic_value <= 90:
        bprisk = "High blood pressure"
    elif (systolic_value >= 120 and systolic_value < 140) or (
        diastolic_value >= 80 and diastolic_value < 90
    ):
        bprisk = "Pre-high blood pressure"
    elif (systolic_value >= 90 and systolic_value < 120) or (
        diastolic_value >= 60 and diastolic_value < 80
    ):
        bprisk = "Ideal blood pressure"
    elif systolic_value <= 90 and diastolic_value <= 60:
        bprisk = "Low blood pressure"
    else:
        bprisk = "Invalid reading"
    return bprisk


def main():
    get_input()


if __name__ == "__main__":
    main()
