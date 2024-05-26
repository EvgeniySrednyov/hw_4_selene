import allure

from pages.registration_page import RegistrationPage


@allure.title('Успешное заполнение  регистрационной формы')
def test_filling_student_registration_form(setup_browser):

    registration_page = RegistrationPage()

    with allure.step('Открытие формы'):
        registration_page.open()

    with allure.step('Заполнение формы'):
        registration_page.fill_first_name('Евгений')
        registration_page.fill_last_name('Иванов')
        registration_page.fill_user_email('evgen@gmail.com')
        registration_page.select_gender('Male')
        registration_page.fill_mobile_number('1234567890')
        registration_page.fill_date_of_birth('1989', 'February', '8')
        registration_page.fill_subjects('English')
        registration_page.select_hobbies('Music')
        registration_page.upload_picture('cat.png')
        registration_page.fill_current_address('Мой адрес не дом и не улица 25/17')
        registration_page.select_state('Haryana')
        registration_page.select_city('Panipat')

    with allure.step('Подтверждение формы'):
        registration_page.submit()

    with allure.step('Проверка заполнения формы'):
        registration_page.should_have_registered_user_with(
            'Евгений Иванов',
            'evgen@gmail.com',
            'Male',
            '1234567890',
            '08 February,1989',
            'English',
            'Music',
            'cat.png',
            'Мой адрес не дом и не улица 25/17',
            'Haryana Panipat'
        )
