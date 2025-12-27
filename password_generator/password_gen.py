"""
Password Generator Application
A secure password generator with customizable options.
"""

import random
import string
import secrets


class PasswordGenerator:
    """A secure password generator with various options."""
    
    def __init__(self):
        """Initialize character sets for password generation."""
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate(self, length=12, use_uppercase=True, use_digits=True, 
                 use_special=True, exclude_ambiguous=False):
        """
        Generate a secure random password.
        
        Args:
            length: Length of the password (default: 12)
            use_uppercase: Include uppercase letters (default: True)
            use_digits: Include digits (default: True)
            use_special: Include special characters (default: True)
            exclude_ambiguous: Exclude ambiguous characters like 0, O, l, 1 (default: False)
        
        Returns:
            A randomly generated password string
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters!")
        
        # Build character pool
        chars = self.lowercase
        
        if exclude_ambiguous:
            ambiguous = "il1Lo0O"
            chars = ''.join(c for c in chars if c not in ambiguous)
        
        if use_uppercase:
            upper = self.uppercase
            if exclude_ambiguous:
                upper = ''.join(c for c in upper if c not in "IO")
            chars += upper
        
        if use_digits:
            digits = self.digits
            if exclude_ambiguous:
                digits = ''.join(c for c in digits if c not in "01")
            chars += digits
        
        if use_special:
            chars += self.special
        
        if not chars:
            raise ValueError("No characters available for password generation!")
        
        # Generate password ensuring at least one character from each selected category
        password = []
        
        # Add at least one character from each category
        password.append(secrets.choice(self.lowercase))
        if use_uppercase:
            password.append(secrets.choice(self.uppercase))
        if use_digits:
            password.append(secrets.choice(self.digits))
        if use_special:
            password.append(secrets.choice(self.special))
        
        # Fill the rest randomly
        remaining_length = length - len(password)
        password.extend(secrets.choice(chars) for _ in range(remaining_length))
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password)
        
        return ''.join(password)
    
    def calculate_strength(self, password):
        """
        Calculate password strength score.
        
        Returns:
            A tuple of (score, strength_label)
        """
        score = 0
        
        # Length check
        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if len(password) >= 16:
            score += 1
        
        # Character variety check
        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in self.special for c in password):
            score += 1
        
        # Determine strength label
        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        elif score <= 6:
            strength = "Strong"
        else:
            strength = "Very Strong"
        
        return score, strength


def main():
    """Main function to run the password generator."""
    gen = PasswordGenerator()
    
    print("=" * 60)
    print("Secure Password Generator".center(60))
    print("=" * 60)
    
    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Generate Multiple Passwords")
        print("3. Check Password Strength")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '4':
            print("Stay secure!")
            break
        
        elif choice == '1':
            try:
                length = int(input("Password length [12]: ") or "12")
                use_upper = input("Include uppercase? (y/n) [y]: ").strip().lower() != 'n'
                use_digits = input("Include digits? (y/n) [y]: ").strip().lower() != 'n'
                use_special = input("Include special characters? (y/n) [y]: ").strip().lower() != 'n'
                exclude_ambiguous = input("Exclude ambiguous characters (0,O,l,1)? (y/n) [n]: ").strip().lower() == 'y'
                
                password = gen.generate(length, use_upper, use_digits, use_special, exclude_ambiguous)
                score, strength = gen.calculate_strength(password)
                
                print("\n" + "-" * 60)
                print(f"Generated Password: {password}")
                print(f"Strength: {strength} (Score: {score}/7)")
                print("-" * 60)
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            try:
                count = int(input("How many passwords? [5]: ") or "5")
                length = int(input("Password length [12]: ") or "12")
                
                print("\n" + "=" * 60)
                print("Generated Passwords:".center(60))
                print("=" * 60)
                
                for i in range(count):
                    password = gen.generate(length)
                    score, strength = gen.calculate_strength(password)
                    print(f"{i+1}. {password} [{strength}]")
                
                print("=" * 60)
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            password = input("Enter password to check: ").strip()
            if password:
                score, strength = gen.calculate_strength(password)
                print(f"\nPassword Strength: {strength} (Score: {score}/7)")
                
                print("\nSuggestions:")
                if len(password) < 12:
                    print("- Use at least 12 characters")
                if not any(c.isupper() for c in password):
                    print("- Add uppercase letters")
                if not any(c.isdigit() for c in password):
                    print("- Add digits")
                if not any(c in gen.special for c in password):
                    print("- Add special characters")
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
