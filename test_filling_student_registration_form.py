from selene import browser, be, have, command


def test_filling_student_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Евгений')
    browser.element('#lastName').should(be.blank).type('Иванов')
    browser.element('#userEmail').should(be.blank).type('evgen@gmail.com')
    '''Клик по радиобаттону смог сделать только через js.
    В других случаях был «ElementClickInterceptedException», даже с добавлением явного ожидания в 1 мин.
    Если есть другой, более правильный метод, то расскажите.'''
    browser.element('#gender-radio-1').perform(command.js.click)
    browser.element('#userNumber').should(be.blank).type('+712345678')
    browser.element('#dateOfBirthInput').click()
    browser.all('[class=react-datepicker__year-select]>[value]').element_by(have.exact_text('1989')).click()
    browser.all('[class=react-datepicker__month-select]>[value]').element_by(have.exact_text('February')).click()
    browser.all('[class=react-datepicker__week]').second.click() #переделать селектор. выбирается что то рандомное и непонятно какая дата будет

    browser.element('[id="firstName"]').should(have.exact_text('Евгений')) #потом удалить. использую для создания скрина