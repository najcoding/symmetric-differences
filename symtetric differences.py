# Python program to find the symmetric difference between two sets

def get_set_from_input(prompt):
    """
    Reads a line of input, splits it by spaces, and returns a set of elements.
    Handles empty input gracefully.
    """
    try:
        elements = input(prompt).strip()
        if not elements:
            return set()
        return set(elements.split())
    except Exception as e:
        print(f"Error reading input: {e}")
        return set()

def main():
    print("=== Symmetric Difference Finder ===")
    
    
    set1 = get_set_from_input("Enter elements of the first set (space-separated): ")
    set2 = get_set_from_input("Enter elements of the second set (space-separated): ")
    
   
    symmetric_diff = set1.symmetric_difference(set2)
    
   
    print("\nFirst Set:", set1)
    print("Second Set:", set2)
    print("Symmetric Difference:", symmetric_diff)

if __name__ == "__main__":
    main()
