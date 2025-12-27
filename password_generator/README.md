# Password Generator

A secure password generator with customizable options and password strength checker.

## Features

- Generate secure passwords using Python's `secrets` module
- Customizable password length
- Options to include/exclude:
  - Uppercase letters
  - Digits
  - Special characters
  - Ambiguous characters (0, O, l, 1)
- Generate multiple passwords at once
- Password strength calculator
- Security best practices

## Usage

```bash
python password_gen.py
```

## Example

```
Secure Password Generator
============================================================

Menu:
1. Generate Password
2. Generate Multiple Passwords
3. Check Password Strength
4. Exit

Select option (1-4): 1
Password length [12]: 16
Include uppercase? (y/n) [y]: y
Include digits? (y/n) [y]: y
Include special characters? (y/n) [y]: y
Exclude ambiguous characters (0,O,l,1)? (y/n) [n]: n

------------------------------------------------------------
Generated Password: K7@mP!qR9#xL2nT5
Strength: Very Strong (Score: 7/7)
------------------------------------------------------------
```

## Security Features

- Uses `secrets` module for cryptographically strong random generation
- Ensures at least one character from each selected category
- Provides password strength analysis
- Suggests improvements for weak passwords
