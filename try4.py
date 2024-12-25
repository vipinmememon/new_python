import qrcode
import time
menu = {
    "pasta": 40,
    "burger": 50,
    "salad": 40,
    "coffee": 60,
    "shake": 90,
    "sandwich": 120
}

# Seats: 0 = available, 1 = booked
seat = [0] * 11

bill = {}

def view_menu():
    print("---- MENU ----")
    for item, price in menu.items():
        print(f"{item.capitalize()} - Rs{price}")
    print("----------------")


def book_seat():
    seat_no = int(input("Enter your seat number (1-10): "))
    if seat_no < 1 or seat_no > 10:
        print("Invalid seat number. Please select between 1 and 10.")
    elif seat[seat_no] == 1:
        print("Sorry, this seat is already booked.")
    else:
        seat[seat_no] = 1
        bill[seat_no] = 0
        print(f"Your seat number {seat_no} has been booked.")


def ordered_item():
    seat_no = int(input("Enter your seat number: "))
    if seat_no not in bill:
        print(f"Seat number {seat_no} is not booked.")
        return

    item = input("Enter the item you want to order: ").lower()
    if item in menu:
        cost = menu[item]
        bill[seat_no] += cost
        print(f"Your item {item} has been added. ")
    else:
        print(f"Sorry, {item} is not available.")


def bill_amount():
    seat_no = int(input("Enter your seat number: "))
    if seat_no in bill and bill[seat_no] > 0:
        print(f"Your total bill for seat {seat_no} is Rs{bill[seat_no]}.")
        print("Please make the payment using the QR code.")
        
        # Generate UPI Payment QR Code
        phonepay_url = f'upi://pay?pa=8102303285@ybl&pn=vipin&mc=1234&am={bill[seat_no]}&tn=Thank you for payment'
        payphone_qrcode = qrcode.make(phonepay_url)
        payphone_qrcode.save('payphone_qrcode.png')
        payphone_qrcode.show()
        time.sleep(10)

        # waiting for payment confirmation
        while True:
            confirmation = input("Enter 'yes' to confirm payment or 'no' to cancel: ").strip().lower()
            if confirmation == 'yes':
                print("Payment confirmed. Thank you for dining with us!")
                texttspeech('Payment confirmed. Thank you for dining with us')
                seat[seat_no] = 0  # Mark seat as available
                del bill[seat_no]
                break
            elif confirmation == 'no':
                print("Payment not completed. Please try again.")
                texttspeech('Payment not completed. Please try again')
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print(f"No orders found for seat {seat_no}.")

#for voice
import speech_recognition as sr
import pyttsx3

#function to sppech to text
def sptext():
    recornige=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        recornige.adjust_for_ambient_noise(source)
        audio=recornige.listen(source)
        try:
            print('reconiging......')
            data=recornige.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print('not understand')



#function to yext to speech
def texttspeech(data):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.say(data)
    engine.runAndWait()


if __name__=='__main__': 
    texttspeech('welcome to vipin restaurant')
    while True:
       print("\n_______  Restaurant Management _______")
       print("1 - Book Seat")
       print("2 - View Menu")
       print("3 - Order Item")
       print("4 - Bill")
       print("5 - Exit")
       texttspeech('enter a choice')
       choice = int(input("Enter your choice: "))
       
       
       if choice == 1:
           book_seat()
       elif choice == 2:
           view_menu()
       elif choice == 3:
           ordered_item()
       elif choice == 4:
           bill_amount()
       elif choice == 5:
           print("Thank you! Closing the program.")
           texttspeech('Thank you! Closing the program.')
           break
       else:
           print("Invalid input Please try again")
           texttspeech('please  enter a valid choice')

