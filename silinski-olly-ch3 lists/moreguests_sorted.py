guest_list = ['vincent van gogh', 'anthony bourdain', 'jane goodall', 'ursula le guin']

gogh = f"Vincent Van Gogh, I would love to talk with you about your tree paintings, please join me for a meal."
bourdain = f"Anthony Bourdain, I would love to hear your thoughts on current geopolitical conflict, lets grab some food."
goodall = f"Jane Goodall, I would love to talk with you about human-animal relations. Please join me for a meal."
guin = f"Ursula le Guin, I would love to hear your thoughts on literally anything, please join me for a meal!"
talley = f"Andre Leon Talley, please join me to have a discussion over food about making the fashion industry more sustainable!"
lorde = f"Audre Lorde, I would love to hear your thoughts about the current activism movements, please join me for a meal!"
irwin = f"I'd love to share a meal with you discussing human-animal relationships!"

message_list = ['Vincent Van Gogh, I would love to talk with you about your tree paintings, please join me for a meal.', 'Anthony Bourdain, I would love to hear your thoughts on current geopolitical conflict, lets grab some food.', 'Jane Goodall, I would love to talk with you about human-animal relations. Please join me for a meal.', 'Ursula le Guin, I would love to hear your thoughts on literally anything, please join me for a meal!', 'Andre Leon Talley, please join me to have a discussion over food about making the fashion industry more sustainable!', 'Audre Lorde, I would love to hear your thoughts about the current activism movements, please join me for a meal!', 'I would love to share a meal with you discussing human-animal relationships!']

print(gogh)
print(bourdain)
print(goodall)
print(guin)

guest_list.append('andre leon talley')
guest_list.insert(0, 'audre lorde')
guest_list.insert(3, 'steve irwin')

print(sorted(guest_list))
print(f"Everyone, I found a larger table! Come join me!")
print(sorted(message_list))


