#!/usr/bin/env python3
import secrets
import string
import argparse

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    char_pools = []
    if use_lower:
        char_pools.append(string.ascii_lowercase)
    if use_upper:
        char_pools.append(string.ascii_uppercase)
    if use_digits:
        char_pools.append(string.digits)
    if use_symbols:
        # safe set of symbols; remove characters that may cause shell issues if you want
        char_pools.append("!@#$%^&*()-_=+[]{};:,.<>?")

    if not char_pools:
        raise ValueError("At least one character type must be enabled.")

    # ensure at least one from each chosen category
    password_chars = [secrets.choice(pool) for pool in char_pools]

    all_chars = "".join(char_pools)
    remaining = length - len(password_chars)
    if remaining > 0:
        password_chars += [secrets.choice(all_chars) for _ in range(remaining)]

    # shuffle securely
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="password length (default 16)")
    parser.add_argument("--no-upper", action="store_true", help="exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="exclude symbols")
    args = parser.parse_args()

    pwd = generate_password(
        length=args.length,
        use_upper=not args.no_upper,
        use_lower=not args.no_lower,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols
    )
    print(pwd)

if __name__ == "__main__":
    main()
