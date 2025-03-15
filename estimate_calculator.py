#!/usr/bin/env python3

import os
import datetime

# Define texture types and their price ranges ($ per sq. ft.)
TEXTURE_PRICES = {
    "1": {"name": "Orange Peel", "low": 0.80, "medium": 1.15, "high": 1.50},
    "2": {"name": "Knockdown", "low": 1.00, "medium": 1.75, "high": 2.50},
    "3": {"name": "Popcorn (Acoustic)", "low": 1.00, "medium": 1.50, "high": 2.00},
    "4": {"name": "Skip Trowel", "low": 1.50, "medium": 2.25, "high": 3.00},
    "5": {"name": "Sand Texture", "low": 1.00, "medium": 1.75, "high": 2.50},
    "6": {"name": "Slap Brush (Crow's Foot)", "low": 1.00, "medium": 1.50, "high": 2.00},
    "7": {"name": "Stomp Texture", "low": 1.50, "medium": 2.25, "high": 3.00}
}

# Mileage rate per mile
MILEAGE_RATE = 2.25

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the company header."""
    print("=" * 60)
    print("                SPRAY TEXTURE ESTIMATE CALCULATOR                ")
    print("=" * 60)
    print()

def get_square_footage():
    """Get the square footage from the user."""
    while True:
        try:
            sq_ft = float(input("Enter the square footage of the house: "))
            if sq_ft <= 0:
                print("Square footage must be greater than zero.")
                continue
            return sq_ft
        except ValueError:
            print("Please enter a valid number.")

def display_texture_options():
    """Display the available texture options."""
    print("\nAvailable Texture Types:")
    print("-" * 50)
    for key, texture in TEXTURE_PRICES.items():
        print(f"{key}. {texture['name']}: ${texture['low']:.2f} - ${texture['high']:.2f} per sq. ft.")
    print("-" * 50)

def get_texture_choice():
    """Get the texture choice from the user."""
    display_texture_options()
    
    while True:
        choice = input("\nSelect a texture type (1-7): ")
        if choice in TEXTURE_PRICES:
            return choice
        print("Invalid choice. Please select a number between 1 and 7.")

def get_price_tier():
    """Get the price tier from the user."""
    print("\nPrice Tiers:")
    print("1. Low - Basic finish")
    print("2. Medium - Standard finish")
    print("3. High - Premium finish")
    
    while True:
        tier = input("\nSelect a price tier (1-3): ")
        if tier == "1":
            return "low"
        elif tier == "2":
            return "medium"
        elif tier == "3":
            return "high"
        print("Invalid choice. Please select a number between 1 and 3.")

def get_mileage():
    """Get the commute distance in miles."""
    while True:
        try:
            miles = float(input("\nEnter the commute distance (miles): "))
            if miles < 0:
                print("Mileage cannot be negative.")
                continue
            return miles
        except ValueError:
            print("Please enter a valid number.")

def calculate_estimate(sq_ft, texture_choice, price_tier, miles):
    """Calculate the estimate based on inputs."""
    texture = TEXTURE_PRICES[texture_choice]
    texture_name = texture["name"]
    price_per_sqft = texture[price_tier]
    
    texture_cost = sq_ft * price_per_sqft
    mileage_cost = miles * MILEAGE_RATE
    total_cost = texture_cost + mileage_cost
    
    return {
        "texture_name": texture_name,
        "price_per_sqft": price_per_sqft,
        "texture_cost": texture_cost,
        "mileage_cost": mileage_cost,
        "total_cost": total_cost
    }

def display_estimate(estimate, sq_ft, miles):
    """Display the formatted estimate."""
    clear_screen()
    print_header()
    
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    print(f"Square Footage: {sq_ft:.2f} sq. ft.")
    print(f"Texture Type: {estimate['texture_name']}")
    print(f"Price per sq. ft.: ${estimate['price_per_sqft']:.2f}")
    print(f"Commute Distance: {miles:.2f} miles")
    print("\n" + "-" * 50)
    print(f"Texture Cost: ${estimate['texture_cost']:.2f}")
    print(f"Mileage Cost (${MILEAGE_RATE:.2f}/mile): ${estimate['mileage_cost']:.2f}")
    print("-" * 50)
    print(f"TOTAL ESTIMATE: ${estimate['total_cost']:.2f}")
    print("=" * 50)
    print("\nThank you for choosing our services!")
    print("This estimate is valid for 30 days from the date above.")
    print("=" * 50)

def save_estimate(estimate, sq_ft, miles, customer_name):
    """Save the estimate to a file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"estimate_{timestamp}.txt"
    
    try:
        with open(filename, "w") as f:
            f.write("=" * 60 + "\n")
            f.write("                SPRAY TEXTURE ESTIMATE                \n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"Customer: {customer_name}\n")
            f.write(f"Square Footage: {sq_ft:.2f} sq. ft.\n")
            f.write(f"Texture Type: {estimate['texture_name']}\n")
            f.write(f"Price per sq. ft.: ${estimate['price_per_sqft']:.2f}\n")
            f.write(f"Commute Distance: {miles:.2f} miles\n")
            f.write("\n" + "-" * 50 + "\n")
            f.write(f"Texture Cost: ${estimate['texture_cost']:.2f}\n")
            f.write(f"Mileage Cost (${MILEAGE_RATE:.2f}/mile): ${estimate['mileage_cost']:.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"TOTAL ESTIMATE: ${estimate['total_cost']:.2f}\n")
            f.write("=" * 50 + "\n\n")
            f.write("Thank you for choosing our services!\n")
            f.write("This estimate is valid for 30 days from the date above.\n")
            f.write("=" * 50 + "\n")
        
        print(f"\nEstimate saved to {filename}")
        return True
    except Exception as e:
        print(f"\nError saving estimate: {e}")
        return False

def main():
    """Main function to run the estimate calculator."""
    clear_screen()
    print_header()
    
    print("Welcome to the Spray Texture Estimate Calculator!")
    print("This program will help you calculate estimates for spray texture jobs.")
    print("\nPlease enter the following information:")
    
    customer_name = input("\nCustomer Name: ")
    sq_ft = get_square_footage()
    texture_choice = get_texture_choice()
    price_tier = get_price_tier()
    miles = get_mileage()
    
    estimate = calculate_estimate(sq_ft, texture_choice, price_tier, miles)
    display_estimate(estimate, sq_ft, miles)
    
    save_option = input("\nWould you like to save this estimate? (y/n): ")
    if save_option.lower() == 'y':
        save_estimate(estimate, sq_ft, miles, customer_name)
    
    print("\nThank you for using the Spray Texture Estimate Calculator!")

if __name__ == "__main__":
    main()