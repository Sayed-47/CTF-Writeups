import base64
import hashlib
from cryptography.fernet import Fernet

# Function to generate a key from the password
def generate_key(password):
    password_bytes = password.encode('utf-8')
    key = hashlib.sha256(password_bytes).digest()
    return base64.urlsafe_b64encode(key)

# Function to decrypt an encrypted message
def decrypt_message(encrypted_message, password):
    try:
        # Generate the key from the password
        key = generate_key(password)
        cipher = Fernet(key)

        # Decrypt the message
        decrypted_data = cipher.decrypt(encrypted_message)
        return decrypted_data.decode('utf-8')  # Return as plain text
    except Exception:
        return None  # Return None if decryption fails

def main():
    # Encrypted messages (replace with actual data)
    encrypted_messages = [
        b"gAAAAABnbO285CLp59VwjWxb2E0zl3DbvgPG5pbroxMda_OucjsmCDHOPJs8_XZD5C5WfqKvUzE0WkELmDYb6OOOE-uCnKo7iy-XYrZhWXUxQMiui8s7s4qEBfTpOzfzgj3erPD-BSjTwvMH_nZwC3euR9PFTQhoraWUVPfsL61JgFL5uYZMU2lxgxaJHA5Ta_oC19GEhiDJuK9PLjxMWi6_Y1x4OsmGRPu-cfl9PyZYI_XR_-NAU-mMfDe6sKtYHV_YI94Oc-diHBRlXimoHe1J4deJFuS6RKzjq9oS79qF-40C5Hgi2BNAA9DPTqwhYkHrrdty11NzyUAZdn3d1Y9kDVGUgoI48XovDyC4Bz06-grIHbX0qbfTHnhUPwdw7eEvwdS2POrfNqR6B_KBgbcO3Eht5sv8u_-_wfBuiFD0GjShSiDV6pvzIm7MQf4qZtDs-ESnFhDnNlrt8u-vsmpI-t4q3kqKDcYH00TGn2UVrALy0QRGJ5UKpHQeyqICgP07rtHE_9dXszcWWU1INsMQNt3iSY5dw5-ZdcaaUqkqAajEN9xH7HUW3Pqz3SELn_KkZZyujM9OwVKO0rklZqsmfw_CPo9sVg3zH8pGMTXR18e29uOVK9HL5gNUQxtZMiK89obdC0GDR9rkWr6YBJeBDyHnHgBVOw==",
        # Add more encrypted messages here
    ]

    # Known years
    years = [str(year) for year in range(1970, 2025)]

    # Comprehensive list of countries
    countries = [
        "afghanistan", "albania", "algeria", "andorra", "angola", "antigua and barbuda",
        "argentina", "armenia", "australia", "austria", "azerbaijan", "bahamas",
        "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize",
        "benin", "bhutan", "bolivia", "bosnia and herzegovina", "botswana", "brazil",
        "brunei", "bulgaria", "burkina faso", "burundi", "cabo verde", "cambodia",
        "cameroon", "canada", "central african republic", "chad", "chile", "china",
        "colombia", "comoros", "congo", "costa rica", "croatia", "cuba", "cyprus",
        "czechia", "denmark", "djibouti", "dominica", "dominican republic", "ecuador",
        "egypt", "el salvador", "equatorial guinea", "eritrea", "estonia", "eswatini",
        "ethiopia", "fiji", "finland", "france", "gabon", "gambia", "georgia", "germany",
        "ghana", "greece", "grenada", "guatemala", "guinea", "guinea-bissau", "guyana",
        "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq",
        "ireland", "israel", "italy", "jamaica", "japan", "jordan", "kazakhstan", "kenya",
        "kiribati", "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon",
        "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg",
        "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshall islands",
        "mauritania", "mauritius", "mexico", "micronesia", "moldova", "monaco",
        "mongolia", "montenegro", "morocco", "mozambique", "myanmar", "namibia", "nauru",
        "nepal", "netherlands", "new zealand", "nicaragua", "niger", "nigeria", "north korea",
        "north macedonia", "norway", "oman", "pakistan", "palau", "panama", "papua new guinea",
        "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia",
        "rwanda", "saint kitts and nevis", "saint lucia", "saint vincent and the grenadines",
        "samoa", "san marino", "sao tome and principe", "saudi arabia", "senegal", "serbia",
        "seychelles", "sierra leone", "singapore", "slovakia", "slovenia", "solomon islands",
        "somalia", "south africa", "south korea", "south sudan", "spain", "sri lanka",
        "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan",
        "tanzania", "thailand", "timor-leste", "togo", "tonga", "trinidad and tobago",
        "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "uae",
        "united kingdom", "usa", "uruguay", "uzbekistan", "vanuatu", "vatican city",
        "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"
    ]

    # Generate all possible passwords
    passwords = [f"{year}{country}" for year in years for country in countries]

    # Try to decrypt each message
    for encrypted_message in encrypted_messages:
        for password in passwords:
            decrypted_message = decrypt_message(encrypted_message, password)
            if decrypted_message:
                print(f"Decryption successful! Password: {password}")
                print(f"Decrypted Message: {decrypted_message}")
                break
        else:
            print("Decryption failed for this message with all passwords.")

if __name__ == "__main__":
    main()
