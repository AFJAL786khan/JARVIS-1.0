from twilio.rest import Client
# from Body.Listen_Hindi import Listen_Hindi
# from Body.Speak import Speak

contacts = {
    'John': '+1234567890',  # Replace with actual numbers
    'Alice': '+916367454630',  # Replace with actual numbers
    'Afzal': '+918003117366'
}

print('Whom do you want to send a message to?')
person = input("Enter Person Name: ")

# Check if the person exists in the contacts
if person in contacts:
    print('What message should I send?')
    Message = input('Enter Message: ')
    number = contacts[person]
    
    account_sid = 'AC5dd5d831ad1b3f9ff6c2e2172cc1358b'
    auth_token = '7d5e57eafccf23ac77b4382b40c221a0'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=Message,
    to=f'whatsapp:{number}'
    )
    print(message.sid)