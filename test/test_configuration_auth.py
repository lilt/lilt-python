"""The API key configured as ApiKeyAuth is sent as HTTP Basic auth, never in the URL."""

import base64
import unittest

import lilt


class TestConfigurationAuth(unittest.TestCase):

    def test_api_key_auth_is_a_basic_authorization_header(self) -> None:
        configuration = lilt.Configuration(api_key={"ApiKeyAuth": "secret"})
        setting = configuration.auth_settings()["ApiKeyAuth"]
        self.assertEqual(setting["in"], "header")
        self.assertEqual(setting["key"], "Authorization")
        self.assertEqual(
            setting["value"],
            "Basic " + base64.b64encode(b"secret:secret").decode("ascii"),
        )

    def test_api_key_auth_equals_basic_auth_with_the_key_twice(self) -> None:
        basic = lilt.Configuration(username="secret", password="secret")
        api_key = lilt.Configuration(api_key={"ApiKeyAuth": "secret"})
        self.assertEqual(
            api_key.auth_settings()["ApiKeyAuth"]["value"],
            basic.auth_settings()["BasicAuth"]["value"],
        )

    def test_api_key_auth_never_adds_a_query_parameter(self) -> None:
        configuration = lilt.Configuration(api_key={"ApiKeyAuth": "secret"})
        with lilt.ApiClient(configuration) as api_client:
            headers: dict = {}
            queries: list = []
            api_client.update_params_for_auth(
                headers, queries, ["ApiKeyAuth", "BasicAuth"], "/", "GET", None
            )
        self.assertEqual(queries, [])
        self.assertTrue(headers["Authorization"].startswith("Basic "))


if __name__ == "__main__":
    unittest.main()
