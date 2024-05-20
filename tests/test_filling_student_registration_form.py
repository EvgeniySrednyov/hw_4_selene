from selene import browser, have, command
import os


def test_filling_student_registration_form(setting_browser):
    '''
    Заполнение формы
    '''
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Евгений')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('evgen@gmail.com')
    browser.element('#gender-radio-1').perform(command.js.click)
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.all('[class=react-datepicker__year-select]>[value]').element_by(have.exact_text('1989')).click()
    browser.all('[class=react-datepicker__month-select]>[value]').element_by(have.exact_text('February')).click()
    browser.all('[class=react-datepicker__week]').second.click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('#hobbies-checkbox-3').perform(command.js.click)
    browser.element('#uploadPicture').send_keys(os.path.abspath(
        '../cat.png'))
    browser.element('#currentAddress').perform(command.js.scroll_into_view).click()
    browser.element('#currentAddress').type('Мой адрес не дом и не улица 25/17')
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').click()

    '''
    Проверка заполнения полей формы
    '''
    browser.element('.table').all('td').even.should(
        have.exact_texts(
        'Евгений Иванов',
        'evgen@gmail.com',
        'Male',
        '1234567890',
        '08 February,1989',
        'English',
        'Music',
        'cat.png',
        'Мой адрес не дом и не улица 25/17',
        'Haryana Panipat'))