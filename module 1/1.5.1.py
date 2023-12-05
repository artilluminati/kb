def get_user_information():
    print("Please enter your information:")
    full_name = input("ФИО: ")
    phone_number = input("Телефон: ")
    email = input("Адрес электронной почты: ")
    address = input("Адрес: ")

    user_info = {
        "Full Name": full_name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address
    }

    return user_info

user_info = get_user_information()
print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key}: {value}")