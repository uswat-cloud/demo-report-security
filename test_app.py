import unittest
from app import app


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def post(self, text):
        return self.client.post(
            "/report",
            data=text,
            content_type="application/yaml",
        )

    def test_healthy_report(self):
        response = self.post(
            "service: Demo Portal\nstatus: healthy\n"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"service": "Demo Portal", "status": "healthy"},
        )

    def test_degraded_report(self):
        response = self.post(
            "service: Demo Reports\nstatus: degraded\n"
        )
        self.assertEqual(response.status_code, 200)

    def test_unknown_status(self):
        response = self.post(
            "service: Demo Portal\nstatus: Maybe\n"
        )
        self.assertEqual(response.status_code, 400)

    def test_blank_service(self):
        response = self.post(
            'service: " "\nstatus: healthy\n'
        )
        self.assertEqual(response.status_code, 400)

    def test_list_rejected(self):
        response = self.post("- Demo Portal\n- healthy\n")
        self.assertEqual(response.status_code, 400)

    def test_invalid_yaml(self):
        response = self.post("service: [\n")
        self.assertEqual(response.status_code, 400)

    def test_python_tag_rejected(self):
        text = (
            "service: !!python/object/apply:builtins.str [123]\n"
            "status: healthy\n"
        )
        self.assertEqual(self.post(text).status_code, 400)

    def test_missing_field(self):
        response = self.post("service: Demo Portal\n")
        self.assertEqual(response.status_code, 400)

    def test_large_request(self):
        response = self.post("x" * 20000)
        self.assertEqual(response.status_code, 413)


if __name__ == "__main__":
    unittest.main()
