import subprocess
import sys
import unittest


class TestReadPlan(unittest.TestCase):
    def test_prints_only_the_plan_summary(self):
        # Run the reader and capture what it prints.
        result = subprocess.run(
            [sys.executable, "src/read_plan.py", "fixtures/plan.json"],
            capture_output=True,
            text=True,
            check=True,
        )

        # Compare the printed text with the answer we expect.
        self.assertEqual(result.stdout.strip(), "aws_s3_bucket.demo: create")