from selene import browser, have, by, command

import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        browser.all('[name=gender').element_by(have.value(value)).element('..').click()

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click().element(by.text(year)).click()
        browser.element(".react-datepicker__month-select").click().element(by.text(month)).click()
        browser.element(f".react-datepicker__day--00{day}").click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, file):
        browser.element('#uploadPicture').send_keys(resource.path(file))

    def fill_current_address(self, value):
        browser.element('#currentAddress').perform(command.js.scroll_into_view).click()
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state').click().element(by.text(value)).click()

    def select_city(self, value):
        browser.element('#city').click().element(by.text(value)).click()

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered_user_with(self, full_name, user_email, gender, mobile_number, date_of_birth, subjects, hobbies, picture,
                                         current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                user_email,
                gender,
                mobile_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city))
