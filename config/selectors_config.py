LOGIN_PAGE = {
    # Login form inputs
    "username_input": "input[name='username']",
    "password_input": "input[name='password']",
    # Submit button for logging in
    "submit_button": "button[type='submit']",
}

DASHBOARD_PAGE = {
    # Button to navigate to the "My Info" section
    "my_info_button": "//span[text()='My Info']",
}

PERSONAL_PAGE = {
    # Personal information input fields
    "first_name_input": "input[name='firstName']",
    "last_name_input": "input[name='lastName']",
    "middle_name_input": "input[name='middleName']",
    # Employee ID input (first input field of this type)
    "employee_id_input": "(//input[contains(@class, 'oxd-input oxd-input--active')])[1]",
    # Other ID input (second input field of this type)
    "other_id_input": "(//input[contains(@class, 'oxd-input oxd-input--active')])[2]",
    # Driver's license number input (third input field of this type)
    "drivers_license_number_input": "(//input[contains(@class, 'oxd-input oxd-input--active')])[3]",
    # License expiry date input
    "license_expiry_date_icon": "//i[contains(@class, 'bi-calendar') and contains(@class, 'oxd-date-input-icon')]",
    "license_expiry_date_datepicker": "(//div[@class='oxd-calendar-date'])[1]",
    # Nationality dropdown
    "nationality_icon": "(//div[contains(@class, 'oxd-select-text--arrow')])[1]",
    "nationality_dropdown": "//div[contains(@class, 'oxd-select-option') and text()='Afghan']",
    # Marital status dropdown
    "marital_status_icon": "(//div[contains(@class, 'oxd-select-text--arrow')])[2]",
    "marital_status_dropdown": "//div[contains(@class, 'oxd-select-option') and text()='Married']",
    # Date of birth input
    "date_of_birth_icon": "//i[contains(@class, 'bi-calendar') and contains(@class, 'oxd-date-input-icon')]",
    "date_of_birth_datepicker": "(//div[@class='oxd-calendar-date'])[1]",
    # Gender radio button
    "gender_radio": "//input[contains(@class, 'oxd-radio-input oxd-radio-input--active')]",
    # Save button
    "save_button": "(//button[@type='submit'])[1]",
    # Loading spinner
    "loading_spinner": ".oxd-loading-spinner",
}
