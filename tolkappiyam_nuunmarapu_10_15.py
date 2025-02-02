# -*- coding: utf-8 -*-
"""Tolkappiyam_Nuunmarapu_10-15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1390SySpbooA3-YQvszBuC-gQQn_efhbQ
"""

pip install Open-Tamil

"""**தமிழ் எழுத்து வடிவங்கள், மாத்திரைகள் பற்றிய தகவல்களை அச்சிடும் பைத்தான் நிரல்**"""

import tamil
# தமிழ் எழுத்து வடிவங்கள் மற்றும் மாத்திரைகள் பற்றிய தகவல்களை அச்சிடும் பைத்தான் நிரல்

def print_tamil_letters_info():
    # நூற்பா 10: உயிர்மெய்க்கு அளபு
    print("நூற்பா 10: உயிர்மெய்க்கு அளபு")
    print("மெய்யோடு இயையினும் உயிர் இயல் திரியா.")
    print("உயிர்மெய் எழுத்துகள்: க, கா, கி, கீ, கு, கூ, கெ, கே, கை, கொ, கோ, கௌ")
    print("இவை உயிர் மற்றும் மெய் எழுத்துகளின் கூட்டு வடிவங்கள்.")
    print()

    # நூற்பா 11: தனிமெய்க்கு அளபு
    print("நூற்பா 11: தனிமெய்க்கு அளபு")
    print("மெய்யது அளபே அரை என மொழிப.")
    print("தனிமெய் எழுத்துகள்: க், ங், ச், ஞ், ட், ண், த், ந், ப், ம், ய், ர், ல், வ், ழ், ள், ற், ன்")
    print("இவை அரை மாத்திரை கொண்ட தனிமெய் எழுத்துகள்.")
    print()

    # நூற்பா 12: சார்பெழுத்துகளுக்கு அளபு
    print("நூற்பா 12: சார்பெழுத்துகளுக்கு அளபு")
    print("அவ் இயல் நிலையும் ஏனை மூன்றே.")
    print("சார்பெழுத்துகள்: கேண்மியா, நாகு, எஃகு")
    print("இவை சார்பெழுத்துகள் மற்றும் அவற்றின் மாத்திரைகள்.")
    print()

    # நூற்பா 13: மகரத்தின் மாத்திரை சுருக்கம்
    print("நூற்பா 13: மகரத்தின் மாத்திரை சுருக்கம்")
    print("அரை அளபு குறுகல் மகரம் உடைத்தே.")
    print("மகர எழுத்து (ம்) சில சந்தர்ப்பங்களில் அரை மாத்திரையாக குறுகும்.")
    print("உதாரணம்: போன்ம், வரும்வண்ணக்கன்")
    print()

    # நூற்பா 14: புள்ளியின் வடிவ வேற்றுமை
    print("நூற்பா 14: புள்ளியின் வடிவ வேற்றுமை")
    print("உள் பெறு புள்ளி உரு ஆகும்மே.")
    print("மகரம் (ம்) மற்றும் பகரம் (ப்) ஆகியவற்றின் புள்ளி வடிவ வேற்றுமை.")
    print("உதாரணம்: ம, ப")
    print()

    # நூற்பா 15: தனிமெய் எழுத்துகளின் இயற்கை
    print("நூற்பா 15: தனிமெய் எழுத்துகளின் இயற்கை")
    print("மெய்யின் இயற்கை புள்ளியொடு நிலையல்.")
    print("தனிமெய் எழுத்துகள் புள்ளியுடன் நிற்கும்.")
    print("உதாரணம்: க், ங், ச், ஞ், ட், ண், த், ந், ப், ம், ய், ர், ல், வ், ழ், ள், ற், ன்")
    print()

    # நூற்பா 16: எகர ஒகர எழுத்துகளின் இயற்கை
    print("நூற்பா 16: எகர ஒகர எழுத்துகளின் இயற்கை")
    print("எகர ஒகரத்து இயற்கையும் அற்றே.")
    print("எகரம் (ெ) மற்றும் ஒகரம் (ொ) ஆகியவற்றின் இயல்பு.")
    print("உதாரணம்: எ், ஒ்")
    print()

