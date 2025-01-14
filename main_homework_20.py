from utils.homework20 import send_email, create_welcome_letter


def main():
    car_information = {
        'car_model': 'Yaris Гібрид',
        'price': 29370.95,
        'year_of_release': 2024 ,
        'number_of_seats': 5,
        'maximum_speed': 175,
        'interior_features': ['кермо оздоблене шкірою','має фонове освітлення','шкіряне комфортне кермо'],
        'luggage_compartment': {
            'the_volume_of_the_luggage_compartment': 191,
            'luggage_space_with_the_seats_laid_down': 852
        },

    }
    body_information = create_welcome_letter(car_information)
    print(body_information)
    recipients = ['msan091010@ukr.net']
    send_email(recipients,
               mail_subject='"Yaris Гібрид Комплектація Lounge" Саме таке авто вам потрібно! '
               , mail_body=body_information,
               )


if __name__ == '__main__':
    main()