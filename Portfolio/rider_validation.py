"""
This program focuses on creating an entry kiosk for a 
new roller coaster at a major theme park.  Due to the
ride's intensity, the computer at the entrance of the 
ride must strictly validate a rider's age and height
before being allowed to board the attraction.
"""

def validate_rider():
    while True:
        try:
            # Riders must be between the ages of 10 and 80, inclusive
            age = int(input("Enter rider's age: "))
            if 10 <= age <= 80:
                break
            print("Safety Criteria Not Met (Age)")

        except ValueError:
            print(f"Invalid input. Please enter a whole number.")


    while True:     
        try:
            # Riders must also be between 120 cm and 210 cm tall, inclusive
            height = int(input("Enter rider's height: "))
            if 120 <= height <= 210:
                print("Rider Validated. Enjoy the G-Force!")
                return [age, height]        
                        
            print("Safety Criteria Not Met (Height)")

        except ValueError:
            print(f"Invalid input. Please enter a whole number.")


def main():
    rider_data = validate_rider()
    print(f"Final Data Saved: {rider_data}")

if __name__ == "__main__":
    main()