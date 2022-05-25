def valid_input():
    valid_speed = "E", "U", "e", "u"
    if reading[0] == "E" or reading[0] == "e":
        kph.append(reading[1:])
        print("Reading saved")
    elif reading[0] == "U" or reading[0] == "u":
        mph.append(reading[1:])
        print("Reading Saved")
    elif len(mph) == 0 and len(kph) == 0:
        print("No data")
    elif reading[0] not in valid_speed:
        print("Invalid shallow speed")


if __name__ == "__main__":
    mph = []
    kph = []
    total_mph = 0
    total_kph = 0
    print("Swallow Speed Analysis")
    while True:
        reading = input("Next reading: ")
        if reading == "" and (len(mph) != 0 or len(kph) != 0):
            print("Results")
            break
        else:
            valid_input()
    for recording_mph in range(len(mph)):
        total_mph += int(mph[recording_mph])
    min_kph = round((int(min(kph)) / 1.60934), 2)
    for recording_kph in range(len(kph)):
        total_kph += int(kph[recording_kph])
    max_kph = round((int(max(mph)) * 1.60934), 2)
    print("Max speed: ", max(mph), "mph,", max_kph, "kph")
    print("Min speed: ", min(kph), "mph,", min_kph, "kph")
    print("Average speed: ", round(total_mph / len(mph)), "mph", round(total_kph / len(kph)), "kph")