# நிரலை இயக்குதல்
print_tamil_letters_info()

"""**விளையாட்டு நிரல்**"""

import random

# தமிழ் எழுத்துகள் மற்றும் மாத்திரைகள்
uyirmei_letters = ["க", "கா", "கி", "கீ", "கு", "கூ", "கெ", "கே", "கை", "கொ", "கோ", "கௌ"]
mei_letters = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன்"]
mathirai_info = {
    "க": 1, "கா": 2, "கி": 1, "கீ": 2, "கு": 1, "கூ": 2, "கெ": 1, "கே": 2, "கை": 2, "கொ": 2, "கோ": 2, "கௌ": 2,
    "க்": 0.5, "ங்": 0.5, "ச்": 0.5, "ஞ்": 0.5, "ட்": 0.5, "ண்": 0.5, "த்": 0.5, "ந்": 0.5, "ப்": 0.5, "ம்": 0.5,
    "ய்": 0.5, "ர்": 0.5, "ல்": 0.5, "வ்": 0.5, "ழ்": 0.5, "ள்": 0.5, "ற்": 0.5, "ன்": 0.5
}

# எழுத்து யோசனை விளையாட்டு
def guess_letter_game():
    print("விளையாட்டு 1: எழுத்து யோசனை")
    print("நீங்கள் ஒரு தமிழ் எழுத்தை யோசிக்க வேண்டும். நான் அதைக் கண்டுபிடிப்பேன்!")
    input("யோசித்து முடிந்ததும் Enter அழுத்தவும்...")
    letter = random.choice(uyirmei_letters + mei_letters)
    print(f"நான் யோசித்த எழுத்து: {letter}")
    print()

# மாத்திரை கணக்கு விளையாட்டு
def mathirai_count_game():
    print("விளையாட்டு 2: மாத்திரை கணக்கு")
    letter = random.choice(list(mathirai_info.keys()))
    print(f"எழுத்து: {letter}")
    answer = input("இந்த எழுத்தின் மாத்திரை எவ்வளவு? (எண்ணாக உள்ளிடவும்): ")
    if float(answer) == mathirai_info[letter]:
        print("சரியான பதில்! வாழ்த்துக்கள்!")
    else:
        print(f"தவறான பதில். சரியான பதில்: {mathirai_info[letter]}")
    print()

# உயிர்மெய் கண்டுபிடி விளையாட்டு
def uyirmei_find_game():
    print("விளையாட்டு 3: உயிர்மெய் கண்டுபிடி")
    letter = random.choice(uyirmei_letters)
    print(f"எழுத்து: {letter}")
    answer = input("இது உயிர்மெய் எழுத்தா? (ஆம்/இல்லை): ").strip().lower()
    if answer == "ஆம்":
        print("சரியான பதில்! வாழ்த்துக்கள்!")
    else:
        print("தவறான பதில். இது உயிர்மெய் எழுத்து.")
    print()

# முதன்மை நிரல்
def main():
    print("தமிழ் எழுத்து விளையாட்டுக்களுக்கு வரவேற்கிறோம்!")
    while True:
        print("1. எழுத்து யோசனை")
        print("2. மாத்திரை கணக்கு")
        print("3. உயிர்மெய் கண்டுபிடி")
        print("4. வெளியேறு")
        choice = input("உங்கள் தேர்வு (1-4): ").strip()

        if choice == "1":
            guess_letter_game()
        elif choice == "2":
            mathirai_count_game()
        elif choice == "3":
            uyirmei_find_game()
        elif choice == "4":
            print("விளையாட்டை முடித்துவிட்டு வெளியேறுகிறீர்கள். நன்றி!")
            break
        else:
            print("தவறான தேர்வு. மீண்டும் முயற்சிக்கவும்.")
        print()

# நிரலை இயக்குதல்
if __name__ == "__main__":
    main()

!pip install Open-Tamil
import tamil
import unicodedata

