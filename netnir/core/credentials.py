import keyring
from getpass import getpass
from netnir.constants import SERVICE_NAME


class Credentials:
    def __init__(
        self,
        username=None,
        password=None,
        confirm_password=None,
        service_name=SERVICE_NAME,
    ):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.service_name = service_name
        self.message = "netnir network authentication"
        self.status = None

    def create(self):
        if self.password is None:
            self.password = getpass(f"{self.message} password: ")
            self.confirm_password = getpass(f"{self.message} confirm passowrd: ")

        if self.password == self.confirm_password:
            keyring.set_password(
                service_name=self.service_name,
                username=self.username,
                password=self.password,
            )

        self.status = "created"
        self.password = self._fetch()

        return self._schema()

    def fetch(self):
        self.password = self._fetch()

        if self.password is None:
            self.create()
        else:
            self.status = "fetched"

        self.password = self._fetch()

        return self._schema()

    def delete(self):
        if self.confirm_password is None:
            self.confirm_password = getpass(f"{self.message} password: ")

        creds = self.fetch()
        self.password = creds["password"]

        if self.password == self.confirm_password:
            keyring.delete_password(
                service_name=self.service_name, username=self.username
            )

            self.status = "deleted"

            return self._schema()

        return creds

    def _fetch(self):
        return keyring.get_password(
            service_name=self.service_name, username=self.username
        )

    def _schema(self):
        return {
            "username": self.username,
            "password": self.password,
            "status": self.status,
        }
