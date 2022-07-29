import random
import i18n


def lang() -> None:
    """Language config"""
    # set localisations directory
    i18n.load_path.append('translations/')
    # Default localisation
    i18n.set('fallback', 'en-us')
    try:
        lang_choice: int = int(input('Choose your language: [1]=EN [2]=UA:'))
    except ValueError:
        print('Choose your language: [1]=EN [2]=UA:')
    else:
        if lang_choice == 2:
            i18n.set('fallback', 'ua-ua')
        else:
            pass


def err() -> None:
    """Check for win"""
    if choice == random.randint(1, 3):
        print(i18n.t('locale.win'))
    else:
        print(i18n.t('locale.lose'))


if __name__ == "__main__":
    # Language set
    lang()

    print(i18n.t('locale.welcome'))

    # Main loop
    while True:
        try:
            # Check input for integer from 1 to 3
            choice: int = int(input(i18n.t('locale.thimble_number')))
        except ValueError:
            print(i18n.t('locale.thimble_number_error'))
        else:
            if 1 <= choice <= 3:
                # Check for win
                err()
            else:
                print(i18n.t('locale.thimble_number_error'))
