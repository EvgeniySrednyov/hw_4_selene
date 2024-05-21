from selene import browser, have, by, command

import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[name=gender').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.number)
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click().element(by.text(user.year)).click()
        browser.element(".react-datepicker__month-select").click().element(by.text(user.month)).click()
        browser.element(f".react-datepicker__day--00{user.day}").click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobbies)).click()
        browser.element('#uploadPicture').send_keys(resource.path(user.picture))
        browser.element('#currentAddress').perform(command.js.scroll_into_view).click()
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#state').click().element(by.text(user.state)).click()
        browser.element('#city').click().element(by.text(user.city)).click()
        browser.element('#submit').click()

    def should_have_registered_user_with(self, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.number,
                f'0{user.day} {user.month},{user.year}',
                user.subjects,
                user.hobbies,
                user.picture,
                user.current_address,
                f'{user.state} {user.city}'))