class தமிழ்_இலக்கண_பகுப்பாய்வி:
    def __init__(self):
        # தமிழ் எழுத்துக்களை வரையறு
        self.மெய்_எழுத்துகள் = ['க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்',
                                'ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்', 'ற்', 'ன்']
        self.உயிர்_எழுத்துகள் = ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ']

    def எழுத்து_வகை_ஆய்வு(self, எழுத்து):
        """கொடுக்கப்பட்ட எழுத்து மெய்யா, உயிரா, உயிர்மெய்யா என ஆராய்தல்"""
        if எழுத்து in self.மெய்_எழுத்துகள்:
            return "மெய்", 0.5  # மெய் - அரை மாத்திரை
        elif எழுத்து in self.உயிர்_எழுத்துகள்:
            return "உயிர்", 1.0  # உயிர் - ஒரு மாத்திரை
        else:
            # உயிர்மெய்யா என சோதித்தல்
            அடிப்படை_எழுத்து = unicodedata.normalize('NFD', எழுத்து)[0]
            if அடிப்படை_எழுத்து in [c.strip('்') for c in self.மெய்_எழுத்துகள்]:
                return "உயிர்மெய்", 1.0  # உயிர்மெய் - ஒரு மாத்திரை
            return "தெரியவில்லை", 0

    def புள்ளி_விதிகள்_சோதனை(self, எழுத்து):
        """புள்ளி விதிகளை சோதித்தல்"""
        if எழுத்து in self.மெய்_எழுத்துகள்:
            return "புள்ளி உள்ளது"
        elif எழுத்து in ['எ்', 'ஒ்']:
            return "சிறப்பு நிலை: எகர ஒகர புள்ளியுடன்"
        else:
            return "புள்ளி இல்லை"

    def மகர_சிறப்பு_விதிகள்_ஆய்வு(self, உரை):
        """மகர எழுத்தின் சிறப்பு விதிகளை ஆராய்தல்"""
        முடிவுகள் = []
        for இடம், எழுத்து in enumerate(உரை):
            if எழுத்து == 'ம்':
                if இடம் < len(உரை) - 1 and உரை[இடம்+1] in ['வ', 'ப']:
                    முடிவுகள்.append(f"இடம் {இடம்} இல் உள்ள மகரம் கால் மாத்திரையாக குறையலாம்")
        return முடிவுகள்

    def விதிகள்_விளக்கம்(self, உரை):
        """அனைத்து இலக்கண விதிகளையும் விளக்குதல்"""
        முடிவுகள் = []
        for எழுத்து in உரை:
            எழுத்து_வகை, மாத்திரை = self.எழுத்து_வகை_ஆய்வு(எழுத்து)
            புள்ளி_நிலை = self.புள்ளி_விதிகள்_சோதனை(எழுத்து)

            முடிவுகள்.append({
                'எழுத்து': எழுத்து,
                'வகை': எழுத்து_வகை,
                'மாத்திரை': மாத்திரை,
                'புள்ளி_நிலை': புள்ளி_நிலை
            })

        return முடிவுகள்

def முதன்மை():
    பகுப்பாய்வி = தமிழ்_இலக்கண_பகுப்பாய்வி()
    # எடுத்துக்காட்டு
    எடுத்துக்காட்டு_சொல் = "கண்ணன்"
    print("\nஆய்வு செய்யும் சொல்:", எடுத்துக்காட்டு_சொல்)
    முடிவுகள் = பகுப்பாய்வி.விதிகள்_விளக்கம்(எடுத்துக்காட்டு_சொல்)

    for முடிவு in முடிவுகள்:
        print(f"\nஎழுத்து: {முடிவு['எழுத்து']}")
        print(f"வகை: {முடிவு['வகை']}")
        print(f"மாத்திரை: {முடிவு['மாத்திரை']}")
        print(f"புள்ளி நிலை: {முடிவு['புள்ளி_நிலை']}")

    # மகர சிறப்பு விதிகள் சோதனை
    மகர_சொல் = "வரும்வண்ணம்"
    print("\nமகர சிறப்பு விதிகள் ஆய்வு:", மகர_சொல்)
    மகர_முடிவுகள் = பகுப்பாய்வி.மகர_சிறப்பு_விதிகள்_ஆய்வு(மகர_சொல்)
    for முடிவு in மகர_முடிவுகள்:
        print(முடிவு)

if __name__ == "__main__":
    முதன்மை()