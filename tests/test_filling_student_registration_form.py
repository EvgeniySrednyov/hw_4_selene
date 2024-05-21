from data.users import User
from pages.registration_page import RegistrationPage


def test_filling_student_registration_form(setting_browser):

    registration_page = RegistrationPage()
    user = User(
        first_name='Евгений',
        last_name='Иванов',
        email='evgen@gmail.com',
        gender='Male',
        number='1234567890',
        year='1989',
        month='February',
        day='8',
        subjects='English',
        hobbies='Music',
        picture='cat.png',
        current_address='Мой адрес не дом и не улица 25/17',
        state='Haryana',
        city='Panipat'
    )
    registration_page.open()
    registration_page.register(user)
    registration_page.should_have_registered_user_with(user)
