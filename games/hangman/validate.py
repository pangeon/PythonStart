class Validator:

    warining_message = "Change your choice. Enter number not letter"

    def catch_incorrect_value(user_data, message):
        while (type(user_data) == str):
            try:
                return int(user_data)
            except:
                user_data = input(message + ": ")
