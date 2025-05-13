# --- Conversion Functions ---

# Length
def km_to_m(km): return km * 1000
def m_to_km(m): return m / 1000
def m_to_cm(m): return m * 100
def cm_to_m(cm): return cm / 100
def km_to_cm(km): return km * 100000
def cm_to_km(cm): return cm / 100000

# Weight
def kg_to_lb(kg): return kg * 2.20462
def lb_to_kg(lb): return lb / 2.20462
def g_to_kg(g): return g / 1000
def kg_to_g(kg): return kg * 1000

# Temperature
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15


# Menu
def show_length_menu():
    print("\nLength Conversions:")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Meters to Centimeters")
    print("4. Centimeters to Meters")
    print("5. Kilometers to Centimeters")
    print("6. Centimeters to Kilometers")

def show_weight_menu():
    print("\nWeight Conversions:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Kilograms")
    print("4. Kilograms to Grams")

def show_temperature_menu():
    print("\nTemperature Conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")


# Main
def main():
    while True:
        print("\n===== Unit Converter =====")
        print("Choose a category:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        category = input("Enter your choice (1-4): ")

        if category == '1':
            show_length_menu()
            option = input("Select conversion (1-6): ")
            try:
                value = float(input("Enter value to convert: "))
                if option == '1':
                    print(f"{value} km = {km_to_m(value)} m")
                elif option == '2':
                    print(f"{value} m = {m_to_km(value)} km")
                elif option == '3':
                    print(f"{value} m = {m_to_cm(value)} cm")
                elif option == '4':
                    print(f"{value} cm = {cm_to_m(value)} m")
                elif option == '5':
                    print(f"{value} km = {km_to_cm(value)} cm")
                elif option == '6':
                    print(f"{value} cm = {cm_to_km(value)} km")
                else:
                    print("Invalid option.")
            except ValueError:
                print("Please enter a valid number.")

        elif category == '2':
            show_weight_menu()
            option = input("Select conversion (1-4): ")
            try:
                value = float(input("Enter value to convert: "))
                if option == '1':
                    print(f"{value} kg = {kg_to_lb(value):.2f} lb")
                elif option == '2':
                    print(f"{value} lb = {lb_to_kg(value):.2f} kg")
                elif option == '3':
                    print(f"{value} g = {g_to_kg(value):.2f} kg")
                elif option == '4':
                    print(f"{value} kg = {kg_to_g(value):.2f} g")
                else:
                    print("Invalid option.")
            except ValueError:
                print("Please enter a valid number.")

        elif category == '3':
            show_temperature_menu()
            option = input("Select conversion (1-4): ")
            try:
                value = float(input("Enter value to convert: "))
                if option == '1':
                    print(f"{value}°C = {c_to_f(value):.2f}°F")
                elif option == '2':
                    print(f"{value}°F = {f_to_c(value):.2f}°C")
                elif option == '3':
                    print(f"{value}°C = {c_to_k(value):.2f}K")
                elif option == '4':
                    print(f"{value}K = {k_to_c(value):.2f}°C")
                else:
                    print("Invalid option.")
            except ValueError:
                print("Please enter a valid number.")

        elif category == '4':
            print("Thanks for using the Unit Converter. Goodbye!")
            break

        else:
            print("Invalid category. Please choose from 1 to 4.")


main()
