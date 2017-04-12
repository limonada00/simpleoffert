from django.contrib.auth.mixins import UserPassesTestMixin


class BaseUserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return True


class SuperUserPassesTestMixin(BaseUserPassesTestMixin):
    raise_exception = True
    def test_func(self):
        if not self.request.user.is_superuser:
            return False

        return True and super().test_func()


class CheckUserPassesTestMixin(BaseUserPassesTestMixin):
    def test_func(self):
        offer=self.kwargs.get('offer')
        if not offer.author == self.request.user:
            return False

        return True and super().test_func()




