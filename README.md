# estimate_calculator
The Spray Texture Estimator is a simple yet effective tool designed to calculate the estimated amount of spray texture required for a given surface area. Whether you're working on a home renovation project, a professional drywall job, or simply planning material costs, this tool helps you get accurate estimates quickly and easily.
## Features

- Calculate estimates for 7 different texture types:
  - Orange Peel
  - Knockdown
  - Popcorn (Acoustic)
  - Skip Trowel
  - Sand Texture
  - Slap Brush (Crow's Foot)
  - Stomp Texture
- Three pricing tiers (Low, Medium, High) for different quality levels
- Automatic mileage cost calculation
- Formatted estimate display with itemized costs
- Option to save estimates as text files with timestamps
- Input validation to prevent calculation errors

## Requirements

- Python 3.x

## Installation

No additional installation is required beyond having Python installed. Simply download the `estimate_calculator.py` file to your computer.

## Usage

1. Open a terminal or command prompt
2. Navigate to the directory containing the script
3. Run the script using Python:

```
python estimate_calculator.py
```

Or if you're on Linux/Mac and have made the script executable:

```
./estimate_calculator.py
```

4. Follow the on-screen prompts to enter:
   - Customer name
   - Square footage of the house
   - Texture type selection
   - Price tier selection
   - Commute distance in miles

5. Review the generated estimate
6. Choose whether to save the estimate to a file

## Example Output

```
============================================================
                SPRAY TEXTURE ESTIMATE CALCULATOR                
============================================================

Date: 2023-07-15
Square Footage: 1500.00 sq. ft.
Texture Type: Knockdown
Price per sq. ft.: $1.75
Commute Distance: 15.00 miles

--------------------------------------------------
Texture Cost: $2625.00
Mileage Cost ($2.25/mile): $33.75
--------------------------------------------------
TOTAL ESTIMATE: $2658.75
==================================================

Thank you for choosing our services!
This estimate is valid for 30 days from the date above.
==================================================
```

## Saved Estimate Files

When you choose to save an estimate, the program creates a text file with a timestamp in the filename (e.g., `estimate_20230715_142530.txt`). This file contains all the estimate details and can be printed or emailed to customers.

## Customization

You can modify the following variables in the script to customize pricing:

- `TEXTURE_PRICES`: Dictionary containing price ranges for each texture type
- `MILEAGE_RATE`: Cost per mile for travel expenses

## License

This project is available for free use and modification.
