from django.test import TestCase
# Create your tests here.
class TestProgress(TestCase):

    def test_get_progress_panel(self):
        page = self.client.get("/progress/progress_panel/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "progress_panel.html")