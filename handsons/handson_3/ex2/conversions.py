#Challenged myself to do each function on one line

def meters_to_feet(meters: float) -> float: return meters / 0.3048

def feet_to_meters(feet: float) -> float: return feet * 0.3048

def title(): print("Feet and Meters Converter")

def menu() -> str: return input("\nConversion Menu:\nA.\tFeet to Meters\nB.\tMeters to Feet\nSelect an Option: ")