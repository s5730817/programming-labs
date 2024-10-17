from time import sleep

def odometer_correct():
    distance = 0
    wrong_distance = 0
    while wrong_distance != 160648:
        distance += 1
        wrong_distance += 1
        if '5' in str(wrong_distance):
            print(f"Actual distance: {distance}")
            print(f"Before: {wrong_distance}")
            wrong_distance = int(str(wrong_distance).replace('5', '6'))
            print(f"After: {wrong_distance}")
            print("#" * 20)
            sleep(0.001)
    return distance

odometer_correct()