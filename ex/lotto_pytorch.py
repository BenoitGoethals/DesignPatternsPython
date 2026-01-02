import torch

def generate_lotto_numbers(num_numbers=6, min_val=1, max_val=45):
    """
    Genereer lotto nummers met PyTorch.
    
    Args:
        num_numbers: Aantal nummers om te genereren (default: 6)
        min_val: Minimum waarde (default: 1)
        max_val: Maximum waarde (default: 45)
    
    Returns:
        Gesorteerde lijst van unieke lotto nummers
    """
    # Genereer unieke nummers door permutatie te gebruiken
    range_tensor = torch.arange(min_val, max_val + 1)
    
    # Shuffle de nummers
    perm = torch.randperm(len(range_tensor))
    
    # Selecteer de eerste num_numbers
    selected = range_tensor[perm[:num_numbers]]
    
    # Sorteer voor leesbaarheid
    lotto_numbers = sorted(selected.tolist())
    
    return lotto_numbers


def generate_lotto_with_bonus(main_numbers=6, bonus_numbers=1, min_val=1, max_val=45):
    """
    Genereer lotto nummers met bonus nummer(s).
    
    Args:
        main_numbers: Aantal hoofdnummers
        bonus_numbers: Aantal bonusnummers
        min_val: Minimum waarde
        max_val: Maximum waarde
    
    Returns:
        Tuple van (hoofdnummers, bonusnummers)
    """
    total = main_numbers + bonus_numbers
    range_tensor = torch.arange(min_val, max_val + 1)
    perm = torch.randperm(len(range_tensor))
    
    all_numbers = range_tensor[perm[:total]].tolist()
    
    main = sorted(all_numbers[:main_numbers])
    bonus = sorted(all_numbers[main_numbers:])
    
    return main, bonus


# Voorbeelden
if __name__ == "__main__":
    print("=== Lotto Number Generator met PyTorch ===\n")
    
    # Standaard 6 nummers
    print("6 lotto nummers (1-45):")
    numbers = generate_lotto_numbers()
    print(f"Jouw nummers: {numbers}\n")
    
    # Met bonus nummer
    print("6 nummers + 1 bonus nummer:")
    main, bonus = generate_lotto_with_bonus()
    print(f"Hoofdnummers: {main}")
    print(f"Bonusnummer: {bonus}\n")
    
    # Custom range (bijvoorbeeld EuroMillions: 1-50)
    print("EuroMillions style (5 nummers van 1-50 + 2 sterren van 1-12):")
    main_nums = generate_lotto_numbers(num_numbers=5, min_val=1, max_val=500)
    star_nums = generate_lotto_numbers(num_numbers=2, min_val=1, max_val=1200)
    print(f"Nummers: {main_nums}")
    print(f"Sterren: {star_nums}\n")
    
    # Meerdere trekkingen
    print("5 verschillende trekkingen:")
    for i in range(1, 6):
        nums = generate_lotto_numbers()
        print(f"Trekking {i}: {nums}")
    
    print("\n⚠️  Let op: Lotto nummers zijn compleet willekeurig!")
    print("Dit is alleen voor demonstratie/entertainment doeleinden.")
