from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    pass

account_activation_token = AccountActivationTokenGenerator()

#Django’s built-in, time-limited token system.